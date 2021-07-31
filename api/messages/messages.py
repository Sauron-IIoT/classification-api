from enum import Enum, unique

@unique
class Messages(Enum):
    BAD_REQUEST = "Bad request"

class ResolveMessage():
    def some_behavior(self):
        pass