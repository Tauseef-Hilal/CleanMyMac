from dataclasses import dataclass
from .utils import formatted_size


@dataclass
class ProcessResult:
    elapsed_time: float
    size_freed: int

    def get_formatted_time(self):
        return f"{self.elapsed_time:.2f}ms"

    def get_formatted_size(self):
        return formatted_size(self.size_freed)

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __add__(self, other: "ProcessResult") -> "ProcessResult":
        return ProcessResult(
            elapsed_time=self.elapsed_time + other.elapsed_time,
            size_freed=self.size_freed + other.size_freed,
        )


@dataclass
class ScanResult:
    cache_dir_size: int
    app_support_cache_size: int
    container_cache_size: int
    xcode_cache_size: int
    ios_device_log_size: int
    user_log_size: int

    @property
    def total_size(self) -> int:
        return (
            self.cache_dir_size
            + self.app_support_cache_size
            + self.xcode_cache_size
            + self.ios_device_log_size
            + self.user_log_size
        )
