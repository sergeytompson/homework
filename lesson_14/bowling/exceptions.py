# TODO файл с ошибками обычно называют просто exceptions, реже errors


# TODO 4 одинаковых класса с разными сообщениями?
#  почему не сделать базовый класс и передавать ему проблемный символ, если в этом есть нужда
#  в 4х наследуемых просто менять сообщение?
#  вспомни про атрибут класса


class BowlingException(ValueError):

    default_message = None

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'{self.message}'
        else:
            return self.default_message


class IncorrectSymbolException(BowlingException):

    default_message = 'Некорректный символ. Значение должно включать: 123456789, X (большая английская икс) ,' \
                   '/ (обратный слеш) и - (тире).'

    def __init__(self, *args):
        super().__init__(*args)


class BackSlashInFirstThrowException(BowlingException):

    default_message = 'Символ / не может быть результатом первого броска в фрейме'

    def __init__(self, *args):
        super().__init__(*args)


class XInSecondThrowException(BowlingException):

    default_message = 'Символ X не может быть результатом второго броска в фрейме'

    def __init__(self, *args):
        super().__init__(*args)


class ExcessSkittlesException(BowlingException):

    default_message = 'Сумма очков за 2 броска не может быть больше 9'

    def __init__(self, *args):
        super().__init__(*args)
