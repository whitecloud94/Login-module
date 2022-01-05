from types import CodeType


class Status_code():
    HTTP_400 = 400
    HTTP_401 = 401
    HTTP_404 = 404
    HTTP_405 = 405
    HTTP_500 = 500

class APIException(Exception):
    status_code= int
    code: str
    msg: str
    detail: str
    ex: Exception

    def __init__(self, 
        status_code: int = Status_code.HTTP_500,
        code: str = None,
        msg: str = None,
        detail: str = None,
        ex: Exception = None) -> None:


        self.status_code = status_code
        self.code = code
        self.msg = msg
        self.detail = detail
        ex = ex
    super().__init__(ex)
    