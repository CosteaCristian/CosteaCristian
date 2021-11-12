###GROUP 13 984165 AND 965396
marks=[99,70,72,65,75,72,40,55,90,38,98,63,55,88,73,84,90,92,74,47,57,97,95,82,64,73,78,81,45,56,60,96,93]
#made a function that takes the marks as a list compares each index in the list and
#counts the number of firsts seconds and lower marks
#then printing the number of each type of marks
def MarksCompute(marks):
    firsts=0
    second=0
    others=0
    for i in range(0,len(marks)):
        if marks[i]>=70:
            firsts=firsts+1
        elif marks[i]>=60 and marks[i]<70:
            second=second+1
        elif marks[i]<60:
            others=others+1
        
    print('There are', firsts,'marks of first')
    print('There are', second,'marks of 2.1`s')
    print('There are', others,'lower marks')
#the first output is 21 marks of firsts, 4 marks of 2.1s and 8 lower marks

def MarksScale(marks):
#this function takes 5 points out of each mark bigger than 60
#so if someone has 75 the mark becomes 70 and so on
#the function modifies the list with the new marks and prints it
#also it compares and counts the marks again
#printing the number of each mark type
    firsts=0
    second=0
    others=0
    for i in range(0,len(marks)):
        if marks[i]>=60:
            marks[i]=marks[i]-5
            marks.insert(i, marks[i])
            if marks[i]>=70:
                firsts=firsts+1
            elif marks[i]>=60 and marks[i]<70:
                second=second+1
            elif marks[i]<60:
                others=others+1
            
        
    print('There are', firsts,'marks of first')
    print('There are', second,'marks of 2.1`s')
    print('There are', others,'lower marks')
    print('The new list of marks is:',marks)
#made a main function that calls the two functions
def main():
    print('This is the first look of the marks')
    MarksCompute(marks)
    print()
    print('Now after rescaling the marks here is the result')
    MarksScale(marks)
main()

