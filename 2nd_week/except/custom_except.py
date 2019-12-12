class NetworkError(RuntimeError):
    def __init__(self, arg):
        self.arg = arg
    """
    def __str__(self):
        return str(self.args)
    """
    """
    def __str__(self):
        return self.arg
    """


def connect():
    raise NetworkError("Bad hostname")

try:
    connect()
except NetworkError as err:
    print(err)
