# PyBoltz
This software package is a translation of the Fortran based Magboltz into Cython. This project was done to allow for more productive work to be done with magboltz.

## General information.
### About Magboltz.
The Magboltz program computes drift gas properties by "numerically integrating the Boltzmann transport equation"-- i.e., simulating an electron bouncing around inside a gas. By tracking how far the virtual electron propagates, the program can compute the drift velocity. By including a magnetic field, the program can also calculate the Lorentz angle. [Read more](http://cyclo.mit.edu/drift/www/aboutMagboltz.html).

### Why Cython?
Cython's static typing improves the speed of python code by about a hundred times. In other words, Cython provides us with the simplicity of python and the speed of Fortran/C. [Read more](https://cython.org/).

## Setting up and running instructions. 
### Setting up.
To be able to run this project you will need python3+, cython, and numpy installed. The setup that we use has python 3.6.7, Cython 0.29.3, and numpy 1.16.1. 

### Gases cross section database.
Before building the code make sure to run the following commands in the Cython directory to get the gases.npy file made, as this file has all the cross section values.
```
$ python3 Setup_npy.py
```
### Building.
To build the code clone this project and run the following command in the Cython directory. This should compile all of the Cython and add the path to your PYTHONPATH so you can access the libraries for anywhere. This will take a few minutes the first time.
```
$ source setup.sh
```
Please note that you might need to change the commands inside the setup.sh file to match your python version.

### Running PyBoltz.
To run the code, you will need to import Magboltz and instantiate an instance of the Magboltz object, fill in the input parameters and calling the Magboltz.Start() function. There are also examples in the Examples directory to how to use PyBoltz.
#### Input parameters.
* **Magboltz.NGAS** - The number of gases in the mixture (goes up to 6).
* **Magboltz.NMAX** - The number of simulated events / 2*10E7.
* **Magboltz.IPEN** - Penning effects included (0 or 1).
* **Magboltz.ITHRM** - Thermal motion included (0 or 1).
* **Magboltz.EFINAL** - Upper limit of electron energy integration (0.0 to automatically calculate this value).
* **Magboltz.NGASN** - Array of six elements that has the number of each gas in the mixture.
* **Magboltz.FRAC** - Array of six elements that has the percentage of each gas in the mixture.
* **Magboltz.TEMPC** - The tempreture in degrees centigrade.
* **Magboltz.TORR** - The pressire \[torr\].
* **Magboltz.EFIELD** - The electric field in the chamber \[Volts/Cm\].
* **Magboltz.BMAG** - The magnitude of the magentic field \[Tesla\].
* **Magboltz.BTHETA** - The angle between the magentic field and the electric field. 
* **Magboltz.NANISO** - This variable is used to fix the angular distrubtions to one of the following types. 
  - Okhrimvoskky Type - Magboltz.NANISO = 2 (default value).
  - Capitelli Longo Type - Magboltz.NANISO = 1.
  - Isotropic Scattering - Magboltz.NANISO = 0.

to compile and setup the enviorment go to the directory 

MAGBOLTZ-py/src/Scripts/Cython

and run 

source setup.sh


Once compiled run the template Test-Magboltz.py

python Test-Magboltz.py


This template includes the gas list and current output paramaters.
