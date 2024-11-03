class MyClass:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

my_object = MyClass(42)


def introspection_info(obj):
    info = {}
    # Получение типа объекта
    info['type'] = type(obj)
    # Получение имени типа объекта
    info['type_name'] = type(obj).__name__
    # Получение атрибутов объекта
    info['attributes'] = vars(obj)
    # Получение методов объекта
    info['methods'] = dir(obj)
    # Получение модуля, к которому объект принадлежит
    info['module'] = obj.__module__
    return info


if __name__ == '__main__':
    number_info = introspection_info(my_object)
    print(number_info)
