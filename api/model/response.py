import json

class Response():
    def __init__(self, score, label, class_):
        self.score = score
        self.label = label
        self.object_class = class_
    
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)