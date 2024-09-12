

class Pet(object):
    __instance = None

    @classmethod
    def Clear(cls):
        cls.__instance = None

    @classmethod
    def get_id(cls):
        return id(cls.__instance)

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            print("Питомец создан.")
        return cls.__instance

    def __init__(self, name: str):
        print("Питомец инициализирован.")
        self.name = name

    def __del__(self):
        print("Питомец удалён.")


p = Pet("Барсик")
p = Pet("Муся")
Pet.Clear()
del p

print("Ура!")