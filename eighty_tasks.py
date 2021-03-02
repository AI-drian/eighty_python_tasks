from random import *


def one():
 user_input = int(input("Enter a number:"))
 squared = user_input ** 2
 print("Your number squared = {}".format(squared))

def two():
 income = 8000
 total_sales = float(input("Enter sales ammount: "))
 sales_income = total_sales * 0.09
 salary = income + sales_income
 print("Your income this month is: {} sek".format(salary))

def three():
 hours =float(input("Enter hours: "))
 minutes = hours * 60
 seconds = minutes * 60
 if hours > 1:
     print("{} hours is: {} minutes. Or {} seconds".format(hours, minutes, seconds))
 else:
     print("{} hour is: {} minutes. Or {} seconds".format(hours, minutes, seconds))

def four():
 num1 = float(input("Enter number 1: "))
 num2 = float(input("Enter number 2: "))
 num3 = float(input("Enter number 3: "))
 num_sum = num1 + num2 + num3
 num_avg = num_sum / 3
 print("Sum of numbers = {}. And avarage number = {}".format(num_sum, num_avg))

def five():
 sek = int(input("Enter SEK: "))
 usd = sek * 6
 gbp = sek * 10
 print("{} sek = {}usd and {}gbp.".format(sek, usd, gbp))

def six():
 a = int(input("Enter number a: "))
 b = int(input("Enter number b: "))
 function = a * b * 3 + 7
 print("ab3 + 7 = {}".format(function))

def seven():
 liters = float(input("Enter liters of petrooooleum: "))
 liter_price = float(input("Enter price per liter: "))
 discount = float(input("How about a discount, enter percent: "))
 discount_percent = discount * 0.01
 total_price = liters * liter_price * discount_percent
 print(total_price)

def eight():
 a = float(input("Enter side A cm: "))
 b = float(input("Enter side B cm: "))
 circumference = a+a+b+b
 area = a*b
 print("The Circumference of the rectangle is: {}cm and the Area: {}cm2".format(circumference, area))

def nine():
 radius = float(input("Enter radius: "))
 diameter = radius * 2
 circumference = 2 * 3.14 * radius
 area = 3.14 * radius**2
 print("Circumference: {}, Area: {}".format(circumference, area))

def ten():
 fahr = int(input("Enter Fahrenheit: "))
 celsius = (fahr-32) * 5 / 9
 print(celsius)

def eleven():
 num1 = int(input("Enter number 1: "))
 num2 = int(input("Enter number 2: "))
 if num1 > num2:
     print("{} is bigger than {}".format(num1, num2))
 else:
     print ("Nah the second number is higher...")

def twelve():
 num1 = int(input("Enter number 1: "))
 num2 = int(input("Enter number 2: "))
 if (num1/2)> num2:
     print("The first number is too high!")

def thirteen():
 num1 = int(input("Enter a number: "))
 if num1 % 2 == 0:
     print("{} is an even number!".format(num1))
 else:
     print("Sorry, uneven numbers are not cool")

def fourteen():
 num1 = int(input("Enter a number: "))
 if num1 % 2 == 0:
     print("{} is an even number!".format(num1))
 else:
     print("{} is uneven".format(num1))

def fifteen():
 num1 = int(input("Enter number 1: "))
 num2 = int(input("Enter number 2: "))
 if num1 % num2 ==0:
     print("{} can be evenly divided with {}".format(num1, num2))

def sixteen():
 price = float(input("Enter item price: "))
 quantity = int(input("Enter quantity: "))
 total = price * quantity
 if total >= 1000:
     total = total*0.90
     print("Wooohoo you passed the 1000kr limit and get a discount! To pay: {}".format(total))
 elif total < 1000:
     print("You owe us: {}kr".format(total))

def seventeen():
 num1 = int(input("Enter number 1: "))
 num2 = int(input("Enter number 2: "))
 if num2 == 0:
     print("ERROR 404 can not divide by zero ")
 else:
     print(int(num1/num2))

def eighteen():
 x = int(input("Enter value x: "))
 y = int(input("Enter value y: "))
 if x >=(y + 5):
     a = 2
 else:
     a = 5
 print(a)

def nineteen():
    
    hourly_income = float(input("Enter your hourly income: "))
    hours = int(input("Enter how many hours you have worked this week: "))
    overtime_income = hourly_income + (hourly_income/2)
    week_income = hourly_income * hours
    
    if hours <= 40:
       print(f"Your income this week: {week_income}")
        
    elif hours > 40:
        overtime = hours - 40
        overtime * overtime_income 
        week_income += overtime_income
        print(f"You've worked overtime, income this week: {week_income}")

def twenty():
 num = int(input("Enter a number 1-9: "))
 if num >=0 and num <10:
     num_squared = num**2
     print("{} squared is equal to {}".format(num, num_squared))
 else:
     print("Error your number is either too low or too high.")

def twentyone():
 num = int(input("Enter a number: "))
 if num >=-10 or num >10:
     print("Your number is somwhere between -10 and +10")

def twentytwo():
 num = int(input("Enter a number: "))
 if num == 5:
     print("Oh ooh, the number 5 is cursed!")
 elif num >= 0 and num < 10:
     print("Number is between 0-9")
 else:
     print("Out of range")

def twentythree():
    '''
    Skriv en funktion som testar om ett inläst tal är jämnt delbart med 3 men inte med 30. I så fall ska talet divideras med 3.
    '''
    num = int(input("Enter a number to check if it can be divided by 3 and 30: "))
    if (num%3 == 0) and (num %30 !=0):
        print(num/3) 
    else:
        print("Not good enough number (or I didnt understan the task)")    

def twentyfour():
 temp = float(input("Enter your body temperature: "))
 if temp >= 42:
     print("You've got a fever!")
 elif temp <= 35:
     print("You're freezing!")
 else:
     print("You're good!")

def twentyfive():
 num = int(input("Enter a number: "))
 if num >= 0:
     print("Positive!")
 elif num  <0:
     print("Negative!")

def twentysix():
 num1 = int(input("Enter number 1: "))
 num2 = int(input("Enter number 2: "))
 if num1 > num2:
     print("{} is the biggest!".format(num1))
 else:
     print("{} is the biggest".format(num2))

def twentyseven():
 num1 = int(input("Enter number 1: "))
 num2 = int(input("Enter number 2: "))
 num3 = int(input("Enter number 3: "))
 if num1 < num2 and num1 < num3:
     print("{} is the smallest".format(num1))
 elif num2 < num1 and num2 < num3:
     print("{} is the smallest".format(num2))
 else: 
     print("{} is the smallest".format(num3))

def twentyeight():
 temp = int(input("Enter temperature: "))
 if temp > 25:
     print("Too hot!")
 elif temp < 18:
     print("Too cold!")
 else: 
     print("The temperature is nice!")

#def twentynine():

def thirty():
 num = int(input("Enter a number: "))
 if num < 10:
     print("Less than 10")
 elif num < 100:
     print("Less than 100")
 else:
     print("Higher than 100")

def thirty_b():
 num = int(input("Enter a number: "))
 while num > 0:
     num = num-1
     print("{}".format(num))

def thirtyone():
 num = 1
 print("Program started exit with 0")
 while num != 0:
     num = int(input("Enter number: "))
     print(num)
 if num == 0:
     print("Program finnished")

def thirtytwo():
 num = 0
 while num != 100:
     num = num +2
     print(num)

def thirtythree():
 num = 100
 while num > 0:
     num = num-1
     print(num)

def thirtyfour():
 inmatning = "!"
 while inmatning != "*" :
     inmatning = input("Enter a character: ")
     print(inmatning)
     if inmatning == "*" :
         print("Program finnished")

def thirtyfive():
 num = 1
 while num < 10:
  squared = num **2
  print("{} squared is equal to: {}".format(num, squared))
  num = num + 1

def thirtysix():
 interest = float(input("Enter interest: "))
 year = 1
 savings = 1000
 while year < 10:
     savings = savings * interest
     print("Year {} you have {} in the bank.".format(year, savings))
     year = year + 1

def thirtyseven():
 quantity = int(input("How many numbers would you like to enter? : "))
 loop = 0
 while loop < quantity:
     num = int(input("Enter a number: "))
     print("Your number is: {}".format(num))
     loop = loop + 1
 print("Program Finnished!")

#def thirtyeight():

def thirtynine():
 price = 1 
 while price != 0:
     price = float(input("\nEnter price: "))
     inc_vat = price * 1.25
     print("The price is {} icluding VAT.".format(inc_vat))
 if price == 0:
     print("Program finnished\n")

def fourty():
 x = -10
 while x < 10:
     f = 3*x**3-5*x**2+2*x-20
     print(f)
     x = x+1

def fourtyone():
 x = 1
 y = 1
 while x <= 50:
    z = x + y
    print("{} + {} = {}".format(x,y,z))
    x += 1
    y += 1

def fourtytwo():
 x = 0
 y = 0
 while x <=20:
     x = x+1
     number = int(input(f"\nEnter number {x} you want to add: "))
     y += number
     print(f"\n sum is: {y}")
 print(f"\n Program finnished, sum is: {y}")    

def fourtythree():

   x =2

   while x <= 30:
       y = x + x
       print(f"\n {x} + {x} = {y}")
       x = x +2
   print("\n Program finnished")

def fourtyfour():
    x = 0
    total = 0
    number_of_numbers = int(input("\n Enter how many numbers you would like to add: "))

    while x < number_of_numbers:
        number_to_add = int(input(f"\n Enter number {x+1} to add: "))
        total += number_to_add 
        x += 1
    print(f"\n The sum of your numbers is: {total}")

def fourtyfive():

    num = int(input("\nEnter number to see how many times it fits in 100 000: "))
    x = 100000/ num
    print(f"\n there is room {x} times in 100 000")

def fourtysix():
    income = 0.01
    x = 1
    while income < 1000000:
        income = income * 2
        x +=1
        print(f"\n {income}")
    print(f"\n After {x} days his income will be one million")

def fourtyseven():
    x = 0
    y = 0
    z = 0
    while x <=15:
        if x%2 == 1:
            y = x
            z = x*y
            print(f"{x}x{y} = {z}")
        x += 1    
   
def fourtyeight():
    n = int(input("\n Enter n!: "))
    x = 1
    y = 2
    while y <= n:
      print(f" {n}! = {x}x{y}")   
      x = x + 2
      y = y + 2 
      
def fourtynine():
    x = int(input("\n Enter x: "))
    n = int(input("\n Enter n: "))

    f = x**n
    print(f"\n {x}^{n} = {f}")
    
def fifty():
    x = 1
    while x < 10:
        y = 1
        print(f"\n {x}ans tabell\n")
        while y < 11:
              z = x * y
              print (f"  {x} x {y} = {z}")
              y = y +1
        x = x +1
         
def fiftyone():
    x = 0
    seven_count = 0

    while x < 100:
        num = randint(1, 50)
        print(f"\n {num}") 
        x = x +1

        if num == 7:
            seven_count = seven_count +1  
        
    print(f"\n Seven appeared {seven_count} times \n")

def fiftytwo():
    x = 0
    total = 0
   
    while x <= 100:
        num = randint(-50, 50)
        print (f"\n Number {x} is: {num}")
        x = x +1
       
        if num > 0:
            total = total + num
            print(f" Added {num}, the total sum is now: {total}")    
   
    print((f"\n Program finnished, TOTAL = {total} \n"))    

def fiftythree():
    counter = 0

    while counter < 10:
        correct_num = randint(5000, 10000)
        correct_num += correct_num
        counter +=1
    average_num = correct_num / 10
    print (f"\n The sum is: {correct_num} \n Average number: {average_num} \n Program Finnished!\n")

def fiftyfour():
    x = 0
    positive = 0
    negative = 0
    zero = 0

    while x < 100:
        num = randint(-50, 50)

        if num >= 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero +=1    
        x += 1
    print(f"\n Positive numbers: {positive} \n Negative numbers: {negative} \n Zero value: {zero} \n Program Finnished")        

def fiftyfive():
    x = 0
    higher = 0
    lower = 0
    first = randint(0,100)
    print(f"\n The first number is: {first}")

    while x <= 100:

        num = randint(0, 100)

        if num < first:
            lower += num
        else:
            higher += num 
       
        x += 1    
    print(f"\n Higher numbers total: {higher} \n Lower number total: {lower}")

def fiftysix():

    print("Enter numbers, I will calculate...")
    numbers = []
    num = 0
    x = 0
   
    while num != 9999:
        num = int(input(": "))
        numbers.append(num)
    if num != 9999:
        print("Program stopping...")    

    for num in numbers:
        x += num  
    x = x - 9999
    avg = x/(len(numbers)-1)
    print(f"Total: {x} average: {avg}") 

def fifyseven():
    print("Exit with 0")
    liters =1
    miles = 1
    total_liter = 0
    total_miles = 0
    while liters != 0:
        liters = int(input("Enter number of liters: "))
        total_liter += liters
        while miles != 0:
            miles = float(input("Enter how many miles you drowe: "))
            total_miles += miles
            print(f"You got {miles/liters} per liter gas.")
    avg = total_miles/total_liter
    print(f" Your average gas consumption per mile: {avg}")       

def fiftyeight():
    print("Enter ten numbers, I will find the highest")
    loop = 0
    highest = 0
    user_input = 0

    while loop < 10:
        try:
            user_input = int(input(": "))
        except:
            print("You can only use integers")   
            loop = loop - 1 
        if user_input > highest:
            highest = user_input
        loop += 1
    print(f"The highest number was: {highest}")  

def fiftynine():
    
    loop = 0
    highest_nr = 0
    lowest_nr = 100000
    number_to_check = 0   
    ammount_of_numbers = int(input("\nEnter ammount of number you want to check: "))
    print(f"Enter {ammount_of_numbers} numbers")

    while loop < ammount_of_numbers:
        number_to_check = int(input(":"))
        if number_to_check < lowest_nr:
            lowest_nr = number_to_check
        elif number_to_check > highest_nr:
            highest_nr = number_to_check
        loop += 1   

    print(f"Highest number: {highest_nr} \nLowest number: {lowest_nr}")  

def sixty():
    user_input = 1
    check1 = 0
    check2 = 0
    count = 0
    print("Enter numbers, exit with 0")
    
    while user_input != 0:
        
        user_input = int(input(":"))
        if user_input == 0:
            break
        elif check2 == check1:
            count += 1
        check1 = user_input
        
        user_input = int(input(":"))
        if user_input == 0:
            break
        check2 = user_input
        if check1 == check2:
            count += 1
   
    print(f"You entered the same numbers next to each other {count} times")        

#def sixtyone():

def sixtytwo():
    print("Enter ten numbers between 5000-10000")
    x = 1
    while x < 11:
        user_input = int(input(f"{x}: "))
        x += 1  
        if user_input <5000 or user_input > 10000:
            print("Your number is too high or low!")
            x = x - 1
          
    print("Correct!")

def sixtythree():    
    x=1
    last_number = 0
    print("Enter numbers in a rising order, exit with 0 ")
    while x != 0:

        user_input = int(input(": "))
        
        if user_input < last_number:
            print("Error 404, input too low!")
            x += 1
        last_number = user_input    
            
def sixtyfour():
    big = 0
    nextbig = 0
    x = 0
    print("Enter ten positive numbers")
    while x < 10:
        x += 1 
        user_input = int(input(f"{x}:"))

        if user_input > nextbig:
            nextbig = user_input
        elif user_input > nextbig:
            big = user_input
           
    print(f"Highest: {big}, next highest: {nextbig}") 

def sixtyfive():
    x = 0
    highest = 0
    second = 0
    while x < 100:
        num = randint(0, 500)
        if num >= highest:
            highest = num
        elif num >= second:
            second = num
        x += 1        
        
    print(f"{highest}, {second} the difference is: {highest-second}")
        
def sixtysix():

    p_nr = [1, 9, 9, 3, 10, 14, "-", 1, 2, 3, 4]

    index = p_nr.index("-")
    if index != 6:
        print("Wrong")
    else:
        print("Correct")

def sixtyseven():
    p_nr = [1, 9, 9, 3, 10, 14, "-", 1, 2, 3, 4]

    if p_nr[9] % 2 == 0:
        print("Female")
    else:
        print("Male")    

def sixtyeight():
    
    x = 0
    num_list = []
    
    while x < 50:
        user_input = randint(1, 100)
        num_list.append(user_input)
        x += 1
    print(num_list)    
    
    num_list[:] = [x * 2 for x in num_list]
    print(num_list)

def sixtynine():

    x = 0
    num_list = []
    
    while x < 50:
        user_input = randint(1, 100)
        num_list.append(user_input)
        x += 1
    print(num_list) 

    numbers = [2+n if i%1 else n for i, n in enumerate(num_list)]
    print(numbers)

def seventy():
        
    x = 0
    num_list = []
    
    while x < 50:
        user_input = randint(-50, 50)
        num_list.append(user_input)
        x += 1
    print(num_list)

    positive = 0
    for num in num_list:
        if num > 0:
            positive += 1
    print(f" Number of positive numbers: {positive}")

def seventyone():
            
    x = 0
    num_list = []
    
    while x < 50:
        user_input = randint(0, 50)
        num_list.append(user_input)
        x += 1
    print(num_list)

    first = num_list[0]
    bigger = 0

    for number in num_list:
        if number >= first:
            bigger += 1
    print(bigger)

def seventytwo():
    x = 0
    num_list = []
    
    while x < 50:
        user_input = randint(-50, 50)
        num_list.append(user_input)
        x += 1
    print(num_list)

    i = len(num_list) - 1

    while i > 0:
        print(num_list[i])
        i -= 1
        if num_list[i] < 0:
            break
    print(f"Last negative number is {num_list[i]} on index {i}")    

def seventythree():
    
    x = 0
    num_list = []
    
    while x < 50:
        user_input = randint(0, 50)
        num_list.append(user_input)
        x += 1
    print(num_list)
    
    total = 0
    for number in num_list:
        total += number

    average = total/len(num_list)

    print(f"Total sum: {total}, average number: {average}") 

def seventyfour():     
    x = 0
    num_list = []
    
    while x < 50:
        user_input = randint(-100, 100)
        num_list.append(user_input)
        x += 1
    print(num_list)

    print(min(num_list), max(num_list)) 

def seventyfive():
    x = 0
    num_list = []
    
    while x < 50:
        user_input = randint(-100, 100)
        num_list.append(user_input)
        x += 1
    print(num_list)

    positive = 0
    negative = 0

    for number in num_list:
        if number > 0:
            positive += number
        elif number < 0:
            negative += number
    print(negative, positive)

def seventysix():
    x = 0
    num_list = []
    
    while x < 10:
        user_input = randint(0, 10)
        num_list.append(user_input)
        x += 1
    print(num_list)

    num_list[::-1]
    reverse_list = [i for i in num_list[::-1]]
    print(reverse_list)

def seventyseven():
    print("Instead of you having to enter ten numbers, I will do it for you")
    x = 0
    num_list = []
    
    while x < 10:
        user_input = randint(0, 10)
        num_list.append(user_input)
        x += 1
    print(num_list)

    print(num_list[::-1])

def seventyeight():
    numbers = []
    print("Enter two numbers to divide")
    täljare = int(input(": "))
    numbers.append(täljare)
    
    nämnare = int(input(": "))
    if nämnare == 0:
        print ("Divide by zero exeption")
    else:    
        print(täljare/nämnare)  

#def seventynine():        
        
#def eighty():

#ENTER PREFERED FUNCTION BELOW AND DO WHAT IT TELLS YOU IN THE TERMINAL!
twentyfour()