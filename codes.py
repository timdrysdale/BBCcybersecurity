# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 07:42:33 2016

@author: Tim Drysdale 24 March 2016

Selected answers to challenges posted here
http://www.bbc.co.uk/news/technology-34312697

"""

import numpy as np

'''
Helper functions
'''

def brute_shift_code(coded_word):
    letter_values = np.array([])
    
    for letter in coded_word:
        this_letter_value = ord(letter) - letterA
        # Assume capital letters for now      
      
        letter_values = np.append(letter_values, this_letter_value)
        
    for shift in np.arange(26):
        this_string = ''
        for letter in letter_values:
            shifted_letter = int(np.mod(letter+shift,26)) + letterA
            this_string = this_string + chr(shifted_letter)
        print shift, ':', this_string

def shift_only_letters(string, shift):
    letterA = 65
    letterZ = letterA + 26
    lettera = 97
    letterz = lettera + 26
    output = ''
    for symbol in string:
        val = ord(symbol) 
        if (val >= lettera) and (val <= letterz):
            char_num = val - lettera
            shift_char_num = int(np.mod(char_num + shift, 26)) + lettera
            output = output + chr(shift_char_num)
            #print chr(shift_char_num)
        elif (val >= letterA) and (val <= letterZ):
            char_num = val - letterA
            shift_char_num = int(np.mod(char_num + shift, 26)) + letterA
            output = output + chr(shift_char_num)
            #print chr(shift_char_num)
        else :
            output = output + chr(val)                
            
            
    return(output)

#challenge 2 - by inspection
print '-- challenge #2 ---'
print 'fibonaccisequence'


#Challenge 3 - brute force attack on Caesar shift
print ' '
print '-- challenge #3 ---'
letterA = 65

coded_word = 'XSKLVVOHHYLEV'        
brute_shift_code(coded_word)   

shift_val = 23
output = shift_only_letters(coded_word,shift_val)
print '\nShift is %d' % shift_val
print output    

#challenge 5 - use first letter of elements, referred to by number
print ' '
print '-- challenge #5 ---'
periodic = {'1': 'H', '2': 'He', '3': 'Li', '4':'Be', '5':'B', '6':'C', '7':'N',
            '8':'O', '9':'F', '10':'Ne', '11':'Na', '12':'Mg', '13':'Al', '14':'Si', '15':'P', '16':'S', 
            '17':'Cl', '18':'Ar', '19':'K', '20':'Ca', '21':'Sc', '22':'Ti', '23':'V', '24':'Cr', '25':'Mn', 
            '26':'Fe', '27':'Co', '28':'Ni', '29':'Cu', '30':'Zn', '31':'Ga', '32':'Ge', '33':'As', '34':'Se', 
            '35':'Br', '36':'Kr', '37':'Rb', '38':'Sr', '39':'Y', '40':'Zr', '41':'Nb', '42':'Mo', '43':'Tc', '44':'Ru', 
            '45':'Rh', '46':'Pd', '47':'Ag', '48':'Cd', '49':'In', '50':'Sn', '51':'Sb', '52':'Te', '53':'I', 
            '54':'Xe', '55':'Cs', '56':'Ba', '72':'Hf', '73':'Ta', '74':'W', '75':'Re', '76':'Os', '77':'Ir', 
            '78':'Pt', '79':'Au', '80':'Hg', '81':'Tl', '82':'Pb', '83':'Bi', '84':'Po', '85':'At', '86':'Rn', '87':'Fr', 
            '88':'Ra', '104':'Rf', '105':'Db', '106':'Sg', '107':'Bh', '108':'Hs', '109':'Mt', '110':'Ds', '111':'Rg', 
            '112':'Cn', '113':'Uut', '114':'Fl', '115':'UUp', '116':'Lv', '117':'Uus', '118':'Uuo', '':'', '':'', 
            '57':'La', '58':'Ce', '59':'Pr', '60':'Nd', '61':'Pm', '62':'Sm', '63':'Eu', '64':'Gd', '65':'Tb', '66':'Dy',
            '67':'Ho', '68':'Er','69':'Tm','70':'Yb','71':'Lu','89':'Ac','90':'Th','91':'Pa','92':'U',
            '93':'Np','94':'Pu','95':'Am','96':'Cm','97':'Bk','98':'Cf','99':'Es','100':'Fm','101':'Md',
            '102':'No','103':'Lr'};

this_string = ''
for num in code:
    key = str(num)
    element = periodic[key] 
    this_string = this_string + element[0]  #just want the first letter
    
print this_string

'''
THE PERIODIC TABLE IS A TABULAR ARRANGEMENT OF THE CHEMICAL ELEMENTS ORGANISED ON THE BASIS OF THEIR ATOMIC NUMBERS ELECTRON CONFIGURATIONS AND RECURRING CHEMICAL PROPERTIES WEVE USED IT TO CREATE A CIPHER BY USING THE INITIAL LETTERS OF THE ELEMENTS BUT TWO LETTERS CANT BE USED WHAT ARE THEY 
'''

# find the two letters that you cannot use in this scheme
alphabet = np.ones(26)

for element in np.arange(1,104):
    key = str(element)
    letter = periodic[key] 
    letter_val = ord(letter[0]) - letterA
    alphabet[letter_val] = 0
    
jj = np.where(alphabet > 0)

L0 = jj[0][0]
L1 = jj[0][1]

print 'The letters you cannot use are: %s and %s'%(chr(L0 + letterA),chr(L1 + letterA))

#challenge 6, puzzle 1 - ASCII code in hex, with the letters shifted but not
#the punctuation
print ' '
print '-- challenge #6:1 ---'
puzzle1 = ['22','4a','72','27','65','72','20','6e','79','79',
           '20','7a','6e','71','20','75','72','65','72','2e',
           '20','56','27','7a','20','7a','6e','71','2e','20',
           '4c','62','68','27','65','72','20','7a','6e','71',
           '2e','22','20','22','55','62','6a','20','71','62',
           '20','6c','62','68','20','78','61','62','6a','20',
           '56','27','7a','20','7a','6e','71','3f','22','20',
           '66','6e','76','71','20','4e','79','76','70','72',
           '2e','20','22','4c','62','68','20','7a','68','66',
           '67','20','6f','72','2c','22','20','66','6e','76',
           '71','20','67','75','72','20','50','6e','67','2c',
           '20','22','62','65','20','6c','62','68','20','6a',
           '62','68','79','71','61','27','67','20','75','6e',
           '69','72','20','70','62','7a','72','20','75','72',
           '65','72','2e']
           
#hex_string_to_letter

hexvalue = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
            '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 
            'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15,};

def hex_to_vale(onechar):
    symbol = ord(onechar)
    symbol

values = np.array([])
for pair in puzzle1:
    this_value = 16 * hexvalue[pair[0]] + hexvalue[pair[1]]    
    values = np.append(values, this_value)

string = ''    
for val in values:
    this_char = chr(int(val))  
    string = string + this_char

print 'Raw ASCII from hex codes:'     
print string   
print ' '
print 'Find shift value by looking for \'FNVQ\' to be \'SAID\''
brute_shift_code('FNVQ') 

#We expect FNVQ to be 'said', so do brute shift attack, reveals shift of 14.

shift = 14

#now set up a function to only shift the letters, retaining capitalisation


print ' '
print 'The final result: '         
output = shift_only_letters(string,13)
print output


