from helpers import check

def test_password_validator():
    # no special chars, matching
    assert check("password", "password") == False

    # one special char, matching
    assert check("password!", "password!") == True

    # minimum length check
    assert check("foo", "foo") == False