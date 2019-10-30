"""The Module Has Been Built for the Counting Calls to functions."""


class CallCount:
    """The Module Has Been Built for the Counting Calls to functions."""

    def __init__(self, f):
        """The Counting Calls Initializer."""
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        """The Counting Calls call counter."""
        self.count += 1
        print("{} Counter: {} & args: {} & kwargs: {}".format(self.f.__name__,
                                                              self.count,
                                                              self.f(*args),
                                                              self.f(**kwargs)
                                                              ))
        return self.f(*args, **kwargs)
