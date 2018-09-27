#Simple SignUp and LogIn Program with addition of mini games element
import sqlite3
import sys

#creating the database to add things into
db = sqlite3.connect("users.db")
cursor = db.cursor()

    #drop the table to remake it
cursor.execute('''DROP TABLE users''')

    #create table
cursor.execute('''CREATE TABLE users (number INT, username STRING, password STRING, security STRING,name STRING, surname STRING,G1HS INT,G2HS INT,G3HS INT)''')

cursor.execute('''INSERT INTO users (number,username,password,security,name,surname,G1HS,G2HS,G3HS) VALUES (1,"rhianmack","1234","Storkey","Rhian","Mackintosh",0,0,0)''')
cursor.execute('''INSERT INTO users (number,username,password,security,name,surname,G1HS,G2HS,G3HS) VALUES (2,"yasminS","2342","Sunthankar","Yasmin","Sunthankar",0,0,0)''')

#========================================================================================================================
def LogIn():
    c = False
    while c == False:
        a = False
        while a == False:
            User = input("Username: ")
            wPass = input("Password: ")

            cursor.execute('''SELECT * FROM users''')
            for row in cursor:
                username = row[1]
                number = row[0]
                if User == username:
                    a = True
                    break
                else:
                    print("Incorrect Username, please try again (error 2)")

#checking if the password matches that chosen username
        b = False
        while b == False:
            cursor.execute('''SELECT password FROM users WHERE username = ?''',(User,))
            for row in cursor:
                if wPass == str(row[0]):
                    b = True
                    c = True
                    break
                else:
                    print("Incorrect Username, please try again (error 1)")
                    b = True
                    
                    
        
    profile(number)

#=========================================================================================================================
def SignUp():
    Nuser = input("Enter your username: ")
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    
    #checking they entered the correct password
    d = False
    while d == False:
        Npass = input("Enter your new password: ")
        confirm = input("Please confirm your password: ")
        if Npass == confirm:
            d = True
        else:
            d = False

    Nsecurity = input("Security Question: Please enter your mothers maiden name: ")
    

    #generating the number so it adds onto the end of the numbers already, wouldnt be efficent with lots of data
    cursor.execute('''SELECT number FROM users''')
    for row in cursor:
        number = row[0]
        print(number)
    number = number + 1

    cursor.execute('''INSERT INTO users (number,username,password,security,name,surname,G1HS,G2HS,G3HS) VALUES (?,?,?,?,?,?,0,0,0)''',(number,Nuser,Npass,Nsecurity,name,surname))
    db.commit()
    Menu()
    
#=========================================================================================================================
def Menu():
    print("======================")
    menu = input("Welcome! Would you like to: \n\
    1. Sign Up\n\
    2. Log In\n")
    e = False
    while e == False:
        if menu == "1":
            e = True
            SignUp()
        elif menu == "2":
            e = True
            LogIn()
        else:
            menu = input("Please enter '1' or '2': ")
#=========================================================================================================================
def Menu2(number):
    menu = input("What would you like to do:\n\
    1. Edit your profile\n\
    2. Go to the games\n")
    e = False
    while e == False:
        if menu == "1":
            e = True
            print("Make edit function")
        elif menu == "2":
            print("Make games menu")
            e = True
        else:
            menu = input("Please enter '1' or '2': ")
    
#=========================================================================================================================
def profile(number):
    cursor.execute('''SELECT * FROM users where number == ?''',(number,))
    for row in cursor:
        username = row[1]
        password = row[2]
        security = row[3]
        name = row[4]
        surname = row[5]
        G1HS = row[6]
        G2HS = row[7]
        G3HS = row[8]
        print("========================================")
        print("WELCOME BACK: "+name+" "+surname)

        Menu2(number)
    
#=========================================================================================================================
#Main body of the program starts here

Menu()


            
