# Password Generator

This Python script generates strong, customizable passwords based on user-specified criteria. It ensures the generated password meets certain complexity requirements and allows the user to approve the password before it's accepted.

## Features

* **Customizable Length:** The user can specify the desired length of the password (between 8 and 16 characters).
* **Constraint-Based Generation:** The script allows users to specify the minimum number of digits, special characters, uppercase letters, and lowercase letters in the password.
* **Acceptable Symbols:** Uses a custom set of acceptable symbols for password generation (`!@#$%^&*-_=+?:;.'`).
* **Strong Randomness:** Employs the `secrets` module for cryptographically secure random character selection.
* **User Approval:**  The generated password is presented to the user for approval. If the user doesn't like the password, a new one is generated until the user approves.
* **Recursive Password Generation:** The `check_password` function uses recursion to regenerate passwords until the user is satisfied.

## How to Use

1.  **Save the code:** Save the Python code as a `.py` file (e.g., `password_generator.py`).
2.  **Run the script:** Open a terminal or command prompt and navigate to the directory where you saved the file. Then, execute the script using `python password_generator.py`.
3.  **Follow the prompts:** The script will prompt you to enter the desired password length and will then generate a password. You'll be asked to approve the generated password. If you don't approve, a new password will be generated.

## Requirements

*   Python 3.6 or higher (due to the use of f-strings).

## Code Explanation

*   **`generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1)`:** This function generates the password. It takes optional arguments to customize the password complexity.  It uses a `while True` loop to keep generating passwords until all constraints are met.
*   **`check_password(new_password)`:** This function presents the generated password to the user and asks for approval. It uses recursion to call `generate_password` if the user doesn't approve.
*   **Character Sets:** The script uses `string.ascii_letters`, `string.digits`, and a custom set of punctuation characters to build the character pool for password generation.
*   **Constraints:** The `constraints` list defines the regular expressions used to check if the generated password meets the specified criteria.
*   **`secrets.choice()`:** This function from the `secrets` module is used to ensure the generated password is cryptographically secure.
