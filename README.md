Requirements (install from requirements.txt):
- PyAutoGUI : http://pyautogui.readthedocs.io/en/latest/install.html
- Opencv-python : https://pypi.python.org/pypi/opencv-python

Run commands: 
- _all_: pytest -s -v
- _by folder_: pytest -s -v folder
- _by file_: pytest -s -v folder/file_test.py

Only files that contains word "test" will be runned
Only functions that start with word "test" will be reported

Use pyenv to easily change between python versions
- https://github.com/pyenv/pyenv

PyCharm setup to use pyenv
- http://victormartinez.co/2017/08/04/integrating-pycharm-with-pyenv
