# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:01:47 2017

@author: AbdelrahmanHussein
"""

print "======== TESTING simple_lesk ===========\n"
from wsd.lesk_algorithms import simple_lesk
from wsd.readxml import readinputfile as rf
print "#TESTING simple_lesk() ..."
print "Context:", rf()
answer = simple_lesk(rf(),'union')
print "Sense:", answer
definition = answer[1].definition() 

print "Definition:", definition
print

print "#TESTING simple_lesk() with POS ..."
print "Context:", rf()
answer = simple_lesk(rf(),'medicine','n')
print "Sense:", answer
definition = answer[1].definition() 

print "Definition:", definition
print




