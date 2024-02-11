import logging

from rasa_sdk import Action

from .llm import LanguageModel
from .qdrant import LocalQdrant, extract_context, unpack_results
from .utils import Config

# Configure logging
logging.basicConfig(filename="rasa_action.log", level=logging.ERROR)

config = Config("actions/config.json")

client = LocalQdrant(
    url=config.qdrant_url,
    qdrant_api_key=config.qdrant_api_key,
    collection_name=config.collection_name,
    openai_api_key=config.openai_api_key,
)

language_model = LanguageModel(
    openai_api_key=config.openai_api_key,
    model=config.model,
    temperature=config.temperature,
)


class ActionAskOpenAI(Action):
    def name(self) -> str:
        return "action_ask_openai"

    def run(self, dispatcher, tracker, domain):
        try:
            # Get the latest message from the user
            message = tracker.latest_message["text"]

            search_results = client.search(query=message)

            if len(search_results) == 0:
                prompt = f"HUMAN: {message}"
            else:
                results = unpack_results(search_results)

                context = extract_context(
                    results=results, token_limit=config.token_limit
                )

                prompt = f"CONTEXT: {context} \n \n HUMAN: {message}"

            if completion := language_model.generate(human_input=prompt):
                dispatcher.utter_message(text=completion)
            else:
                # Send an error message if no completion
                dispatcher.utter_message(text="I'm sorry, I can't assist with that.")
        except Exception as e:
            # Log the error
            logging.error(f"Error in Rasa action: {str(e)}")
            # Send an error message to the user
            dispatcher.utter_message(
                text="An error occurred while processing your request. Please try again later."
            )

        return []
