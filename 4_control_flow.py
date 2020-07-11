###################### Conditional Statements ######################
# Allow us to branch execution based on the value of an expression

if 3 > 2:
    print("It's true")

if False:
    print("It's true")

if bool("eggs"):
    print("Yes Please!")

# If converts string to bool with bool constructor
if "eggs":
    print("Yes Please!")

if 1 < 2:
    print("Yes Please!")
else:
    print("No Please!")

if 1 < 1:
    print("Yes 1")
elif 1==1:
    print("Yes 2")
else:
    print("Final")

###################### While loops ######################

c = 5
while c != 0:
    print('!!!!!!!!!!!!', c)
    c -= 1

# while True:
#     print('Infinite') # Infinite loop

while True:
    response = input()
    if int(response) % 7 == 0:
        print('End')
        break
