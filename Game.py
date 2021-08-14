import time
score = 0
tasks = ["a","b","c"]
no = (0)
name = input("Name of the Player: ")
while True:
    check = input("Are you ready for"   + "  task " + str(no + 1) + " " + name + " [Y/N]: ").lower()

    if check == "y":
        print(tasks[no])
        check1 = input("Were you able to complete your task [Y/N]: ").lower()
        if check1 == "y":
            print("Congrats on completing your task no. " + str(no + 1))
            print("scores: " + str(score + 100))
            score = score + 100
            no = no + 1
        else:
            print("NO problem but best of luck for next task ")
            print("scores: " + str(score - 50))
            score = score - 50
