import logging


def configure_logging(level):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(levelname)-7s - %(message)s",
    )


def get_logger(name: str):
    return logging.getLogger(name)
