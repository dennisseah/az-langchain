import os

from azure.identity import DefaultAzureCredential
from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel


def get_model():
    credential = (
        os.environ["AZURE_OPENAI_API_KEY"]
        if "AZURE_OPENAI_API_KEY" in os.environ
        else DefaultAzureCredential()
        .get_token("https://cognitiveservices.azure.com/.default")
        .token
    )
    return AzureAIChatCompletionsModel(
        endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        credential=credential,
        api_version=os.environ["AZURE_OPENAI_API_VERSION"],
        model_name=os.environ["AZURE_OPENAI_DEPLOYED_MODEL_NAME"],
        temperature=0,
    )
