from colorama import Fore

from .helper import display_scan_results, display_stats, should_clean_cache
from .cleaner import clean, scan_juck, sum_results, CleanType


def main():
    print(Fore.LIGHTYELLOW_EX + "Scanning for junk", end="\t")
    res = scan_juck()
    print(Fore.LIGHTGREEN_EX + "[DONE]")
    display_scan_results(res)

    if not should_clean_cache():
        return

    results = [
        clean(clean_type=CleanType.LIB_CACHE),
        clean(clean_type=CleanType.CONTAINER_CACHE),
        clean(clean_type=CleanType.APP_SUPPORT_CACHE),
        clean(clean_type=CleanType.XCODE_CACHE),
        clean(clean_type=CleanType.USER_LOGS),
    ]

    net_result = sum_results(results)
    display_stats(net_result)


if __name__ == "__main__":
    main()
