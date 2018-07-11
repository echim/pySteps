Automation project based on image recognition and OCR

Create virtualenv:
- python3 -m venv vnv

Enable virtualenv:
- Windows : .\vnv\Scripts\activate
- Ubuntu : source vnv/bin/activate
- Osx : source vnv/bin/activate

Ubuntu requirements:
    sudo apt install python3
    sudo apt install python3-venv
    sudo apt install python3-xlib
    sudo apt-get install python3.6-dev

Requirements (install from requirements.txt):
- pip3 install --force -r requirements.txt

Run commands: 
- _all_: pytest -s -v
- _by folder_: pytest -s -v folder
- _by file_: pytest -s -v folder/file_test.py

Only files that contains word "test" will be runned
Only functions that start with word "test" will be reported

Tested on :
    Windows 10 Pro
    Ubuntu 18.04 LTS