class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, type_name):
        self.kind = type_name


class EventSet:
    def __init__(self, value):
        self.kind = value


class NullHandler:
    def __init__(self, successor=None):
        # передаём следующее звено
        self.__successor = successor

    def handle(self, obj, event):  # обработчик
        if self.__successor is not None:  # даём следующему
            self.__successor.handle(obj, event)
        return None


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event.kind, int):
            obj.integer_field = event.kind
            return

        elif event.kind == int:
            return obj.integer_field

        else:
            super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event.kind, float):
            obj.float_field = event.kind
            return

        elif event.kind == float:
            return obj.float_field

        else:
            super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event.kind, str):
            obj.string_field = event.kind
            return

        elif event.kind == str:
            return obj.string_field

        else:
            super().handle(obj, event)


if __name__ == '__main__':
    chain = IntHandler(FloatHandler(StrHandler(NullHandler())))
    obj1 = SomeObject()
    obj1.integer_field = 42
    obj1.float_field = 3.14
    obj1.string_field = "some text"
    print(chain.handle(obj1, EventGet(int)))
    print(chain.handle(obj1, EventGet(float)))
    print(chain.handle(obj1, EventGet(str)))
    chain.handle(obj1, EventSet(100))
    print(chain.handle(obj1, EventGet(int)))
    chain.handle(obj1, EventSet(0.5))
    print(chain.handle(obj1, EventGet(float)))
    chain.handle(obj1, EventSet('new text'))
    print(chain.handle(obj1, EventGet(str)))
