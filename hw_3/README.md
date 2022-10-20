# Documentation
This script is only named scary, in fact it will make you smile!

If you are using this script please cite
- doi:10.1111/1000-7
***
# Installation 

The script is written in python version 3.11.0rc2 and is produced on the Ubuntu 22.04.1 LTS operating system. For other operating systems, instructions for installing dependencies may differ. Ultraviolence.py also relies on Python library dependencies:

- aiohttp==3.8.3
- bio==1.4.0
- bs4==0.0.1
- google-api-python-client==2.65.0
- lxml==4.9.1
- opencv-python==4.6.0.66
- pandas==1.4.0

These dependencies will be automatically retrieved and installed when using pip for installation (see below).

### Install Python 3.11.0rc2
Detailed information you may find [here](https://ru.linuxcapable.com/how-to-install-python-3-11-on-ubuntu-20-04/).

Short summary is listed below.
```
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev -y
wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0rc2.tar.xz
tar -xf Python*
cd Python-3.11.0rc2
./configure --enable-optimizations
make
sudo make altinstall
```

### Download

You may get this script on your local machine by running the command  
`git clone git@github.com:mskutel/Python_BI_2022.git`  
You will find this script in hw_3 folder.  
`cd hw_3` 


### Install enviroment

First you have to create and activate new python enviroment for this script.
```
python3.11 -m venv .ultraviolence
source .ultraviolence/bin/activate
```
Next you need install all dependencies. This command will help you with this task. (It should be noted that for the correct execution of the command, you must be in the folder with the script and the requiremenets.txt file.  
`pip install -r requirements.txt`  


### Finish line

Now we are rady to execute this script via  
`python ultraviolence.py`

**Enjoy**



