def cone ():
        print("you have choosen the shape 'cone' don't forget the consistency of your input's unit!")
        cone_judge = input("If you want to calculate the sufrace area, enter 'S'. If you want the volume, enter'V'. for both, enter both:")
        print(cone_judge)
        if cone_judge == "s" or cone_judge == "S":
                cone_sliding = float(input("please input the sloop: "))
                cone_radius = float(input("please input the radius of your cone: "))
                cone_surface = 3.14* cone_radius **2* cone_sliding
                print("your cone's surface area is" , cone_surface)
        elif cone_judge == "V" or cone_judge == "v":
                cone_height = float(input("please give the height: "))
                cone_radius = float(input("please give the radius of the cone: "))
                cone_volume = cone_height * cone_radius / 3
                print("your cone's volume is" , cone_volume)
        elif cone_judge == "both":
                cone_height = float(input("please give the height: "))
                cone_radius = float(input("please give the radius of the cone: "))
                cone_sliding = float(input("please input the sloop: "))
                cone_surface = 3.14* cone_radius **2* cone_sliding
                cone_volume = cone_height * cone_radius / 3
                print("your cone's surface area is" , cone_surface , "and your cone's volume is", cone_volume)

                

def sphere ():
        print("you have choosen the shape 'sphere', don't forget the consistency of your input's unit!")
        sphere_judge = str(input("if you want to calculate the surface area, enter 'S'. If you want the volume, enter 'V'. for both, enter both"))
        if sphere_judge == "S":
                sphere_radius = float(input("please give the radius of your sphere"))
                sphere_surface = float(sphere_radius** 3 * 3.14)
                print("your sphere's surface area is" , sphere_surface)





        
