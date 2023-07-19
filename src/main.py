from colorama import Fore
from .cleaner.model import ProcessResult
from .cleaner import clean, CleanType
from .cleaner.cleaners import sum_results


def display_stats(result: ProcessResult) -> None:
    print(Fore.CYAN + "\n# Stats")
    print(
        Fore.LIGHTGREEN_EX
        + f"--> Total space freed:"
        + f" {result.getFormattedSize()}",
    )
    print(f"--> Total time taken: {result.getFormattedTime()}")


def main():
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
