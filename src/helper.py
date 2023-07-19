from colorama import Fore
from .cleaner import formatted_size
from .cleaner.models import ProcessResult, ScanResult


def display_stats(result: ProcessResult) -> None:
    print(Fore.CYAN + "\n# Stats")
    print(
        Fore.LIGHTGREEN_EX
        + f"--> Total space freed:"
        + f" {result.get_formatted_size()}",
    )
    print(f"--> Total time taken: {result.get_formatted_time()}")


def display_scan_results(result: ScanResult) -> None:
    print(Fore.CYAN + "\n#Scan Results")
    print(Fore.LIGHTMAGENTA_EX + "Cache Directory Size: ", end="")
    print(Fore.LIGHTRED_EX + formatted_size(result.cache_dir_size))
    print(Fore.LIGHTMAGENTA_EX + "Application Support Cache Size: ", end="")
    print(Fore.LIGHTRED_EX + formatted_size(result.app_support_cache_size))
    print(Fore.LIGHTMAGENTA_EX + "Container Cache Size: ", end="")
    print(Fore.LIGHTRED_EX + formatted_size(result.container_cache_size))
    print(Fore.LIGHTMAGENTA_EX + "XCode Cache Size: ", end="")
    print(Fore.LIGHTRED_EX + formatted_size(result.xcode_cache_size))
    print(Fore.LIGHTMAGENTA_EX + "IOS Device Log Size: ", end="")
    print(Fore.LIGHTRED_EX + formatted_size(result.ios_device_log_size))
    print(Fore.LIGHTMAGENTA_EX + "User Log Size: ", end="")
    print(Fore.LIGHTRED_EX + formatted_size(result.user_log_size))
    print(Fore.LIGHTCYAN_EX + "\nTotal Junk Size: ", end="")
    print(Fore.LIGHTRED_EX + formatted_size(result.total_size))


def should_clean_cache() -> bool:
    choice = ""
    while choice.upper() not in ("Y", "N"):
        choice = input(
            Fore.LIGHTGREEN_EX + "Would you like to clean the cache? [Y | N]: "
        )

    return choice.upper() == "Y"
