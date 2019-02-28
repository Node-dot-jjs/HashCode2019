from src.photo import Photo
from src.slide import Slide
from src.method4 import group_vertical, create_slideshow
import random


def load_input(f):
    vphotos = []
    hphotos = []

    with open(f) as file:
        photo_id = -1
        for line in file:
            if photo_id != -1:  # Skip first
                line = line.strip()
                line_split = line.split(' ')
                tags = line_split[2:]

                photo = Photo(photo_id, line_split[0], set(tags))
                if line_split[0] == 'V':
                    vphotos.append(photo)
                else:
                    hphotos.append(photo)

            photo_id += 1

    return vphotos, hphotos


def score(slideshow):
    ss_score = 0
    for i in range(0, len(slideshow) - 2):
        ss_score += slideshow[i].score(slideshow[i + 1])

    return ss_score


b = "../input/b_lovely_landscapes.txt"
c = "../input/c_memorable_moments.txt"
d = "../input/d_pet_pictures.txt"

vphotos, hphotos = load_input(b)

vslides = group_vertical(vphotos)  # Method
hslides = []
for hphoto in hphotos:
    hslides.append(Slide(hphoto, is_vertical=False))

slides = vslides + hslides
random.shuffle(slides)

print("Created slides")
print("Original score", score(slides))

slideshow = create_slideshow(slides)

print("Created slideshow")
print("Score: ", score(slideshow))

with open('../output/output.txt', 'w') as output:
    output.write(str(len(slideshow)) + "\n")
    for slide in slideshow:
        if slide.is_vertical:
            output.write(str(slide.v[0].photo_id) + " " + str(slide.v[1].photo_id) + "\n")
        else:
            output.write(str(slide.h.photo_id) + "\n")



