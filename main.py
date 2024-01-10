import os
import shutil

path = "icons/"
path_backup = path + "backups/"

if not os.path.isdir(path):
    print("No icons folder found, please copy your icons folder to this directory (Geometry Dash/Resources/icons)")
    exit

if not os.path.isdir(path_backup):
    print("no backups folder, creating one")
    os.mkdir(path_backup)

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
        mode_string = "robot_"
    case 6:
        mode_string = "spider_"
    case 7:
        mode_string = "swing_"
    case 8:
        mode_string = "jetpack_"

print("Moving original files to backups folder...")
### Moving the original files to the backups folder
os.rename(path + mode_string + replaced + ".png", path_backup + mode_string + replaced + ".png")
os.rename(path + mode_string + replaced + ".plist", path_backup + mode_string + replaced + ".plist")

os.rename(path + mode_string + replaced + "-hd.png", path_backup + mode_string + replaced + "-hd.png")
os.rename(path + mode_string + replaced + "-hd.plist", path_backup + mode_string + replaced + "-hd.plist")

os.rename(path + mode_string + replaced + "-uhd.png", path_backup + mode_string + replaced + "-uhd.png")
os.rename(path + mode_string + replaced + "-uhd.plist", path_backup + mode_string + replaced + "-uhd.plist")

print("Replacing original files with the other icon's ones...")
### Copying the replacement files

shutil.copyfile(path + mode_string + replacing + ".png", path + mode_string + replaced + ".png")
shutil.copyfile(path + mode_string + replacing + ".plist", path + mode_string + replaced + ".plist")

shutil.copyfile(path + mode_string + replacing + "-hd.png", path + mode_string + replaced + "-hd.png")
shutil.copyfile(path + mode_string + replacing + "-hd.plist", path + mode_string + replaced + "-hd.plist")

shutil.copyfile(path + mode_string + replacing + "-uhd.png", path + mode_string + replaced + "-uhd.png")
shutil.copyfile(path + mode_string + replacing + "-uhd.plist", path + mode_string + replaced + "-uhd.plist")

print("Editing the plist files...")
### Editing the plist files

## low quality
with open(path + mode_string + replaced + ".plist", 'r') as file:
    filedata = file.read()

    filedata = filedata.replace(mode_string + replacing, mode_string + replaced)

with open(path + mode_string + replaced + ".plist", 'w') as file:
    file.write(filedata)

## medium quality
with open(path + mode_string + replaced + "-hd.plist", 'r') as file:
    filedata = file.read()

    filedata = filedata.replace(mode_string + replacing, mode_string + replaced)

with open(path + mode_string + replaced + "-hd.plist", 'w') as file:
    file.write(filedata)

## high quality
with open(path + mode_string + replaced + "-uhd.plist", 'r') as file:
    filedata = file.read()

    filedata = filedata.replace(mode_string + replacing, mode_string + replaced)

with open(path + mode_string + replaced + "-uhd.plist", 'w') as file:
    file.write(filedata)

print("Done! copy the icons folder from this directory to the Resources folder.")
exit