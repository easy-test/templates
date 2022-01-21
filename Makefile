install:
	PLAYWRIGHT_BROWSERS_PATH=0 playwright install chromium
	pyinstaller -F app.py