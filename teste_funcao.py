import unittest
from Funcao import transpor_acorde

class TestTransporAcorde(unittest.TestCase):
	def test_transpor_acorde(self):
		self.assertEqual(transpor_acorde("C", 2), "D")

	def test_transpor_acorde_nota_invalida(self):
		with self.assertRaises(ValueError):
			transpor_acorde("H", 2)

	def test_transpor_acorde_tipo_invalido(self):
		with self.assertRaises(TypeError):
			transpor_acorde(1, 2)

if __name__ == "__main__":
	unittest.main()