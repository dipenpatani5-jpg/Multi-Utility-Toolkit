# Multi-Utility Toolkit

A menu-driven Python project demonstrating built-in modules, custom modules, packages, and the `if __name__ == "__main__":` pattern.

## Features

- **Date and time:** current date/time, date difference, custom formatting, stopwatch, countdown.
- **Math:** factorial, compound interest, trigonometry, shape areas, kilometre-to-mile conversion.
- **Random:** random integers/lists, passwords, OTPs, sampling, coin toss.
- **UUID:** generate UUID version 4 identifiers.
- **File operations:** create, overwrite, read, and append text files.
- **Module exploration:** inspect supported modules using `dir()`.

## Project structure

```text
Multi_Utility_Toolkit/
│
├── main.py
├── README.md
└── utilities/
    ├── __init__.py
    ├── file_operations.py
    └── math_utils.py
```

## Requirements

- Python 3.8 or newer
- No external packages are required. The project uses Python's standard library.

## How to run

1. Download or extract the project folder.
2. Open the folder in VS Code.
3. Open the terminal in that folder.
4. Run:

```bash
python main.py
```

On some systems, use `py main.py` instead.

## Example

```text
Welcome to Multi-Utility Toolkit
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
Enter your choice: 4
Generated UUID: 9d2d...
```

## Concepts demonstrated

- Imports: `datetime`, `time`, `math`, `random`, `string`, and `uuid`
- Custom modules and package initialization with `utilities/__init__.py`
- Reusable functions and separation of concerns
- `dir()` for dynamic attribute exploration
- `if __name__ == "__main__":` to control direct execution
- File handling with context managers (`with open(...)`)
- Input validation and exception handling

## Notes

- Files created through the File Operations menu are saved in the current working directory (the folder from which `main.py` is run).
- The stopwatch and countdown run in the terminal. Press `Ctrl+C` to cancel the countdown.
- The password generator is suitable for demonstrating the `random` module in a learning project. For real security-sensitive passwords, use Python's `secrets` module instead.
