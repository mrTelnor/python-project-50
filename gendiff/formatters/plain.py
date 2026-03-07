def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return value


def format_plain(diff, path=""):
    lines = []

    for node in diff:
        name = node["key"]
        status = node["type"]
        new_path = f"{path}.{name}" if path else name

        if status == "added":
            value = format_value(node["value"])
            lines.append(f"Property '{new_path}' was added with value: {value}")

        elif status == "removed":
            lines.append(f"Property '{new_path}' was removed")

        elif status == "changed":
            old = format_value(node["old_value"])
            new = format_value(node["new_value"])
            lines.append(
                f"Property '{new_path}' was updated. From {old} to {new}"
            )

        elif status == "nested":
            lines.extend(format_plain(node["children"], new_path).split("\n"))

    return "\n".join(lines)