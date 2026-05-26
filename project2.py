print("welcome to quiz")
name=input("enter your name:")
print("hello",name,",let's start with the quiz..!")
score=0
print("question no.1")
print("how many days are there in a week? ")
print("(a). 14 ")
print("(b). 7")
print("(c). 11")
ans1=input("enter your answer:")
if ans1 == "b":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("question no.2")
print("2 + 2 = ?")
print("(a). 4")
print("(b). 7")
print("(c). 9")
ans2=input("enter your answer:")
if ans2 == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("question no.3")
print("what is the color of an apple?")
print("(a). red")
print("(b). blue")
print("(c). purple")
ans3=input("enter your answer:")
if ans3 == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("question no.4")
print("4 + 4 = ?")
print("(a). 8")
print("(b). 11")
print("(c). 18")
ans4=input("enter your answer:")
if ans4 == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong!")


print(name,"your final score:",score,"/4")
