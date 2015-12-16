#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Date: 2015-12-16
# author: wjk

# discription
'''
seven stones, each one stands one frog, when you click that stone, the frog say "woog", they can only jump one frog
You should change the place of the three with another three
'''

# method: use MonkeyRunner as a tool to click the screen for user to minimize the using time


from com.android.monkeyrunner import MonkeyRunner
import time

device = MonkeyRunner.waitForConnection()

# coordinates of seven stones, you should change them when they place different place in screen
stones_x = [0, 112, 253, 394, 535, 676, 817, 958]
stones_y = 1115


jump_sequtial = [3, 5, 6, 4, 2, 1, 3, 5, 7, 6, 4, 2, 3, 5, 4]

for command in jump_sequtial:
	device.touch(stones_x[command], stones_y, 'DOWN_AND_DOWN')
	time.sleep(0.1)

