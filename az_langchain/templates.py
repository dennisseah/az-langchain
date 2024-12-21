from langchain_core.prompts import PromptTemplate


def get_translate_template():
    return PromptTemplate(
        template="""You are a translator, translate the following into {language}:

    `{text}`

    Do not provide anything other than the translation.""",
        input_variables=["language"],
    )


def get_back2english_template():
    return PromptTemplate(
        template="""You are a translator, translate the following into English:

    `{input}`.

    Do not provide anything other than the translation.""",
        input_variables=["input"],
    )
