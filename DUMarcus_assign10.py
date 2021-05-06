"""
Marcus Du
4/27/2021
Section 006
Assignment 10
"""
import random
"""
thesaurus = {
              "happy":["glad",  "blissful", "ecstatic", "at ease"],
              "sad"  :["bleak", "blue",     "depressed"]
            }

"""
thesaurus={}
rawdata=open('python_asg10_Roget_Thesaurus.txt','r')
alldata=rawdata.read()
lines=alldata.split('\n')
for i in range(0,len(lines)):
    syn_inc=lines[i].split(",")
    thesaurus[syn_inc[0]]=syn_inc[1:len(syn_inc)]

bieber=open('bieber_baby.txt','r')








phrase=bieber.read()
returnstr=phrase.lower()
for character in returnstr:
    if character.isalpha()==False:
        returnstr.replace(str(character),"")

desired_percentage=float(input("Enter a percentage chance to change a word:  "))

splitwords=returnstr.split(" ")
for i in range(0,len(splitwords)):
    phrase_word=splitwords[i]
    percentage=random.randint(0,100)
    if phrase_word in thesaurus and percentage<=(desired_percentage*100):
        new_word=random.choice(thesaurus[phrase_word])
        new_word=new_word.upper()
        splitwords[i]=new_word    
    else:
        continue
print(*splitwords)









