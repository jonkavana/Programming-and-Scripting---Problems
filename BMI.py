# We need to be able to calculate the BMI of an individual
# we need to obtain their height in metres squared
# we also need thier weight in kilograms 

Height = float(input("Please enter your height in Centimetres: "))
Weight = float(input("Please enter your weight in Kilograms: "))

# new variable needs to be created in order to convert the height input into a useable number
Measurement = ((Height/100)**2)
BMI = round(Weight / Measurement, 2)

# Round has been introduced to curb the length of what the output can be.
# Once this has been calculated and formatted, it can be printed to the screen, in the following way.

print("Your BMI Score is", BMI)