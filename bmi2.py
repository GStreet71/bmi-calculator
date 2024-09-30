def get_valid_height():
  while True:
      height_str = input("Enter your height in m: ")
      try:
          height = float(height_str)
          if height <= 0:
              print("Height must be a positive number.")
          else:
              return height
      except ValueError:
          print("Please enter a valid height in m.")

def get_valid_weight():
  while True:
      weight = input("Enter your weight in kg: ")
      try:
          weight = float(weight)
          if weight <= 0:
              print("Weight must be a positive number.")
          else:
              return weight
      except ValueError:
          print("Please enter a valid weight in kg.")

# Addition from Pt.1
# -----------------------------------------------------------------
# -----------------------------------------------------------------

def get_interpretation(bmi):
    if bmi <= 18:
        print(f"Your BMI is {bmi}, you are underweight.\n")
    elif bmi > 18 and bmi <= 25:
        print(f"Your BMI is {bmi}, you are normal weight.\n")
    elif bmi > 25 and bmi <= 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.\n")
    elif bmi > 30 and bmi <= 35:
        print(f"Your BMI is {bmi}, you are obese.\n")
    else:
        print(f"Your BMI is {bmi}, you are clinically obese.\n")

# -----------------------------------------------------------------
# -----------------------------------------------------------------

def calcBMI(height, weight):
  bmi = round(weight / (height ** 2))
  get_interpretation(bmi) # Addition from Pt. 1

height = get_valid_height()
weight = get_valid_weight()
calcBMI(height, weight)
