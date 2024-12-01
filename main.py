class Human:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def __len__(self):
        return self.age
        
    def __del__(self):
        print(f"{self.name} is gone")
        
den = Human('Denis', 32)

print(den.name)
print(den.age)
den.age += 10
print(den.age)
# input()
print(len(den))