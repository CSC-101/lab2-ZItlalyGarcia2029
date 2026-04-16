from typing import Optional

def checked_access(L: list[int], idx: int) -> Optional[int]:
    test = idx >= 0 and idx < len(L) #what is the value of test on each call?
    if test:                          #first call: False , second call: True
        return L[idx]    #what is the check preventing? prevents an IndexError
    else:
        return None

first = checked_access([1, 0, 1], 9) #what is the value of first? first = None
second = checked_access([1, 0, 1],2) #what is the value of second? second = 1
print()

def length_sum(L: list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2]) #for which call below is this statement evaluated?
                                                   # for first
    elif len(L) > 1:            #and what are the values being added? 'this', 'is', 'the' which are 4, 2, 3
        result = len(L[0]) + len(L[1]) #for which call below is this statement evaluated? for second ,
    elif len(L) > 0:      #and what are the values being added? 'second call' --> 11
        result = len(L[0])   #for which call below is this statement evaluated? for third
    else:
        result = 0   #and what are the values being added? 'another', 'call' which are 7 + 4 = 11
    return result

first = length_sum(['this', 'is', 'the', 'first', 'call'])
second = length_sum(['second call'])
third = length_sum(['another', 'call'])
print()

def surprising(L: list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L

words = ['this', 'is', 'confusing', 'code.']
first = surprising(words, 'Avoid')
second = surprising(words, 'such.')
#what is the value of words at this point?
#['this', 'is', 'confusing', 'code,', 'AVOID', 'SUCH.']
#what are the values of first and second at this point?
#first --> ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
#second --> ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
#what happened? the function duplicates the list using .append, in other words, anything that changes affects all the variables from that list
print()






