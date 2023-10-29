def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height * height)
    print("BMI = " + f"{bmi:.2f}")

    if bmi>25.0:
        print("Over Weight")
    elif bmi<18.5:
        print("Under Weight")
    else:
        print("Normal Weight")

calculate_bmi(weight=67, height=1.65)
