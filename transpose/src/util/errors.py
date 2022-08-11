# Transpose Bad Request
class TransposeBadRequest(Exception):
    def __init__(self, error_code: int, message: str) -> None:
        self.error_code = error_code
        self.message = message
        super().__init__('{} Bad Request: {}'.format(error_code, message))
        
# Transpose Rate Limit
class TransposeRateLimit(Exception):
    def __init__(self, error_code: int, message: str) -> None:
        self.error_code = error_code
        self.message = message
        super().__init__('{}: Rate Limit: {}'.format(error_code, message))
        
# Transpose Invalid API Key
class TransposeInvalidAPIKey(Exception):
    def __init__(self, error_code: int, message: str) -> None:
        self.error_code = error_code
        self.message = message
        super().__init__('{}: Invalid API Key: {}'.format(error_code, message))
        
# Transpose Internal Server Error
class TransposeInternalServerError(Exception):
    def __init__(self, error_code: int, message: str) -> None:
        self.error_code = error_code
        self.message = message
        super().__init__('{}: Internal Server Error: {}'.format(error_code, message))
        
# Transpose Resource Not Fount
class TransposeResourceNotFound(Exception):
    def __init__(self, error_code: int, message: str) -> None:
        self.error_code = error_code
        self.message = message
        super().__init__('{}: Not Found: {}'.format(error_code, message))
        
# Transpose Dependency Error
class TransposeDependencyError(Exception):
    def __init__(self, packages: list) -> None:
        self.message = ' '.join(packages)
        super().__init__('Missing Dependencies. You can install these via `pip install {}`'.format(' '.join(packages)))
        
def raise_custom_error(error_code: int, message: str) -> None:
    if   error_code == 400:
        raise TransposeBadRequest(error_code, message)
    elif error_code == 403 or error_code == 401:
        raise TransposeInvalidAPIKey(error_code, message)
    elif error_code == 500:
        raise TransposeInternalServerError(error_code, message)
    elif error_code == 404:
        raise TransposeResourceNotFound(error_code, message)
    elif error_code == 429:
        raise TransposeRateLimit(error_code, message)
    else:
        raise Exception('{}: {}'.format(error_code, message))