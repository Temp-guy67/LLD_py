from threading import Lock

class ThreadSafeSingleton:
    _instance = None
    _lock = Lock()
    _initialized = False  # Custom flag to simulate private constructor

    def __new__(cls, *args, **kwargs):
        print("Getting called1 ")
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

    def __init__(self):
        
        if not getattr(self, '_initialized', False):
            # Only run initialization once
            self.value = 42
            self._initialized = True
            print("Getting called")

        


obj = ThreadSafeSingleton()
obj2 = ThreadSafeSingleton()
print(obj ==obj2)