secret="this is my secret"
love_name=input("your loves name: ")
birthday=input("your loves year of birth: ")

t= secret + love_name
t=t[::-1]
print(t+birthday)