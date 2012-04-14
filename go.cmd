@echo off

:: Install dependencies...
for %%a in (colorama,lettuce) do (
	pip freeze | findstr %%a > nul
	if ERRORLEVEL 1 (
		pip install %%a
	)
)

:: pip installs an ancient version of pywinauto by default - work around it...
pip freeze | findstr pywinauto > nul
if ERRORLEVEL 1 (
	pip install hg+https://code.google.com/p/pywinauto
)

:: Run the tests...
echo on
lettuce features --with-xunit --xunit-file=results.xml --verbosity=4