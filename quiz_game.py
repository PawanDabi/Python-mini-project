print("\t\t******* Welcome to My Computer Quiz Game *******")
cont = input("Do You Want to Play Quiz Game ? =>")
if cont.lower() != 'yes':
    quit()
print("Ohkyy...!! Let's Start the Quiz Game....")
score = 0

answer = input("What does CPU Stands For? =>")
if answer.lower() == "central processing unit":
    print("Correct Answer!...")
    score = score + 1
else:
    print(" Incorrect Answer!...")

answer = input("What does GPU Stands For? =>")
if answer.lower() == "graphics processing unit":
    print("Correct Answer!...")
    score = score + 1
else:
    print("Incorrect Answer!...")

answer = input("What does RAM Stands For? =>")
if answer.lower() == "random access memory":
    print("Correct Answer!...")
    score = score + 1
else:
    print("Incorrect Answer!...")

answer = input("What does ROM Stands For? =>")
if answer.lower() == "read only memory":
    print("Correct Answer!...")
    score = score + 1
else:
    print("Incorrect Answer!...")

answer = input("What does OS Stands For? =>")
if answer.lower() == "operating system":
    print("Correct Answer!...")
    score = score + 1
else:
    print("Incorrect Answer!...")

answer = input("What does GUI Stands For? =>")
if answer.lower() == "graphical user interface":
    print("Correct Answer!...")
    score = score + 1
else:
    print("Incorrect Answer!...")

answer = input("What does DRAM Stands For? =>")
if answer.lower() == "dynamic random access memory":
    print("Correct Answer!...")
    score = score + 1
else:
    print("Incorrect Answer!...")

answer = input("What does SRAM Stands For? =>")
if answer.lower() == "static random access memory":
    print("Correct Answer!...")
    score = score + 1
else:
    print("Incorrect Answer!...")

answer = input("What does SDRAM Stands For? =>")
if answer.lower() == "synchronous dynamic random access memory":
    print("Correct Answer!...")
    score = score + 1
else:
    print("Incorrect Answer!...")

answer = input("What does HD Stands For? =>")
if answer.lower() == "hard drive":
    print("Correct Answer!...")
    score = score + 1
else:
    print("Incorrect Answer!...")
print("")

per = (score / 10) * 100
print("You got " + str(score) + " Correct Answer!...")
print("Your Percentage: ", str(per), "%")

if 91 <= per <= 100:
    print("You Got A1 Grade")
elif 81 <= per <= 91:
    print("You Got A2 Grade")
elif 71 <= per <= 81:
    print("You Got B1 Grade")
elif 61 <= per <= 71:
    print("You Got B2 Grade")
elif 51 <= per <= 61:
    print("You Got C1 Grade")
elif 41 <= per <= 51:
    print("You Got C2 Grade")
else:
    print("You Failed the Quiz! Try again...")

