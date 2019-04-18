import sys
import os

os.chdir('data/vanilla')
games_list = os.listdir()
games_list.sort()

os.chdir('../subsample')
for game in games_list:
	os.mkdir(game)

