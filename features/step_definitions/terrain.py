from pywinauto import *
from pywinauto.controls import HwndWrapper
import colorama
from lettuce import *
import re

def register_pywinauto_custom_control(control_class, base_control_class):
	'''
		You can use this function to register custom controls with pywinauto
		after it initialises.  This code code for this came from the guts of 
		the pywinauto library.
	'''
	if not control_class in controls.win32_controls.EditWrapper.windowclasses:
		controls.win32_controls.EditWrapper.windowclasses.append(control_class)
		HwndWrapper._MetaWrapper.re_wrappers[re.compile(control_class)] = base_control_class
		HwndWrapper._MetaWrapper.str_wrappers[control_class] = base_control_class

@before.all
def initialise():
	colorama.init()
	
	# Register a custom edit control...
	register_pywinauto_custom_control('SNET$Edit', controls.win32_controls.EditWrapper)