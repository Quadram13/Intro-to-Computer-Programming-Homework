"""
Marcus Du
3/4/2021
Section 006
Program 2: Pick Up Sticks Two Player Version

ggwp=whether the game ending condition has been fufilled
sc=original stick count at the start of the game
s_t=sticks taken by player
s_i=whether the number of sticks on the table is valid
player_n=which players turn it is
p_t=the variable that determines when turns switch
"""

p_t=1
ggwp=False
sc=0
s_t=0
s_i=False
player_n=""

while s_i==False:
    sc=int(input("How many sticks (10-100)?"))
    if sc>100:
        print("Sorry, that's too many sticks. Try again")
        continue
    elif sc<10:
        print("Sorry, that's too few sticks. Try again.")
        continue
    else:
        s_i=True
        print("Great Let's play ...")
while ggwp==False:
    if p_t%2!=0:
        player_n="Player 1"
    else:
        player_n="Player 2"

    print("Turn:",player_n)
    print("There are",sc,"sticks on the table")
    s_t=int(input("How many sticks do you want to take (1, 2 or 3)?"))
    if s_t>3 or s_t<1:
        print("Sorry, that's not a valid number.")
        continue
    elif sc<s_t:
        print("Sorry, that would bring the total # of sticks below 0. Try again.")
        continue
    else:
        sc=sc-s_t
        p_t=p_t+1
    if sc==0 and p_t%2!=0:
        print("There are no sticks left on the table!  Game over.")
        print("PLayer 1 wins!")
        ggwp=True
    elif sc==0:
        print("There are no sticks left on the table!  Game over.")
        print("PLayer 2 wins!")
        ggwp=True