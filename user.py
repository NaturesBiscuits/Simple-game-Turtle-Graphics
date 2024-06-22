from subprocess import call


def openprogram():
    call(['python', 'avoidTheBoxes'])


print("Avoid-The-Boxes!\n")

username = input("Enter user: ")

print("\nWelcome " + username + "!"
      "\nAvoid-The-Boxes is a simple game"
      "\nUse the arrow-keys to move, Up, Down, Right, Left."
      "\nAvoid the boxes and collect gold."
      "\nYou have 3 lives, 1 gold-coin is equal to 100 points.")

print("\nSpeed may vary depending how fast your computer is."
      "\nif your running on a newer device."
      '\nEnter down "0.3" if not, "2" will be just fine.' 
      "\nbut you can always customize it however you like it."
      "\nthink of it as your set difficulty.\n")
speed = eval(input("Enter speed: "))

answer = input("\nPress Enter to proceed to the game")

if answer == 'y':
    openprogram()
