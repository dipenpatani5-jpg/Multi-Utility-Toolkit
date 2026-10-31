"""File handling functions used by the toolkit."""


def create_file(filename):
    try:
        with open(filename, "x", encoding="utf-8"):
            pass
        return "File created successfully!"
    except FileExistsError:
        return "A file with that name already exists."
    except OSError as exc:
        return f"File creation failed: {exc}"


def write_file(filename, content):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        return "Data written successfully!"
    except OSError as exc:
        return f"Writing failed: {exc}"


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def append_file(filename, content):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(content)
        return "Data appended successfully!"
    except OSError as exc:
        return f"Appending failed: {exc}"


if __name__ == "__main__":
    print("file_operations module: run main.py to use the menu.")
