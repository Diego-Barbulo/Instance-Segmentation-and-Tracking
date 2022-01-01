import os
import re

log_path = '/path_to_minimum-flow-logs/'
path = '/path_to_UV_images/'
files = os.listdir(path)
log = open(log_path + 'X.txt', 'r')
lines = log.readlines()
sub = "normalizing"
sub1 = "Writing"

is_there = False
minimumUV = []

for line in lines:

    if sub in line:
        continue
    if sub1 in line:
        is_there = True
        continue
    if is_there:
        motion = list(map(float, re.findall(r'[-+]?\d*\.\d+|\d+', line)))
        u = motion[1]
        v = motion[3]
        minimumUV.append([u, v])
print(minimumUV)

lsu = [round(i[0]) for i in minimumUV]
lsv = [round(i[1]) for i in minimumUV]

print(lsu)
print(lsv)

# The loop below renames all UV images with their respective minimum-flow values. The "x" and "y" terminations are the required format if the flow images are going to be used within Track R-CNN.

for c in range(232):
    old_name1 = r"/path_to_UV-images/{:06d}_u.png".format(c)
    new_name1 = r"/path_to_UV-images/{:06d}_x_minimal{}.png".format(c, lsu[c])
    old_name2 = r"/path_to_UV-images/{:06d}_v.png".format(c)
    new_name2 = r"/path_to_UV-images/{:06d}_y_minimal{}.png".format(c, lsv[c])
    os.rename(old_name1, new_name1)
    os.rename(old_name2, new_name2)
