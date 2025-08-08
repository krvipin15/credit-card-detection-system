import sys
from src.logger import logger

def error_message_detail(error: Exception, error_detail) -> str:
    """
    Constructs a detailed error message including the script name, line number, and the actual error message.

    Args:
        error (Exception): The exception object that was raised.
        error_detail (traceback): Typically `sys`, used to extract traceback information.

    Returns:
        str: A formatted string containing file name, line number, and error message.
    """
    # Extract traceback object from error_detail
    _, _, exc_tb = error_detail.exc_info()

    # Get the file name and line number where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_num = exc_tb.tb_lineno

    # Custom error message
    error_message = f"Error occured in python script name [{file_name}] line number [{line_num}] error message [{str(error)}]"

    return error_message

class CustomException(Exception):
    """
    Custom exception class that includes detailed error context (file name, line number, error message).

    Attributes:
        error_message (str): The formatted error message.
    """
    def __init__(self, error_message, error_detail):
        """
        Initializes the custom exception with a detailed error message.

        Args:
            error_message (str): The original error message.
            error_detail (traceback): Typically `sys`, used to extract traceback info.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
        logger.error(self.error_message)

    def __str__(self) -> str:
        """
        Returns the detailed error message as the string representation of the exception.

        Returns:
            str: The detailed error message.
        """
        return self.error_message
