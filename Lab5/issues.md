

# Lab 5 — Static Code Analysis Issues

| Issue | Type | Line(s) in Original Code | Description | Fix Approach |
|---|---|---|---|---|
| Shell command execution using `os.system()` | Security — High | 31 | Executing a shell command with input concatenated into the command can expose the program to command injection. | Replaced shell execution with Python's `print()` function. |
| Weak MD5 hash | Security — High | 16 | MD5 is considered weak for security-sensitive hashing. | Replaced MD5 with SHA-256. |
| Possible SQL injection | Security — Medium | 11 | SQL values were inserted into a query using string formatting instead of parameters. | Replaced string construction with a parameterized SQL query. |
| Missing module and function docstrings | Code quality | Multiple | Missing documentation makes the code harder to understand and maintain. | Added a module docstring and function docstrings. |
| Function names not in snake_case | Code quality / Style | Multiple | CamelCase names do not follow Python's conventional naming style. | Renamed functions to use snake_case. |
| Comparison with `None` using `==` | Code quality / Style | 36 | Direct equality comparison with `None` is discouraged. | Changed the comparison to `fat is None`. |
| Unused import | Code quality | 2 | The unused `json` import adds unnecessary clutter. | Removed the unused import. |
| Long lines and indentation issues | Style | Multiple | Long lines and incorrect indentation reduce readability and violate style checks. | Wrapped statements and corrected indentation. |

## Verification

- Pylint: target score above 9.5/10.
- Bandit: no reported security issues.
- Flake8: no reported style violations.

