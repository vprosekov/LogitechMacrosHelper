import re

s = """
Sleep(23)
MoveMouseRelative(0, 3)
Sleep(23)
MoveMouseRelative(0, 27)
Sleep(23)
MoveMouseRelative(0, 3)
Sleep(23)
MoveMouseRelative(0, 27)
Sleep(23)
MoveMouseRelative(0, 3)
Sleep(23)
MoveMouseRelative(0, 27)
Sleep(23)
MoveMouseRelative(0, 3)
Sleep(23)
MoveMouseRelative(0, 27)
Sleep(23)
MoveMouseRelative(0, 3)
Sleep(23)
MoveMouseRelative(0, 27)
Sleep(23)
MoveMouseRelative(0, 3)
Sleep(23)
MoveMouseRelative(0, 27)
Sleep(23)
MoveMouseRelative(0, 3)
Sleep(23)
MoveMouseRelative(0, 27)
Sleep(23)
MoveMouseRelative(0, 3)
Sleep(23)
MoveMouseRelative(0, 27)
Sleep(23)
MoveMouseRelative(0, 3)
Sleep(23)
MoveMouseRelative(0, 27)
Sleep(23)
MoveMouseRelative(0, 3)
Sleep(23)
MoveMouseRelative(0, 27)
Sleep(23)
MoveMouseRelative(0, 3)
Sleep(23)
MoveMouseRelative(0, 27)
Sleep(23)
MoveMouseRelative(0, 3)
Sleep(23)
MoveMouseRelative(0, 27)
Sleep(23)
MoveMouseRelative(0, 3)
Sleep(23)
MoveMouseRelative(0, 27)
Sleep(23)
MoveMouseRelative(0, 3)
Sleep(23)
MoveMouseRelative(0, 27)
Sleep(23)
MoveMouseRelative(0, 1)

                
"""
sep = s.splitlines()
# print(sep)

old = 0.629
new = 0.063

output = ""

for i in sep:
    ints = re.findall(r"[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", i)
    if("Sleep" in i):
        # ints = [int(s) for s in i.split() if s.isdigit()]
        output+=(i+"\n")
        # print(f"Sleep({int(ints[0])*0.6/1.6})")
    elif("MoveMouseRelative" in i):
        # ints = [int(s) for s in i.split() if s.isdigit()]
        output+=(f"MoveMouseRelative({round(int(ints[0])*old/new)}, {round(int(ints[1])*old/new)})")+"\n"
    else:
        output+=(i)+"\n"
print(output)

f = open("changesensitivity.txt", "w")
f.write(output)
f.close()
# print(round(20*0.192/0.52))
# for i in sep:
#     print(i)