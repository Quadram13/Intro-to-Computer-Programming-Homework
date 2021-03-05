"""
Marcus Du
2/25/2021
Section 006
Problem #3: Birthday Analyzer
"""
print("Instructions: Enter the start date and birthdate for a candidates to determine their age at the start of the show.")
b_date=int(input("Enter start date MMDDYYYY:"))
s_date=int(input("Enter birth date MMDDYYYY:"))
s_yr=s_date%10000
b_yr=b_date%10000
s_month=s_date//1000000
b_month=b_date//1000000
s_day=((s_date-s_yr)%100000)/10000
b_day=((b_date-b_yr)%100000)/10000
prt_day=0
prt_month=0


if s_month==1:
    prt_month="January"
elif s_month==2:
    prt_smonth="February"
elif s_month==3:
    prt_month="March"
elif s_month==4:
    prt_smonth="April"
elif s_month==5:
    prt_month="May"
elif s_month==6:
    prt_month="June"
elif s_month==7:
    prt_month="July"
elif s_month==8:
    prt_smonth="August"
elif s_month==9:
    prt_month="September"
elif s_month==10:
    prt_month="October"
elif s_month==11:
    prt_smonth="November"
elif s_month==12:
    prt_smonth="December"


if s_day==1:
    prt_day="1st"
elif s_day==2:
    prt_day="2nd"
elif s_day==3:
    prt_day="3rd"
elif s_day==4:
    prt_day="4th"
elif s_day==5:
    prt_day="5th"
elif s_day==6:
    prt_day="6th"
elif s_day==7:
    prt_day="7th"
elif s_day==8:
    prt_day="8th"
elif s_day==9:
    prt_day="9th"
elif s_day==10:
    prt_day="10th"
elif s_day==11:
    prt_day="11th"
elif s_day==12:
    prt_day="12th"
elif s_day==13:
    prt_day="13th"
elif s_day==14:
    prt_day="14th"
elif s_day==15:
    prt_day="15th"
elif s_day==16:
    prt_day="16th"
elif s_day==17:
    prt_day="17th"
elif s_day==18:
    prt_day="18th"
elif s_day==19:
    prt_day="19th"
elif s_day==20:
    prt_day="20th"
elif s_day==21:
    prt_day="21st"
elif s_day==22:
    prt_day="22nd"
elif s_day==23:
    prt_day="23rd"
elif s_day==24:
    prt_day="24th"
elif s_day==25:
    prt_day="25th"
elif s_day==26:
    prt_day="26th"
elif s_day==27:
    prt_day="27th"
elif s_day==28:
    prt_day="28th"
elif s_day==29:
    prt_day="29th"
elif s_day==30:
    prt_day="30th"
elif s_day==31:
    prt_day="31st"


print("The contestant was born on",prt_month,prt_day,s_yr)
if (b_yr-s_yr)>21:
    print("ELIGIBLE: The contestant will be 21 by the time taping begins")
elif (b_yr-s_yr)==21 and b_month>s_month:
    print("ELIGIBLE: The contestant will be 21 by the time taping begins")
elif b_day>s_day:
    print("ELIGIBLE: The contestant will be 21 by the time taping begins")
else:
    print("NOT ELIGIBLE: The contestant won't be 21 by the time taping begins")
    
