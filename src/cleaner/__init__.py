from enum import Enum
from .cleaners import (
    clean_app_support_cache,
    clean_containers,
    clean_lib_cache,
    clean_user_logs,
    clean_xcode_cache,
    scan_juck,
    sum_results,
)

from .models import ProcessResult
from .utils import formatted_size


class CleanType(Enum):
    LIB_CACHE = 0
    CONTAINER_CACHE = 1
    APP_SUPPORT_CACHE = 2
    XCODE_CACHE = 3
    USER_LOGS = 4


def clean(clean_type: CleanType) -> ProcessResult:
    match clean_type:
        case CleanType.LIB_CACHE:
            return clean_lib_cache()
        case CleanType.CONTAINER_CACHE:
            return clean_containers()
        case CleanType.APP_SUPPORT_CACHE:
            return clean_app_support_cache()
        case CleanType.XCODE_CACHE:
            return clean_xcode_cache()
        case CleanType.USER_LOGS:
            return clean_user_logs()
