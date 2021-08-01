
class Response():
    def __init__(self, score, label, class_):
        self.response = {
            "score": score,
            "label": label,
            "class": class_
        }