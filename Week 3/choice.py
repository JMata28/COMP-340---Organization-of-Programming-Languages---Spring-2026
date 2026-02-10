#curColor has currentColor of traffic light

# def changecolor(curColor):

#     if curColor == "green":
#         curColor = "yellow"
#     elif curColor == "yellow":
#         curColor = "red"
#     else:
#         curColor = "green"

#     return curColor

# curColor = changecolor("red")
# print(curColor)


#if expression with ternary operator

curColor = "red"

curColor = "green" if curColor=="red" else "red" if curColor=="yellow" else "yellow"

print(curColor)
