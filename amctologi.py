import re

s = """
Delay 23 ms
MoveR 0 3
Delay 23 ms
MoveR 0 27
Delay 23 ms
MoveR 0 3
Delay 23 ms
MoveR 0 27
Delay 23 ms
MoveR 0 3
Delay 23 ms
MoveR 0 27
Delay 23 ms
MoveR 0 3
Delay 23 ms
MoveR 0 27
Delay 23 ms
MoveR 0 3
Delay 23 ms
MoveR 0 27
Delay 23 ms
MoveR 0 3
Delay 23 ms
MoveR 0 27
Delay 23 ms
MoveR 0 3
Delay 23 ms
MoveR 0 27
Delay 23 ms
MoveR 0 3
Delay 23 ms
MoveR 0 27
Delay 23 ms
MoveR 0 3
Delay 23 ms
MoveR 0 27
Delay 23 ms
MoveR 0 3
Delay 23 ms
MoveR 0 27
Delay 23 ms
MoveR 0 3
Delay 23 ms
MoveR 0 27
Delay 23 ms
MoveR 0 3
Delay 23 ms
MoveR 0 27
Delay 23 ms
MoveR 0 3
Delay 23 ms
MoveR 0 27
Delay 23 ms
MoveR 0 3
Delay 23 ms
MoveR 0 27
Delay 23 ms
MoveR 0 1
"""
sep = s.splitlines()
# print(sep)
output=""
for i in sep:
    ints = re.findall(r"[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", i)
    if("Delay" in i):
        # ints = [int(s) for s in i.split() if s.isdigit()]
        output+=(f"Sleep({ints[0]})")+"\n"
    elif("MoveR" in i):
        # ints = [int(s) for s in i.split() if s.isdigit()]
        output+=(f"MoveMouseRelative({ints[0]}, {ints[1]})")+"\n"

        
f = open("amctologi.txt", "w")
f.write(output)
f.close()

# for i in sep:
#     print(i)