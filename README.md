# Material for the OHBM 2023 Educational Course Tutorial "One person’s signal is another person's noise: hands-on tutorial to remove physiological fluctuations from MRI data"

In this repository you can find the data to follow OHBM 2023 Educational Course Tutorial _One person’s signal is another person's noise: hands-on tutorial to remove physiological fluctuations from MRI data_, part of the Educational Course [_Physiologic fMRI signals: friend or foe? How and why to measure, model, and account for physiology_](https://ww6.aievolution.com/hbm2301/index.cfm?do=ev.viewEv&ev=1241) (see also [here](https://physiopy.github.io/ohbm23_tutorials/) for the other tutorials in the same Educational Course)

# Laptop setup

To follow this tutorial, you will need a laptop, requiring a little bit of setup beforehand.

## 0. Prerequisites
You will need a laptop with python installed, as well as _pip_. Python version should be 3.7 or above.
You also need to download the files in this repository, either [zipped in a package](https://github.com/smoia/ohbm2023noisetutorial/archive/refs/heads/master.zip) or by locally cloning the repository.

## 1. Optional - Set up a virtual environment
The best way to ensure the software functioning without changing anything in your system is using a virtual environment.
For that, first install _virtualenv_:

``` shell
pip install -U virtualenv
```
(Note you might need to use _pip3_ instead of _pip_, depending on your OS and setup, to work with python 3)

Then, create and activate the virtual environment - in this case I called it _OHBM2023noise_, but you can use a different name:

``` shell
virtualenv OHBM2023noise
source OHBM2023noise/bin/activate
``` 

Note that the first command above will create a folder where you called it from, and the second command assumes this is the case - if you want you can specify a different path though.

Once you activated the virtual environment, you can proceed with package installation

## 2. Package installation

You will need to install a few python packages. First and foremost, [_wxPython_](). Its installation depends on the OS you are using.
While you can find [detailed instructions here](https://wxpython.org/pages/downloads/), following is the summary.

### Install _wxPython_ on Windows and macOS
``` shell
pip install -U wxPython
```
(Note you might need to use _pip3_ instead of _pip_, depending on your OS and setup, to work with python 3)

### Install _wxPython_ on Linux
Check [this folder](https://extras.wxpython.org/wxPython4/extras/linux/) for the right python package, depending on the version of GTK you are using, as well as your OS, then using the link to the right folder, install _wxPython_ version _4.2.0_, if possible.
In this example, I will assume we're working with GTK3 on Ubuntu 20.04:
``` shell
pip install -U \
    -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-20.04 \
    wxPython==4.2.0
```
(Note you might need to use _pip3_ instead of _pip_, depending on your OS and setup, to work with python 3)

### Install all other packages
You also need to install _peakdet_ and _phys2denoise_. Optionally, you can also install _ipython_, a nice CLI environment to work with python.

The fastest option is to use the _requirements.txt_ file in this repository:
``` shell
pip install -U -r path/to/requirements.txt
```
(Note you might need to use _pip3_ instead of _pip_, depending on your OS and setup, to work with python 3)

Alternatively, you can install directly what you need. Please ensure to install matplotlib version 3.6.3 or below, otherwise you will incur into a deprecation error:
``` shell
pip install -U peakdet phys2denoise matplotlib==3.6.3 ipython
```
(Note you might need to use _pip3_ instead of _pip_, depending on your OS and setup, to work with python 3)

## 3. Check the installation
Within the virtual environment, you can either call _pip_ to list your packages (`pip list` or `pip3 list`), or open ipython and import _peakdet_ and _phys2denoise_
```python
import peakdet
import phys2denoise
```

If you have no issues doing that, you're all good to go!

**Note that peakdet's GUI might not work in GUI-like environments like Jupyter notebooks or Spyder**

## 4. Download files for the tutorial

You can downlaod some files that contain data for the tutorial - we will be using these files during the live tutorial.

You can download the physiological files [here](https://osf.io/download/64b55a9e903ac10028dcc8e5/) and [here](https://osf.io/download/64b55a6c465d140032a3175b/). There is BOLD fMRI data associated to these physiological files to play with, as well as motion paramters ready for denoising, [here](https://files.de-1.osf.io/v1/resources/3txqr/providers/osfstorage/64b5f2c7465d1400cfa31ac3/?zip=).
The results and intermediate steps of the tutorial can be found [here](https://files.de-1.osf.io/v1/resources/3txqr/providers/osfstorage/64b55ab8903ac10028dcc8e9/?zip=).

You can also download the full folder with all files [here](https://files.de-1.osf.io/v1/resources/3txqr/providers/osfstorage/64b55a44903ac10021dcc910/?zip=).

If you have your own data, feel free to _also_ bring it with you! I would suggest to download the tutorial data as well, just in case there is any issue.
