from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

from az_langchain.azure_openai_model import get_model as get_openai_model
from az_langchain.azure_phi3_model import get_model as get_phi3_model
from az_langchain.logger import enable_logging
from az_langchain.templates import get_back2english_template, get_translate_template

load_dotenv()

enable_logging()
phi3_model = get_phi3_model()
openai_model = get_openai_model()

translate_template = get_translate_template()
back2english_template = get_back2english_template()

parser = StrOutputParser()

translate_chain = translate_template | openai_model | parser
retranslate_chain = back2english_template | phi3_model | parser

chain = translate_chain | RunnableParallel(
    translate=RunnablePassthrough(),
    back2english=RunnablePassthrough() | retranslate_chain,
)
response = chain.invoke({"language": "japanese", "text": "Merry Christmas"})
print(response)
