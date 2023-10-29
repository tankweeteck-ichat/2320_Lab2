def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height * height)
    print("BMI = " + f"{bmi:.2f}")

    if bmi>25.0:
        print("Over Weight")
        result = 1
    elif bmi<18.5:
        print("Under Weight")
        result = -1
    else:
        print("Normal Weight")
        result = 0
    return result


outcome = calculate_bmi(weight=67, height=1.65)
print("Outcome = ", outcome)
