# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 14:53:16 2022

@author: santi
"""
from excepciones import NotZeroError as NZE
from calculadora_imc import CalculadoraIMC
calculado = False
while not calculado:
        try: 
            peso = float(input("Ingrese su peso en kg: "))
            altura = float(input("Ingrese su altura en m: "))
            calculadora = CalculadoraIMC(peso,altura)
            calculadora.peso = peso
            calculadora.altura = altura
        except NZE as msg:
            print("Ingreso un dato incorrecto,", msg)
        except ValueError as msg:
            print ("Ingreso un dato incorrecto,", msg)
        else:
            print("Su IMC es de: ", calculadora.imc)
            print("Su condicion hes: ", calculadora.condicion)
            calculado = True
        