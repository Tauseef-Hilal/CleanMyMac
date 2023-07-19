from dataclasses import dataclass


@dataclass
class ProcessResult:
    elapsed_time: float
    size_freed: int

    def getFormattedTime(self):
        return f"{self.elapsed_time:.2f}ms"

    def getFormattedSize(self):
        size = self.size_freed / 1024
        suffixes = ["KB", "MB", "GB", "TB"]

        for suffix in suffixes:
            if size < 1024:
                break

            size /= 1024

        return f"{size:.2f}{suffix}"

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __add__(self, other: "ProcessResult") -> "ProcessResult":
        return ProcessResult(
            elapsed_time=self.elapsed_time + other.elapsed_time,
            size_freed=self.size_freed + other.size_freed,
        )
