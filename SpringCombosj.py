# Assignment
# File: 
# Date:    12/7/22
# By:      Jacob Freidline
# Section: 005
# Team:    259
# 
# ELECTRONIC SIGNATURE
# Jacob Freidline
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This script is a header template that will be used for 
# all your python files the rest of the semester.

import math

def Keqseries(K1,K2):
    Req = 1/((1/K1)+(1/K2))
    return Req

def F1series(Ftotal):
    Req = Ftotal
    return Req

def F2series(Ftotal):
    Req = Ftotal
    return Req

def X1series(K1,F1):
    Req = F1/K1
    return Req

def X2series(K2,F2):
    Req = F2/K2
    return Req

def Xtotalseries(Keq,Ftotal):
    Req = Keq/Ftotal
    return Req

def Keqparallel(K1,K2):
    Req = K1+K2
    return Req

def F1parallel(K1,X1):
    Req = K1*X1
    return Req

def F2parallel(K2,X2):
    Req = K2*X2
    return Req

def X1parallel(Xtotal):
    Req = Xtotal
    return Req

def X2parallel(Xtotal):
    Req = Xtotal
    return Req

def Xtotalparallel(Keq,Ftotal):
    Req = Keq/Ftotal
    return Req