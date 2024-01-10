import os
import shutil

path = "icons_test"

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
        replacing_id = int(input("Insert the ID of the icon you want: "))
        break
    except ValueError:
        print("Please, insert an integer.")
        continue

print("")

while True:
    try:
        replaced_id = int(input("Insert the ID of the icon you want to replace: "))
        break
    except ValueError:
        print("Please, insert an integer.")
        continue

print("")

if replacing_id <= 9:
    replaced = "0" + str(replaced_id)
else:
    replaced = str(replaced_id)

match mode:
    case 1:
        mode_string = "player"
    case 2:
        mode_string = "ship"
    case 3:
        mode_string = "player_ball"
    case 4:
        mode_string = "bird"
    case 5:
        mode_string = "robot"
    case 6:
        mode_string = "spider"
    case 7:
        mode_string = "swing"
    case 8:
        mode_string = "jetpack"

    #png
os.rename(path + "/" + mode_string + "_" + replaced + ".png", path + "/" + mode_string + "_" + replaced + ".png.bak")
os.rename(path + "/" + mode_string + "_" + replaced + "-hd.png", path + "/" + mode_string + "_" + replaced + "-hd.png.bak")
os.rename(path + "/" + mode_string + "_" + replaced + "-uhd.png", path + "/" + mode_string + "_" + replaced + "-uhd.png.bak")
    #plist
os.rename(path + "/" + mode_string + "_" + replaced + ".plist", path + "/" + mode_string + "_" + replaced + ".plist.bak")
os.rename(path + "/" + mode_string + "_" + replaced + "-hd.plist", path + "/" + mode_string + "_" + replaced + "-hd.plist.bak")
os.rename(path + "/" + mode_string + "_" + replaced + "-uhd.plist", path + "/" + mode_string + "_" + replaced + "-uhd.plist.bak")