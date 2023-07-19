def formatted_size(size: int) -> str:
    size /= 1024
    suffixes = ["KB", "MB", "GB", "TB"]

    for suffix in suffixes:
        if size < 1024:
            break

        size /= 1024

    return f"{size:.2f}{suffix}"
