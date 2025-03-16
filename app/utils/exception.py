class CustomException(Exception):
    def __init__(self, code, message, details=None):
        self.code = code
        self.message = message
        self.details = details
        super().__init__(f"[{code}] {message}")

    def __str__(self):
        error_str = super().__str__()
        if self.details:
            error_str += f"\nDetails: {self.details}"
        return error_str


class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)
