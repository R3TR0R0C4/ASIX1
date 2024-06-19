import unittest
#import Examen_sol as Examen
import Examen

class TestExamen(unittest.TestCase):
    def test_exercici1(self):
        self.assertEqual(Examen.generarArray(2, 3), [2,2,2])
        self.assertEqual(Examen.generarArray(2, 0), [])
        self.assertEqual(Examen.generarArray(8, 9), [8,8,8,8,8,8,8,8,8])
        self.assertEqual(Examen.generarArray(5, 'abc'), 'Paràmetre no permès') 
        self.assertEqual(Examen.generarArray([], 2), [[],[]])
        self.assertEqual(Examen.generarArray([1,2], 2), [[1,2],[1,2]])
        self.assertEqual(Examen.generarArray('abc', 2), ['abc','abc'])

    
    def test_exercici2(self):
        self.assertEqual(Examen.mediana([1,1]), 1)
        self.assertEqual(Examen.mediana([0]), 0)
        self.assertEqual(Examen.mediana([1,2,3]), 2)
        self.assertEqual(Examen.mediana([3,1,2]), 2)
        self.assertEqual(Examen.mediana([2,4,4,3,1]), 3)
        self.assertEqual(Examen.mediana([1,2,3,4,5,6]), 3.5)
        self.assertEqual(Examen.mediana([4,2,3,1,6,5]), 3.5)
        self.assertEqual(Examen.mediana([2,3,-100000,4,5,6]), 3.5)
        self.assertEqual(Examen.mediana([6,7,3,8,-100000,2,3,4,5,6]), 4.5)
        self.assertEqual(Examen.mediana([-100000,1000000000000, 1]), 1)
        self.assertEqual(Examen.mediana([]), 'Llista buida!')
    
    def test_exercici3(self):
        self.assertEqual(Examen.replicar([1,1], 1), [1,1])
        self.assertEqual(Examen.replicar([1,1], 2), [1,1,1,1])
        self.assertEqual(Examen.replicar([1,2,3], 0), [])
        self.assertEqual(Examen.replicar([1,2,3], 5), [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3])
        self.assertEqual(Examen.replicar([1,2,3], 'abc'), 'Paràmetre no permès') 
        self.assertEqual(Examen.replicar([1,'abc',3], 2), [1,1,'abc','abc',3,3])
        self.assertEqual(Examen.replicar([1,[1,2],3], 3), [1,1,1,[1,2],[1,2],[1,2],3,3,3])     
