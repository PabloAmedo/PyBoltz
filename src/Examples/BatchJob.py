import sys
import warnings
import time
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
print(sys.path)
from PyBoltz import PyBoltz
import numpy as np

CF4 = 1
He4 = 3
He3 = 4
Ne  = 5
Kr  = 6
Xe  = 7
CH4 = 8
ETHANE = 9
PROPANE = 10
ISOBUTANE = 11
CO2 = 12
H2O = 14
O2 = 15
N2 = 16
H2 = 21
DEUTERIUM = 22
DME = 24

GASES = [np.nan, 'CF4', 'ARGON', 'HELIUM4', 'HELIUM3', 'NEON', 'KRYPTON', 'XENON', 'CH4', 'ETHANE', 'PROPANE'
         , 'ISOBUTANE', 'CO2', np.nan, 'H2O', 'OXYGEN', 'NITROGEN', np.nan, np.nan, np.nan, np.nan
         , 'HYDROGEN', 'DEUTERIUM', np.nan, np.nan, 'DME']

Object = PyBoltz()

import time
t1 =time.time()

Args = sys.argv

efield     = float(Args[1])
OUT        = str(Args[2])
GAS       = int(Args[3])

# Set the number of gases
Object.NumberOfGases =1
# Set the number of collisons 
Object.MaxNumberOfCollisions =15*40000000.0
# Set penning
Object.EnablePenning = 0
# Calculate the electron energy
Object.EnableThermalMotion=0
Object.FinalElectronEnergy = 2.5#0.0
# Set the gas's with there given number
Object.GasIDs=[GAS,0,0,0,0,0]

# Set the gas fractions
Object.GasFractions=[100,0,0,0,0,0]
# Set the tempature
Object.TemperatureCentigrade = float(23)
# Set the pressure
Object.PressureTorr = 750.062
# Set the eletric field
Object.EField = efield
# Set the magnetic field and angle
Object.BFieldMag =0
Object.BFieldAngle =0
Object.ConsoleOutputFlag = 1
Object.WhichAngularModel = 2


Object.Start()

INFO = [
Object.GasFractions[1],
Object.PressureTorr,
Object.EField,
Object.VelocityZ,
Object.VelocityErrorZ,
Object.TransverseDiffusion,
Object.TransverseDiffusionError,
Object.LongitudinalDiffusion, 
Object.LongitudinalDiffusionError,
Object.TransverseDiffusion1,
Object.TransverseDiffusion1Error,
Object.LongitudinalDiffusion1,
Object.LongitudinalDiffusion1Error,
Object.MeanElectronEnergy,
Object.MeanElectronEnergyError]


INFO = np.array(INFO)
np.save(OUT,INFO)


t2 =time.time()

print("************************************************")
print("************************************************")
print("*****         Here are the outputs         *****")
print("************************************************ \n")
print("run time [s]= ",round(t2-t1,3))

for I in range(Object.NumberOfGases):
    if Object.GasIDs[I]<=25:
        print("Percentage of "+GASES[int(Object.GasIDs[I])]+" = "+  str(Object.GasFractions[I]))

print("Tempature [C]         = ", Object.TemperatureCentigrade)
print("Pressure [torr]       = ", Object.PressureTorr)
print("Eletric field [V/cm]  = ", Object.EField)
print("----------------------------------------------------")
print("Drift velocity [mm/mus]              = ", round(Object.VelocityZ,3))
print("----------------------------------------------------")
print("Drift velocity error [%]             = ", round(Object.VelocityErrorZ,3))
print("----------------------------------------------------")
print("Transverse diffusion [cm**2/s]       = ", round(Object.TransverseDiffusion,3))
print("----------------------------------------------------")
print("Transverse diffusion error [%]       = ", round(Object.TransverseDiffusionError,3))
print("----------------------------------------------------")
print("Longitudinal diffusion [cm**2/s]     = ", round(Object.LongitudinalDiffusion,3))
print("----------------------------------------------------")
print("Longitudinal diffusion error [%]     = ", round(Object.LongitudinalDiffusionError,3))
print("----------------------------------------------------")
print("Transverse diffusion [mum/cm**0.5]   = ", round(Object.TransverseDiffusion1,3))
print("----------------------------------------------------")
print("Transverse diffusion error [%]       = ", round(Object.TransverseDiffusion1Error,3))
print("----------------------------------------------------")
print("Longitudinal diffusion [mum/cm**0.5] = ", round(Object.LongitudinalDiffusion1,3))
print("----------------------------------------------------")
print("Longitudinal diffusion error [%]     = ", round(Object.LongitudinalDiffusion1Error,3))
print("----------------------------------------------------")
print("Diffusion X [cm**2/s]       = ", round(Object.DiffusionX,3))
print("----------------------------------------------------")
print("Diffusion X error [%]     = ", round(Object.ErrorDiffusionX,3))
print("----------------------------------------------------")
print("Diffusion Y [cm**2/s]       = ", round(Object.DiffusionY,3))
print("----------------------------------------------------")
print("Diffusion Y error [%]     = ", round(Object.ErrorDiffusionY,3))
print("----------------------------------------------------")
print("Diffusion Z [cm**2/s]       = ", round(Object.DiffusionZ,3))
print("----------------------------------------------------")
print("Diffusion Z error [%]     = ", round(Object.ErrorDiffusionZ,3))
print("----------------------------------------------------")
print("Diffusion YZ [cm**2/s]       = ", round(Object.DiffusionYZ,3))
print("----------------------------------------------------")
print("Diffusion YZ error [%]     = ", round(Object.ErrorDiffusionYZ,3))
print("----------------------------------------------------")
print("Diffusion XY [cm**2/s]       = ", round(Object.DiffusionXY,3))
print("----------------------------------------------------")
print("Diffusion XY error [%]     = ", round(Object.ErrorDiffusionXY,3))
print("----------------------------------------------------")
print("Diffusion XZ [cm**2/s]       = ", round(Object.DiffusionXZ,3))
print("----------------------------------------------------")
print("Diffusion XZ error [%]     = ", round(Object.ErrorDiffusionXZ,3))
print("----------------------------------------------------")
print("Mean electron energy [eV]            = ", round(Object.MeanElectronEnergy,3))
print("----------------------------------------------------")
print("Mean electron energy error [%]       = ", round(Object.MeanElectronEnergyError,3))
print("----------------------------------------------------")
print("Mean Collision Time [PicoSeconds]            = ", round(Object.MeanCollisionTime,3))
print("----------------------------------------------------")
print("************************************************")
print("************************************************")

