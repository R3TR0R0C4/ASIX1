import unittest
import operacions
class Testoperacions(unittest.TestCase):
    def test_parell(self):
        self.assertTrue(operacions.parell(4))
        self.assertTrue(operacions.parell(2))
        self.assertFalse(operacions.parell(3))
        self.assertFalse(operacions.parell(-3))
        self.assertTrue(operacions.parell(0))
        self.assertTrue(operacions.parell(-4))
        self.assertEqual(operacions.parell("AAAA"),"Entrada no vàlida")

    def test_quadrat(self):
        self.assertEqual(operacions.quadrat(5), 25)
        self.assertEqual(operacions.quadrat(-3), 9)
        self.assertEqual(operacions.quadrat(0), 0)
        self.assertEqual(operacions.parell("AAAA"),"Entrada no vàlida")
    
    def test_cubic(self):
        self.assertEqual(operacions.cubic(5), 125)
        self.assertEqual(operacions.cubic(-3), -27)
        self.assertEqual(operacions.cubic(0), 0)
        self.assertEqual(operacions.cubic("AAAA"),"Entrada no vàlida")
    
    def test_cubic(self):
        self.assertEqual(operacions.saluda("pepe"),"Hello, pepe")
        self.assertEqual(operacions.saluda(111),"Entrada no vàlida")
