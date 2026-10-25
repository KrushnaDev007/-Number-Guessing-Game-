#My First Python Project NUMBER GUESSING GAME
#HOPE YOU ENJOY :-)

print("Welcome To The Number Guessing Game Programme")

print("You Will Have 5 total attempts to guess a randomized number between 1 to 30 the computer have chosen")

print("According to your accuracy the programme itself will tell you whether you are close or far from that number")

print("So let us proceed Further")

import random
a = random.randint(1 , 30)

b = int(input("Enter The Value You Are Guessing Computer has picked up :"))


#1st ATTEMPT


if b > 30 :
    print("ERROR Number Cannot Be Greater Than 30 its")

if b == a :
    print("BOOYAH! you guessed it correct in your 1st ATTEMPT")

    import sys                                             #If a user guesses correct number 
                                                           #then program will be stopped by itself with this command
    sys.exit("Wanna Have Fun Again ? , Then PLAY") 

elif b - a  == 1 :                  
    print("More Closer")    

elif a - b  == 1 :                  
    print("More Closer")            
        

# to compare the guessed number with actual number from close to far
#  we calculated difference between them with increment of guessed value accordingly 

elif b - a == 2:                    
    print("Closer")

elif a - b == 2:
    print("Closer")

elif b - a == 3:                    
    print("Good one")

elif a - b == 3:
    print("Good one")

elif b - a == 4:                    
    print("OK not bad")

elif a - b == 4:
    print("Ok not bad")

elif b - a == 5:                    
    print("Nice try")

elif a - b == 5:
    print("Nice try")

elif b - a == 6:                    
    print("Far")

elif a - b == 6:
    print("Far")

elif a - b == 7:
    print("Too Far")

elif b - a == 7:                    
    print("Too Far")

elif b - a == 8:                    
    print("So Much Far")  

elif a - b == 8:
    print("So Much Far") 

else:                               
    print("Really Far")


#2nd ATTEMPT


b = int(input("Enter The Value You Are Guessing Computer has picked up :"))
if b > 30 :
    print("ERROR Number Cannot Be Greater Than 30 its")

if b == a :
    print("BOOYAH! you guessed it correct")

    import sys
    sys.exit("Wanna Have Fun Again ? , Then PLAY")

elif b - a  == 1 :                  
    print("More Closer")               

elif a - b == 1:
    print("More Closer")

elif b - a == 2:                    
    print("Closer")

elif a - b == 2:
    print("Closer")

elif b - a == 3:                    
    print("Good one")

elif a - b == 3:
    print("Good one")

elif b - a == 4:                    
    print("OK not bad")

elif a - b == 4:
    print("Ok not bad")

elif b - a == 5:                    
    print("Nice try")

elif a - b == 5:
    print("Nice try")

elif b - a == 6:                    
    print("Far")

elif a - b == 6:
    print("Far")

elif a - b == 7:
    print("Too Far")

elif b - a == 7:                    
    print("Too Far")

elif b - a == 8:                    
    print("So Much Far")  

elif a - b == 8:
    print("So Much Far") 

else:                               
    print("Really Far")


#3rd ATTEMPT


b = int(input("Enter The Value You Are Guessing Computer has picked up :"))

if b > 30 :
    print("ERROR Number Cannot Be Greater Than 30 its")

if b == a :
    print("BOOYAH! you guessed it correct")
    
    import sys
    sys.exit("Wanna Have Fun Again ? , Then PLAY")

elif b - a  == 1 :                  
    print("More Closer")               

elif a - b == 1:
    print("More Closer")

elif b - a == 2:                    
    print("Closer")

elif a - b == 2:
    print("Closer")

elif b - a == 3:                    
    print("Good one")

elif a - b == 3:
    print("Good one")

elif b - a == 4:                    
    print("OK not bad")

elif a - b == 4:
    print("Ok not bad")

elif b - a == 5:                    
    print("Nice try")

elif a - b == 5:
    print("Nice try")

elif b - a == 6:                    
    print("Far")

elif a - b == 6:
    print("Far")

elif a - b == 7:
    print("Too Far")

elif b - a == 7:                    
    print("Too Far")

elif b - a == 8:                    
    print("So Much Far")  

elif a - b == 8:
    print("So Much Far") 

else:                               
    print("Really Far")



#4th ATTEMPT


b = int(input("Enter The Value You Are Guessing Computer has picked up :"))

if b > 30 :
    print("ERROR Number Cannot Be Greater Than 30 its")

if b == a :
    print("BOOYAH! you guessed it correct")

    import sys
    sys.exit("Wanna Have Fun Again ? , Then PLAY")

elif b - a  == 1 :                  
    print("More Closer")               

elif a - b == 1:
    print("More Closer")

elif b - a == 2:                    
    print("Closer")

elif a - b == 2:
    print("Closer")

elif b - a == 3:                    
    print("Good one")

elif a - b == 3:
    print("Good one")

elif b - a == 4:                    
    print("OK not bad")

elif a - b == 4:
    print("Ok not bad")

elif b - a == 5:                    
    print("Nice try")

elif a - b == 5:
    print("Nice try")

elif b - a == 6:                    
    print("Far")

elif a - b == 6:
    print("Far")

elif a - b == 7:
    print("Too Far")

elif b - a == 7:                    
    print("Too Far")

elif b - a == 8:                    
    print("So Much Far")  

elif a - b == 8:
    print("So Much Far") 

else:                               
    print("Really Far")



#5th ATTEMPT(Last One)


b = int(input("Enter The Value You Are Guessing Computer has picked up :"))

if b > 30 :
    print("ERROR Number Cannot Be Greater Than 30 its")

if b == a :
    print("BOOYAH! you guessed it correct in Your FINAL ATTEMPT")

    import sys
    sys.exit("Wanna Have Fun Again ? , Then PLAY")

else:
    print(f"Sorry! You Failed to Guess The Number {a} WANNA RETRY ??")
    