import os

print("")
print("Thanks for trying this tool!")
print("To find the icon IDs, you can use GDColon's page. (https://gdbrowser.com/iconkit/)")
print("")
print("Select the gamemode you want:")
print("1: Cube")
print("2: Ship")
print("3: Ball")
print("4: UFO")
print("5: Robot")
print("6: Spider")
print("7: Swing")
print("8: Jetpack")

while True:
    try:
        mode = int(input("Insert a number (1-8): "))
        if 1 <= mode <= 8:
            break
        else:
            print("Please, insert a number between 1-8")
            continue
    except ValueError:
        print("Please, insert an integer")
        print("")
        continue

print("")

while True:
    try:
        replacingID = int(input("Insert the ID of the icon you want: "))
        break
    except ValueError:
        print("Please, insert an integer.")
        continue

print("")

while True:
    try:
        replacedID = int(input("Insert the ID of the icon you want to replace: "))
        break
    except ValueError:
        print("Please, insert an integer.")
        continue

print("")