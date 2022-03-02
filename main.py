
print("-welcome to quiz game-".upper())

playing = input("do u want to play? ")
if playing.lower() != "yes":
    quit()
print('okey! lets play : ) ')
score = 0

answer = input("which is most popular language:")
if answer == "python":
    print("correct")
    score +=1
else:
    print("incorrect")

answer = input("list is mutable or not:")
if answer == "mutable":
    print("correct")
    score +=1
else:
    print("incorrect")

answer = input("set values are not consist duplicate values true not false:")
if answer == "false":
    print("correct")
    score +=1
else:
    print("incorrect")
print("you got " + str(score) + " questions correct")
print("you got " + str((score/4) * 100) + " %.")