import os

one_argument = 1
two_argument = 2
out_argument = 0

#This loop creates a flow-file out of each pair of consecutive images in dataset 0000 (located in folder "images"). Change content of folder "images" with another dataset and adapt the loop's range to the new dataset.
for i in range(232): 
	os.system("python pytorch-pwc/run.py --model default --one /home/diego/pytorch-pwc/images/{:06d}.png --two /home/diego/pytorch-pwc/images/{:06d}.png --out /home/diego/pytorch-pwc/out/{:06d}.flo".format(one_argument, two_argument, out_argument))

	one_argument += 1
	two_argument += 1
	out_argument += 1
