# 100 students sit a 'before' exam, and their marks can be assumed to be in the array b. 
# Later, they do an 'after' exam, and those marks are in a. Print the subscript number 
# (i.e in range 1 to 100) of the student who:
# a)	got the lowest mark overall (before + after)
# b)	improved the most between b and a.

lowposition = 1
lowvalue = 1

a = [0, 79, 42, 33, 30, 29, 57, 19, 96, 57, 12, 9, 96, 64, 97, 6, 2, 81, 85, 52, 93, 85, 98, 50, 12, 21, 75, 72, 84, 69, 39, 22, 93, 42, 32, 77, 72, 2, 62, 58, 41, 76, 50, 67, 98, 14, 8, 50, 49, 46, 52, 50, 45, 45, 54, 83, 25, 44, 78, 2, 56, 54, 56, 0, 37, 84, 94, 82, 87, 23, 78, 14, 6, 91, 95, 71, 25, 79, 50, 72, 40, 95, 51, 94, 20, 2, 4, 30, 88, 48, 70, 74, 25, 7, 0, 95, 54, 75, 93, 72, 57]
b = [74, 5, 32, 5, 3, 55, 65, 21, 64, 70, 64, 46, 10, 87, 1, 72, 86, 17, 33, 43, 30, 28, 50, 34, 73, 15, 97, 63, 3, 76, 41, 74, 29, 45, 45, 95, 51, 11, 79, 94, 15, 88, 99, 97, 2, 18, 88, 56, 6, 32, 70, 79, 99, 13, 1, 72, 86, 40, 98, 21, 66, 23, 41, 77, 87, 74, 49, 5, 97, 95, 89, 57, 88, 12, 74, 52, 63, 34, 32, 25, 66, 88, 18, 98, 94, 42, 78, 41, 77, 47, 35, 97, 81, 96, 80, 3, 50, 3, 37, 69, 5]

for student in range(0,101):
        if a[student] + b[student] < lowvalue:
                lowvalue = a[student]+b[student]
                lowposition = student

print(lowposition)
