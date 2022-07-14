class IncorrectSymbolError(ValueError):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'IncorrectSymbolError {self.message}'
        else:
            return 'IncorrectSymbolError has been raised'


class BackSlashInFirstThrowError(ValueError):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'BackSlashInFirstThrowError {self.message}'
        else:
            return 'BackSlashInFirstThrowError has been raised'


class XInSecondThrowError(ValueError):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'XInSecondThrowError {self.message}'
        else:
            return 'XInSecondThrowError has been raised'


class ExcessSkittlesError(ValueError):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'ExcessSkittlesError {self.message}'
        else:
            return 'ExcessSkittlesError has been raised'
