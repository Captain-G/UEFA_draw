import random
# group winners
manCity = {
    "name": "Man City",
    "position": 1,
    "country": "England",
    "group": "A"
}
ajax = {
    "name": "Ajax",
    "position": 1,
    "country": "Netherlands",
    "group": "C"
}
realMadrid = {
    "name": "Real Madrid",
    "position": 1,
    "country": "Spain",
    "group": "D"
}
bayern = {
    "name": "Bayern",
    "position": 1,
    "country": "Germany",
    "group": "E"
}
juventus = {
    "name": "Juventus",
    "position": 1,
    "country": "Italy",
    "group": "H"
}
liverpool = {
    "name": "Liverpool",
    "position": 1,
    "country": "England",
    "group": "B"
}
lille = {
    "name": "Lille",
    "position": 1,
    "country": "France",
    "group": "G"
}
manUnited = {
    "name": "Man United",
    "position": 1,
    "country": "England",
    "group": "F"
}

# runners up
atletico = {
    "name": "Atletico",
    "position": 2,
    "country": "Spain",
    "group": "B"
}
benfica = {
    "name": "Benfica",
    "position": 2,
    "country": "Portugal",
    "group": "E"
}
chelsea = {
    "name": "Chelsea",
    "position": 2,
    "country": "England",
    "group": "H"
}
inter = {
    "name": "Inter",
    "position": 2,
    "country": "Italy",
    "group": "D"
}
psg = {
    "name": "PSG",
    "position": 2,
    "country": "France",
    "group": "A"
}
salzburg = {
    "name": "Salzburg",
    "position": 2,
    "country": "Austria",
    "group": "G"
}
sporting = {
    "name": "Sporting",
    "position": 2,
    "country": "Portugal",
    "group": "C"
}
villareal = {
    "name": "Villareal",
    "position": 2,
    "country": "Spain",
    "group": "F"
}
runnersUp = [villareal, sporting, chelsea, psg, salzburg, benfica, atletico, inter]
groupWinners = [manCity, ajax, realMadrid, juventus, lille, liverpool, bayern, manUnited]
# startDraw = input("Press any key to start draw : ").lower()
startDraw = "a"
if startDraw.isalnum():
    while True:
        for i in range(8):
            w1 = random.choice(groupWinners)
            r1 = random.choice(runnersUp)
            if w1["country"] == r1["country"]:
                for j in range(5):
                    r1 = random.choice(runnersUp)
                    if w1["country"] != r1["country"]:
                        break
            if w1["group"] == r1["group"]:
                for j in range(5):
                    r1 = random.choice(runnersUp)
                    if w1["group"] != r1["group"]:
                        break
            w1Index = groupWinners.index(w1)
            r1Index = runnersUp.index(r1)
            groupWinners.pop(w1Index)
            runnersUp.pop(r1Index)
            print(w1["name"] + " vs " + r1["name"])
        break






