def is_valid_number(n):
    valid = True
    try:
        val = int(n)
        if not is_positive(val):
            valid = False
    except ValueError:
        valid = False
    return valid


def is_positive(num):
    if num > 0:
        return True
    else:
        return False
