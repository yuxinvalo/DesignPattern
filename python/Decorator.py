from datetime import datetime
from functools import wraps

def log(func):
    def wrapper(*args, **kw):
        print("call %s()" % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def printTime():
    print(str(datetime.now()))

printTime()

'''Second example'''

KEY = 0
def key_required(func):
    @wraps(func)
    def wrapper(*args, **kw):
        if args[0].key != KEY:
            print("Failed unlock.")
            raise Exception("You have no right key.")
        else:
            return func(*args, **kw)
    return wrapper

class Lock(object):
    def __init__(self, key):
        self.key = key

    @key_required
    def unlock(self):
        print("Unlock successfully.")

lock = Lock(0)
lock.unlock()
print("change a key")
lock = Lock(1)
lock.unlock()
