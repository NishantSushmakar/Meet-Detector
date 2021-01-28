# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:32:32 2021

@author: nishant
"""
from googletrans import Translator



def cvt_to_en(text):
    translator = Translator()
    translated  = translator.translate(text,dest='en')
    return translated.text


text = 'Aap Kaise ho'
print(cvt_to_en(text))