"""
Marcus Du
4/19/2021
Section 006
Assignment 9
"""
answerkeyunsep = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answerkey=answerkeyunsep.split(",")
input_file=input("Enter a class file to grade (i.e. class1 for class1.txt): ")
filename=input_file+".txt"

filefound=False
while filefound==False:

    try:
        file_object=open(filename,"r")

    except:
        print("File cannot be found. ")
        input_file=input("Enter a class file to grade (i.e. class1 for class1.txt): ")

    else:
        print("Successfully opened",filename)
        break

rawdata=file_object.read()
lines=rawdata.split("\n")
file_object.close()
num_students=len(lines)
num_corrupt=0
student_ans= dict()
students=list()
student_grades=list()


for i in range(0,len(lines)):
    corrupted_test=lines[i].split(",")
    if len(corrupted_test)!=26:
        num_corrupt+=1
        num_students+=-1
        continue
    student_ans[corrupted_test[0]]=corrupted_test[1:26]
    students.append(corrupted_test[0])
for j in range(0,len(students)):
    idv_grade=0
    for k in range(0,len(student_ans[students[j]])):
       
        try:
            ord(student_ans[students[j]][k])
        except:
            idv_grade+=0
        else:
            if str(student_ans[students[j]][k]) in str(answerkey[k]):
                idv_grade+=4
            else:
                idv_grade+=-1
    student_grades.append(idv_grade)
Median_form=student_grades.copy()
Median_form.sort()
if len(Median_form)%2!=0:
    Median=Median_form[(len(Median_form)//2)]
else:
    Median=(Median_form[int(len(Median_form)/2)]+Median_form[int((len(Median_form)/2)-1)])/2
unique=list()
times_seen=list()
mode_form=Median_form
for l in range(0,len(mode_form)):
    x=mode_form[l] 
    if x not in unique:
        unique.append(x)
        times_seen.append(1)
    elif x in unique:
        times_seen[unique.index(x)]+=1
    mode=unique[times_seen.index(max(times_seen))]








print("Grade Summary:")
print("Total Students:",num_students)
print("Unusable lines in the file:",num_corrupt)
print("Highest score: ",max(student_grades))
print("Lowest score:",min(student_grades))
print("Mean Score",format(sum(student_grades)/len(student_grades),'.2f'))
print("Median score:",Median)
print("Mode Score:",mode)
print("Range:",(max(student_grades)-min(student_grades)))

file_object2=open((input_file+"_grades.txt"),'w')
for m in range(0,num_students):
    file_object2.write(students[m]+','+format(student_grades[m],'.2f')+"\n")
file_object2.close()
curve_yn=input("Would you like to curve the exam? 'y' or 'n': ")

if curve_yn=='n':
    exit()

elif curve_yn=='y':
    curve_mean=float(input("Enter a desired mean (i.e. 75.0 to raise the mean score to 75.0): "))
curve_amount=curve_mean-(sum(student_grades)/len(student_grades))    
while curve_amount <=0:
    print("Invalid curve, try again.")
    print()
    curve_mean=float(input("Enter a desired mean (i.e. 75.0 to raise the mean score to 75.0): "))
    curve_amount=curve_mean-(sum(student_grades)/len(student_grades))  
fileobject3=open((input_file+"_grades.txt"),'w')
for n in range(0,num_students):  
    studentcurvedgrade=int(student_grades[n]+curve_amount)
    fileobject3.write(students[n]+','+str(student_grades[n])+","+str(studentcurvedgrade)+'\n')
fileobject3.close()


    
    
    
    
    
