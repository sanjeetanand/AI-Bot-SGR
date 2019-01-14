import pyscreenshot as ImageGrab
import os
import time
import pyautogui
from PIL import ImageOps
from numpy import *
x_pad=224
y_pad=225

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

sushiTypes = {2352:'onigiri', 
              2996:'caliroll',
              2359:'gunkan',}
class Blank:
	seat_1 = 8465
	seat_2 = 6210
	seat_3 = 11659
	seat_4 = 11406
	seat_5 = 7132
	seat_6 = 8986

class Cord:
	f_shrimp = (39+x_pad,394+y_pad)
	f_rice = (92+x_pad,392+y_pad)
	f_nori = (39+x_pad,447+y_pad)
	f_roe = (94+x_pad,448+y_pad)
	f_salmon = (37+x_pad,503+y_pad)
	f_unagi = (95+x_pad,503+y_pad)

	phone = (582+x_pad, 430+y_pad)

	menu_toppings = (547+x_pad, 329+y_pad)

	t_shrimp = (494+x_pad, 281+y_pad)
	t_nori = (495+x_pad, 334+y_pad)
	t_roe = (577+x_pad, 334+y_pad)
	t_salmon = (494+x_pad, 388+y_pad)
	t_unagi = (578+x_pad, 279+y_pad)
	t_exit = (595+x_pad, 392+y_pad)

	menu_rice = (543+x_pad, 352+y_pad)
	buy_rice = (546+x_pad, 341+y_pad)

	delivery_norm = (492+x_pad, 353+y_pad)





 

def check_bubs():
 
	checkFood()
	s1 = get_seat_one()
	if s1 != Blank.seat_1:
		if sushiTypes.has_key(s1):
    			print 'table 1 is occupied and needs %s' % sushiTypes[s1]
    			makeFood(sushiTypes[s1])
		else:
    			print 'sushi not found!\n sushiType = %i' % s1

	else:
		print 'Table 1 unoccupied'
 
	clear_tables()
	checkFood()
	s2 = get_seat_two()
	if s2 != Blank.seat_2:
		if sushiTypes.has_key(s2):
			print 'table 2 is occupied and needs %s' % sushiTypes[s2]
			makeFood(sushiTypes[s2])
		else:
			print 'sushi not found!\n sushiType = %i' % s2

	else:
		print 'Table 2 unoccupied'

	checkFood()
	s3 = get_seat_three()
	if s3 != Blank.seat_3:
		if sushiTypes.has_key(s3):
    			print 'table 3 is occupied and needs %s' % sushiTypes[s3]
    			makeFood(sushiTypes[s3])
		else:
    			print 'sushi not found!\n sushiType = %i' % s3

	else:
		print 'Table 3 unoccupied'

	checkFood()
	s4 = get_seat_four()
	if s4 != Blank.seat_4:
		if sushiTypes.has_key(s4):
    			print 'table 4 is occupied and needs %s' % sushiTypes[s4]
    			makeFood(sushiTypes[s4])
		else:
    			print 'sushi not found!\n sushiType = %i' % s4

	else:
		print 'Table 4 unoccupied'

	clear_tables()
	checkFood()
	s5 = get_seat_five()
	if s5 != Blank.seat_5:
		if sushiTypes.has_key(s5):
    			print 'table 5 is occupied and needs %s' % sushiTypes[s5]
    			makeFood(sushiTypes[s5])
		else:
    			print 'sushi not found!\n sushiType = %i' % s5

	else:
		print 'Table 5 unoccupied'

	checkFood()
	s6 = get_seat_six()
	if s6 != Blank.seat_6:
		if sushiTypes.has_key(s6):
    			print 'table 1 is occupied and needs %s' % sushiTypes[s6]
    			makeFood(sushiTypes[s6])
		else:
    			print 'sushi not found!\n sushiType = %i' % s6

	else:
		print 'Table 6 unoccupied'

	clear_tables()

def checkFood():
	for i, j in foodOnHand.items():
		if i == 'nori' or i == 'rice' or i == 'roe':
			if j <= 3:
				print '%s is low and needs to be replenished' % i
				buyFood(i)
def get_seat_one():
	box = (29+x_pad,116+y_pad,31+54+x_pad,116+22+y_pad)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	print a  
	return a
def get_seat_two():
	box = (130+x_pad,116+y_pad,126+60+x_pad,116+22+y_pad)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	print a   
	return a
 
def get_seat_three():
	box = (231+x_pad,116+y_pad,227+60+x_pad,116+22+y_pad)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	print a
	return a
 
def get_seat_four():
	box = (332+x_pad,116+y_pad,328+60+x_pad,116+22+y_pad)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	print a
	return a
 
def get_seat_five():
	box = (433+x_pad,116+y_pad,429+60+x_pad,116+22+y_pad)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	print a
	return a
 
def get_seat_six():
	box = (534+x_pad,116+y_pad,530+60+x_pad,116+22+y_pad)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	print a
	return a

def makeFood(food):
	if food == 'caliroll':
		print 'Making a caliroll'
		foodOnHand['rice'] -= 1
		foodOnHand['nori'] -= 1
		foodOnHand['roe'] -= 1 
		mousePos(Cord.f_rice)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_nori)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_roe)
		leftClick()
		time.sleep(.1)
		foldMat()
		time.sleep(1.5)
     
	elif food == 'onigiri':
		print 'Making a onigiri'
		foodOnHand['rice'] -= 2
		foodOnHand['nori'] -= 1
		mousePos(Cord.f_rice)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_rice)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_nori)
		leftClick()
		time.sleep(.1)
		foldMat()
		time.sleep(1.5)
 
	elif food == 'gunkan':
		foodOnHand['rice'] -= 1
		foodOnHand['nori'] -= 1
		foodOnHand['roe'] -= 2
		mousePos(Cord.f_rice)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_nori)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_roe)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_roe)
		leftClick()
		time.sleep(.1)
		foldMat()
		time.sleep(1.5)

def foldMat():
	mousePos((Cord.f_rice[0]+40,Cord.f_rice[1])) 
	leftClick()
	time.sleep(.1)

def clear_tables():
	mousePos((85+x_pad, 263+y_pad))
	leftClick()

	mousePos((185+x_pad, 263+y_pad))
	leftClick()

	mousePos((285+x_pad, 263+y_pad))
	leftClick()

	mousePos((385+x_pad, 263+y_pad))
	leftClick()

	mousePos((485+x_pad, 263+y_pad))
	leftClick()

	mousePos((585+x_pad, 263+y_pad))
	leftClick()
	time.sleep(1)

def buyFood(food):
     	mousePos(Cord.phone)
	mousePos(Cord.menu_toppings)

	mousePos(Cord.t_shrimp)
	mousePos(Cord.t_nori)
	mousePos(Cord.t_roe)
	mousePos(Cord.t_salmon)
	mousePos(Cord.t_unagi)
	mousePos(Cord.t_exit)

	mousePos(Cord.menu_rice)
	mousePos(Cord.buy_rice)

	mousePos(Cord.delivery_norm)
     
	if food == 'rice':
		mousePos(Cord.phone)
		time.sleep(.1)
		leftClick()
		mousePos(Cord.menu_rice)
		time.sleep(.05)
		leftClick()
		s = screenGrab()
		if s.getpixel(Cord.buy_rice) != (127, 127, 127):
			print 'rice is available'
			mousePos(Cord.buy_rice)
			time.sleep(.1)
			leftClick()
			mousePos(Cord.delivery_norm)
			foodOnHand['rice'] += 10
			time.sleep(.1)
			leftClick()
			time.sleep(2.5)
		else:
			print 'rice is NOT available'
			mousePos(Cord.t_exit)
			leftClick()
			time.sleep(1)
			buyFood(food)
		     

	     
	if food == 'nori':
		mousePos(Cord.phone)
		time.sleep(.1)
		leftClick()
		mousePos(Cord.menu_toppings)
		time.sleep(.05)
		leftClick()
		s = screenGrab()
		print 'test'
		time.sleep(.1)
		if s.getpixel(Cord.t_nori) != (53,53,39):
			print 'nori is available'
			mousePos(Cord.t_nori)
			time.sleep(.1)
			leftClick()
			mousePos(Cord.delivery_norm)
			foodOnHand['nori'] += 10
			time.sleep(.1)
			leftClick()
			time.sleep(2.5)
		else:
			print 'nori is NOT available'
			mousePos(Cord.t_exit)
			leftClick()
			time.sleep(1)
			buyFood(food)

	if food == 'roe':
		mousePos(Cord.phone)
		time.sleep(.1)
		leftClick()
		mousePos(Cord.menu_toppings)
		time.sleep(.05)
		leftClick()
		s = screenGrab()
		 
		time.sleep(.1)
		if s.getpixel(Cord.t_roe) != (101,13,13):
			print 'roe is available'
			mousePos(Cord.t_roe)
			time.sleep(.1)
			leftClick()
			mousePos(Cord.delivery_norm)
			foodOnHand['roe'] += 10
			time.sleep(.1)
			leftClick()
			time.sleep(2.5)
		else:
			print 'roe is NOT available'
			mousePos(Cord.t_exit)
			leftClick()
			time.sleep(1)
			buyFood(food)

def get_all_seats():
	get_seat_one()
	get_seat_two()
	get_seat_three()
	get_seat_four()
	get_seat_five()
	get_seat_six()

def startGame():
	#location of first menu
	mousePos((540, 484))
	leftClick()
	time.sleep(1)

	#location of second menu
	mousePos((548, 675))
	leftClick()
	time.sleep(1)

	#location of third menu
	mousePos((808, 734))
	leftClick()
	time.sleep(1)

	#location of fourth menu
	mousePos((547, 665))
	leftClick()
	time.sleep(1)


def screenGrab():
	box = (x_pad+1, y_pad+1, x_pad+640, y_pad+479)
	im = ImageGrab.grab()
	##im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
	return im

def grab():
	box = (x_pad + 1,y_pad+1,x_pad+640,y_pad+479)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	print a
	return a


def get_cords():
	x,y = pyautogui.position()
	print(x,y)

def leftClick():
	pyautogui.click(button='left')
def leftDown():
	pyautogui.mouseDown(button='left')
def leftUp():
	pyautogui.mouseUp(button='left')
def rightClick():
	pyautogui.click(button='right')
def rightDown():
	pyautogui.mouseDown(button='right')
def rightUp():
	pyautogui.mouseUp(button='right')
def mousePos(cord):
	pyautogui.moveTo(cord[0],cord[1])
     


def main():
	startGame()
	i=1
	while(i<20):
		check_bubs()
		i=i+1
 
if __name__ == '__main__':
	main()
