import os
import shutil

path = "icons/"
ldr_path = "replaced_icons/icons/"

if not os.path.isdir("icons"):
    print("No icons folder found, please copy your icons folder to this directory (Geometry Dash/Resources/icons)")
    exit

if not os.path.isdir("replaced_icons"):
    print("no pack folder, creating one")
    os.mkdir("replaced_icons")

if not os.path.isdir("replaced_icons/icons"):
    print("no pack icons folder, creating one")
    os.mkdir("replaced_icons/icons")
    

while True:
    print("Select the gamemode you want:")
    print("1: Cube")
    print("2: Ship")
    print("3: Ball")
    print("4: UFO")
    print("5: Wave")
    print("6: Robot")
    print("7: Spider")
    print("8: Swing")
    print("9: Jetpack")

    while True:
        try:
            mode = int(input("Insert a number (1-9): "))
            if 1 <= mode <= 9:
                break
            else:
                print("Please, insert a number between 1 and 9")
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
            print("Please, insert an integer number.")
            continue

    print("")

    if replaced_id <= 9:
        replaced = "0" + str(replaced_id)
    else:
        replaced = str(replaced_id)

    if replacing_id <= 9:
        replacing = "0" + str(replacing_id)
    else:
        replacing = str(replacing_id)

    match mode:
        case 1:
            mode_string = "player_"
        case 2:
            mode_string = "ship_"
        case 3:
            mode_string = "player_ball_"
        case 4:
            mode_string = "bird_"
        case 5:
            mode_string = "dart_"
        case 6:
            mode_string = "robot_"
        case 7:
            mode_string = "spider_"
        case 8:
            mode_string = "swing_"
        case 9:
            mode_string = "jetpack_"

    list_ = [".png", "-hd.png", "-uhd.png", ".plist", "-hd.plist", "-uhd.plist"]

    for quality in list_:
        shutil.copyfile(path + mode_string + replacing + quality, ldr_path + mode_string + replaced + quality)

    print("Editing the plist files...")
    ### Editing the plist files

    plists = [".plist", "-hd.plist", "-uhd.plist"]

    for plist in plists:
        with open(path + mode_string + replacing + plist, "r") as file:
            filedata = file.read()
            filedata = filedata.replace(mode_string + replacing, mode_string + replaced)
        with open(ldr_path + mode_string + replaced + plist, "w") as file:
            file.write(filedata)

    print("")
    shutil.copyfile("pack.json","replaced_icons/pack.json")
    while True:
        try:
            repeat = int(input("Done! Do you want to make another change? (1 for Yes, 0 for No): "))
            break
        except ValueError:
            print("Please, insert an integer.")
            continue

    if repeat == 1:
        continue
    elif repeat == 0:
        break
print("")
print("Copy the icons folder from this directory to the TextureLDR packs folder.")