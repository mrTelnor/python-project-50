INDENT_SIZE = 4
PREFIX_WIDTH = 2  # место под "- " / "+ " / "  "


def stringify(value, depth):
    if not isinstance(value, dict):
        if value is True:
            return "true"
        if value is False:
            return "false"
        if value is None:
            return "null"
        return str(value)

    indent = " " * (depth * INDENT_SIZE)
    lines = ["{"]

    for key, val in value.items():
        lines.append(
            f"{indent}{key}: {stringify(val, depth + 1)}"
        )

    lines.append(" " * ((depth - 1) * INDENT_SIZE) + "}")

    return "\n".join(lines)


def format_stylish(diff, depth=1):
    lines = ["{"]

    for node in diff:
        indent = " " * (depth * INDENT_SIZE - PREFIX_WIDTH)

        key = node["key"]
        node_type = node["type"]

        if node_type == "nested":
            children = format_stylish(node["children"], depth + 1)
            lines.append(f"{indent}  {key}: {children}")

        elif node_type == "added":
            value = stringify(node["value"], depth + 1)
            lines.append(f"{indent}+ {key}: {value}")

        elif node_type == "removed":
            value = stringify(node["value"], depth + 1)
            lines.append(f"{indent}- {key}: {value}")

        elif node_type == "unchanged":
            value = stringify(node["value"], depth + 1)
            lines.append(f"{indent}  {key}: {value}")

        elif node_type == "changed":
            old_val = stringify(node["old_value"], depth + 1)
            new_val = stringify(node["new_value"], depth + 1)

            lines.append(f"{indent}- {key}: {old_val}")
            lines.append(f"{indent}+ {key}: {new_val}")

    lines.append(" " * ((depth - 1) * INDENT_SIZE) + "}")

    return "\n".join(lines)
