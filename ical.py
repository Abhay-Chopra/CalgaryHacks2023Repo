from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime
from pathlib import Path
import os
import pytz

eventCal = Calendar()
eventCal.add('prodid', '-//CluBot//')
eventCal.add('version', '2.0')
set(pytz.all_timezones_set)  
class iCal:
    #date format yyyy/mm/dd, time is MST and 24 hour format
    def make_event(self, name, description, startTime, endTime, startDate, endDate):
        event = Event()
        startD = startDate.split("/")
        if((endDate is None)):
            endD = startDate.split("/")
        else:
            endD = endDate.split("/")
        startT = startTime.split(":")
        endT = endTime.split(":")
        try:
            if((startDate is None) or (startTime is None) or (endTime is None)):
                raise TypeError
            event.add('name', '{}'.format(name))
            event.add('description', '{}'.format(description))
            event.add('dtstart', datetime(int(startD[0]), int(startD[1]), int(startD[2]), int(startT[0]) + int(int(startT[1])/60), 0, 0, tzinfo=pytz.timezone('Canada/Mountain')))
            event.add('dtend', datetime(int(endD[0]), int(endD[1]), int(endD[2]), int(endT[0]) + int(int(endT[1])/60), 0, 0, tzinfo=pytz.timezone('Canada/Mountain')))
            eventCal.add_component(event)
        
        except TypeError:
            return None
        
        #returns an ical file
        return eventCal.to_ical()
    
    def makeICal(self):
        directory = Path.cwd() / 'MyCalendar'
        try:
            directory.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            print("Folder exists")
        
        f = open(os.path.join(directory, 'event.ics'), 'wb')
        f.write(eventCal.to_ical())
        f.close()
