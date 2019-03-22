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
'''


'''
Task 1:
Set-up one dimensional arrays to store:
    • Student names
    • Student marks for Test 1 and Test 2
        o Test 1 is out of 20 marks
        o Test 2 is out of 25 marks
    • Total score for each student
Input and store the names for 30 students. You may assume that the students’ names are unique.
Input and store the students’ marks for Test 1, and Test 2. All the marks must be validated on
entry and any invalid marks rejected.
'''

'''
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
CLASS_SIZE =  30

