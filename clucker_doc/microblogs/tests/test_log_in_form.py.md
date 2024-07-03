# test_log_in_form.py

## ClassDef LogInFormTestCase

The function of the class is to test the log in form.

**Attributes**:

- `form_input` (`dict`): A dictionary containing username and password as inputs for the form.

**Functions**:

- `test_forms_contains_required_fields` ()
    - Parameters: None
    - Returns: None
    - Description: This function tests if the log in form contains required fields, including 'username' and 'password'.

- `test_form_acceptes_valid_input` (data: `dict`)
    - Parameters:
        - data (`dict`): A dictionary containing username and password as inputs for the form.
    - Returns: None
    - Description: This function tests if the log in form accepts valid input, including a username and password.

- `test_form_rejects_blank_username` (data: `dict`)
    - Parameters:
        - data (`dict`): A dictionary containing username and password as inputs for the form.
    - Returns: None
    - Description: This function tests if the log in form rejects an attempt to submit a form with a blank username.

- `test_form_rejects_blank_password` (data: `dict`)
    - Parameters:
        - data (`dict`): A dictionary containing username and password as inputs for the form.
    - Returns: None
    - Description: This function tests if the log in form rejects an attempt to submit a form with a blank password.

- `test_form_accepts_incorrect_username` (data: `dict`)
    - Parameters:
        - data (`dict`): A dictionary containing username and password as inputs for the form.
    - Returns: None
    - Description: This function tests if the log in form accepts an incorrect username but still considers it valid.

- `test_form_accepts_incorrect_psw` (data: `dict`)
    - Parameters:
        - data (`dict`): A dictionary containing username and password as inputs for the form.
    - Returns: None
    - Description: This function tests if the log in form accepts an incorrect password but still considers it valid.

**Called_functions**: 

- No functions are called within this file.