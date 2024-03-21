import datetime

def czyPrzestepny(rok):
  if rok % 400 == 0 and rok % 100 == 0:
    return True 
  elif rok % 4 == 0 and rok % 100 != 0:
    return True
  else:
    return False
    
def addToFile(name,rok):
  lista=[]
  for i in range(12):
    miesiac=i+1
    dzien=0
    if miesiac==1:
      dzien=30
    if miesiac==2 and czyPrzestepny(rok):
      dzien=28
    if miesiac==2 and not czyPrzestepny(rok):
      dzien=27
    if miesiac==3:
      dzien=30
    if miesiac==4:
      dzien=29
    if miesiac==5:
      dzien=30
    if miesiac==6:
      dzien=29
    if miesiac==7:
      dzien=30
    if miesiac==8:
      dzien=30
    if miesiac==9:
      dzien=29
    if miesiac==10:
      dzien=30
    if miesiac==11:
      dzien=29
    if miesiac==12:
      dzien=30
      
    if miesiac<10:
        miesiac=str("0"+str(miesiac))
    else:
        miesiac=str(miesiac) 
    if int(dzien)<10:
        dzien="0"+str(dzien)
    print (rok, miesiac, dzien)
    f0.write("BEGIN:VEVENT\n")
    f0.write("DTSTART:"+str(rok)+str(miesiac)+str(dzien)+"T070000Z\n")
    f0.write("DTEND:"+str(rok)+str(miesiac)+str(dzien)+"T080000\n")
    f0.write("DTSTAMP:20240101T125937Z\n")
    f0.write("UID:\n")
    f0.write("CLASS:PRIVATE\n")
    f0.write("CREATED:20240101T125437Z\n")
    f0.write("DESCRIPTION:\n")
    f0.write("LAST-MODIFIED:20240101T125437Z\n")
    f0.write("LOCATION:\n")
    f0.write("SEQUENCE:0\n")
    f0.write("STATUS:CONFIRMED\n")
    f0.write("SUMMARY:"+name+"\n")
    f0.write("TRANSP:TRANSPARENT\n")
    f0.write("BEGIN:VALARM\n")
    f0.write("ACTION:DISPLAY\n")
    f0.write("DESCRIPTION:This is an event reminder\n")
    f0.write("TRIGGER:-P0DT17H0M0S\n")
    f0.write("END:VALARM\n")
    f0.write("END:VEVENT\n")

if __name__ == "__main__":
  f0 = open("gaz.ics", "w")

  f0.write("BEGIN:VCALENDAR\n")
  f0.write("PRODID:-//Google Inc//Google Calendar 70.9054//EN\n")
  f0.write("VERSION:2.0\n")
  f0.write("CALSCALE:GREGORIAN\n")
  f0.write("METHOD:PUBLISH\n")
  f0.write("X-WR-CALNAME:GAZ\n")
  f0.write("X-WR-TIMEZONE:Europe/Warsaw\n")

  currentDateTime = datetime.datetime.now()
  date = currentDateTime.date()
  rok = int(date.strftime("%Y"))
  addToFile("GAZ",rok)
          

  f0.write("END:VCALENDAR")
  f0.close()
