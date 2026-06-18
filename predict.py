import pickle
with open("efficiency_model.pkl", "rb") as file:
    model = pickle.load(file)

print("\n===== AI Driving Efficiency Optimizer =====")

speed = float(input("Enter Speed (km/h): "))
terrain = int(input("Terrain (0=Flat, 1=Hilly, 2=Mountain): "))
braking = int(input("Braking Frequency (0-20): "))

import pandas as pd

input_data = pd.DataFrame({
    "Speed": [speed],
    "Terrain_Code": [terrain],
    "Braking": [braking]
})

efficiency = model.predict(input_data)[0]

print(f"\nPredicted Efficiency Score: {efficiency:.2f}/100")

print("\n===== Driving Recommendations =====")

if speed > 90:
    print("• Reduce speed for better energy efficiency.")

if braking > 10:
    print("• Avoid sudden braking and maintain smooth control.")

if terrain == 2:
    print("• Mountain roads increase energy consumption.")

if speed <= 90 and braking <= 10:
    print("• Good driving habits detected.")

if efficiency >= 75:
    print("• Excellent energy-efficient driving style.")
elif efficiency >= 50:
    print("• Moderate efficiency. Small improvements recommended.")
else:
    print("• Low efficiency. Consider smoother driving patterns.")

print("\nAnalysis Completed Successfully.")