#group13 984165 and 965396
#inputting the grades for each student and converting them to integers so
#we can make calculations
m1=int(input('Please enter the first mark of the first student:'))
m2=int(input('Please enter the second mark of the first student:'))
g1=int(input('Please enter the first mark of the second student:'))
g2=int(input('Please enter the second mark of the second student:'))
n1=int(input('Please enter the first mark of the third student:'))
n2=int(input('Please enter the second mark of the third student:'))
#putting each mark in a student list
student1=[m1,m2]
student2=[g1,g2]
student3=[n1,n2]
#making the average between each index of the list and the length of the list
average1=(student1[0]+student1[1])/len(student1)
average2=(student2[0]+student2[1])/len(student2)
average3=(student3[0]+student3[1])/len(student3)
#print each student`s average
print('The average of the first student is:',average1)
print('The average of the second student is:',average2)
print('The average of the third student is:',average3)
#finding out the decreasing order of the averages by using the max functions
#so if the average 1 is the bigges show me the second bigger mark by making the
#max of the other two averages...and so on for each case
biggest_mark=max(average1,average2,average3)
if biggest_mark==average1:
    second_biggest_mark=max(average2,average3)
if biggest_mark==average2:
    second_biggest_mark=max(average1,average3)
if biggest_mark==average3:
    second_biggest_mark=max(average1,average2)
#printing the biggest and the second biggest mark
print('The biggest mark is:',biggest_mark)
print('The second mark is:',second_biggest_mark)
