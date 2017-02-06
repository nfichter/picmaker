import math
import random

def create():
	f = open("image.ppm","r+")
	
	s = "P3 500 500 255\n"
	for x in range(0,510):
		for y in range(0,102):
			r = x % 255
			g = (x + 55) % 255
			b = (x + 110) % 255
			s+="%s %s %s "%(r,g,b)
		s+="\n"
	for x in range(0,510):
		for y in range(103,204):
			r = y % 255
			g = (y + 55) % 255
			b = (y + 110) % 255
			s+="%s %s %s "%(r,g,b)
		s+="\n"
	for x in range(0,510):
		for y in range(205,306):
			r = (x + y) % 255
			g = (x + y + 55) % 255
			b = (x + y + 110) % 255
			s+="%s %s %s "%(r,g,b)
		s+="\n"
	for x in range(0,510):
		for y in range(307,408):
			r = (x - y) % 255
			g = (x - y + 55) % 255
			b = (x - y + 110) % 255
			s+="%s %s %s "%(r,g,b)
		s+="\n"
	for x in range(0,510):
		for y in range(409,510):
			r = (x * y) % 255
			g = (x * y + 55) % 255
			b = (x * y + 110) % 255
			s+="%s %s %s "%(r,g,b)
		s+="\n"
			
	f.write(s)
	
create()