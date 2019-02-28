import collections
from src.slide import Slide


def group_vertical(vphotos):
    pairs = []
    for i in range(len(vphotos)):
        if i % 100 == 0:
            print(i)
        for j in range(i + 1, len(vphotos)):
            pairs.append((vphotos[i], vphotos[j], len(vphotos[i].tags.intersection(vphotos[j].tags))))

    pairs = sorted(pairs, key=lambda x: x[2], reverse=False)

    used = set()
    slides = []
    for pair in pairs:
        if pair[0] not in used and pair[1] not in used:
            slides.append(Slide([pair[0], pair[1]], is_vertical=True))
            used.add(pair[0])
            used.add(pair[1])

    """
    slides = collections.deque([pairs[0][0], pairs[0][1]])

    for pair in pairs[1:]:
        if slides[0] == pair[0]:
            slides.appendleft(pair[1])
        elif slides[0] == pair[1]:
            slides.appendleft(pair[0])
        elif slides[-1] == pair[0]:
            slides.append(pair[1])
        elif slides[-1] == pair[1]:
            slides.append(pair[0])
            """

    return slides


def create_slideshow(slides):
    # Start with two highest scores at middle
    slideshow = collections.deque([slides[0]])

    slides = set(slides[1:])
    i = 0

    while len(slides) > 0:
        i += 1
        if i % 100 == 0:
            print(i, len(slides))

        if i == 10000:
            return slideshow

        found = False
        for slide in slides:
            left_score = slide.score(slideshow[0])
            right_score = slide.score(slideshow[-1])
            if left_score > 0 or right_score > 0:
                if left_score > right_score:
                    slideshow.appendleft(slide)
                else:
                    slideshow.append(slide)

                found = True
                slides.remove(slide)
                break

        if not found:
            slideshow.append(slides.pop())

    return slideshow

