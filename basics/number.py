number = [1, 2, 3, 4, 5] 
for i in number:
    x = i 
    print(x)

for s in number:
    if s > 2:
        print(s)

temperatures = [10, -20, 100]

def cel_to_fahr(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

for temperature in temperatures:
    print(cel_to_fahr(temperature))
