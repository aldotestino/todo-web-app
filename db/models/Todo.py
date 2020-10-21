from uuid import uuid4


class Todo():
    def __init__(self, content, date, done=False):
        self.id = str(uuid4())
        self.content = content
        self.done = done
        self.date = date

    def update(self):
        self.done = not(self.done)

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "done": self.done,
            "date": self.date
        }
