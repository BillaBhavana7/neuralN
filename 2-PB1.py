First_name = ( input("Your First Name : "))
last_name = (input("Your Last Name : "))
Full_Name = print(First_name + last_name)

def string_alternative(Str):
    output = ""
    for a in range(len(Str)):
        if a % 2 == 0:
            output += Str[a]
    return output
print(string_alternative("Good evening"))
