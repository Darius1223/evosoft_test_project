from typing import Callable
from functools import wraps

from loguru import logger


def job_logger(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f" === START '{func.__name__.upper()}' JOB ===")
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            logger.error(exc)
            raise exc
        else:
            logger.success(f" === FINISH '{func.__name__.upper()}' JOB ===")
            return result

    return wrapper
