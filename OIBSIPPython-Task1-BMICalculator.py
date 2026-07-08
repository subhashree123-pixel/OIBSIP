#!/usr/bin/env python3

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Return BMI given weight (kg) and height (m)."""
    if height_m <= 0:
        raise ValueError("Height must be greater than 0.")
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than 0.")
    return weight_kg / (height_m ** 2)

def classify_bmi(bmi: float) -> str:
    """Classify BMI into standard categories."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def read_positive_float(prompt: str) -> float:
    """Read a positive float from user input with validation."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value <= 0:
                print("Please enter a positive number greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g., 70 or 1.75).")

def main():
    print("BMI Calculator")
    print("==============")
    weight = read_positive_float("Enter your weight (kg): ")
    height = read_positive_float("Enter your height (m): ")

    try:
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError as e:
        # This is a safety net; normal paths should be validated already.
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
