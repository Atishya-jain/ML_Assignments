import numpy as np
from PIL import Image
import sys
import sys
import os
import random
from sklearn.model_selection import train_test_split
import pickle

np.set_printoptions(threshold=sys.maxsize)

# file_x = open('data/train_x_full','w')
# file_y = open('data/train_y_full','w')


os.chdir('data/validation_vanilla')
games_list = os.listdir()
games_list.sort()

X = []
Y = []

subsample_list = os.listdir()
subsample_list.remove('rewards.csv')
# for i in range(len(subsample_list)):
	# subsample_list[i] = int(subsample_list[i])
subsample_list.sort()	
labels = open("rewards.csv").readlines()
for i in range(len(labels)):
	labels[i] = int(float(labels[i].strip().split(',')[1]))
for tt, subsample in enumerate(subsample_list):
	# file_y.write(str(labels[subsample])+"\n")
	Y.append(labels[tt])
	os.chdir(str(subsample))
	images_list = os.listdir()
	images_list.sort()
	to_add = np.array([])
	ct=0
	prev = []
	for image in images_list:
		img = Image.open(image).convert('L')
		area = (8, 32, 152, 196)
		img = img.crop(area)
		img = img.resize((36, 41),Image.ANTIALIAS)

		arr = np.array(img)
		arr[arr > 0] = 1
		# arr=arr/255
		shape = arr.shape
		flat_arr = arr.ravel()
		vector = np.array(flat_arr, dtype = np.int16)
		if ct==0:
			to_add = vector
		else:
			to_add = np.append(to_add, vector - prev)				
		prev = np.copy(vector)
		ct+=1
	to_add.astype(int)
	X.append([])
	for i in to_add:
		X[-1].append(i)
	os.chdir("../")

		# file_x.write(str(i)+" ")
	# file_x.write("\n");
	# break
X = np.array(X).astype(int)
Y = np.array(Y).astype(int)
print(X.shape)
# train = {"X":X_train, "Y":Y_train}
# test = {"X":X_test, "Y":Y_test}
os.chdir("../")
# f = open("train_0_100_r", 'wb')
# pickle.dump(train, f)
# f.close()
# f = open("test_0_100_r", 'wb')
# pickle.dump(test, f)
# f.close()
np.save("x_val", X)
np.save("y_val", Y)
