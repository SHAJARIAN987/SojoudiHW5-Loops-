length_of_list = int(input("How many Fibonacci numbers would you like? "))
Fibonacci_list = [0, 1]
while len(Fibonacci_list) < length_of_list:
    Fibonacci_list.append(Fibonacci_list[-1]+Fibonacci_list[-2])
print(Fibonacci_list)

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

length = int(input("Enter the length of the box: "))
height = int(input("Enter the height of the box (this number must be odd): "))

for line in range(height):
    if(line == 0 or line == height-1):
        line_text = ""
        i = 0
        for i in range(length):
            line_text += "*"
        print(line_text)
        continue
    elif(line % 2 == 1):
        print()
        continue
    elif (line % 2 == 0):
        line_text = "*"
        i = 0
        for i in range(length-2):
            line_text += " "
        line_text += "*"
        print(line_text)
        continue

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

width = int(input("Enter the width of the right triangle: "))

for w in range(0, width):
    line_text = ""
    for s in range (0, w+1):
        line_text += "*"
    print(line_text)

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

width = int(input("Enter the width of the isosceles triangle (this number must be odd): "))

for w in range (0, int((width-1)/2)+1):
    line_text = ""
    stars = (w*2) + 1
    spaces_on_each_side = int((width - stars)/2)
    for space in range(0, spaces_on_each_side):
        line_text += " "
    for star in range(0, stars):
        line_text += "*"
    for space in range(0, spaces_on_each_side):
        line_text += " "
    print(line_text)