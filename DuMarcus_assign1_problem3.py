"""
Marcus Du
2/3/2021
Section 006
Problem #3: Math Expressions
"""
print("--------------------------------------------------------------")
title="mL to US Fluid Volume Units" #title without formatting, if printed there would be no indent
title_formatted=format(title,">43s") #adds 16 character indent, moving the title to the center
print(title_formatted)
print("--------------------------------------------------------------")
"""
unit string length 16
"""
mL250=250.0  #the specific amount in mL that is being converted
mL_to_tsp=mL250*0.202884   
mL_to_tbsp=mL_to_tsp/3
mL_to_cups=mL_to_tbsp/16
mL_to_pints=mL_to_cups/2
mL_to_quarts=mL_to_pints/2
mL_to_gallons=mL_to_quarts/4
mL_to_floz=mL250/29.5735
"""
above are variables that store the conversions from ml to a corresponding US fluid volume unit
"""
mL_formatted=format('mL:','<15s')
tsp_formatted=format('tsp:','<15s')
tbsp_formatted=format('tbsp:','<15s')
cups_formatted=format('cup(s):','<15s')
pints_formatted=format('pint(s):','<15s')
quarts_formatted=format('quart(s):','<15s')
gallons_formatted=format('gallon(s):','<15s')
floz_formatted=format('fl oz:','<15s')
"""
above are just the units but formatted so that the numbers that will come after will all line up
"""
print("       ",mL_formatted,mL250)
print("       ",tsp_formatted,mL_to_tsp)
print("       ",tbsp_formatted,mL_to_tbsp)
print("       ",cups_formatted,mL_to_cups)
print("       ",pints_formatted,mL_to_pints)
print("       ",quarts_formatted,mL_to_quarts)
print("       ",gallons_formatted,mL_to_gallons)
print("       ",floz_formatted,mL_to_floz)
"""
above is the code that prints the formatted units and values
"""
print("--------------------------------------------------------------")
