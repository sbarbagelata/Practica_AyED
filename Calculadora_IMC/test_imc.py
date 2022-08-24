# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 15:56:30 2022

@author: santi
"""
from excepciones import NotZeroError as NZE
from calculadora_imc import CalculadoraIMC
import unittest

class TestIMC(unittest.TestCase):
    def setUp(self):
        print ("Corre SetUp")
        calc = CalculadoraIMC(70, 1.70)
    def test_imc(self):
        