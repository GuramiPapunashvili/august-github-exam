def is_divisible(*arg):
    for i in arg:
        if arg[0] % i != 0:
            return False
    return True