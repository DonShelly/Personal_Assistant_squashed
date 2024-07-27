import logging

from flask import request

from app import logger


def log_request_info():
    if logger.isEnabledFor(logging.INFO):
        logger.info(request.headers)
        logger.info(request.get_json(silent=True))


def log_response_info(response):
    if logger.isEnabledFor(logging.INFO):
        # check if the response is in direct passthrough mode
        if response.direct_passthrough:
            logger.info("Response is in direct passthrough mode, skipping logging of response data.")
        else:
            logger.info(response.get_data())
    return response
