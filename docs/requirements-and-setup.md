> **macOS High Sierra requirements:**
* Install python 3.6.6 [link](https://www.python.org/downloads/release/python-366/)
* Install tesseract 4.0.0-beta.1 as described [here](https://github.com/tesseract-ocr/tesseract/wiki/Compiling#macos)
* pip3 install pyobjc-core
* pip3 install pyobjc

> **Windows 10 Pro requirements:**

* Install python 3.6.6 [link](https://www.python.org/downloads/release/python-366/)
* Install tesseract 4.0.0-beta.1 as described [here](../docs/tesseract-windows-install.md)

> **Ubuntu 18.04 LTS requirements:**

* sudo apt-get install build-essential
* sudo apt-get install checkinstall
* sudo apt-get install zlib1g-dev
* sudo apt-get update

* Install python 3.6.6 manually
    * Download gzipped tarball from [link](https://www.python.org/downloads/release/python-366)
    * Extract archive and cd into it
        * sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
        * ./configure
        * make
        * sudo make install

* sudo apt install python3-setuptools python3-pkg-resources
* sudo apt install python3-venv
* sudo apt install python3-xlib
* sudo apt install python3.6-dev
* sudo apt install python3-tk

* sudo apt install scrot

* pip3 install python3-xlib ( in case of from Xlib.display import Display error )

> Run pySteps
1. Install virtualenv:
    * pip3 install virtualenv

2. Create virtualenv:
    * python3 -m venv vnv

3. Enable virtualenv:
    * Windows : .\vnv\Scripts\activate
    * Ubuntu : source vnv/bin/activate
    * Osx : source vnv/bin/activate

4. Project Requirements (install from requirements.txt):
    * pip3 install --force -r requirements.txt

5. Run test commands:
    * all_: pytest -s -v
    * by folder_: pytest -s -v folder
    * by file_: pytest -s -v folder/file_test.py

> **Naming**

    * Only files that contains word "test" will be runned
    * Only functions that start with word "test" will be reported