Feature: Notepad automation example.

	Scenario: Start Notepad and type some content.
		Given I have started Notepad
		And I see a window titled "Untitled - Notepad"
		When I add "Hello" to the document
		Then I can exit Notepad without saving