import os
import shutil
from time import time

from colorama import Fore
from .model import ProcessResult
from .constants import (
    APPLICATION_SUPPORT_DIR,
    APPLICATION_SUPPORT_SUFFIX,
    CACHE_DIR_PATH,
    CONTAINER_SUFFIX,
    CONTAINERS_DIR_PATH,
    IOS_DEVICE_LOGS_DIR,
    USER_LOGS_DIR,
    XCODE_DERIVED_DATA_DIR,
)


def sum_results(results: list[ProcessResult]) -> ProcessResult:
    net_result = ProcessResult.zero()
    for result in results:
        net_result += result

    return net_result


def clean_directory(dir_path: str) -> ProcessResult:
    start_time = time()
    size = 0

    try:
        dir = os.listdir(dir_path)

        if not dir:
            print(Fore.LIGHTYELLOW_EX + f"Skipping empty dir {dir_path}")
            return ProcessResult.zero()

        for file in dir:
            path = f"{dir_path}/{file}"

            print(Fore.LIGHTYELLOW_EX + f"--> Removing {path}", end="\t")

            try:
                file_size = os.stat(path).st_size

                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
            except PermissionError:
                print(Fore.LIGHTRED_EX + "[ACCESS DENIED]")
            else:
                size += file_size
                print(Fore.LIGHTGREEN_EX + f"[DONE]")

    except PermissionError as e:
        print(Fore.LIGHTRED_EX + f"--> Error reading {e.filename}")

    elapsed_time = (time() - start_time) * 1000
    return ProcessResult(elapsed_time, size)


def clean_containers() -> ProcessResult:
    print(Fore.CYAN + "\n# Cleaning container caches")

    results: list[ProcessResult] = []

    for _path in os.listdir(CONTAINERS_DIR_PATH):
        path = f"{CONTAINERS_DIR_PATH}/{_path}/{CONTAINER_SUFFIX}"
        if os.path.isdir(path):
            res = clean_directory(path)
            results.append(res)

    return sum_results(results)


def clean_app_support_cache() -> ProcessResult:
    print(Fore.CYAN + "\n# Cleaning application support caches")

    results: list[ProcessResult] = []

    for _path in os.listdir(APPLICATION_SUPPORT_DIR):
        path = f"{APPLICATION_SUPPORT_DIR}/{_path}/{APPLICATION_SUPPORT_SUFFIX}"
        if os.path.isdir(path):
            res = clean_directory(path)
            results.append(res)

    return sum_results(results)


def clean_user_logs() -> ProcessResult:
    print(Fore.CYAN + "\n# Cleaning user logs")

    results: list[ProcessResult] = []

    for _path in os.listdir(USER_LOGS_DIR):
        path = f"{USER_LOGS_DIR}/{_path}"
        if os.path.isdir(path):
            res = clean_directory(path)
            results.append(res)

    return sum_results(results)


def clean_lib_cache() -> ProcessResult:
    print(Fore.CYAN + "# Cleaning cache directory")
    return clean_directory(dir_path=CACHE_DIR_PATH)


def clean_xcode_cache() -> ProcessResult:
    print(Fore.CYAN + "\n# Cleaning XCode cache")

    res1 = clean_directory(dir_path=XCODE_DERIVED_DATA_DIR)
    res2 = clean_directory(dir_path=IOS_DEVICE_LOGS_DIR)

    return res1 + res2
