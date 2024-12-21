import logging
import os
import sys


def enable_logging():
    logger = logging.getLogger("azure")
    logger.setLevel(os.environ.get("LOG_LEVEL", "INFO"))

    handler = logging.StreamHandler(stream=sys.stdout)
    logger.addHandler(handler)

    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    handler.setFormatter(formatter)
