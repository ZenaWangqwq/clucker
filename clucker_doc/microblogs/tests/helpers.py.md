# helpers.py

## ClassDef LogInTester

The function of the class is to test if the user is logged in or not.

**Attributes**:

- client (`type`): This attribute represents the client session, which contains information about the current logged-in user.

**Functions**:

- `_is_logged_in(self)`: -> `bool`
    - Parameters:
        - self (`type`): The instance of the class.
    - Returns:
        - `bool`: A boolean value indicating whether the user is logged in or not.

**Code Description**: This function checks if a specific session key '_auth_user_id' exists in the client's session. If it does, it means the user is logged in, and the function returns True; otherwise, it returns False.

**Note**: The return value of this function can be used to determine whether the current user is logged in or not, which can be useful in various scenarios.

**Input Example**: This function does not require any input, as it operates solely on the client's session information.

**Output Example**: The output of this function will be a boolean value indicating whether the user is logged in (True) or not (False).