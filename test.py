class User:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance

        return cls.__instance

    def __init__(self, *args, **kwargs) -> None:
        self.args = args
        # self.name = kwargs.get('name')
        # self.age = kwargs.get('age')
        for key, value in kwargs.items():
            setattr(self, key, value)
        

list = [1,2,3]
dict = {'name': "Micky", 'age': 42, 'gender': 'male'}

user1 = User(*list, **dict)
print(user1.args)   
print(user1.name)
print(user1.age)
print(user1.gender)

