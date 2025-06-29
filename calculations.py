
def calculate_co2_savings(action):
    savings = {
        "Reused item": 1.5,
        "Repaired item": 3.0,
        "Upcycled": 2.0,
        "Shared/Rented": 4.0
    }
    return savings.get(action, 0)

def calculate_water_savings(action):
    return 0
