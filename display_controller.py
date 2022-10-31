import subprocess as sp
import pyautogui as pg
from time import sleep
import os
import sys

class sketch_group:
	def __init__(self, name, windows):
		self.name = name
		self.windows = windows
		self.i = 0
		self.n = len(self.windows)
	
	def activate_next_window(self):
		next_window = self.windows[self.i % self.n]
		os.system('xdotool windowactivate {}'.format(next_window))
		self.i += 1

sketch_names = sys.argv
sketch_groups = {}
interval = 30

windows = sp.getoutput('xdotool search chromium').split('\n')[1:]

for sketch in sketch_names:
	sketch_windows = []
	for window in windows:
		window_name = sp.getoutput('xdotool getwindowname {}'.format(window))
		if sketch in window_name:
			sketch_windows.append(window)
	sketch_groups[sketch] = sketch_group(sketch, sketch_windows)

print(sketch_windows)
sleep(10)

for i in range(10):
	pg.hotkey('ctrl', 'r')
	sketch_groups["warpGrid"].activate_next_window()
	for i in range(interval, 0, -1):
		if i % 5 == 0:
			
			print(i)
		sleep(1)
