class MyClass:
    
    static = 'figure'
    
    def __init__(self, state):
        self.state = state

    def static_print(self):
       print(self.static)
    
    @classmethod
    def change_static(cls):
        cls.static = 'Programmer'

obj1 = MyClass(True)
obj2 = MyClass(False)

obj1.change_static()

obj1.static_print()
obj2.static_print()
