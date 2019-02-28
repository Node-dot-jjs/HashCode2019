class Photo:

    def __init__(self, photo_id, ori, tags):
        self.photo_id = photo_id
        self.ori = ori
        self.tags = tags

    def __str__(self):
        return str(self.photo_id) + " | " + self.ori + " | " + str(self.tags)

    def __eq__(self, other):
        return self.photo_id == other.photo_id

    def __hash__(self):
        return self.photo_id
