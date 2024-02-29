

def stringify_list(data: list[str], delimiter: str = ",") -> str:
    return delimiter.join([f"'{x}'" for x in data])
