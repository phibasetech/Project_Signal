class BaseFinder:
    """
    Base class for all Signal Finders.
    Defines the standard interface.
    """
    def __init__(self, name):
        self.name = name

    def scan(self, config):
        """
        The main scan method. Must be implemented by all subclasses.
        It should return a list of "signal" dictionaries.
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def _log(self, message):
        """Helper for logging."""
        print(f"  [{self.name}] {message}")