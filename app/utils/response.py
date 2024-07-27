from flask import make_response

from app.utils.logger import get_request_id


class Response:
    """
    The `Response` class represents a response object that can be returned from an API endpoint. It contains methods for building and creating response objects.

    Attributes:
        - `HTTP_SUCCESS`: Represents the HTTP status code for success (200).
        - `HTTP_ACCEPTED`: Represents the HTTP status code for accepted (202).
        - `HTTP_MOVED_PERMANENTLY`: Represents the HTTP status code for moved permanently (301).
        - `HTTP_BAD_REQUEST`: Represents the HTTP status code for bad request (400).
        - `HTTP_UNAUTHORIZED`: Represents the HTTP status code for unauthorized (401).
        - `HTTP_FORBIDDEN`: Represents the HTTP status code for forbidden (403).
        - `HTTP_NOT_FOUND`: Represents the HTTP status code for not found (404).
        - `HTTP_ERROR`: Represents the HTTP status code for internal server error (500).
        - `HTTP_NOT_IMPLEMENTED`: Represents the HTTP status code for not implemented (501).

    Methods:
        - `__init__(self, data=None, status=None)`: Initializes a new instance of the `Response` class.
            - `data` (optional): The data payload to be included in the response.
            - `status` (optional): The HTTP status code to be set in the response.

        - `build(self)`: Builds the response object based on the data and status set in the instance.
            Returns:
                - `resp`: The built response object.

        - `make(data, status, deprecation_warning=False, deprecation_date=None)`: Creates a new response object with the provided data and status.
            Parameters:
                - `data`: The data payload to be included in the response.
                - `status`: The HTTP status code to be set in the response.
                - `deprecation_warning` (optional): Flag indicating if a deprecation warning should be included in the response (default: False).
                - `deprecation_date` (optional): The date when the endpoint will be deprecated (default: None).
            Returns:
                - `resp`: The created response object.

    Note: The `Response` class relies on external functions `get_request_id()` and `make_response()` which are not defined in this class.
    """
    HTTP_SUCCESS = 200
    HTTP_ACCEPTED = 202
    HTTP_MOVED_PERMANENTLY = 301
    HTTP_BAD_REQUEST = 400
    HTTP_UNAUTHORIZED = 401
    HTTP_FORBIDDEN = 403
    HTTP_NOT_FOUND = 404
    HTTP_ERROR = 500
    HTTP_NOT_IMPLEMENTED = 501

    def __init__(self, data=None, status=None):
        self.data = data
        self.status = status

    def build(self):
        response = {
            "status": self.status,
            "payload": self.data,
            "correlation_id": get_request_id(),
        }
        resp = make_response(response)

        return resp

    @staticmethod
    def make(data, status, deprecation_warning=False, deprecation_date=None):
        response = {
            "status": status,
            "payload": data,
            "correlation_id": get_request_id(),
        }
        if deprecation_warning:
            deprecation_message = (
                "This endpoint is deprecated and will be removed in the future."
            )
            if deprecation_date:
                deprecation_message += (
                    f" This endpoint will be removed on {deprecation_date}."
                )
            response["deprecation_warning"] = deprecation_message
        resp = make_response(response, status)
        return resp
