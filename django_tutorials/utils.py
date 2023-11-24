def random_string(length):
    """
    :param length: size of the string
    :return: random string token
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))