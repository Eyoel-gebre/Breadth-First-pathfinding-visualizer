import pygame
import sys
import queue
from math import floor

q = queue.Queue()
q.put('')
opath = list()

R = 1
L = -1
U = -10
D = 10

#checks if most recent path finds the target
def Found():
        global R
        global L
        global U
        global D
        global opath
        global start
        global grid
        global map
        path = opath[-1]
        path = list(path)
        pos = start

        for i in range(len(path)):
                if path[i] == 'R':
                        pos = pos + R
                elif path[i] == 'L':
                        pos = pos + L
                elif path[i] == 'U':
                        pos = pos + U
                elif path[i] == 'D':
                        pos = pos + D
        print(pos)
        if map[pos] == '-':
        	map[pos] = 'p'
        	grid.update()
        	pygame.display.update()
        if map[pos] == 'o':
                return True
        else:
                return False
        

#checks if path is a possible path
def Works(s):
        global R
        global L
        global U
        global D
        global start
        global map
        path = list(s)
        pos = start
        for i in range(len(path)):

                if path[i] == 'R':
                        pos = pos + R
                elif path[i] == 'L':
                        pos = pos + L
                elif path[i] == 'U':
                        pos = pos + U
                elif path[i] == 'D':
                        pos = pos + D

                if map[pos] == '#':
                        return False
                if pos < 0 or pos >= len(map):
                        return False
        return True

#draws the map with direction
def Draw():
        global R
        global L
        global U
        global D
        global opath
        global map
        global start
        path = opath[-1]
        pos = start
        for i in range(len(path)):
                if path[i] == 'R':
                        pos = pos + R
                elif path[i] == 'L':
                        pos = pos + L
                elif path[i] == 'U':
                        pos = pos + U
                elif path[i] == 'D':
                        pos = pos + D

                if map[pos] != 'o' and map[pos] != 'x':
                        map[pos] = '*'
      
        num = 0
        for i in range(10):
            print(map[num:num+10])
            num = num + 10

def FindStart():
        global map
        pos = 0
        for i in range(len(map)):
                if map[i] == 'x':
                        break
                else:
                        pos = pos + 1
        print('Startt Found')
        print(pos)
        return pos


def FindEnd():
        global map
        pos = 0
        for i in range(len(map)):
                if map[i] == 'o':
                        break
                else:
                        pos = pos + 1
        print('End Found')
        print(pos)
        return pos



#defines the map
map = list(('#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
            '#', '-', '-', '-', '-', '-', '-', '-', '-', '#',
            '#', '-', '-', '-', '-', '-', '-', '-', '-', '#',
            '#', '-', '-', '-', '-', '-', '-', '-', '-', '#',
            '#', '-', '-', '-', '-', '-', '-', '-', '-', '#',
            '#', '-', 'x', '-', '-', '-', '-', 'o', '-', '#',
            '#', '-', '-', '-', '-', '-', '-', '-', '-', '#',
            '#', '-', '-', '-', '-', '-', '-', '-', '-', '#',
            '#', '-', '-', '-', '-', '-', '-', '-', '-', '#',
            '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',))

#start and end points




#BREADTH-FIRST algorithim
def FindPath():
    global start
    global end
    start = FindStart()
    end = FindEnd()
    global q
    numattempts = 0
    while True:
            x = q.get()
            opath.append(x)
            print(opath[-1])
            numattempts = numattempts + 1
            if not(Found()):
                    r = x + 'R'
                    if (Works(r)):
                            q.put(r)
                    l = x + 'L'
                    if (Works(l)):
                            q.put(l)
                    u = x + 'U'
                    if (Works(u)):
                            q.put(u)
                    d = x + 'D'
                    if (Works(d)):
                            q.put(d)
            else:
                    break
    print('\n')
    print('Number of Attempted Paths: ' + str(numattempts))
    print('Shortest Possible Path: ' + opath[-1])
    Draw()
    with q.mutex:
    	q.queue.clear()
    q.put('')


def clear():
	global map
	for i in range(len(map)):
		if i < 10 or i > 89 or (i % 10) == 0 or ((i + 1) % 10) == 0:
			map[i] = '#'
		else: 
			map[i] = '-'



#-------------------General-----------------
#creates the pygame window
pygame.init()
surface = pygame.display.set_mode((500,600))


class Button(object):
	def __init__(self, name, color, dims, p):
		self.name = name
		self.col = color
		self.dim = dims
		self.p = p


	def norm(self):
		button = pygame.draw.rect(surface, self.col, self.dim)

		obj = pygame.font.SysFont('comicsansms', 30)
		text = obj.render(self.name, False, (255,255,255))
		surface.blit(text, self.p)

	def hover(self):
		button = pygame.draw.rect(surface, (self.col[0], self.col[1] + 50, self.col[2]), self.dim)

		obj = pygame.font.SysFont('comicsansms', 30)
		text = obj.render(self.name, False, (255,255,255))
		surface.blit(text, self.p)

#-----------------------Grid Class-----------
class Grid():
    def __init__(self):
        global map
        self.map = map

    def update(self):
        p = 0
        l = 0
        name = 0
        for i in self.map:
            if i == 'x':
                pygame.draw.rect(surface, (0, 0, 255), (p * 50,l * 50,50,50))
                pygame.draw.rect(surface, (255, 255, 255), (p * 50,l * 50,50,50), 1)
            elif i == 'o':
                pygame.draw.rect(surface, (0, 255, 0), (p * 50,l * 50,50,50))
                pygame.draw.rect(surface, (255, 255, 255), (p * 50,l * 50,50,50), 1)
            elif i == '#':
                pygame.draw.rect(surface, (255, 100, 0), (p * 50,l * 50,50,50))
                pygame.draw.rect(surface, (255, 255, 255), (p * 50,l * 50,50,50), 1)
            elif i == '*':
                pygame.draw.rect(surface, (0, 200, 200), (p * 50,l * 50,50,50))
                pygame.draw.rect(surface, (255, 255, 255), (p * 50,l * 50,50,50), 1)
            elif i == 'p':
                pygame.draw.rect(surface, (0, 100, 100), (p * 50,l * 50,50,50))
                pygame.draw.rect(surface, (255, 255, 255), (p * 50,l * 50,50,50), 1)
            else:
                pygame.draw.rect(surface, (0, 0, 0), (p * 50,l * 50,50,50))
                pygame.draw.rect(surface, (255, 255, 255), (p * 50,l * 50,50,50), 1)

            p = p + 1
            if (p % 10) == 0:
                l = l + 1
                p = 0

#--------------------MainLoop-----------------
sbutton = Button('Start', (0,150,0), (350,530,100,40), (360, 527))
rbutton = Button('Reset', (200,0,0), (50,530,100,40), (60, 527))
grid = Grid()
turn = 1
while True:

    #event loop checking for input events
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            x = floor(event.pos[0]/50)
            y = floor(event.pos[1]/50)
            mpos = y*10 + x
            #allows you to draw obstacles
            if mpos <= len(map) and mpos >= 0:
	            if event.buttons[0] == 1:
	                map[mpos] = '#'
	            if event.buttons[2] == 1:
	                map[mpos] = '-'
	        #start button changes color
            if event.pos[0] > 350 and event.pos[0] < 450 and event.pos[1] > 520 and event.pos[1] < 570:
            	sbutton.hover()
            else:
            	sbutton.norm()
            #Reset button changes colors
            if event.pos[0] > 50 and event.pos[0] < 150 and event.pos[1] > 520 and event.pos[1] < 570:
            	rbutton.hover()
            else:
            	rbutton.norm()


        #start Button click
        if event.type == pygame.MOUSEBUTTONDOWN:
        	if event.button == 1:
	        	if event.pos[0] > 350 and event.pos[0] < 450 and event.pos[1] > 520 and event.pos[1] < 570:
	         		FindPath()

	    #reset button click
        if event.type == pygame.MOUSEBUTTONDOWN:
        	if event.button == 1:
        		if event.pos[0] > 50 and event.pos[0] < 150 and event.pos[1] > 520 and event.pos[1] < 570:
        			clear()

        # places start and end nodes 		
        if event.type == pygame.MOUSEBUTTONDOWN:
        	if event.button == 2:
        		x = floor(event.pos[0]/50)
        		y = floor(event.pos[1]/50)
        		bpos = y*10 + x
        		if bpos >= 0 and bpos <= len(map):
        			
        			if turn == 1:
        				for i in range(len(map)):
        					if map[i] == 'x':
        						map[i] = '-'
        				map[bpos] = 'x'
        				turn = 2
        			elif turn == 2:
        				for i in range(len(map)):
        					if map[i] == 'o':
        						map[i] = '-'
        				map[bpos] = 'o'
        				turn = 1



    grid.update()
    pygame.display.update()
    