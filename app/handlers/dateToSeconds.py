from datetime import datetime
import pytz


class DateToSeconds:
    
    def getSeconds(self, birthDate: datetime) -> int:
        today: datetime = datetime.now(pytz.timezone('Europe/Stockholm')) #.strftime("%Y-%m-%d %H:%M:%S")
        #print(today)
        #print(birthDate)
        birthDate = birthDate.astimezone(pytz.timezone('Europe/Stockholm'))
        delta = today-birthDate
        return delta.total_seconds()
        