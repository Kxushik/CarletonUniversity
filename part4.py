#Part 4 Kaushik Paul
#101158930


#Input/Variable Initialization
cad_to_usd=0.87
valueUSD=5
price_A=float(input("Enter Price:"))
price_B=float(input("Enter Price:"))
price_C=float(input("Enter Price:"))

#Function to Convert
def conversion(price,conversion):
    return(abs(price*conversion))

#Prices in USD
price_A_USD=conversion(price_A,cad_to_usd)
price_B_USD=conversion(price_B,cad_to_usd)
price_C_USD=conversion(price_C,cad_to_usd)

#Function for Closest Value
def closestValue(A,B,C,value):
    if abs(A-valueUSD) < abs(B-valueUSD) and abs(A-valueUSD) < abs(C-valueUSD):
        print("CAD $" + str(price_A) + " is the closest.")
        
    elif abs(B-valueUSD) < abs(C-valueUSD):
        print("CAD $" +str(price_B) +" is the closest.")
    else:
        print("CAD $" +str(price_C) +" is the closest.")

#Execute Function with Given Parameters
closestValue(price_A_USD,price_B_USD,price_C_USD,valueUSD)


