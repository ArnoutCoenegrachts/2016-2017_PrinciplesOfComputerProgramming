#variabelen
import datetime
uren = datetime.datetime.now().time().hour
mins = datetime.datetime.now().time().minute
uren2=0
from graphics import GraphicsWindow
win=GraphicsWindow(200,200)
canvas=win.canvas()
error=True

from math import cos, sin, pi
#input
    #2 mogelijkheden: 'systeemtijd' en 'tijdstip kiezen'
tijd=str(input("'systeemtijd' of 'tijdstip kiezen'? "))
    #2 mogelijkheden: '12'formaat en '24'formaat
formaat=str(input("'12'-or '24'-uren formaat? "))


#systeemtijd
if tijd=="systeemtijd":
    if formaat=="12":
        error=False
        if uren>12:
            uren2=uren-12
        else:
            uren2=uren
        canvas.drawText(85, 25, "12am")
        canvas.drawText(30, 133, "6am")
        canvas.drawText(155, 133, "6pm")
        if uren < 10:
            if mins < 10:
                canvas.drawText(87, 145, "0" + str(uren2) + ":0" + str(mins)+" am")
            if mins >= 10:
                canvas.drawText(87, 145, "0" + str(uren2) + ":" + str(mins)+" am")
        if uren > 12:
            if mins < 10:
                canvas.drawText(87, 145, str(uren2) + ":0" + str(mins)+" pm")
            if mins >= 10:
                canvas.drawText(87, 145,str(uren2) + ":" + str(mins) + " pm")
        if uren<=12:
            if mins<10:
                canvas.drawText(87, 145, str(uren2) + ":0" + str(mins) + " am")
            if mins>=10:
                canvas.drawText(87, 145, str(uren2) + ":" + str(mins) + " am")

    if formaat=="24":
        error=False
        canvas.drawText(95, 25, "12")
        canvas.drawText(40, 133, "6")
        canvas.drawText(155, 133, "18")
        if uren < 10:
            if mins < 10:
                canvas.drawText(87, 145, "0" + str(uren) + ":0" + str(mins))
            if mins >= 10:
                canvas.drawText(87, 145, "0" + str(uren) + ":" + str(mins))
        if uren >= 10:
            if mins < 10:
                canvas.drawText(87, 145, str(uren) + ":0" + str(mins))
            if mins >= 10:
                canvas.drawText(87, 145, str(uren) + ":" + str(mins))

#tijdstip kiezen
if tijd=="tijdstip kiezen":
    uren=int(input("Typ het uur: ")) #enkel het uur, niet de minuten
    mins=int(input("Typ de minuten: ")) #enkel de minuten, mins<60
    if mins >= 60:
        uren = uren + 1
        mins = mins - 60
    if uren >= 24:
        uren = uren - 24
    if formaat=="12":
        error=False
        if uren>12:
            uren2=uren-12
        else :
            uren2=uren
        canvas.drawText(85, 25, "12am")
        canvas.drawText(30, 133, "6am")
        canvas.drawText(155, 133, "6pm")
        if uren2 < 10:
            if mins < 10:
                if uren<=12:
                    canvas.drawText(87, 145, "0" + str(uren2) + ":0" + str(mins) + " am")
                if uren>12:
                    canvas.drawText(87, 145, str(uren2) + ":0" + str(mins) + " pm")
            if mins >= 10:
                if uren<=12:
                    canvas.drawText(87, 145, "0" + str(uren2) + ":" + str(mins) + " am")
                if uren>12:
                    canvas.drawText(87, 145,str(uren2) + ":" + str(mins) + " pm")
        if uren2 >= 10:
            if mins < 10:
                canvas.drawText(87, 145, str(uren) + ":0" + str(mins) + " am")
            if mins >= 10:
                canvas.drawText(87, 145, str(uren) + ":" + str(mins) + " am")
    if formaat=="24":
        error=False
        canvas.drawText(95, 25, "12")
        canvas.drawText(40, 133, "6")
        canvas.drawText(155, 133, "18")
        if uren < 10:
            if mins < 10:
                canvas.drawText(87, 145, "0" + str(uren) + ":0" + str(mins))
            if mins >= 10:
                canvas.drawText(87, 145, "0" + str(uren) + ":" + str(mins))
        if uren >= 10:
            if mins < 10:
                canvas.drawText(87, 145, str(uren) + ":0" + str(mins))
            if mins >= 10:
                canvas.drawText(87, 145, str(uren) + ":" + str(mins))

x1=0
y1=0
R=45
hoek=0
if error==True:
    print("input error: please try again")
if error==False:
    canvas.drawRect(50, 40, 100, 100)
    m=(uren*60+mins)-360
    hoek=pi-m*(pi/720)
    x1=100+R*cos(hoek)
    y1=140-R*sin(hoek)
    if uren > 6 and uren < 18:
        canvas.drawLine(100,140,x1,y1)

win.wait()