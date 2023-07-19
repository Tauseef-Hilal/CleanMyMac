from dataclasses import dataclass

@dataclass
class ProcessResult:
    elapsed_time: float
    size_freed: int

    def getFormattedTime(self):
        return f"{self.elapsed_time:.2f}ms"

    def getFormattedSize(self):
        return (
            f"{round(self.size_freed / 1024, 2)}KB"
            if self.size_freed < 10486
            else f"{round(self.size_freed / 1048576, 2)}MB"
        )

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __add__(self, other: "ProcessResult") -> "ProcessResult":
        return ProcessResult(
            elapsed_time=self.elapsed_time + other.elapsed_time,
            size_freed=self.size_freed + other.size_freed,
        )

