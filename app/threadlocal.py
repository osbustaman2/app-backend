import threading
from functools import wraps


threadlocal = threading.local()


class thread_local(object):

    def __init__(self, **kwargs):
        self.options = kwargs

    def __enter__(self):
        for attr, value in self.options.items():
            setattr(threadlocal, attr, value)

    def __exit__(self, exc_type, exc_value, traceback):
        for attr in self.options.keys():
            setattr(threadlocal, attr, None)

    def __call__(self, test_func):

        @wraps(test_func)
        def inner(*args, **kwargs):
            # the thread_local class is also a context manager
            # which means it will call __enter__ and __exit__
            with self:
                return test_func(*args, **kwargs)

        return inner


def get_thread_local(attr, default=None):
    """ use this method from lower in the stack to get the value """
    return getattr(threadlocal, attr, default)