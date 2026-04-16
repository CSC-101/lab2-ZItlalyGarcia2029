def smallest(n:float, m:float) -> float:
    if n < m:
        return n #for which calls below is this statement evaluated?
    else:           #the second call and when n is less than m
        return m
first = smallest(3,2) #what is the value of first? first = 2
second = smallest(2, 2) #what is the value of second? Is this a reasonable result? Why/why not?
print()                         # the value is 2 and it is reasonable since it's the same number (smallest value).


def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b #In general, when will a call to this function evaluate this statement?
    elif b > c:        #if the number is greater than B and C, ex: (3, 2, 1)
        return b + c #In general, when will a call to this function evaluate this statement?
    else:              #if the number is greater than C, ex:(1, 3, 2)
        return 2 * c #In general, when will a call to this function evaluate this statement?
                        #when both expressions do not pass the requirement
answer1 = function2(3, 2, 1) #what is the value of answer1? answer1 = 1
answer2 = function2(2, 3, 1) #what is the value of answer2? answer2 = 4
answer3 = function2(2, 1, 3) #what is the value of answer3? answer3 = 6
print()
