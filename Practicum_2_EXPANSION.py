def main():
    h = 0
    while h == 0:
        h = int(input("Wat is de hoogte van de ruimte? "))
        if h == 0:
            print("Input is ongeldig")
    b = 0
    while b == 0:
        b = int(input("Wat is de breedte van de ruimte? "))
        if b == 0:
            print("Input is ongeldig")
    else:
        het_doolhof = creeerDoolhof(h, b)
        acties(h, b, het_doolhof)

def creeerDoolhof(hoogte, breedte):
    doolhof = []
    kader_rij_lijst = [" ", " "]
    for i in range(breedte):
        kader_rij_lijst.insert(i+1, "-")
    doolhof.append(kader_rij_lijst)
    for i in range(hoogte):
        rij_lijst = ["|", "|"]
        for j in range(breedte):
            rij_lijst.insert(j+1, ".")
        doolhof.append(rij_lijst)
    doolhof.append(kader_rij_lijst)
    return(doolhof)

def acties(h, b, doolhof):
    print("Acties:")
    print("1. Doolhof tonen")
    print("2. Muren plaatsen")
    print("3. Korste pad bepalen")
    print("4. Standaard doolhof laden")
    print("5. \"Onoplosbaar\" doolhof laden")
    print("6. Voorbeeld doolhof laden")
    print("7. Standaard doolhof Uitbreiding laden")
    print("8. Voorbeeld doolhof Uitbreiding laden")
    print("9. Nieuw doolhof aanmaken")
    print("0. Afsluiten")
    keuze=int(input("Keuze? "))
    if keuze == 1:
        toonDoolhof(h,doolhof)
        acties(h,b,doolhof)
    if keuze == 2:
        posities = input("Op welke posities wil u muren plaatsen (komma's tussen de x- en y-coördinaten, spaties tussen de coördinatenparen)? ")
        posities_lijst = posities.split(" ")
        for i in range (len(posities_lijst)):
            coordinaten_set = posities_lijst[i].split(",")
            if int(coordinaten_set[0])+1>b or int(coordinaten_set[0])<0 or int(coordinaten_set[1])+1>h or int(coordinaten_set[1])<0:
                print("Coördinatenpaar #"+str(i+1)+" is ongeldig")
                posities_lijst[i] = ["-1","-1"]
            else:
                posities_lijst[i] = coordinaten_set
        doolhof = voegMuurToe(doolhof,posities_lijst)
        print("Muren geplaatst!")
        toonDoolhof(h,doolhof)
        acties(h, b, doolhof)
    if keuze == 3:
        correcteStart = False
        while correcteStart == False:
            start = input("Wat is de startpositie? ")
            start_lijst = start.split(",")
            sx = int(start_lijst[0])
            sy = int(start_lijst[1])
            correcteStart = check(sx+1, sy+1, doolhof, h, b)
            if correcteStart == False:
                print("Ongeldige coördinaten")
        correcteEnd = False
        while correcteEnd == False:
            einde = input("Wat is de eindpositie? ")
            einde_lijst = einde.split(",")
            ex = int(einde_lijst[0])
            ey = int(einde_lijst[1])
            correcteEnd = check(ex+1, ey+1, doolhof, h, b)
            if correcteEnd == False:
                print("Ongeldige coördinaten")
        if sx == ex and sy == ey:
            print("Start- en eindpositie vallen samen.")
            print("De afstand is dus 0.")
        else:
            geefKortstePad(sx, sy, ex, ey, doolhof, h, b)
        acties(h, b, doolhof)
    if keuze == 4:
        h = 10
        b = 10
        doolhof = creeerStandaardDoolhof()
        toonDoolhof(h,doolhof)
        acties(h,b,doolhof)
    if keuze == 5:
        h = 3
        b = 3
        doolhof = creeerOnoplosbaarDoolhof()
        toonDoolhof(h,doolhof)
        acties(h, b, doolhof)
    if keuze == 6:
        h=7
        b=12
        doolhof=creeerVoorbeeldDoolhof()
        toonDoolhof(h, doolhof)
        acties(h, b, doolhof)
    if keuze == 7:
        h=5
        b=5
        doolhof=creeerStandaardDoolhofUitbreiding()
        toonDoolhof(h,doolhof)
        acties(h,b,doolhof)
    if keuze == 8:
        h=4
        b=4
        doolhof=creeerVoorbeeldDoolhofUitbreiding()
        toonDoolhof(h,doolhof)
        acties(h,b,doolhof)
    if keuze == 9:
        nieuwe_h = False
        while nieuwe_h == False:
            h = int(input("Wat is de hoogte van de ruimte? "))
            if h == 0:
                print("Input is ongeldig")
            else:
                nieuwe_h = True
        nieuwe_b = False
        while nieuwe_b == False:
            b = int(input("Wat is de breedte van de ruimte? "))
            if b == 0:
                print("Input is ongeldig")
            else:
                nieuwe_b = True
        doolhof = creeerDoolhof(h, b)
        toonDoolhof(h, doolhof)
        acties(h, b, doolhof)
    if keuze == 0:
        print("Programma beëindigd")
    if keuze not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("Ongeldige keuze")
        acties(h,b,doolhof)

def check(x,y,doolhof,h,b):
    if doolhof[y][x] == "*" or doolhof[y][x] == "|" or x > b or y > h:
        return False
    else:
        return True

def toonDoolhof(hoogte,doolhof):
    toon_doolhof = doolhof.copy() #een kopie van het doolhof zodat de structuur niet aangepast wordt.
    for i in range(hoogte+2):
        toon_doolhof[i] = "".join(toon_doolhof[i])
    for i in range(len(toon_doolhof)):
        print(toon_doolhof[i])

def voegMuurToe(doolhof,posities_lijst):
    for i in range(len(posities_lijst)):
        temp = posities_lijst[i]
        x = int(temp[0]) + 1
        y = int(temp[1]) + 1
        if x>0 and y>0:
            doolhof[y][x] = "*"
    return(doolhof)

def geefKortstePad(sx,sy,ex,ey,doolhof,h,b):
    paden = []
    Pad_doolhof = doolhof.copy()
    pad=[[sx+1,sy+1]]
    Pad_doolhof[sy+1][sx+1]="S"
    Pad_doolhof[ey+1][ex+1]="F"
    vindPad(pad,Pad_doolhof,sx+1,sy+1,h,b,paden)
    if len(paden)==0:
        toonDoolhof(h, Pad_doolhof)
        print("Er is geen oplossing voor dit doolhof.")
    else:
        kader=[]
        HetPad = paden[0]
        for s in HetPad:
            x = int(s[0])
            y = int(s[1])
            if Pad_doolhof[y][x] == "." :
                Pad_doolhof[y][x] = "O"
            elif Pad_doolhof[y][x] == "|" or Pad_doolhof[y][x] == "-":
                kader.append([x,y])
        toonDoolhof(h, Pad_doolhof)
        for k in kader:
            if k in HetPad:
                HetPad.remove(k)
        K = len(HetPad) - 1
        print("De kortste afstand tussen punten (" + str(sx) + "," + str(sy) + ") en (" + str(ex) + "," + str(
            ey) + ") is " + str(K))

def vindPad(pad, doolhof, x, y,h,b,paden):
    stap = MogelijkeStap(doolhof, x, y, pad,paden)
    L = len(paden)
    if stap == Opgelost:
        if L < 1:
            paden.append(pad)
        if L >= 1:
            if len(pad) < len(paden[0]):
                paden.pop(0)
                paden.append(pad)
    elif stap != Onmogelijk:
        stappen = VolgendeStap(x,y,h,b)
        nieuw_pad = creeerPad(pad,stappen)
        for p in nieuw_pad:
            vindPad(p, doolhof, p[-1][0], p[-1][1], h, b, paden)

Onmogelijk = 3
Verderdoen = 4
Opgelost = 5

def MogelijkeStap(doolhof,x,y,pad,paden):
    padw = pad[0:-1]
    D = doolhof[y][x]
    if D == "F":
        return Opgelost
    elif D == "*"  or [x, y] in padw:
        return Onmogelijk
    elif len(paden) > 0:
        if len(pad) > len(paden[0]):
            return Onmogelijk
    else:
        return Verderdoen

def VolgendeStap(x, y, h, b):
    Stappen = []
    if x != 0:
        Stappen.append([x-1, y])
    else:
        Stappen.append([b,y])
    if y != 0:
        Stappen.append([x, y-1])
    else:
        Stappen.append([x,h])
    if x != b+1:
        Stappen.append([x+1, y])
    else:
        Stappen.append([1,y])
    if y != h+1:
        Stappen.append([x, y+1])
    else:
        Stappen.append([x,1])
    return Stappen

def creeerPad(pad, stappen):
    v = []
    for s in stappen:
        nieuwPad = list(pad)
        nieuwPad.append(s)
        v.append(nieuwPad)
    return(v)

def creeerStandaardDoolhof(): #start = 0,2 & finish = 7,7
    doolhof = []
    kader_rij_lijst = [" ", " "]
    for i in range(10):
        kader_rij_lijst.insert(i + 1, "-")
    doolhof.append(kader_rij_lijst)
    for i in range(10):
        rij_lijst = ["|", "|"]
        for j in range(10):
            rij_lijst.insert(j + 1, ".")
        doolhof.append(rij_lijst)
    doolhof.append(kader_rij_lijst)
    muren=[['3', '0'], ['3', '1'], ['1', '2'], ['3', '2'], ['5', '2'], ['6', '2'], ['7', '2'], ['8', '2'], ['1', '3'], ['1', '4'], ['3', '4'], ['4', '4'], ['9', '4'], ['4', '5'], ['1', '6'], ['4', '6'], ['6', '6'], ['7', '6'], ['8', '6'], ['1', '7'], ['4', '7'], ['6', '7'], ['1', '8'], ['6', '8']]
    doolhof = voegMuurToe(doolhof,muren)
    return(doolhof)

def creeerOnoplosbaarDoolhof(): #start = 0,1 & finish = 2,1
    doolhof = []
    kader_rij_lijst = [" ", " "]
    for i in range(3):
        kader_rij_lijst.insert(i + 1, "-")
    doolhof.append(kader_rij_lijst)
    for i in range(3):
        rij_lijst = ["|", "|"]
        for j in range(3):
            rij_lijst.insert(j + 1, ".")
        doolhof.append(rij_lijst)
    doolhof.append(kader_rij_lijst)
    muren = [['1', '0'], ['1', '1'], ['1', '2']]
    doolhof = voegMuurToe(doolhof, muren)
    return (doolhof)

def creeerVoorbeeldDoolhof(): #start = 0,2 & finish = 11,4
    doolhof = []
    kader_rij_lijst = [" ", " "]
    for i in range(12):
        kader_rij_lijst.insert(i + 1, "-")
    doolhof.append(kader_rij_lijst)
    for i in range(7):
        rij_lijst = ["|", "|"]
        for j in range(12):
            rij_lijst.insert(j + 1, ".")
        doolhof.append(rij_lijst)
    doolhof.append(kader_rij_lijst)
    muren = [['4', '0'], ['5', '0'], ['1', '1'], ['2', '1'], ['4', '1'], ['7', '1'], ['9', '1'], ['10', '1'], ['11', '1'], ['1', '2'], ['7', '2'], ['3', '3'], ['4', '3'], ['10', '3'], ['1', '4'], ['2', '4'], ['3', '4'], ['7', '4'], ['10', '4'], ['3', '5'], ['5', '5'], ['7', '5'], ['9', '5'], ['10', '5'], ['0', '6'], ['1','6'], ['5', '6']]
    doolhof = voegMuurToe(doolhof, muren)
    return (doolhof)

def creeerStandaardDoolhofUitbreiding():
    doolhof = []
    kader_rij_lijst = [" ", " "]
    for i in range(5):
        kader_rij_lijst.insert(i + 1, "-")
    doolhof.append(kader_rij_lijst)
    for i in range(5):
        rij_lijst = ["|", "|"]
        for j in range(5):
            rij_lijst.insert(j + 1, ".")
        doolhof.append(rij_lijst)
    doolhof.append(kader_rij_lijst)
    muren = [['1', '1'], ['2', '1'], ['2', '2'], ['3', '2'], ['2', '4']]
    doolhof = voegMuurToe(doolhof, muren)
    return (doolhof)

def creeerVoorbeeldDoolhofUitbreiding():
    doolhof = []
    kader_rij_lijst = [" ", " "]
    for i in range(4):
        kader_rij_lijst.insert(i + 1, "-")
    doolhof.append(kader_rij_lijst)
    for i in range(4):
        rij_lijst = ["|", "|"]
        for j in range(4):
            rij_lijst.insert(j + 1, ".")
        doolhof.append(rij_lijst)
    doolhof.append(kader_rij_lijst)
    muren = [['1', '1'], ['2', '1'], ['1', '2'], ['1', '3']]
    doolhof = voegMuurToe(doolhof, muren)
    return doolhof

main()