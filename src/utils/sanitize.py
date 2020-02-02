def sanitize(data: str) -> str:
    result = ''
    for char in data:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
            result += char

    return result
