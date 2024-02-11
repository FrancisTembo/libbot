import json


class Config:
    """
    Configuration class to handle the application settings.
    """

    def __init__(self, config_file: str):
        """
        Initialize the Config instance with the configuration file.

        Args:
            config_file (str): Path to the configuration file.
        """
        self.config_file = config_file
        self.load_config()

    def load_config(self) -> None:
        """
        Load the configuration from the specified file.
        """
        with open(self.config_file) as f:
            config = json.load(f)
            self.openai_api_key = config["openai_api_key"]
            self.model = config["model"]
            self.token_limit = config["token_limit"]
            self.temperature = config["temperature"]
            self.qdrant_api_key = config["qdrant_key"]
            self.qdrant_url = config["qdrant_url"]
            self.vector_size = config["vector_size"]
            self.collection_name = config["collection_name"]
