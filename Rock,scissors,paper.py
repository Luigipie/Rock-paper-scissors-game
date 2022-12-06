import random

choose_random = ['rock', 'paper', 'scissors',]

p_pc = 0 #Pc Score
p_pl = 0 #PLayer Score

print ('Hi,Do you wanna play rock,paper,scissors?')
answer = input()
if answer == 'yes':
    Game = True
while Game == True:         #start of the loop
    print ('What do you launch?')
    launch = input()
    x = (random.choice(choose_random))
    if launch == 'rock':
        print ('Pc throw' , x )
        if x == 'scissors':    #istance for rock vs scissors
            print ("Bravo!You've Won \n")
            
            p_pl +=1
            print ("You've" , p_pl , "Point" , "Pc has" , p_pc , "Pointt")
            
            print ('Do you wanna still play? \n')
            c = input ()
            if c == 'no':
                print ('Goodbye and thank you to have played! \n')
                exit()
        if x == 'paper':        #istance for paper vs rock
            print ("Sorry,but you've loste! \n")
            p_pc +=1
            
            print("You've" , p_pl , "Point" , "The pc has" , p_pc , "Pointt")
            
            print ('Do you wanna still play? \n ')
            c = input ()
            if c == 'no':
                print ('Goodbye and thank you to have played! \n ')
                exit()
        if x == 'rock':         #istance for rock vs rock
            print ('Draw, relaunch! \n ')
            
            ("You've" , p_pl , "Point" , "The pc has" , p_pc , "Pointt")
            
            print ('Do you wanna still play? \n')
            c = input ()
            
            if c == 'no':
                print ('Goodbye and thank you to have played! \n')
                exit()
    if launch == 'paper':
        print ('Pc Throw' , x )
        if x == 'scissors':         #istance per paper vs scissors
            print ("Sorry You've lost \n ")

            p_pc +=1
            print("You've" , p_pl , "Point" , "The pc has" , p_pc , "Point")
            
            print ('Do you wanna still play? \n ')
            c = input ()
            if c == 'no':
                print ('Goodbye and thank you to have played! \n ')
                exit()
        if x == 'paper':            #istance for paper vs paper
            print ('Draw!,Re-launch! \n ')
            
            print ("You've" , p_pl , "Point" , "The pc has" , p_pc , "Point")
            
            print ('Do you wanna still play? \n ')
            c = input ()
            if c == 'no':
                print ('Goodbye and thank you to have played! \n ')
                exit()
        if x == 'rock':             #istance for paper vs rock
            print ("Bravo,you've won! \n" )
            p_pl +=1
            print ("You've" , p_pl , "Pointt" , "The pc has" , p_pc , "Pointt")
            
            print ('Do you wanna still play? \n ')
            c = input ()
            if c == 'no':
                print ('Goodbye and thank you to have played! \n ')
                exit()
    if launch == 'scissors':
        print ('Pc Throw' , x )
        if x == 'scissors':         #instance for scissors vs scissors
            print ('Draw! Re-launch \n ')
            
            print("you've" , p_pl , "Point" , "The pc has" , p_pc , "Pointt")
            
            print ('Do you wanna still play? \n ')
            c = input ()
            if c == 'no':
                print ('Goodbye and thank you to have played! \n ')
                exit()
        if x == 'paper':            #Instance for paper vs scissors
            print ("Bravo!You've Won! \n" )
            p_pl +=1
            print ("You've" , p_pl , "Point" , "The pc has" , p_pc , "Pointt")
            
            print ('Do you wanna still play? \n ')
            c = input ()
            if c == 'no':
                print ('Goodbye and thank you to have played! \n !')
                exit()
        if x == 'rock':             #instance for scissors vs rock
            print ("Sorry!You've lost! \n" )

            p_pc +=1
            print ("You've" , p_pl , "Point" , "The pc has" , p_pc , "Point")
            
            print ('Do you wanna still play? \n ')
            c = input ()
            if c == 'no':
                print ('Goodbye and thank you to have played! \n ')
                exit()

