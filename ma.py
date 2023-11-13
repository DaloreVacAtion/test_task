class Parent:
    def __init__(self, i: int=3):
        self.i  = i

    def isFirst(self):
        return issubclass(self.__class__, First)

    @property
    def isSecond(self):
        from mb import Second
        return issubclass(self.__class__, Second)

    def fnc(self, a: int):
        return a**2 * self.i


class First(Parent):
    ...


class A(First):
    def fnc(self, a: int):
        if a ==7:
            raise MyError('Error text')
        return super().fnc(a)

class MyError(Exception):
    pass