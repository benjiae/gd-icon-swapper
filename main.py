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

replaced = str(replaced_id)
replacing = str(replacing_id)
# Por ahora voy a copiar "player_01" a "player_02" y player_02 a player_02.bak
if mode == 1:
    if replaced_id <= 9:
        os.rename(path + "/player_0" + replaced + ".png", path + "/player_0" + replaced + ".png.bak")
        os.rename(path + "/player_0" + replaced + "-hd.png", path + "/player_0" + replaced + "-hd.png.bak")
        os.rename(path + "/player_0" + replaced + "-uhd.png", path + "/player_0" + replaced + "-uhd.png.bak")

        os.rename(path + "/player_0" + replaced + ".plist", path + "/player_0" + replaced + ".plist.bak")
        os.rename(path + "/player_0" + replaced + "-hd.plist", path + "/player_0" + replaced + "-hd.plist.bak")
        os.rename(path + "/player_0" + replaced + "-uhd.plist", path + "/player_0" + replaced + "-uhd.plist.bak")

    elif replaced_id >= 10:
        os.rename(path + "/player_" + replaced + ".png", path + "/player_" + replaced + ".png.bak")
        os.rename(path + "/player_" + replaced + "-hd.png", path + "/player_" + replaced + "-hd.png" + ".bak")
        os.rename(path + "/player_" + replaced + "-uhd.png", path + "/player_" + replaced + "-uhd.png" + ".bak")

        os.rename(path + "/player_0" + replaced + ".plist", path + "/player_0" + replaced + ".plist.bak")
        os.rename(path + "/player_0" + replaced + "-hd.plist", path + "/player_0" + replaced + "-hd.plist.bak")
        os.rename(path + "/player_0" + replaced + "-uhd.plist", path + "/player_0" + replaced + "-uhd.plist.bak")
"""""
    if replacing_id <= 9 and replaced_id <= 9:
      shutil.copy(path + "/player_0" + replacing, path + "/player_0", replaced)

    elif replacing_id >= 10 and replaced_id >= 10:
        shutil.copy(path + "/player_" + replacing, path + "/player_" + replaced)

    elif replacing_id <= 9 and replaced_id >= 10:
        shutil.copy(path + "/player_0" + replacing, path + "/player_" + replaced)

    elif replacing_id >= 10 and replaced_id <= 9:
        shutil.copy(path + "/player_" + replacing, path + "/player_0" + replaced)
        """""