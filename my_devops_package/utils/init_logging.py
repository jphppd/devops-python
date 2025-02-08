"""Logging initialization."""

import logging
import logging.handlers


def get_handlers(log_file: str):
    """Create the handlers."""
    default_handler = logging.handlers.RotatingFileHandler(
        maxBytes=1000000,
        backupCount=5,
        filename=log_file,
        delay=True,
    )

    debug_handler = logging.StreamHandler()

    log_format = (
        "%(asctime)s|%(levelname)s|%(module)s|%(funcName)s:%(lineno)s|%(message)s"
    )
    log_formatter = logging.Formatter(log_format)

    debug_formatter = logging.Formatter(
        "%(module)s|%(funcName)s:%(lineno)s|%(message)s"
    )
    debug_handler.setFormatter(debug_formatter)
    debug_handler.setLevel("DEBUG")

    default_handler.setFormatter(log_formatter)

    return {
        "default": default_handler,
        "debug": debug_handler,
    }


def init_logging(log_name: str, debug_to_stdout=False):
    """
    Configure logging.

    By default, also log to stdout if it's a tty (terminal).
    """
    handlers = get_handlers(log_name)

    logging.getLogger().addHandler(handlers["default"])
    logging.getLogger().setLevel("INFO")

    if debug_to_stdout:
        # Log to stdout
        logging.getLogger().addHandler(handlers["debug"])
