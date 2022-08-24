# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 16:45:30 2022

@author: santi
"""
print('Ingrese su peso en kg')
peso = float(input ())
print ('Ingrese su altura en metros: ')
altura = float(input ())
IMC = peso/(altura**2)
print ('Peso: ',peso,'kg')
print ('Altura: ', altura, 'm')
print ('IMC: ', IMC)
