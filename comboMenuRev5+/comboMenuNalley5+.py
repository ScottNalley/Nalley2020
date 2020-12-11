#typically at the very top you will create global variables
order=[]
total=0                         #accumulative variable
final=0
tax=0
sandwhichSelected=False         #flag variable
beverageSelected=False
friesSelected=False
keepGoing=True
while (keepGoing!="no"):

    print (f'''
                                        GALLEY GRUB
        1 Krabby Patty...       $1.25                 2 Krabby Meal...        $3.50
          w/sea cheese...       $1.50                 3 Double Krabby M...    $3.75
        4 Double Krabby Patty.. $2.00                 5 Triple Krabby Me..    $4.00
          w/sea cheese...       $2.25                 6 Salty Sea Dog.....    $1.25
        7 Triple Krabby Patty.. $3.00                 8 Footlong..........    $2.00
          w/sea cheese...       $3.25                 9 Sailor's Surprise.    $3.00
                                                      10 Golden Loaf......    $2.00
                                                        w/sauce... $2.50
    ''')
    sandwhich = input("Please pick a type of main order: ")
    #if (sandwhich=="c" or sandwhich=="b" or sandwhich=="t"):           another valid method for the discount
    #   sandwhichSelected=True
    print(sandwhich)
    beverage = input("Would you like a drink, y or n? ")
    if(beverage=="y"):
        beverageSelected=True
        beverage=input("s for $1.00, m for $1.75, l for $2.25, c for $2.63 ")
        print("you said ",beverage, " drink.")  #print(string,string,string,string)
    
    def sandwhich14710(name,c,ch):
        t=0
        t += c
        sandwhich=input("Would you like sea cheese for an additional $.25? (y or n)")
        if (sandwhich == "y"):
            t += ch
        ss=True
        return t,ss
    
    if sandwhich=="1":
        ts=sandwhich14710("Krabby Patty",1.25,.25)
        sandwhichSelected=ts[1]
        total+=ts[0]
    elif sandwhich=="2":
        total += 3.50
        sandwhichSelected=True
    elif sandwhich=="3":
        total += 3.75
        sandwhichSelected=True
    elif sandwhich=="4":
        ts=sandwhich14710("Double Krabby Patty",2.00,.25)
        total+=ts[0]
        sandwhichSelected=ts[1]
        
    elif sandwhich=="5":
        total += 4.00
        sandwhichSelected=True
    elif sandwhich=="6":
        total += 1.25
        sandwhichSelected=True
    elif sandwhich=="7":
        ts=sandwhich14710("Triple Krabby Patty",3.00,.25)
        sandwhichSelected=ts[1]
        total+=ts[0]
    elif sandwhich=="8":
        total += 2.00
        sandwhichSelected=True
    elif sandwhich=="9":
        total += 3.00
        sandwhichSelected=True
    elif sandwhich=="10":
        ts=sandwhich14710("Golden Loaf",2.00,.5)
        sandwhichSelected=ts[1]
        total+=ts[0]
    if beverage=="s":
        total += 1.00
    elif beverage=="m":
        total += 1.75
    elif beverage=="l":
        total += 2.25
    elif beverage=="c":
        total += 2.63
    #iteration 3 asking for fries
    fries = input("Would you like french fries, y or n? ")
    if(fries=="y"):
        fries = input("Would you like a s for $1, m for $1.50, or l for $2? ")
        friesSelected=True
    if (fries == "s"):
        total = total + 1
    elif (fries == "m"):
        total = total + 1.50
    elif (fries == "l"):
        fries=input("Would you like a child size fry instead for an addition $.38? (y or n)")
        if (fries == "y"):              #nested conditional statement
            total += 2.38
        else:
            total+=2
    #iteration 4
    #if you do not convert input to int() it will be a sequence or a string
    ketchup=int(input("How many ketchup packets would you like? "))*.25
    total+=ketchup
    #but you could combine the top two lines into one
    if(sandwhichSelected and beverageSelected and friesSelected):     #and looks for 2 true statements
    #if variable==true   AND variable==true   AND variable==true
        total-=1
    #print("You're total is",total)

    order.append(sandwhich,fries,beverage,ketchup)


    #print('Your order is a {0} sandwich, a {1} drink, a {2} fry, and {3} ketchup packet(s) \nfor a total of {4}'.format(sandwhich,beverage,fries,ketchup,total))
    j=0
    for i in range(len(order)):
        j+=1
        print('''
        Your order {} is: 
            {} sandwich,
            {} drink,
            {} fries,
            {} packets
        
        '''.format(j,order[i][0],order[i][1],order[i][2],order[i][3]))

    print("For a total of ${:,.2f}".format(total))
    tax=(total*0.07)
    final=tax+total
    print("Your tax is " + str(round(tax,2)))
    print("Your final amount is " + str(round(final,2)))
    keepGoing = input("Would you like to order again (yes) or (no): ")
    #print('${:,.2f}'.format(total))  #string formatting
