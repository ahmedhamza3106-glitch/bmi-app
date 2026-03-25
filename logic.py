# logic.py

def calculate_bmi_logic(weight, length):
    """الدالة دي هي المحرك اللي بيحسب وبيرجع النتيجة للواجهة"""
    length_in_m = (length / 100)
    bmi = weight / (length_in_m**2)

    if bmi < 16:
        category = "Severe Thinness"
    elif 16 <= bmi < 17:
        category = "Moderate Thinness"
    elif 17 <= bmi < 18.5:
        category = "mild Thinness"
    elif 18.5 <= bmi < 25:
        category = "Normal Weight - Congrats! 🎉"
    elif 25 <= bmi < 30:
        category = "overwight"
    else:
        category = "Obese"
        
    return bmi, category