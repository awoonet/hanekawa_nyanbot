class DotDict(dict):
    """
    Special dict class for acessing dict elements like in js.

    Args:
        dict: python dict class
    """

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value
