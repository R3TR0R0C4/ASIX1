def remove_last_newline(text):
    parts = text.rsplit('\n', 1)
    if len(parts) == 2:
        return parts[0] + parts[1]
    return text

# Example usage:
text = "This\n is a\n string with\n a newline at the end.\nass"
result = remove_last_newline(text)
print(result)