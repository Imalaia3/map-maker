import os
import pygame
from settings import *
cwd = os.getcwd()
class Utils:

	def get_files(fold):
		res = []

		for path in os.listdir(fold):
			if os.path.isfile(os.path.join(fold, path)):
				res.append(path)
		return res





def setup_texture(fold):
	folder = cwd + fold
	TEXTURE_LIST = {}
	cont = Utils.get_files(folder)
	for name in cont:
		pic = pygame.image.load(folder+"/"+name).convert_alpha()
		pic = pygame.transform.scale(pic, (TILE_W, TILE_H))
		TEXTURE_LIST[name.split(".")[0]] = pic


	return TEXTURE_LIST