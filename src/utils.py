import logging

def setup_logging(log_file="logs/project.log"):
    """
    Set up logging for the project, which will log to both console and a file.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # File handler for logging
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Console handler for logging
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Log format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def log_message(logger, message, level="INFO"):
    """
    Log messages at different severity levels.
    """
    if level == "DEBUG":
        logger.debug(message)
    elif level == "INFO":
        logger.info(message)
    elif level == "WARNING":
        logger.warning(message)
    elif level == "ERROR":
        logger.error(message)
    elif level == "CRITICAL":
        logger.critical(message)
