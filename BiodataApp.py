name = input("Your Name: ")
Class = input("Your Class: ")
major = input("Your Major: ")
quote = input("your quote: ")
age = int(input("your age: "))
iLikespiceFood = bool(input("I Like Spice Food: "))
hobbies = input("your hobbies: ").split(',')


print(f"My name is: {name}\nClass: {Class}\nMajor: {major}\nQuote: {quote}\nAge: {age}\niLikespiceFood: {iLikespiceFood}\nHobbies: {hobbies}  ")

print("="*50)
print("nama : ",type(name))
print("class : ",type(Class))
print("major : ",type(major))
print("quote : ",type(quote))
print("age : ",type(age))
print("i like spice food : ",type(iLikespiceFood))
print("hobbies : ",type(hobbies))
