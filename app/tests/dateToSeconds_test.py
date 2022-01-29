from datetime import datetime, timedelta
import unittest
from ..handlers.dateToSeconds import DateToSeconds 
from ..models.birthdaySeconds import BirthdaySeconds
class TestDateToSeconds(unittest.TestCase):
    dateToSeconds = DateToSeconds()
    birthdaySeconds = BirthdaySeconds()
    def test_getSeconds(self):
        self.birthdaySeconds.birthday = datetime.now()
        date2 = datetime(self.birthdaySeconds.birthday.year, 
                         self.birthdaySeconds.birthday.month, 
                         self.birthdaySeconds.birthday.day-1, 
                         self.birthdaySeconds.birthday.hour, 
                         self.birthdaySeconds.birthday.minute, 
                         self.birthdaySeconds.birthday.second)
        
        delta = self.dateToSeconds.getSeconds(date2)
        self.assertAlmostEquals(delta.__int__(), 86400)
        