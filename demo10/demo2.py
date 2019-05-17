#单元测试
import unittest

class Arithmetic_Operation:
    number1 = 0
    number2 = 0
    def __init__(self, n1, n2):
        self.number1 = n1
        self.number2 = n2
    def jiafa(self):
        return self.number1+self.number2
    def jianfa(self):
        return self.number1-self.number2
    def chengfa(self):
        return self.number1*self.number2
    def chufa(self):
        if self.number2 == 0:
            return -1
        else:
            return self.number1/self.number2

class Test_Arithmetic_Operation(unittest.TestCase):
    def test_jiafa(self):
        a = Arithmetic_Operation(1, 2)
        self.assertEqual(a.jiafa(), 3)


if __name__ == "__main__":
    unittest.main()
