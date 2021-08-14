import time
score = 0
tasks = ["1.Consume less",
"2.Buy local ",
"3.Compost ",
"4.Use fewer chemicals",
"5.Choose reusable over single-use ",
"6.Walk, bike or carpool",
"7.Upcycle more ",
"8.Use less water",
"9.Recycle properly ",
"10.Use your purchasing power for good ",
"11.Shop secondhand ",
"12.Conserve electricity",
"13.Don’t buy single-use plastics.",
"14.Volunteer for a wildlife or environmental organisation.",
"15.Reduce the amount of meat you eat, or even better become vegetarian.",
"16.Use public transport, when you can, for everyday travel.",
"17.Reduce emissions from cars by walking or cycling. These are not just great alternatives to driving, they are also great exercise." ,
"18.Wherever possible, separate biodegradable and recyclable waste from non-biodegradable and work to reduce the amount of non-biodegradable ",
"19.Send your drinking bottles, paper, used oil, old batteries and used tires to a depot for recycling or safe disposal; all these very cause serious pollution.",
"20.When going shopping, make it a habit to bring your own eco-bags and say no to plastic bags as much as possible."]
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

