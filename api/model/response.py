
class Response():
    def __init__(self, score, label, class_, datetime):
        self.response = {
            "score": score,
            "label": label,
            "class": class_,
            "started_datetime": datetime
        }