import unittest
from ..handlers.textManipulator import TextManipulator
from ..models.desperado import Desperado


class TextManipulator_test(unittest.TestCase):
    
    def test_getText(self):
        textMnpltr = TextManipulator()
        text = textMnpltr.getCharOrText("c")
        self.assertEqual(text, "coc")
    def test_getChar(self):
        textMnpltr = TextManipulator()
        input: str = "o"
        text: str = textMnpltr.getCharOrText(input)
        self.assertEqual(text, "o")
    def test_transform(self):
        desperado = Desperado(text="test")
        textMnpltr = TextManipulator()
        output = textMnpltr.transform(desperado)
        self.assertEqual(output.text, 'totesostot')
if __name__ == '__main__':
    unittest.main()