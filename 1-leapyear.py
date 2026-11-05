def leapyear(n):
    n = int(input("Enter a year"))
# for century years
    if (n % 400 == 0):
        if(n % 100 != 0):
            print("LEAP YEAR") 

    #for non century years
        else(n % 4 == 0):
            print("LEAP YEAR")
    else:
        print("Not A LEAP YEAR")

leapyear(2007)




    
        