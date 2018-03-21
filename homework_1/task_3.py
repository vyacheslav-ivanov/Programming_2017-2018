class UniqObject:
    obj = None
    def __init__(self):
        if self.obj is not None:
            return "Object has been created already"

    @classmethod
    def create_object(cls):
        if cls.obj is None:
            cls.obj = UniqObject()
        return cls.obj


singletone = UniqObject()
print(singletone.create_object())
    
