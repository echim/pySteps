Generic python automation framework with PyAutogui, OpenCV and Tesseract-OCR for desktop apps.

Ubuntu Ubuntu 18.04 LTS requirements:
    sudo apt-get install build-essential
    sudo apt-get install checkinstall
    sudo apt-get install zlib1g-dev
    sudo apt-get update

    Install python 3.6.6 manually
     Download gzipped tarball https://www.python.org/downloads/release/python-366
     Extract archive and cd into it
        sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
        ./configure
        make
        sudo make install

    sudo apt install python3-setuptools python3-pkg-resources
    sudo apt install python3-venv
    sudo apt install python3-xlib
    sudo apt install python3.6-dev
    sudo apt install python3-tk

    sudo apt install scrot

    pip install python3-xlib ( in case of from Xlib.display import Display )

Create virtualenv:
    python3 -m venv vnv

Enable virtualenv:
    Windows : .\vnv\Scripts\activate
    Ubuntu : source vnv/bin/activate
    Osx : source vnv/bin/activate

Requirements (install from requirements.txt):
    pip3 install --force -r requirements.txt

Run test commands:
    all_: pytest -s -v
    by folder_: pytest -s -v folder
    by file_: pytest -s -v folder/file_test.py

Only files that contains word "test" will be runned
Only functions that start with word "test" will be reported

Tested on :
    Windows 10 Pro
    Ubuntu 18.04 LTS