class Singleton :
    """class decorator to make any class be singleton, not in multi-threads"""
    def __init__(self, cls):
        """cls is a class"""
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            """_instance is the only one who is instanced"""
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        """ can't be directely called """
        raise TypeError('Singleton must be called by Instance()')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)

@Singleton
class A:
    def __init__(self):
        pass
    def display(self):
        return id(self)

s1 = A.Instance()
s2 = A.Instance()
print(s1, s1.display())
print(s2, s2.display())
print(s1 is s2)

"""
output:
(<__main__.A instance at 0x7fceabcc1878>, 140525622270072)
(<__main__.A instance at 0x7fceabcc1878>, 140525622270072)
True
"""
