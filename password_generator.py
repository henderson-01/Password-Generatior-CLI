import secrets
import string


def generate_password(
    length: int = 12, include_special: bool = True, include_numbers: bool = True
) -> str:
    """Generates a cryptographically secure random password, guaranteeing requested character types."""
    if length < 4:
        raise ValueError(
            "Password length should be at least 4 characters to meet constraints."
        )

    # Character pool
    characters = string.ascii_letters
    if include_special:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits

    # Loop to generate a password that actually contains the required character types
    while True:
        password = "".join(secrets.choice(characters) for _ in range(length))

        # Verify the password meets our minimum requirements
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_special = (
            any(c in string.punctuation for c in password) if include_special else True
        )
        has_number = any(c.isdigit() for c in password) if include_numbers else True

        if has_lower and has_upper and has_special and has_number:
            return password


def validate_password(
    password: str, require_special: bool = True, require_numbers: bool = True
) -> bool:
    """Validates if a password meets modern security complexity requirements based on constraints."""
    if len(password) < 8:
        return False

    # Check against a few common weak patterns
    weak_patterns = ["123456", "password", "qwerty", "admin"]
    if any(pattern in password.lower() for pattern in weak_patterns):
        return False

    # Ensure complexity
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)

    # Only mandate special/digit if they were requested
    has_digit = any(c.isdigit() for c in password) if require_numbers else True
    has_special = (
        any(c in string.punctuation for c in password) if require_special else True
    )

    # all() returns True only if every condition inside the list is True
    return all([has_lower, has_upper, has_digit, has_special])


if __name__ == "__main__":
    print("\n--- Secure Password Generator ---")

    # Error handling for user input
    try:
        password_length = int(input("\nEnter the desired password length (min 8): "))
        if password_length < 8:
            print("Length too short. Forcing length to 8 for security.")
            password_length = 8
    except ValueError:
        print("Invalid input detected. Using default length of 12.")
        password_length = 12

    # Yes and No is (y/n)
    include_special = (
        input("Include special characters? (y/n): ").strip().lower() == "y"
    )
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == "y"

    # Generate the password
    new_password = generate_password(password_length, include_special, include_numbers)
    print(f"\nGenerated Password: {new_password}")

    # Validate the generated password using the same rules
    if validate_password(new_password, include_special, include_numbers):
        print("Status: Password is strong. ✅\n")
    else:
        print("Status: Password is weak. ⚠️\n")
