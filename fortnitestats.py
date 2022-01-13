from tkinter import *
import tkinter
from tkinter.font import BOLD
import tkinter.font
import requests
from bs4 import BeautifulSoup

HEIGHT = 600
WIDTH = 600

app = Tk()
app.title("Tayler's Fortnite Stats")
#app.resizable(False, False)


def format_reponse(doc):
    try:
        username = doc.find(class_="card-title").string

        kills = doc.find(class_='f-4-label', text = "KILLS").string
        killsparent = doc.find(class_='f-4-label', text = "KILLS").parent
        killsvalue = killsparent.find(class_='f-4-size-and-color').string

        wins = doc.find(class_='f-4-label', text = "WINS").string
        winsparent = doc.find(class_='f-4-label', text = "WINS").parent
        winsvalue = winsparent.find(class_='f-4-size-and-color').string

        winrate = doc.find(class_='f-4-label', text = "WIN %").string
        winrateparent = doc.find(class_='f-4-label', text = "WIN %").parent
        winratevalue = winrateparent.find(class_='f-4-size-and-color').string

        KD = doc.find(class_='f-4-label', text = "K/D").string
        KDparent = doc.find(class_='f-4-label', text = "K/D").parent
        KDvalue = KDparent.find(class_='f-4-size-and-color').string

        timeplayed = doc.find(class_="f-input__label", text = "TIME PLAYED").string
        timeplayedparent = doc.find(class_="f-input__label", text = "TIME PLAYED").parent
        timeplayedvalue = timeplayedparent.find(class_='f-2-size-and-color').string

        solo_matches = doc.find(class_="text-success-font-and-color mr-2", text = "MATCHES PLAYED").string
        solo_matchesparent = doc.find(class_="text-success-font-and-color mr-2", text = "MATCHES PLAYED").parent
        solo_matchesvalue = solo_matchesparent.find(class_='text-nowrap-and-color').string
        solo_matchesvalueint = int(solo_matchesvalue.replace(",",""))

        duo_matches = doc.findAll(class_="text-success-font-and-color mr-2", text = "MATCHES PLAYED")[1].string
        duo_matchesparent = doc.findAll(class_="text-success-font-and-color mr-2", text = "MATCHES PLAYED")[1].parent
        duo_matchesvalue = duo_matchesparent.find(class_="text-nowrap-and-color").string
        duo_matchesvalueint = int(duo_matchesvalue.replace(",",""))

        squad_matches = doc.findAll(class_="text-success-font-and-color mr-2", text = "MATCHES PLAYED")[2].string
        squad_matchesparent = doc.findAll(class_="text-success-font-and-color mr-2", text = "MATCHES PLAYED")[2].parent
        squad_matchesvalue = squad_matchesparent.find(class_="text-nowrap-and-color").string
        squad_matchesvalueint = int(squad_matchesvalue.replace(",",""))

        totalmatchesplayed = solo_matchesvalueint + duo_matchesvalueint + squad_matchesvalueint

        solo_outlived = doc.find(class_="text-success-font-and-color mr-2", text = "PLAYERS OUT LIVED").string
        solo_outlivedparent = doc.find(class_="text-success-font-and-color mr-2", text = "PLAYERS OUT LIVED").parent
        solo_outlivedvalue = solo_outlivedparent.find(class_='text-nowrap-and-color').string
        solo_outlivedvalueint = int(solo_outlivedvalue.replace(",",""))

        duo_outlived = doc.findAll(class_="text-success-font-and-color mr-2", text = "PLAYERS OUT LIVED")[1].string
        duo_outlivedparent = doc.findAll(class_="text-success-font-and-color mr-2", text = "PLAYERS OUT LIVED")[1].parent
        duo_outlivedvalue = duo_outlivedparent.find(class_="text-nowrap-and-color").string
        duo_outlivedvalueint = int(duo_outlivedvalue.replace(",",""))

        squad_outlived = doc.findAll(class_="text-success-font-and-color mr-2", text = "PLAYERS OUT LIVED")[2].string
        squad_outlivedparent = doc.findAll(class_="text-success-font-and-color mr-2", text = "PLAYERS OUT LIVED")[2].parent
        squad_outlivedvalue = squad_outlivedparent.find(class_="text-nowrap-and-color").string
        squad_outlivedvalueint = int(squad_outlivedvalue.replace(",",""))

        total_outlived = solo_outlivedvalueint + duo_outlivedvalueint + squad_outlivedvalueint


        usernamestring = username.replace("\n", "")
        usernamestringfinal = usernamestring.replace(" ", "")

        winratevaluestring = winratevalue.replace("\n","")
        winratevaluestringfinal = winratevaluestring.replace(" ","")

        winsvaluestring = winsvalue.replace("\n","")
        winsvaluestringfinal = winsvaluestring.replace(" ","")

        killsvaluestring = killsvalue.replace("\n","")
        killsvaluestringfinal = killsvaluestring.replace(" ","")

        KDvaluestring = KDvalue.replace("\n","")
        KDvaluestringfinal = KDvaluestring.replace(" ","")

        timeplayedvaluestring = timeplayedvalue.replace("\n", "")
        timeplayedvaluestringfinal = timeplayedvaluestring.replace(" ", "").split("H")[0]
        timeplayedvaluestringfinal2 = timeplayedvaluestring.replace(" ", "").split("H")[1]

        finalstr = f"Username: {usernamestringfinal} \nKills: {killsvaluestringfinal} \nWins: {winsvaluestringfinal} \nWinrate: {winratevaluestringfinal}% \nK/D: {KDvaluestringfinal} \nTime Played: {timeplayedvaluestringfinal}H {timeplayedvaluestringfinal2} \nTotal Matches Played: {'{:,}'.format(totalmatchesplayed)} \nTotal Players Outlived: {'{:,}'.format(total_outlived)}"
    
    except:

        finalstr = 'There was an error retrieving \nthe information.'

    return finalstr


def get_stats(name):
    url = f"https://fortnitetracker.gg/profile/v2/{name}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    label['text'] = format_reponse(doc)
    


canvas = Canvas(app, height= HEIGHT, width= WIDTH)
canvas.pack()

'''IMAGEURL = "https://imgur.com/M40ALt4"
u = urlopen(IMAGEURL)
raw_data = u.read()
u.close()'''

background_img = PhotoImage(file = 'D:\Python Projects\Hypixel\sky3.png')
background_label = Label(app, image = background_img)
background_label.place(x = 0, y = 0, relwidth=1, relheight=1)

frame = Frame(app, bg = '#000000', bd=5)
frame.place(relx=0.5 , rely = 0.1 ,relheight= 0.1, relwidth= 0.75, anchor='n')

entry = Entry(frame, font = ('Verdana', 18), foreground= "white", bg = "black", insertbackground= "white")
entry.place(relwidth=0.67, relheight= 1)

button = Button(frame, text = "Get Stats", font = ('Verdana', 12,'bold'), bg = 'black', foreground = 'white', activebackground = "White",command = lambda: get_stats(entry.get()))
button.place(relx = 0.7,relwidth=0.3, relheight=1)


lower_frame = Frame(app, bg ='#000000', bd=10)
lower_frame.place(relx =0.5, rely = 0.25, relwidth= 0.75, relheight= 0.6, anchor= 'n')


label = Label(lower_frame, font = ('Verdana', 18), anchor= 'nw', justify = 'left', bd = 4, background='black', foreground= 'white')
label.place(relwidth= 1, relheight=1)

#rank.tag_configure("red", foreground="red")

app.mainloop()

