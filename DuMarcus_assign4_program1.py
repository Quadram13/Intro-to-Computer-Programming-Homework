"""
Marcus Du
3/4/2021
Section 006
Program 1: Roll the Dice
List of variables
si=side input(whether the input for #of sides is valid)
ds = how many sides on the dice
sec=whether the user has rolled snake eyes or not
do=dice 1 rolled value
dt=dice 2 rolled value
dr=double roll
hr=high roll
hlr=high/low roll
er=even roll
o_r=odd roll
sv=sum value
se=Snake eyes
drc=double roll count
hrc=high roll count
hlrc=high/low roll count
erc=even roll count
o_rc=odd roll count
svc=sum value count
trc=total roll count
dot=sum value of all die 1 rolls
dtt=sum value of all die 2 rolls
drp=double roll percentage
hrp=high roll percentage
hlrp=high/low roll percentage
erp=even roll percentage
o_rp=odd roll percentage
svp=sum value percentage
ado=average roll for die 1
adt=average roll for die 2
"""
from random import randint
si = False

while si == False:
    ds=int(input("How many sides on your dice?(4, 6, 8, 10, 12 or 20)?"))
    if ds in [4,6,8,10,12,20]:
        si = True
        
    else:
        print("Invalid size, try again.")

print("Thanks, here we go!")
sec=False
dr=""
hr=""
hlr=""
er=""
o_r=""
se=""
sv=0
drc=0
hrc=0
hlrc=0
erc=0
o_rc=0
svc=0
trc=0
dot=0
dtt=0
while sec==False:
    do=randint(1,ds)
    dt=randint(1,ds)
    if do==dt:
        dr=" Doubles! "
        drc=drc+1
    else:
        dr=""
    if do==dr==ds:
        hr=" High Roll! "
        hrc=hrc+1
    else:
        hr=""
    if (do-dt)==(ds-1)or(dt-do)==(ds-1):
        hlr=" High/Low Roll! "
        hlrc=hlrc+1
    else:
        hlr=""
    if do%2==0 and dt%2==0:
        er=" Even Roll! "
        erc=erc+1
    else:
        er=""
    if do%2!=0 and dt%2!=0:
        o_r=" Odd Roll! "
        o_rc=o_rc+1
    else:
        o_r=""
    if do+dt==ds:
        sv=" Sum value is size value! "
        svc=svc+1
    else:
        sv=""
    if do==dt==1:
        se=" Snake Eyes! "
    else:
        se=""

    print("Die #1 is *",do,"* and die #2 is *",dt,"*",dr,hr,hlr,er,o_r,sv,se)
    dot=dot+do
    dtt=dtt+dt
    trc=trc+1

    if se==" Snake Eyes! ":
        sec=True
    else:
        continue

drp=format(((drc/trc)*100),'.2f')
hrp=format(((hrc/trc)*100),'.2f')
hlrp=format(((hlrc/trc)*100),'.2f')
erp=format(((erc/trc)*100),'.2f')
o_rp=format(((o_rc/trc)*100),'.2f')
svp=format(((svc/trc)*100),'.2f')
ado=format((dot/trc),'.2f')
adt=format((dtt/trc),'.2f')

print("You finally got snake eyes on roll#",trc)
print("Along the way you rolled DOUBLES ",drc," times. (",drp,"% of all rolls were doubles)")
print("Along the way you rolled TWO HIGH VALUES ",hrc," times. (",hrp,"% of all rolls were two high values)")
print("Along the way you rolled HIGH/LOW ",hlrc," times. (",hlrp,"% of all rolls were high/low)")
print("Along the way you rolled TWO EVENS ",erc," times. (",erp,"% of all rolls were two evens)")
print("Along the way you rolled TWO ODDS ",o_rc," times. (",o_rp,"% of all rolls were two odds)")
print("Along the way you rolled A SUM VALUE ",svc," times. (",svp,"% of all rolls were a sum value)")
print("Average roll for die #1: ",ado)
print("Average roll for die #2: ",adt)


    


