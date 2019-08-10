# WW 3-2018

# function to compare arguments for a and b
def compare(a,b):

# if a is greater than b, return 1
    if a > b:
        return 1

# if a and b are equal, return 0
    elif a == b:
        return 0

# if a less than b, return -1
    elif a < b :
        return -1

# testing
if __name__=="__main__":

# call the compare function with a and b
    print('compare(5,2) %d'%compare(5,2))
    print('compare(2,5) %d'%compare(2,5))
    print('compare(3,3) %d'%compare(3,3))

# switch to user input; get values for a and b
    a=int(input("Enter the value for a: "))
    b=int(input("Enter the value for b: "))

    print('compare(%d,%d) %d'%(a,b,compare(a,b)))
