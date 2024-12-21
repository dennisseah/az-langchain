import os

from azure.identity import DefaultAzureCredential
from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel


def get_model():
    return AzureAIChatCompletionsModel(
        endpoint=os.environ["AZURE_PHI3_ENDPOINT"],
        credential=(
            os.environ["AZURE_PHI3_KEY"]
            if "AZURE_PHI3_KEY" in os.environ
            else DefaultAzureCredential()
        ),
        client_kwargs={"logging_enable": True},
    )
