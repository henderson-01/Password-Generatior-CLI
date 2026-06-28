# Secure CLI Password Generator

A simple, cryptographically secure password generator for the command line. This tool generates strong passwords locally without relying on any external dependencies or making network requests.

## Why is it safe?

* **Zero External Dependencies:** The script strictly uses Python's built-in standard libraries (`secrets` and `string`). You do not need to install anything via `pip`, which eliminates the risk of downloading malicious third-party packages.
* **Fully Local Execution:** The password generation and validation happen entirely in your computer's RAM. The script makes zero network requests, meaning your newly generated passwords are never sent over the internet.
* **No File System Access:** The script does not read, write, or modify any files on your hard drive. It simply takes text input from your keyboard and prints text back to your screen.
* **Safe Handling of Input:** The script gracefully handles basic user errors (like typing letters instead of numbers) to prevent unexpected crashes in your terminal.

## Prerequisites

* Python 3 installed on your system.
* **No Virtual Environment Required:** Because this script only uses standard libraries, you do not need to set up a virtual environment (venv) to run it safely.

## How to Run It

1. Save the code in a file named `password_generator.py`.
2. Open your CLI (Terminal on Mac/Linux, or Command Prompt/PowerShell on Windows).
3. Navigate to the folder where you saved the file.
4. Run the following command directly (no `venv` activation needed):

```bash
python password_generator.py
```

> [Note]
> You may need to use `python3` instead of `python` depending on how your Mac/Linux system is configured.

*The script will prompt you for your preferences right there in the console and output your secure password immediately.*

## Example from CLI Output

```text
--- Secure Password Generator ---

Enter the desired password length (min 8): 30
Include special characters? (y/n): y
Include numbers? (y/n): y

Generated Password: 8Orh5'CfzP"Vn(>snwbvI[b5'5S\*u
Status: Password is strong. ✅

```

## ⚠️ Disclaimer

> [!CAUTION]
> This is provided "as-is" without any warranty of any kind. I am not responsible for any issues, data loss, or other problems that may arise from using this project. (code-related or otherwise) **Use it at your own risk**.
