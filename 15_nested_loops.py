#can be used to easily generate coordinates, for eg.:
#(x, y)
#(0, 0)
#(0, 1)
#(0, 2)
#(1, 0)
#(1, 1)
#(1, 2)

for x in range(4):                                 #x takes values upto 4, not including 4, i.e., outer loop is executed 4 times
    for y in range(3):                             #y takes values upto 3, not including 3, i.e., inner loop is executed 3 times
        print(f"({x}, {y})")
