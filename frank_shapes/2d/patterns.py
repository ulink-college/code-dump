
class not_a_triangle(OverflowError):
    pass


def triangle ():
    global regular_bottom ,regular_height , regular_side_A , regular_side_B , area_of_regular , circumference_of_regular
    judge = input("if it's a regular triangle , enter regular , if it is right angled , enter right angled:")
    if judge == "regular":
        CorS = str(input("if you like to calculate the area , enter a capitalized S. if the Circumference ， enter capitalized C. if you like to print both, enter both:"))
        if CorS == "S":
            regular_bottom = float(input("enter the bottom of your triangle："))
            regular_height = float(input("enter the height of your triangle："))
            area_of_regular = regular_bottom*regular_height
            print("your triangle's area is" , area_of_regular)
        elif CorS == "C":
            regular_bottom = float(input("enter the bottom of your triangle："))
            regular_side_A = float(input("give a side of your triangle："))
            regular_side_B = float(input("give another side of your triangle："))
            circumference_of_regular = regular_bottom+regular_side_A+regular_side_B
            if regular_side_A +regular_side_B < regular_bottom or regular_bottom + regular_side_A < regular_side_B or regular_bottom + regular_side_B < regular_side_A:
                raise not_a_triangle ("you can't define a triangle which if you add up its two sides and it's greather than the third!!!")
            else:
                print("your triangle's circumference is" , circumference_of_regular)
        elif CorS == "both":
            regular_bottom , regular_height = float(input("enter the bottom of your triangle：")) , float(input("enter the height of your triangle:")) 
            regular_side_A , regular_side_B = float(input("enter a side of your triangle:")) , float(input("enter another side of your triangle:"))
            area_of_regular = regular_bottom*regular_height
            circumference_of_regular = regular_bottom+regular_side_A+regular_side_B
            print("your triangle's area is", area_of_regular ,"and your triangle's circumference is", circumference_of_regular)

    elif judge == "right angled":
        global right_bottom , right_height , right_hypotenus , area_of_right , circumference_of_right
        right_CorS = str(input("if you want to calculate the area, enter capitalized S, if circumference, enter capitalized C. If both, enter both"))
        if right_CorS.upper() == "S":
            right_bottom = float(input("please enter the bottom of your triangle"))
            right_height = float(input("please enter the height of your triangle"))
            area_of_right = right_bottom*right_height
            print("your triangle's area is", area_of_right)
        elif right_CorS == "C":
            right_bottom = int(input("please enter the bottom of your triangle"))
            right_height = int(input("please enter the height of your triangle"))
            right_hypotenus = float(input("please enter the hypotenus of your triangle"))
            if right_bottom + right_height < right_hypotenus or right_bottom + right_hypotenus < right_height or right_hypotenus + right_height < right_bottom:
                raise not_a_triangle("you cant define a triangle as its two sides' sum is lower than the third!!!")
            elif right_bottom**2 + right_height**2 != right_hypotenus**2:
                raise not_a_triangle("you can't define a right angled triangle when it's right angle sides' square sum dosn't equal the third side!!!")
            else:
                circumference_of_right = right_bottom + right_height + right_hypotenus
                print("the C of your triangle is", circumference_of_right)
        elif right_CorS == "both" or "Both" or "BOTH":
            right_bottom , right_height = float(input("please enter the bottom of your triangle")) , float(input("please enter the height of your triangle"))
            right_hypotenus = float(input("please enter the hypotenus of your triangle"))
            circumference_of_right , area_of_right= right_bottom + right_height + right_hypotenus , right_height*right_bottom
            print("your triangle's area is" , circumference_of_right , "and the area is" , area_of_right)

                

def rectangle():
    width_of_rectangle = float(input("please enter the width of your rectangle:"))
    length_of_rectangle = int(input("please enter the legnth of your rectangle:"))
    rectangle_CorS = str(input("if you want the area, enter capitalized 'S' if you want circumference, enter capitalized'C' if you want both, enter both:"))
    if rectangle_CorS == "S":
        print("the area of your rectangle is", width_of_rectangle*length_of_rectangle)
    elif rectangle_CorS == "C":
        print("the circumference of your rectangl is", width_of_rectangle*2 + length_of_rectangle*2)
    elif rectangle_CorS == "both":
        print("the area of your rectangle is", width_of_rectangle*length_of_rectangle , "the circumference of your rectangle is", width_of_rectangle*2 + length_of_rectangle*2)



def square():
    Length_of_side = int(input("please enter a length of your square's side:"))
    square_CorS = str(input("if you want to calculate the area, enter capitalized 'S' if you wanted the circumference, enter capitalized'C' if both , enter both:"))
    if square_CorS == "S":
        print ("the area of your square is" , Length_of_side^2)
    elif square_CorS == "C":
        print ("the circumference of your square is" + Length_of_side*4)
    elif square_CorS == "both":
        print("the area of your square:", Length_of_side ^2 , "the circumference of your square", Length_of_side*4)
        


def circle ():
    diameter = float(input("please enter the diameter of your circle"))
    circle_CorS = str(input("if you want to calculate the area , enter capitalized 'S' for Circumference enter capitalized 'C' for both, enter both:"))
    if circle_CorS == "S":
        print ("your circle's area is", 3.14*(diameter/2)**2)
    elif circle_CorS == "C":
        print ("your circle's Circumference is", diameter*3.14)
    elif circle_CorS == "both":
        print ("your circle's area:", diameter/2*3.14*3.14 ,  "your circle's circumference is" , diameter*3.14 )
