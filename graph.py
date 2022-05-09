import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("data.csv")
radius = df["Radius"].tolist()
mass = df["Mass"].tolist()
gravity = df["Gravity"].tolist()

mass.sort()
radius.sort()
gravity.sort()

plt.plot(radius,mass)
plt.xlabel("RADIUS")
plt.ylabel("MASS")
plt.title("RADIUS-MASS GRAPH")
plt.show()
plt.plot(radius,gravity)
plt.xlabel("RADIUS")
plt.ylabel("GRAVITY")
plt.title("RADIUS-GRAVITY GRAPH")
plt.show()