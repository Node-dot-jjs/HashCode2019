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
    pairs = []
    slide_sums = [0 for _ in range(len(slides))]

    for i in range(len(slides)):
        for j in range(len(slides)):
            score = slides[i].score(slides[j])
            slide_sums[i] += score

            pairs.append((slides[i], slides[j], score))

    slides_scores = [(slides[i], slide_sums[i]) for i in range(0, len(slides))]
    slides_scores = sorted(slides_scores, key=lambda x: x[1], reverse=True)

    print("Calculated scores")

    # Start with two highest scores at middle
    slideshow = collections.deque([slides_scores[0][0], slides_scores[1][0]])

    remaining_ss = slides_scores[2:]
    while len(remaining_ss) > 0:
        best = remaining_ss[0]
        best_val = 0

        for ss in remaining_ss:
            score_left = ss[0].score(slideshow[0])
            score_right = ss[0].score(slideshow[-1])

            if max(score_left, score_right) > best_val:
                best = ss
                best_val = max(score_left, score_right)

        best_left = best[0].score(slideshow[0])
        best_right = best[0].score(slideshow[-1])
        if best_left > best_right:
            slideshow.appendleft(best[0])
        else:
            slideshow.append(best[0])

        remaining_ss.remove(best)

    return slideshow
