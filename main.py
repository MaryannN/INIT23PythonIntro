# int
# str
# bool
# chr
# tuple - List you cant edit after you declare it
# list - Array
# dict - map

# stringHelloWorld --> CamelCase

# Ver 1
# print("Hello World")

# Ver 2
# string_hello_world = "Hello World" #snake_case

# Ver 3
# strHello = input("What greeting would you like?: ")
# print(strHello)

#Print Types
#print("My name is "+name+ ", I am "+age+" and my fav color is "+fav_color) #concatination
#print('My name is {}, I am {} and my fav color is {}!'.format(name,age,fav_color)) #str format
#print(f'My name is {name}, I am {age} and my fav color is {fav_color}!') #f string

#list_name_idk = []

'''
User Input
Collecting info on 4 people
'''
accepted_color_list = ["cyan", "black", "purple", "blue", "pink"]

#Range (2 Start, 1 End, 3 Jump)
for i in range(5): #For I Loop
  if(i>0): #Conditional Statement 
    print("\n")
  
  print("User Info # " + str(i)) #TypeCasting casting an int to a string 
  
  name = input("What is your name?: ")
  
  age = input("What is your age?: ")
  while(not age.isdigit()):
    age = input("That's not a number dude. Enter a number: ")
  while(int(age)<1):
    age = input("Woahhh there's no way you're that young. Enter an older age: ")
  
  fav_color = input("What is your fav color?: ")
  while(fav_color.lower() not in accepted_color_list): 
    fav_color = input("BOOOOOOOO BAD COLOR!! Pick another one now: ")
  
  print(f'Your name is {name}, you are {age} and your fav color is {fav_color}!') #f string
  
  
  
