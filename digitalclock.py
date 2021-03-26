"""
digital clock
"""
import digitalclock
# function:   horizontal_line
# input:      a width value (integer) and a single character (string)
# processing: generates a single horizontal line of the desired size
# output:     returns the generated pattern (string)
def horizontal_line(width,char):
    return width*char + "\n"

# function:   vertical_line
# input:      a shift value and a height value (both integers)  and a single character (string)
# processing: generates a single vertical line of the desired height.  the line is
#             offset from the left side of the screen using the shift value
# output:     returns the generated pattern (string)
def vertical_line(shift,height,char):
    pattern = ""
    for i in range(height):
        pattern += shift*" " + char + "\n"
    return pattern

# function:   two_vertical_lines
# input:      a width value and a height value (both integers)  and a single character (string)
# processing: generates two vertical lines.  the first line is along the left side of
#             the screen. the second line is offset using the "width" value supplied
# output:     returns the generated pattern (string)
def two_vertical_lines(width,height,char):
    pattern = ""
    for i in range(height):
        pattern += char + " "*(width-2) + char + "\n"
    return pattern

def number_0(width, char):
	
	return horizontal_line(width,char)+\
    two_vertical_lines(width, 3, char)+\
    horizontal_line(width,char)

def number_1(width, char):
	
	return vertical_line(width-1, 5, char)

def number_2(width, char):
	
	return horizontal_line(width,char)+\
    vertical_line(width-1, 1, char)+\
    horizontal_line(width,char)+\
    vertical_line(0, 1, char)+\
    horizontal_line(width,char)

def number_3(width, char):
	
	return horizontal_line(width,char)+\
    vertical_line(width-1, 1, char)+\
    horizontal_line(width,char)+\
    vertical_line(width-1, 1, char)+\
    horizontal_line(width,char)

def number_4(width, char):
	
	return two_vertical_lines(width, 2, char)+\
    horizontal_line(width,char)+\
    vertical_line(width-1, 2, char)

def number_5(width, char):
	
	return horizontal_line(width,char)+\
    vertical_line(0, 1, char)+\
    horizontal_line(width,char)+\
    vertical_line(width-1, 1, char)+\
    horizontal_line(width,char)

def number_6(width, char):
	
	return horizontal_line(width,char)+\
    vertical_line(0, 1, char)+\
    horizontal_line(width,char)+\
    two_vertical_lines(width, 1, char)+\
    horizontal_line(width,char)

def number_7(width, char):
	
	return horizontal_line(width,char)+\
    vertical_line(width-1, 4, char)

def number_8(width, char):
	
	return horizontal_line(width,char)+\
    two_vertical_lines(width, 1, char)+\
    horizontal_line(width,char)+\
    two_vertical_lines(width, 1, char)+\
    horizontal_line(width,char)
    
def number_9(width, char):
	
	return horizontal_line(width,char)+\
    two_vertical_lines(width, 1, char)+\
    horizontal_line(width,char)+\
    vertical_line(width-1, 1, char)+\
    horizontal_line(width,char)

def print_number(number,width,char):
    if number==0:
        print(number_0(width,char))
    elif number==1:
        print(number_1(width,char))
    elif number==2:
        print(number_2(width,char))
    elif number==3:
        print(number_3(width,char))
    elif number==4:
        print(number_4(width,char))
    elif number==5:
        print(number_6(width,char))
    elif number==7:
        print(number_7(width,char))
    elif number==8:
        print(number_8(width,char))
    elif number==9:
        print(number_9(width,char))



def plus(width,char):
    if width%2!=0:
        return vertical_line((width//2),2,char)+\
            horizontal_line(width,char)+\
            vertical_line(width//2,2,char)

    elif width%2==0:
        
        
        return vertical_line(int(width/2),2,char*2)+\
            horizontal_line(width,char)+\
            vertical_line(width/2,2,char*2)

def minus(width,char):
    return horizontal_line(width,char)




def check_answer(num1,num2,ans,operator):
    
    if (operator=="+"):
        if (num1 + num2) == ans:
            return True
        else:
            return False
        
    else:
        if (num1 - num2) == ans:
            return True
        else:
            return False



