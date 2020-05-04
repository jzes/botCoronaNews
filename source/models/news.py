
class New:
    def __init__(self, jsonData):
        self.title = jsonData['title']
        self.body = jsonData['snippet']
        self.link = jsonData['link']