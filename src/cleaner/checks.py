import os
from .constants import CACHE_DIR_PATH, CONTAINERS_DIR_PATH, LIB_PATH


def execute_path_checks():
    assert os.path.exists(LIB_PATH) == True
    assert os.path.exists(CONTAINERS_DIR_PATH) == True
    assert os.path.exists(CACHE_DIR_PATH) == True
