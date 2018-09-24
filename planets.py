def weight_on_planets():

   #Input
   
   weight = float(input("What do you weigh on earth? "))


   #Calculation
   
   weightOnMars = weight * 0.38
   weightOnJupiter = weight * 2.34
   
   
   #Output
   
   print("\nOn Mars you would weigh {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format(weightOnMars, weightOnJupiter))
   
   
if __name__ == '__main__':
    weight_on_planets()
