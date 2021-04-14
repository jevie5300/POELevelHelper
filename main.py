import time
from os import system

path = "C:/Program Files (x86)/Steam/steamapps/common/Path of Exile/logs/Client.txt"

print("Do you want to start a new run?y/n")
new_run = input()

if new_run == 'y':
    route_file = open("progress.default", encoding="latin1")
    route = route_file.readlines()
    print(route[0].strip("\n"))
    route.pop(0)
else:
    route_file = open("current_run.txt", encoding="latin1")
    route = route_file.readlines()
    print(route[0].strip("\n"))

last_line = "*** New Run ***"

try:
    while True:
        with open(path, encoding="latin1") as f:
            lines = f.readlines()
            lines_total = len(lines)-1
            current_line = lines[lines_total].strip("\n")
            if current_line != last_line and lines_total != -1:
                last_line = current_line
                if "You have entered " in last_line:
                    compare_string = last_line[last_line.index("]")+21:-1]
                    if compare_string in route[0]:
                        route.pop(0)
                        system('cls')
                        actions = route[0].split("-")
                        for a in actions:
                            print(a.strip("\n"))
        with open("current_run.txt", "w") as f:
            f.writelines(route)
        time.sleep(1)
except KeyboardInterrupt:
    f.close()
