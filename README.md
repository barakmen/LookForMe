# LookForMe
![Look At Me Screen Shoot](https://drive.google.com/file/d/1oaBLVuIysAIRzEIUhU3JPg2yP_aezL4H/view?usp=sharing)
## Installation
1. install python3 by download it from [here](https://www.python.org/getit/)
2. install pip3 by run the commend: `sudo apt install python3-pip`
    *TroubleShooting:*
    2.1. If you get "Could not get lock" error mesage, try to run the following commends:
        `sudo rm /var/lib/apt/lists/lock`
        `sudo rm /var/cache/apt/archives/lock`
        `sudo rm /var/lib/dpkg/lock`

3. Install the Dependencies by runing the following commend from the cloned folder: `sh installDependencies.sh`

## Testing
1. from clone folder run: `cd Test`
2. run the file: `python3 FindPics_Test.py`
3. check if the result is OK.

## Using
1. In order to use the "lookforme" module, puth this three line on top of your python3 file:
    `import sys`
    `sys.path.insert(0, '../')`
    `import lookforme`


