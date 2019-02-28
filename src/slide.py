class Slide:

    def __init__(self, p, is_vertical=False):
        self.is_vertical = is_vertical
        if is_vertical:
            self.v = p
            self.h = None
        else:
            self.h = p
            self.b = None

    def get_tags(self):
        if self.is_vertical:
            return self.v[0].tags.union(self.v[1].tags)
        else:
            return self.h.tags

    def score(self, slide):
        first = self.get_tags().intersection(slide.get_tags())
        second = self.get_tags().difference(slide.get_tags())
        third = slide.get_tags().difference(self.get_tags())
        return min(len(first), len(second), len(third))

    def __str__(self):
        return "Slide: " + (str(self.v[0]) + ", " + str(self.v[1]) if self.is_vertical else str(self.h))
