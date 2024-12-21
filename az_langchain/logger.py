import logging
import os
import sys

logger = logging.getLogger("az_langchain")
logger.setLevel(os.environ.get("LOG_LEVEL", "INFO"))

handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
handler.setFormatter(formatter)
