
timeToLand = 14

crew = [
    "Marlon", "Laura", "Beniamin", "Lazaro", "Eliene", "Roberto", "Mateus",
    "Geysa", "Teresa Cristina", "Maria Clara", "Miguel", "Jesiel"
    ]

total = 900
items = 900
days = 0

while items > 0:
    for member in crew:
        items -= 5
    days += 1

print("\n For a crew of {} people, with each one getting 5 items everyday\n  {} items last for {} days.".format(len(crew), total, days))

if timeToLand < days:
    print("\n Since the time to land is {} days, there is enough food for everyone \n till that date. No reason to worry!".format(timeToLand))
else:
    print("\n Since the time to land is {} days, there is NOT enough food for everyone \n till that date! DO SOMETHING ABOUT IT ASAP!".format(timeToLand))

        
