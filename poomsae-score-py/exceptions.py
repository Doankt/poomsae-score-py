class InvalidEmail(Exception):
    def __init__(self, iemail):
        Exception.__init__(self)
        self.message = '{} is not a valid email'.format(iemail)

    def __str__(self):
        return self.message


class EmailAlreadyExists(Exception):
    def __init__(self, email):
        Exception.__init__(self)
        self.message = 'Email: {} is already taken'.format(email)

    def __str__(self):
        return self.message


class UserAlreadyExists(Exception):
    def __init__(self, username):
        Exception.__init__(self)
        self.message = 'Username: {} is already taken'.format(username)

    def __str__(self):
        return self.message


class UserDoesNotExist(Exception):
    def __init__(self, username):
        Exception.__init__(self)
        self.message = 'Username: {} does not exist'.format(username)

    def __str__(self):
        return self.message
