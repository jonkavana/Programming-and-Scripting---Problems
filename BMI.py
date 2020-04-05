# We need to be able to calculate the BMI of an individual
# we need to obtain their height in metres squared
# we also need thier weight in kilograms 

Height = float(input("Please enter your height in Centimetres: "))
Weight = float(input("Please enter your weight in Kilograms: "))

Measurement = ((Height/100)**2)
BMI = round(Weight / Measurement)

print("Your BMI Score is", BMI)