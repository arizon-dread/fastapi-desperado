
from datetime import datetime
from pydantic import BaseModel

class BirthdaySeconds(BaseModel):
    birthday: datetime = datetime.now()
    birthdaySeconds: int = 0