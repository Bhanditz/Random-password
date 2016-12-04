import random


def main():

    #random capital letter
    randomCap = rcl()
    #random lowercase letter
    randomLower = rlcl()
    #random symbol
    randomSymbol = rs()
    #random number
    number = random.randint(0,9)

    strong_weak = int(input('How strong do you want your password to be? 1,2,3,4? 4 being stong and 1 being  weak: '))

    if strong_weak == 1:
        weak1 = password1()
        print('Your password is "',weak1,'".')
        
    elif strong_weak == 2:
        weak2 = password2()
        print('Your password is "',weak2,random.randint(0,9),'".')

    elif strong_weak == 3:
        strong3 = password3(randomCap,randomLower,randomSymbol,number)
        strong3 = str(strong3)
        print('Your password is:')
        print (strong3)

    elif strong_weak == 4:
        strong4 = password4(randomCap,randomLower,randomSymbol,number)
        strong4 = str(strong4)
        print('Your password is:')
        print (strong4)

    else:
        print('Wrong number.')
        
def rcl():
    #List of random capital letters
    randomCap = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    random1 = random.randint(0,25)
    return randomCap[random1]

def rlcl():
    #List of random lowercase letters
    randomLower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    random1 = random.randint(0,25)
    return randomLower[random1]

def rs():
    #List of symbols
    randomSymbol = ['!','@','$','%','^','&','*','#']
    random1 = random.randint(0,7)
    return randomSymbol[random1]

def password1():
    password1 = ['password','dragon','football','baseball','welcome','master','monkey','login']

    pick_random_password = random.randint(0,7)

    password = password1[pick_random_password]
    return password

def password2():
    password2 = ['Password','Dragon','Football','Baseball','Welcome','Master','Monkey','Login']
    
    pick_random_password = random.randint(0,7)

    password = password2[pick_random_password]
    return password

def password3(randomCap,randomLower,randomSymbol,number):
    
    length = random.randint(10,15)
    password = []

    for i in range(0,length):
        
        random1 = random.randint(0,3)
        if random1 == 0:
            randomCap = rcl()
            password.append(randomCap)
        elif random1 == 1:
            randomLower = rlcl()
            password.append(randomLower)
        elif random1 == 2:
            randomSymbol = rs()
            password.append(randomSymbol)
        elif random1 == 3:
            number
            password.append(number)
            
    return password

def password4(randomCap,randomLower,randomSymbol,number):
    length = random.randint(15,25)
    password = []

    for i in range(0,length):
        
        random1 = random.randint(0,3)
        if random1 == 0:
            randomCap = rcl()
            password.append(randomCap)
        elif random1 == 1:
            randomLower = rlcl()
            password.append(randomLower)
        elif random1 == 2:
            randomSymbol = rs()
            password.append(randomSymbol)
        elif random1 == 3:
            number
            password.append(number)
            
    return password
    
    
main()
