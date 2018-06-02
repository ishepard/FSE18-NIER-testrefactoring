total_nof = []
total_nom = []
total_wmc = []
total_loc = []

with open("total_results.txt", "r") as f:
    for line in f:
        nof, nom, wmc, loc = line.strip().split(",")

        total_nof.append(nof)
        total_nom.append(nom)
        total_wmc.append(wmc)
        total_loc.append(loc)


HVL = 0
HL = 0
HM = 0
HH = 0
MVL = 0
ML = 0
MM = 0
MH = 0
LVL = 0
LL = 0
LM = 0
LH = 0
VLVL = 0
VLL = 0
VLM = 0
VLH = 0

for row in total_nof:
    if row == "HIGH:HIGH":
        HH +=1
    if row == "HIGH:MEDIUM":
        HM += 1
    if row == "HIGH:LOW":
        HL += 1
    if row == "HIGH:VERY_LOW":
        HVL += 1
    if row == "MEDIUM:HIGH":
        MH += 1
    if row == "MEDIUM:MEDIUM":
        MM += 1
    if row == "MEDIUM:LOW":
        ML += 1
    if row == "MEDIUM:VERY_LOW":
        MVL += 1
    if row == "LOW:HIGH":
        LH += 1
    if row == "LOW:MEDIUM":
        LM += 1
    if row == "LOW:LOW":
        LL += 1
    if row == "LOW:VERY_LOW":
        LVL += 1
    if row == "VERY_LOW:HIGH":
        VLH += 1
    if row == "VERY_LOW:MEDIUM":
        VLM += 1
    if row == "VERY_LOW:LOW":
        VLL += 1
    if row == "VERY_LOW:VERY_LOW":
        VLVL += 1

print(HVL,
        HL,
        HM,
        HH,
        MVL,
        ML,
        MM,
        MH,
        LVL,
        LL,
        LM,
        LH,
        VLVL,
        VLL,
        VLM,
        VLH)