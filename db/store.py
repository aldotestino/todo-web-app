class Store:
    def __init__(self):
        self.list = []

    def get(self):
        return self.list

    def getOne(self, id):
        for item in self.list:
            if item.id == id:
                return item
        raise Exception('Todo not found')

    def add(self, item):
        self.list.append(item)

    def updateOne(self, id):
        for item in self.list:
            if item.id == id:
                item.update()
                return item
        raise Exception('Todo not found')

    def deleteOne(self, id):
        for item in self.list:
            if item.id == id:
                deleted = item
                self.list.remove(item)
                return deleted
        raise Exception('Todo not found')

todos = Store()