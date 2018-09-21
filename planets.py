def weight_on_planets():

   #Input
   
   weight = float(input("What do you weigh on earth? "))
   
   
   #Calculation
   
   weightOnMars = weight * 0.38
   weightOnJupiter = weight * 2.34
   
   
   #Output
   
   print("\nOn Mars you would weigh " + str(weightOnMars) + 
        " pounds.\nOn Jupiter you would weigh " + 
        str(weightOnJupiter) + " pounds.")
   
   
if __name__ == '__main__':
    weight_on_planets()
