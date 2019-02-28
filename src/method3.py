import collections
from src.slide import Slide
import src.method1 as m1


def group_vertical(vphotos):
    return m1.group_vertical(vphotos)


def create_slideshow(slides):
    slideshow = []

    for i in range(0, len(slides), 100):
        print("Section", i)
        ss = m1.create_slideshow(slides[i:i+100])
        slideshow = slideshow + list(ss)

    return slideshow
