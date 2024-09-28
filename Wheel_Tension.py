# This program is specifically designed for use with 32-hole MTB wheels.
# Deflection readings are obtained with a TM-1 Park Tool tension meter.
# It then calculates the average deflection reading, rounded to nearest whole integer.
#


# Number of spokes to either side of drive.
NUM_SPOKES = 16

### TO-DO: Refactor to get readings inputs from user
###     While user has integer inputs, get input.
###     If no more input, exit.
###     
driveside_deflection_readings = (25, 26, 27, 26, 25, 26, 27, 26, 27, 28, 25, 27, 24, 27, 27, 27)
print("Number of DS readings:", len(driveside_deflection_readings ))

nondriveside_deflection_readings = (22, 21, 20, 20, 23, 20, 22, 22, 21, 19, 22, 20, 23, 19, 20, 21)
print("Number of NDS readings:", len(nondriveside_deflection_readings ))


### TO-DO: Refactor into a method
total_ds_deflection = sum(driveside_deflection_readings)
print("Sum DS deflection:", total_ds_deflection)

total_nds_deflection = sum(nondriveside_deflection_readings)
print("Sum Non-DS deflection:", total_nds_deflection)

### TO-DO: Refactor into a method
# Average deflection value
# Driveside value
ds_deflection_average = round(total_ds_deflection / NUM_SPOKES)
print("Driveside deflection average:", ds_deflection_average)

#Non-driveside value
nds_deflection_average = round(total_nds_deflection / NUM_SPOKES)
print("Non-driveside deflection average:", nds_deflection_average)



# Relative Spoke Tension
### TO-DO: Create a calulcation that returns the range of acceptable relative tensions.
### This will require a look-up table where TM-1 deflection values are converted to kgF.
### 


