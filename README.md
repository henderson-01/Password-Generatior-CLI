# 🔒 Secure CLI Password Generator

A simple, cryptographically secure password generator for the command line. This tool generates strong passwords locally without relying on any external dependencies or making network requests.

## 🫆 Why is it safe?

* **Zero External Dependencies:** The script strictly uses Python's built-in standard libraries (`secrets` and `string`). `uv` is only used for managing the virtual environment and development tooling (like `ruff`) — no third-party packages are involved in password generation, which eliminates the risk of downloading malicious packages.
* **Fully Local Execution:** The password generation and validation happen entirely in your computer's RAM. The script makes zero network requests, meaning your newly generated passwords are never sent over the internet.
* **No File System Access:** The script does not read, write, or modify any files on your hard drive. It simply takes text input from your keyboard and prints text back to your screen.
* **Safe Handling of Input:** The script gracefully handles basic user errors (like typing letters instead of numbers) to prevent unexpected crashes in your terminal.

## 📜 Prerequisites

* [uv](https://docs.astral.sh/uv/) installed on your system.
* Python 3.12+ (managed automatically by `uv`).

## ▶️ How to Run It

1. Clone the repository (or save the code in a file named `password_generator.py`).
2. Open your CLI (Terminal on Mac/Linux, or Command Prompt/PowerShell on Windows).
3. Navigate to the project folder.
4. Install the project dependencies (creates the `.venv` virtual environment):

```bash
uv sync
```

5. Run the script:

```bash
uv run password_generator.py
```

> [!Note]
> `uv` automatically manages the correct Python interpreter, so you do not need to worry about `python` vs `python3`.

*The script will prompt you for your preferences right there in the console and output your secure password immediately.*

## 📸 Example from CLI Output

```text
--- Secure Password Generator ---

Enter the desired password length (min 8): 30
Include special characters? (y/n): y
Include numbers? (y/n): y

Generated Password: 8Orh5'CfzP"Vn(>snwbvI[b5'5S\*u
Status: Password is strong. ✅

```

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENCE) for details.
