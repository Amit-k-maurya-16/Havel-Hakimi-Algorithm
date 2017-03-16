import os

#Setup for system detection
#For clearing console and importing libraries specific to OS
def setup():
    import platform # for system detection
    if (str(platform.system())=='Windows'):
        print("Windows System Detected")
        if((input("Clear screen? y/n : "))=='y'):
            os.system('cls')
    if (str(platform.system())=='Linux'):
        print("Android System Detected")
        if((input("Clear screen? y/n : "))=='y'):
            os.system('clear')
    return

setup()

#docstring function
def doc():
    print("""
** The Havel-Hakimi Algorithm **
 
         v. 3/15/17
       Mason  Hoffman

Reduces a degree sequence using the Havel-Hakimi algorithm.

Use:
havelHakimi([degreeSequence])

* Determines if a degree sequence forms a valid graph.
* Outputs each step of the reduction process

    """)
    return

doc()

# Havel-Hakimi Alorithm for reducing degree sequences
# Determines if a degree sequence is graphic
def havelHakimi(sequence):
    # Things that may immediatly disqualify a sequence:
    # 1) non-integers
    # 2) negative numbers
    # 3) sum of sequence is not even
    if all(isinstance(deg, int) for deg in sequence):
        s = list(sequence) 
    else:
        return False #list contains non-integer degrees
    #An empty sequence is still graphic
    if len(s) == 0:
        print("Empty sequence!")
        return True 
    if min(s)<0:
        print("Negative number detected in sequence!")
        return False # negative degree
    if sum(s)%2:
        print("Sum of sequence is not even!")
        return False # sum of sequence is not even
    #Now for the actual algorithm to reduce the sequence
    while s:
        s.sort() # sorts into increasing order
        s.reverse() # reverses s into descending order
        print("Sequence: "+str(s))
        if s[0]<0: # found negative numbers in the sequence
            print("Subtracted too much from the nodes!")
            return False
        d=s.pop(0) # pops largest degree from front
        if d==0: # the sequence has been reduced to ([0])
            print("The degree sequence is graphic!")
            return True # done!
        if d>len(s): # the largest degree is too large for sequence
            print(str(d)+" is too large for sequence!")
            return False
        for i in range(0,d):
            s[i]-=1
        print("Popped: "+str(d))
    return False
