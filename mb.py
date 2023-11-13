from ma import Parent


class Second(Parent):
    ...

class B(Second):
    def fnc(self, a: int, b: int):
        return a * b * self.i