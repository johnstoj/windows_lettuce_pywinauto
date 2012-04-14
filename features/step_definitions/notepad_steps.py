from lettuce import *
from pywinauto import *

@before.each_scenario
def before_each_scenario(scenario):
	world.application = application.Application()

@after.each_scenario
def after_each_scenario(scenario):
	# This ensures notepad is closed if an assertion happens.
	world.application.Kill_()

# ##############################################################################
@step(u'Given I have started Notepad')
def given_i_have_started_notepad(step):
	world.application.start_(ur"C:\\Windows\\System32\\notepad.exe")

@step(u'And I see a window titled "([^"]*)"')
def and_i_see_a_window_titled_title(step, title):
	assert world.application.window_(title = title).Exists(timeout = 5)

@step('When I add "([^"]*)" to the document')
def when_i_add_text_to_the_document(step, text):
	world.application.notepad.edit.TypeKeys(text)

@step('Then I can exit Notepad without saving')
def then_i_can_exit_notepad_without_saving(step):
	world.application.notepad.MenuSelect("File->Exit")
	world.application.notepad.DontSave.Click()
	assert world.application.notepad.Exists(timeout = 1) == False


