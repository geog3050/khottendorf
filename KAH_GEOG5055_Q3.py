climate=input("Please enter your desired climate (Tropical, Continental, or other):")
temps=list(map(float, input("Please input your list of temperatures as temp1 temp2 temp3 etc.:").split()))
if climate=="Tropical"or"tropical":
    for item in temps:
        if item<=30.0:
            print("The leaves are folded.")
        else:print("The leaves are unfolded.")
elif climate=="Continental"or"continental":
     for item in temps:
        if item<=25.0:
            print("The leaves are folded.")
        else:print("The leaves are unfolded.")
else:
    for item in temps:
        if item<=18.0:
            print("The leaves are folded.")
        else:print("The leaves are unfolded.")
