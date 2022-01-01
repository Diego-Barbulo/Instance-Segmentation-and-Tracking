import os
import sys

one_argument = 0
two_argument = 0

#Each loop uses the file "color_flow" to generate color flow-images out of the flow-files stored in the "flow" folder. The minimum and maximum flow values of each flow-file are part of the terminal output. Save this output to a log to later extract the minimum-flow values.

for i in range(1):
    for i in range(232):

        os.system("./color_flow path_to_flow_files/{:06d}.flo path_to_output_folder/{:06d}.png".format(one_argument, two_argument))

        one_argument += 1
        two_argument += 1

    for i in range(298):

        os.system("./color_flow flow/D1-Flow_files/{:06d}.flo end1/{:06d}.png".format(one_argument, two_argument))
        one_argument += 1
        two_argument += 1

    for i in range(79):

        os.system("./color_flow flow/D2-Flow_files/{:06d}.flo end2/{:06d}.png".format(one_argument, two_argument))

        one_argument += 1
        two_argument += 1


    for i in range(99):

        os.system("./color_flow flow/D3-Flow_files/{:06d}.flo end3/{:06d}.png".format(one_argument, two_argument))

        one_argument += 1
        two_argument += 1

    for i in range(60):

        os.system("./color_flow flow/D5-Flow_files/{:06d}.flo end5/{:06d}.png".format(one_argument, two_argument))

        one_argument += 1
        two_argument += 1

    for i in range(85):

        os.system("./color_flow flow/D6-Flow_files/{:06d}.flo end6/{:06d}.png".format(one_argument, two_argument))

        one_argument += 1
        two_argument += 1


    for i in range(99):

        os.system("./color_flow flow/D7-Flow_files/{:06d}.flo end7/{:06d}.png".format(one_argument, two_argument))

        one_argument += 1
        two_argument += 1
