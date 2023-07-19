import os
import shutil
from time import time

from colorama import Fore
from .models import ProcessResult, ScanResult
from .constants import (
    APPLICATION_SUPPORT_DIR,
    APPLICATION_SUPPORT_SUFFIX,
    CACHE_DIR_PATH,
    CONTAINER_SUFFIX,
    CONTAINERS_DIR_PATH,
    IOS_DEVICE_LOGS_DIR,
    LIB_PATH,
    USER_LOGS_DIR,
    XCODE_DERIVED_DATA_DIR,
)


def scan_juck() -> ScanResult:
    cache_dir_size = get_directory_size(CACHE_DIR_PATH)
    xcode_cache_size = get_directory_size(XCODE_DERIVED_DATA_DIR)
    ios_device_log_size = get_directory_size(IOS_DEVICE_LOGS_DIR)
    user_log_size = get_directory_size(USER_LOGS_DIR)

    container_cache_size = 0
    for item in os.listdir(CONTAINERS_DIR_PATH):
        path = f"{CONTAINERS_DIR_PATH}/{item}"
        if os.path.isfile(path):
            continue

        container_cache_size += get_directory_size(
            f"{path}/{CONTAINER_SUFFIX}",
        )

    app_support_cache_size = 0
    for item in os.listdir(APPLICATION_SUPPORT_DIR):
        path = f"{APPLICATION_SUPPORT_DIR}/{item}"
        if os.path.isfile(path):
            continue

        app_support_cache_size += get_directory_size(
            f"{path}/{APPLICATION_SUPPORT_SUFFIX}",
        )

    return ScanResult(
        cache_dir_size=cache_dir_size,
        app_support_cache_size=app_support_cache_size,
        container_cache_size=container_cache_size,
        xcode_cache_size=xcode_cache_size,
        ios_device_log_size=ios_device_log_size,
        user_log_size=user_log_size,
    )


def sum_results(results: list[ProcessResult]) -> ProcessResult:
    net_result = ProcessResult.zero()
    for result in results:
        net_result += result

    return net_result


def get_directory_size(dir_path: str) -> int:
    size = 0
    for path, _, files in os.walk(dir_path):
        for f in files:
            size += os.path.getsize(f"{path}/{f}")

    return size


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
                if os.path.isdir(path):
                    file_size = get_directory_size(path)
                    shutil.rmtree(path)
                else:
                    file_size = os.path.getsize(path)
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
