"""
Marcus Du
4/2/2021
Section 006
Part 2a
"""
from random import choice
from string import ascii_letters

def add_letters(word,num):
    scramble=""
    for i in range(0,len(word)):
        chr_string=""

        for j in range(0,num):
            add_chr=choice(ascii_letters)
            chr_string+=add_chr
        scramble+=word[i]+chr_string
    return(scramble)

def remove_letters(word, num):
    return(word[0:len(word):num+1])

def shift_characters(word, num):
    shifted_word=""
    for i in range(0,len(word)):
        shifted_char=chr(ord(word[i])+num)
        shifted_word+=shifted_char
    return(shifted_word)





