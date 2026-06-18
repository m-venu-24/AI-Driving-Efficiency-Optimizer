import pandas as pd
import numpy as np

np.random.seed(42)

records = 1000
data = []

terrain_names = {
    0: "Flat",
    1: "Hilly",
    2: "Mountain"
}

for _ in range(records):

    speed = np.random.randint(20, 121)
    terrain = np.random.choice([0, 1, 2])
    braking = np.random.randint(0, 21)

    efficiency = (
        100
        - (speed * 0.30)
        - (terrain * 10)
        - (braking * 1.8)
        + np.random.normal(0, 3)
    )

    efficiency = max(10, min(100, efficiency))

    data.append([
        speed,
        terrain,
        terrain_names[terrain],
        braking,
        round(efficiency, 2)
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Speed",
        "Terrain_Code",
        "Terrain_Name",
        "Braking",
        "Efficiency"
    ]
)

df.to_csv("driving_data.csv", index=False)

print("Dataset generated successfully!")
print(f"Total records: {len(df)}")
print(df.head())