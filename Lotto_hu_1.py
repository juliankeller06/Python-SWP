import random


def ziehe_lottozahlen():

    gezogene_zahlen = []

    while len(gezogene_zahlen) < 6:
        zahl = random.randint(1, 45)
        if zahl not in gezogene_zahlen:
            gezogene_zahlen.append(zahl)


    gezogene_zahlen.sort()
    return gezogene_zahlen

lottozahlen = ziehe_lottozahlen()

c = range(10)

print("Lottozahlen:", lottozahlen)
