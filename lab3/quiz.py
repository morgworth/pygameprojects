total=3;
numCorrect=0;

print("Quiz!")
print("Question 1")
ans=float(input("What is 3 + 4? "))
if ans == 7:
	numCorrect+=1
	print("Correct!")
else:
	print("Fuckin' wrong dude!")
print("Question 2")
print("Which of these is not a cat?")
print("A. Lion")
print("B. Lemur")
print("C. Lynx")
ans=input("Answer with a letter: ")
if ans.lower()=="b":
	numCorrect+=1
	print("Correct!")
else:
	print("Nope!")
print("Question 3")
ans=float(input("What is the value of 5+8/4? "))
if ans == 7:
	numCorrect+=1
	print("Correct!")
else:
	print("Haha! Wrong!")

print()
print("Grade is ", numCorrect/total*100)