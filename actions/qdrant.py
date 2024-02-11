from typing import List

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient
from qdrant_client.models import Distance
import tiktoken


class LocalQdrant:
    """A class that wraps the QdrantClient and provides some convenience methods for working with a collection."""

    def __init__(
        self, url: str, qdrant_api_key: str, collection_name: str, openai_api_key: str
    ):
        """
        Initializes an instance of the Qdrant class.
        """
        # Initialize the client
        self.name: str = collection_name
        self.client: QdrantClient = QdrantClient(url=url, api_key=qdrant_api_key)
        self.embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        self.qdrant = Qdrant(
            client=self.client,
            collection_name=self.name,
            embeddings=self.embeddings,
            content_payload_key="Answer",
        )
        self.retriever = self.qdrant.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={"k": 10, "score_threshold": 0.75},
        )

    def search(self, query: str) -> List[dict]:
        """
        Search the collection for relevant results based on a query.

        Args:
            query (str): The query to search the collection with.
            token_limit (int, optional): The maximum token limit for the extracted context. Defaults to 1000.

        Returns:
            list: List of dictionaries representing the search results.
        """
        results = self.retriever.get_relevant_documents(query)
        return results


def tiktoken_len(text: str, base: str = "cl100k_base") -> int:
    """
    Get the length of the tokenized text using the specified base.

    Args:
        text (str): The text to tokenize and measure.
        base (str, optional): The base used for tokenization. Defaults to "cl100k_base".

    Returns:
        int: The length of the tokenized text.
    """
    tokenizer = tiktoken.get_encoding(base)
    tokens = tokenizer.encode(text, disallowed_special=())
    return len(tokens)


def unpack_results(search_results: List) -> List[dict]:
    """
    Unpack the search results into a list of dictionaries.

    Args:
        search_results (list): List of search results.

    Returns:
        list: List of dictionaries representing the unpacked search results.
    """
    return [vars(result) for result in search_results]


def extract_context(results, token_limit):
    """
    Extract relevant context from the results based on a token limit.

    Args:
        results (list): List of results to extract context from.
        token_limit (int): The maximum token limit for the extracted context.
        sub_key (str, optional): The sub-key to access the nested context, if applicable. Defaults to None.

    Returns:
        tuple: A tuple containing the extracted context list and its token count.
    """
    context_list: list = []
    for result in results:
        context = str(result["page_content"])
        if tiktoken_len(" ".join(context_list + [context])) > token_limit:
            break
        context_list.append(context)
    return context_list, tiktoken_len(" ".join(context_list))
