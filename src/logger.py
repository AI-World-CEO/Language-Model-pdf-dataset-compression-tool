import logging
import sys


def setup_logger(name: str, log_file: str, level=logging.INFO) -> logging.Logger:
    """Function setup as many loggers as you want"""

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    logger_instance = logging.getLogger(name)
    logger_instance.setLevel(level)
    logger_instance.addHandler(file_handler)
    logger_instance.addHandler(stream_handler)  # Add StreamHandler

    return logger_instance


def close_logger(logger_instance: logging.Logger):
    """Closes the handlers of the provided logger instance."""
    for handler in logger_instance.handlers:
        handler.close()
        logger_instance.removeHandler(handler)


# Setup your logger
my_logger = setup_logger('my_logger', 'first_logfile.log')


def main():
    # your main code here
    # perhaps some logging
    my_logger.info("Starting program...")

    try:
        # your program logic here
        # perhaps some logging
        my_logger.info("Running some task...")
    except Exception:
        # log the exception and then re-raise
        my_logger.exception("An error occurred!")
        raise
    finally:
        # We're done with logging at this point, so close the logger.
        close_logger(my_logger)


if __name__ == "__main__":
    main()
