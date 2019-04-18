import sys
import os
import random


def mkdir(path, folder_name):
	cur_dir = os.getcwd()
	os.chdir(path)
	os.mkdir(folder_name)
	os.chdir(cur_dir)

os.chdir('data/vanilla')
games_list = os.listdir()
games_list.sort()


for game in games_list:
	os.chdir(game)
	images = os.listdir()
	images.sort()
	images.remove('rew.csv')
	image = 0
	new_game = 0

	rewards = open("rew.csv").readlines()
	for i in range(len(rewards)):
		rewards[i] = float(rewards[i].strip())
	# print(len(rewards))
	# print(len(images))
	reward_file = open('../../subsample/'+game+'/labels','w')
	while(image+6+1<len(images)):
		images_7 = images[image:image+7]
		rewards_to_write = rewards[image+6+1 - 1]#-1 as frame t has it's reward at reward t-1 (0 indexing of both)

############################################################
		if(rewards_to_write>0):
		#avoiding this and doing random sampling of i,j
		# do this only when reward is 1
			# for i in range(0,6):
			# 	for j in range(i+1,7):
			# 		# if(image!=0 and j==7):
			# 			# continue
			# 		mkdir("../../subsample/"+game+"/", str(new_game))
			# 		reward_file.write(str(rewards_to_write)+"\n")
			# 		images_5 = list.copy(images_7)
			# 		del images_5[j]
			# 		del images_5[i]
			# 		for k in images_5:
			# 			os.system("cp "+str(k)+" ../../subsample/"+game+"/"+str(new_game)+"/"+str(k))
			# 		# print(images_5)
			# 		new_game+=1
			for num in range(4):#repeat 5 times for 1 reward
				i = random.randint(0,4)
				j = random.randint(i+1,5)
				# while(j==i):
					# j = random.randint(i+1,5)
				mkdir("../../subsample/"+game+"/", str(new_game))
				reward_file.write(str(rewards_to_write)+"\n")
				images_5 = list.copy(images_7)
				del images_5[j]
				del images_5[i]
				for k in images_5:
					os.system("cp "+str(k)+" ../../subsample/"+game+"/"+str(new_game)+"/"+str(k))
				new_game+=1
#############################################################
		else:
			for num in range(1):#repeat 2 times for 0 reward
				i = random.randint(0,4)
				j = random.randint(i+1,5)
				# while(j==i):
					# j = random.randint(i+1,6)
				mkdir("../../subsample/"+game+"/", str(new_game))
				reward_file.write(str(rewards_to_write)+"\n")
				images_5 = list.copy(images_7)
				del images_5[j]
				del images_5[i]
				for k in images_5:
					os.system("cp "+str(k)+" ../../subsample/"+game+"/"+str(new_game)+"/"+str(k))
				new_game+=1




		for t in range(1,7):
			if(image+t+6+1<len(images) and rewards[image+t+6+1 - 1]==1):
				image+=t
				break
		else:
			image+=7
############################################################
	os.chdir("../")
	# reward_file.close()
	print (game)
