def generate_progress_bar(
    current,
    total
):

    if current > total:

        current = total

    filled = int(
        (current / total) * 10
    )

    empty = 10 - filled

    bar = (
        "█" * filled
        +
        "░" * empty
    )

    percent = int(
        (current / total) * 100
    )

    return f"{bar} {percent}%"