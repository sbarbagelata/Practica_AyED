# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 14:41:52 2022

@author: santi
"""
from excepciones import NotZeroError as NZE
class CalculadoraIMC:
    """Clase par calcular el IMC a partir de peso en kg y altura en m"""
    def __init__(self, pPeso, pAltura):
        self.peso = pPeso
        self.altura = pAltura
    @property
    def peso(self):
        return self.peso
    @peso.setter
    def peso(self, pvalor):
        if pvalor <= 0:
           raise NZE ("el dato incorrecto es: Peso")
        elif type(pvalor) != float:
            raise ValueError ("dato mal ingresado: Peso")
        else:
            self._peso = pvalor
    @property
    def altura(self):
        return self.altura
    @altura.setter
    def altura (self, avalor):
        if avalor <= 0:
            raise NZE ("el dato incorrecto es: Altura")
        elif type(avalor) != float:
            raise ValueError("dato mal ingresado: Altura")
        else:
            self._altura = avalor
    @property
    def imc(self):
        self._imc = float(self._peso/(self._altura**2))
        return (round(self._imc,2))
    @property
    def condicion(self):
        if self._imc < 18.5:
            return ("El imc indica 'Debajo de lo normal'")
        elif 18.5 < self._imc < 25:
            return ("El imc indica 'Normal'")
        elif 25 < self._imc < 30:
            return ("El imc indica 'Sobrepeso'")
        elif self._imc > 30:
            return ("El imc indica 'Obesidad'")
        
    