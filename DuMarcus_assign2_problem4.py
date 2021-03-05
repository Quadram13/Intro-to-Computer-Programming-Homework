"""
Marcus Du
2/17/2021
Section 006
Problem #4: Unit Conversion Calculator
"""
print("--------------------------------------------------------------")
title="mL Conversion Calculator" 
title_formatted=format(title,">43s") 
print(title_formatted)
print("--------------------------------------------------------------")
print()
mL=float(input("What amount in mL would you like converted?"))
mL_to_tsp=format((mL*0.202884),".2f")
mL_to_tsp_formatted=format(mL_to_tsp,">32s")
mL_to_tbsp=format((mL*0.202884*3),".2f")
mL_to_tbsp_formatted=format(mL_to_tbsp,">30s")
mL_to_micro=format(mL*1000,".2f")
mL_to_micro_formatted=format(mL_to_micro,">30s")
mL_to_nano=format(1000000*mL,".2f")
mL_to_nano_formatted=format(mL_to_nano,">31s")


unit_tsp=format("tsp","<5s")
unit_tbsp=format("tbsp","<5s")
unit_micro=format("uL","<5s")
unit_nano=format("nL","<5s")


print(mL,"mL . . .")
print(". . . in teaspoons",mL_to_tsp_formatted,unit_tsp)
print(". . . in tablespoons",mL_to_tbsp_formatted,unit_tbsp)
print(". . . in microliters",mL_to_micro_formatted,unit_micro)
print(". . . in nanoliters",mL_to_nano_formatted,unit_nano)
