import functools
import traceback

from marshmallow import ValidationError

from app import logger
from app.errors import ProcessingException, ValidationException
from app.utils.messages import Error
from app.utils.response import Response


def handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationException as ve:
            logger.info(str(ve.messages))
            return Response.make(ve.messages, Response.HTTP_BAD_REQUEST)
        except ProcessingException as pe:
            logger.info(str(pe.messages))
            return Response.make(pe.messages, Response.HTTP_BAD_REQUEST)
        except ValidationError as err:
            logger.info(err)
            return Response.make(err.messages, Response.HTTP_BAD_REQUEST)
        except Exception as e:
            traceback.print_exc()
            logger.error(f"general exception {e}")
            return Response.make(Error.REQUEST_FAILED, Response.HTTP_ERROR)

    return wrapper
