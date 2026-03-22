class SingleMeta(type):
    def __init__(cls, *args, **kwargs):
        cls._instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class SinglePerson(object, metaclass=SingleMeta):
    pass



if __name__ == '__main__':
    p1 = SinglePerson()
    p2 = SinglePerson()

    print(id(p1), id(p2))

    print(p1 is p2)
    print(p1 == p2)