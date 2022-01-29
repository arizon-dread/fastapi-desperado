from app.models.desperado import Desperado
from ..models.desperado import Desperado
class TextManipulator:
    
    def transform(self, input: Desperado):
        responseText: str = ""
        text = input.text
        for c in text:
            responseText += self.getCharOrText(c)
        response = Desperado(text=responseText)
        
        return response

    def getCharOrText(self,c):
        if (c in "bcdfghjklmnpqrstvxz"):
            return c+"o"+c
        elif (c in "BCDFGHJKLMNPQRSTVXZ"):
            return c+"o"+c.lower()
        else:
            return c