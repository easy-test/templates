 #!/usr/bin/bash

.venv/bin/python -m pip install --upgrade pip playwright
PLAYWRIGHT_BROWSERS_PATH=$HOME/pw-browsers .venv/bin/python -m playwright install
# playwright install firefox

#npm i -D @playwright/test
## install supported browsers
#npx playwright install