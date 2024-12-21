from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import BaseGenerationOutputParser
from langchain_core.outputs import ChatGeneration, Generation


class OutputParser(BaseGenerationOutputParser[str]):
    """
    Custom Parser for Azure AI Chat Completions to print the token usages

    :param BaseGenerationOutputParser: Base class for output parsers
    """

    def parse_result(self, result: list[Generation], *, partial: bool = False) -> str:
        if len(result) != 1:
            raise NotImplementedError(
                "This output parser can only be used with a single generation."
            )
        generation = result[0]
        if not isinstance(generation, ChatGeneration):
            # Say that this one only works with chat generations
            raise OutputParserException(
                "This output parser can only be used with a chat generation."
            )

        print(generation.message.response_metadata)

        return generation.message.content  # type: ignore
