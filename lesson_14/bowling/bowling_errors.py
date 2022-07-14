# TODO файл с ошибками обычно называют просто exceptions, реже errors


# TODO 4 одинаковых класса с разными сообщениями?
#  почему не сделать базовый класс и передавать ему проблемный символ, если в этом есть нужда
#  в 4х наследуемых просто менять сообщение?
#  вспомни про атрибут класса

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

    def __init__(self, *args):  # TODO где то я это уже видел
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):  # TODO где то я это уже видел
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
            # TODO message - аргумент который ты передаешь в ошибку,
            #  не проще ли передавать проблемный символ, а полное сообщение хранить в атрибуте классе?
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
