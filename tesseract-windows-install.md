Install steps are the same as explained [here](https://github.com/tesseract-ocr/tesseract/wiki/Compiling#windows)
but slightly changed to provide more details

1. Todo
    * Uninstall any previous version of Tesseract.
    * Install Visual Studio Community edition.

2. Required:
    * CMake : Get app from [here](https://cmake.org/download/)
        * while installing, check option: **Add CMake to the system PATH**

    * CPPAN : Download from [here](https://cppan.org/client/cppan-master-Windows-client.zip)
        * create folder **C:\Program Files (x86)\cppan**
        * move the **cppan.exe** file to **C:\Program Files (x86)\cppan**
        * add **C:\Program Files (x86)\cppan** to system PATH

3. Compiling steps
    * cd C:\
    * git clone https://github.com/tesseract-ocr/tesseract tesseract
    * cd tesseract
    * cppan
    * mkdir build
    * cd build
    * cppan ..
    * cmake .. -G "Visual Studio 15 2017 Win64"

    * Edit cppan.yml and uncomment, and edit, this line:
        * \#generator: Visual Studio 14 2015 Win64 -> generator: Visual Studio 15 2017 Win64

    * cppan --generate .

    * Open tesseract.sln from Visual Studio
        1) File -> Open -> Project/Solution ( select **C:\tesseract\Win64\tesseract.sln** )
        2) Right click on tesseract solution ( from Solution Explorer )
            * Select Configuration Properties ( left dropdown)
            * Select C/C++ ( dropdown )
            * Select Language option
                * From the Language options check that Open MP Support is set to Yes ( /openmp )

        3) From Solution Configuration ( Debug might be selected ) select Release
        4) From Build menu click Build Solution

    * The build output is located at **C:\tesseract\Win64\bin\Release**
        * Add this to the system PATH ( restart might be required )

    * Run tesseract --version in a new command prompt
        It should print tesseract 4.0.0-beta.1

    * Create tessdata folder in 'C:\tesseract\Win64\bin\Release'
        * Download [traineddata](https://github.com/tesseract-ocr/tessdata/blob/master/eng.traineddata) to **C:\tesseract\Win64\bin\Release\tessdata**
        * Download [traineddata](https://github.com/tesseract-ocr/tessdata/blob/master/osd.traineddata) to **C:\tesseract\Win64\bin\Release\tessdata**

    * Create new configs folder in **C:\tesseract\Win64\bin\Release\tessdata**
        * Copy [hocr](../hocr) file in **C:\tesseract\Win64\bin\Release\tessdata\configs**
        * Copy [tsv](../tsv) file in **C:\tesseract\Win64\bin\Release\tessdata\configs**