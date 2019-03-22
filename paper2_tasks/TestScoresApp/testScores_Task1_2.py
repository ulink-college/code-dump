########################################33333
# Test Scores Calculation App
#
# A teacher needs a program to record marks for a class of 30 students who have sat two computer science tests.
# The system will need to store studnets names and their marks in seperate arrays and all marks will need to be validated on entry. 
# The teacher wants to be able to display the total score for each student and average class score.
# The teacher also wants to see the highest and the lowest score in the class
'''
System Requirements
# Record and store scores for 30 students on 2 papers
# Validate scores on entry, rejecting invalid scores
# Calculate the average score
# Highest score and lowest score

Task 1:

Task 1 Plan:
* Create 3 arrays/lists - name, test 1 and test 2
* Collect user input and store in correct variable
* Check the input is valid
* Repeat until 30 sets of data have been entered

###Ver.2

student []
test1Score []
test2Score []
CLASS_SIZE <-- 30

FOR i IN RANGE 1 TO 30 DO
    INPUT student[i]
    WHILE test1Score[i] is not valid
        INPUT test1Score[i]
            IF test1Score[i] < 0 or > 20
                THEN
                    OUTPUT "Invalid score"
    END WHILE
    WHILE test1Score[i] is not valid
        INPUT test2Score[i]
            IF test2Score[i] < 0 or > 20
                THEN
                    OUTPUT "Invalid score"
    END WHILE
NEXT

'''

#Set up variables, lists, constants etc
student = []
test1Score = []
test2Score =  []
CLASS_SIZE =  3       #I used a constant so it makes it easy to change the number of entries

#Create the loop to start collecting input
for i in range(0, CLASS_SIZE):
    student.append(input("Enter student name: "))


#DEBUG:
print(student)
