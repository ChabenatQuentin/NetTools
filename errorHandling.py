class Error(Exception):
    pass


class ServCreationError(Error):
    def __init__(self, msg):
        super().__init__(msg)


class IncompatibleOsError(Error):
    def __init__(self, msg):
        super().__init__(msg)
