# helpers.py

## LogInTester ClassDef

The function of the class is to test whether a user is logged in or not.

**Attributes**:

- None

**Functions**:

- `_is_logged_in` (`self`, `type`) -> `bool`
    - Parameters:
        - `self` (`object`): The instance of the LogInTester class.
    - Returns:
        - `bool`: A boolean value indicating whether the user is logged in or not.

The `_is_logged_in` function checks if a session key '_auth_user_id' exists in the client's session. If it does, it means the user is logged in; otherwise, the user is not logged in.

**Code Description**: The LogInTester class provides a method to determine whether a user is logged in or not based on the presence of the '_auth_user_id' key in their session.

**Note**: This function can be used to verify login status before performing any actions that require a logged-in user.

No input or output examples are provided as this is a utility class and does not accept any inputs.