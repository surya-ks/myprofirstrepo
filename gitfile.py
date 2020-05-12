print("enter the numbers to check for the greatest one ")
def largestnumber(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        print("num1 is greater")
    elif num2 >= num1 and num2 >= num3:
        print("num2")
    else:
        print("num3 is greater")
largestnumber(num1=(input()),num2=(input()),num3=(input()))
