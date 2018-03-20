Requirements (install from requirements.txt):
- pip install --force -r requirements.txt

Install Tesseract on Windows 3.5.1
- https://github.com/parrot-office/tesseract/releases/tag/3.5.1
To access tesseract-OCR from any location you may have to add the directory where the tesseract-OCR binaries are located to the Path variables, probably C:\Program Files\Tesseract-OCR.

Instal Tesseract 3.0.5 on Linux from
- https://lucacerone.net/2017/install-tesseract-3-0-5-in-ubuntu-16-04/
 

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
