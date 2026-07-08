# import lib
# lib.lineanime(["hello"])
try:
    num = float(input("enter numerator : "))
    den = float(input("enter denominator : "))
    sum = num/den
    print(sum)

except ZeroDivisionError:
    print("cannot divide a number by 0") 

except:
    print("error occured check that input is vaild or not and try again")