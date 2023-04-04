
import unittest

def decimal_a_romano(decimal):
    if  decimal <= 3:
        return 'I' * decimal
    if decimal == 5:
        return 'V'
    if decimal == 10:
        return "X"
    if decimal == 4:
        return"IV"
    if decimal >5 and decimal <9:
        return ( "V" + "I"*(decimal-5))
    if decimal == 9:
        return "IX"
    
    if decimal > 10:
        decimal == "X" 
        


    
    



class TestDecimalARoman(unittest.TestCase):
    def test_1(self):
        # pre condicion
        ### NO HAY ###
        # proceso
        resultado = decimal_a_romano(1)
        # verificacion
        self.assertEqual(resultado, 'I')

    def test_10(self):
        resultado = decimal_a_romano(10)
        self.assertEqual(resultado, 'X')
    
    def test_5(self):
        resultado = decimal_a_romano(5)
        self.assertEqual(resultado, 'V')

    def test_2(self):
        resultado = decimal_a_romano(2)
        self.assertEqual(resultado, 'II')

    def test_3(self):
        resultado = decimal_a_romano(3)
        self.assertEqual(resultado, 'III')

    def test_4(self) :
        resultado = decimal_a_romano(4)
        self.assertEqual(resultado,"IV") 
        
    def test_6(self) :
        resultado = decimal_a_romano(6)
        self.assertEqual(resultado,"VI") 

    def test_7(self) :
        resultado = decimal_a_romano(7)
        self.assertEqual(resultado,"VII")     

    def test_8(self) :
        resultado = decimal_a_romano(8)
        self.assertEqual(resultado,"VIII") 

    def test_9(self) :
        resultado = decimal_a_romano(9)
        self.assertEqual(resultado,"IX") 
    
    




if __name__ == '__main__':
    unittest.main()