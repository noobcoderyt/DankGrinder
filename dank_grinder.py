from pynput.keyboard import *
import time

keyboard = Controller()

time.sleep(3)

for i in range(20):
	for char in "pls beg":
		keyboard.press(char)
		keyboard.release(char)
		time.sleep(0.05)

	keyboard.press(Key.enter)
	time.sleep(1.5)

	for char in "pls hunt":
		keyboard.press(char)
		keyboard.release(char)
		time.sleep(0.06)

	keyboard.press(Key.enter)
	time.sleep(1.5)

	for char in "pls fish":
		keyboard.press(char)
		keyboard.release(char)
		time.sleep(0.08)

	keyboard.press(Key.enter)
	time.sleep(1.5)

	for char in "pls dig":
		keyboard.press(char)
		keyboard.release(char)
		time.sleep(0.05)

	keyboard.press(Key.enter)
	time.sleep(1.5)

	for char in "pls crime":
		keyboard.press(char)
		keyboard.release(char)
		time.sleep(0.07)

	keyboard.press(Key.enter)
	time.sleep(3)
	

	for char in "pls search":
		keyboard.press(char)
		keyboard.release(char)
		time.sleep(0.03)

	keyboard.press(Key.enter)
	time.sleep(3)

	keyboard.type("pls sell")
	keyboard.press(Key.enter)

	time.sleep(1.5)

	keyboard.type("pls bal")
	keyboard.press(Key.enter)

	time.sleep(18)