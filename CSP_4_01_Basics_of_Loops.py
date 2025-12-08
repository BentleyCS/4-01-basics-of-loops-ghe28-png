#All questions must use a loop for full points.
import random
def oddNumbers(n:int) ->str:
    x=""
    for i in range(n+1):
        if(i%2==1):
            x+=str(i)
            if(i+2<=n):
                x+=" "

    return x

    """
    Print out all odd numbers from 1 to n(inclusive) in a single string seperated by spaces.
    example oddNumbers(5) -> "1 3 5"
    example oddNumbers(8) -> "1 3 5 7"
    example oddNumbers(-8) -> ""
    """


def backwards(n)-> int:
    x=""
    for i in range(n,0,-1):
        x+=str(i)
        if(i!=1):
            x+=" "
    return x
    """
    modify the below function such that it prints out all the numbers from n to 1
    inclusive starting at n and counting down to 1
    example backwards(5) -> "5 4 3 2 1"
    example backwards(8) -> "8 7 6 5 4 3 2 1"
    example backwards(-2) -> ""
    """



def randomRepeating():
    x=0
    y=0
    while x!=10:
        x=random.randint(1,10)
        y+=1
    return y
    """
    Print out a random number from 1-10 until you get a 10. Then print out how many
    times it took to roll a 10
    NOTE: Given randomness no test for this question
    :return:
    """
    tries = 0
    print(f"it took {tries} tries to get a 10")
def randomRange(n):
    x=0
    highest=0
    lowest=random.randint(1,100)
    for i in range(1,n-1,1):
        x=random.randint(1,100)
        if(lowest>x):
            x=lowest
        if x>highest:
            hightest=x
    return hightest, lowest


    """
    Generate a random number from 1 to 100 n number of times. Then after that is
    done print out what the highest number and the lowers number was from the rolled numbers.
    NOTE: Given randomness no test for this question
    :param n:
    :return:
    """
def reverse(word:str)->str:
    x=len(word)
    y=""
    for i in range(x,0,-1):
        y+=word[i-1]
    return y



    # """
    # Takes in a string as an argument and return the given string in reverse.
    # example reverse("cat") -> "tac"
    # example reverse("Hello") -> "olleH"
    # """

def fizzBuzzContinuous(n):
    x=""
    for i in range(1,n+1,1):
        if (i!=n):
            if(i%3==0 and i%5==0):
                x+="fizzbuzz"+" "

            else:
                if (i%3==0):
                    x+="fizz"+" "
                else:
                    if (i%5==0):
                        x+="buzz"+" "
                    else:
                        x+=str(i)+" "
        else:
            if (i % 3 == 0 and i % 5 == 0):
                x += "fizzbuzz"
            else:
                if (i % 3 == 0):
                    x += "fizz"
                else:
                    if (i % 5 == 0):
                        x += "buzz"
                    else:
                        x += str(i)

    return x
    """
    Modify the function such that it does the fizzbuzz operation on all numbers
    from 1 to n(inclusive).
    Fizz buzz is defined as
    if the number is divisble by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.

    As with above questions add each anseer to a string and return the final string.
    :param n:
    :return:
    """

def collatz(n):
    x=""
    x += str(n)
    while n!=1:
            if (n%2==0):
                n=n//2
                x+=" "+str(n)
            else:
                n=n*3+1
                x+=" "+ str(n)

    return x
    """
    Modify this function such that it mimics the collatz conjecture starting at n
    and prints out each number.
    The collatz conjecture is that if n is an even number divide it by 2. if n is
    an odd number multiply it by 3 and add 1.
    Repeat this process until n == 1.
    :param n:
    :return:
    """


def fibonacci(n):
    y=0
    x=1
    u=str(y)
    for i in range (1,n,1):
        z=y
        y+=x
        x=z
        u+=" "+str(y)
    return u
    """
    for the given argument n print out the first n numbers of the fibonacci
    sequence in a single string sperated by spaces.
    The fibonacci sequence is defined as a sequence that starts with 0 then 1 as
    the first two numbers. Every subsequent number is the prior two numbers added together.
    Example fibonacci(6) -> "0 1 1 2 3 5"
    Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    Example fibonacci(1) -> "0"
    :param n:
    :return:
    """


print(fibonacci(300))