# Merge PDFs

A simple program to merge all PDFs in a directory into one pdf file.

## Prerequisites

- You will need Python installed
    - Make sure Python is in your Enviornment Variables PATH
    - You can install Python [here](https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe)

- You will need Inno Setup to compile the Installer
    - You can install Inno Setup [here](https://jrsoftware.org/download.php/is.exe)


## How to use

- Clone this repository with `git clone https://github.com/mobaphile/MergePDF.git`    
- Change into the Directory you cloned the repository in `cd MergePDF`    
- Install Python dependancies `pip install cx_Freeze fitz`    
- Run `python setup.py build`
    - This builds the merge.py script into an executable located in the build directory    
- Compile Setup.exe with Inno Setup
    - Right click setup.iss and click `Compile`
        - If you do not see Compile in the context menu, make sure you have installed [Inno Setup](https://jrsoftware.org/download.php/is.exe)
    - This builds the installer from the build directory we just made

## Setup
Run Setup.exe to install PDFMerger on any PC

***

#### Add/Remove Registry Entries
- If you need to add or remove the registry entires, you can run the appropriate .reg file in the `Registry Keys` Directory of this Repository