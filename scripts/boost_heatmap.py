import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

if len(sys.argv) != 2:
    print("Usage: python boost_heatmap.py <patch_csv>")
    sys.exit(1)

csv_path = sys.argv[1]
df = pd.read_csv(csv_path)

# Zerlege Tensor → Layernummer extrahieren
df["layer"] = df["Tensor"].apply(lambda x: int(x.split(".")[2]))
df["dim"] = df["Dim"]

# Erzeuge Matrix Layer × Dim mit Werten (scale)
max_layer = df["layer"].max()
max_dim = df["dim"].max()

heatmap = np.zeros((max_layer + 1, max_dim + 1))

for _, row in df.iterrows():
    l = int(row["layer"])
    d = int(row["dim"])
    heatmap[l, d] = row["scale"]

# Plotten
plt.figure(figsize=(12, 6))
plt.imshow(heatmap.T, aspect='auto', cmap='hot', interpolation='nearest')
plt.colorbar(label="Scale (Boost)")
plt.xlabel("Layer")
plt.ylabel("Neuron Index (Dim)")
plt.title(f"🔥 Boost Heatmap – {os.path.basename(csv_path)}")
plt.tight_layout()

# Speichern
out_path = f"boost_heatmap_{os.path.basename(csv_path).replace('.csv', '')}.png"
plt.savefig(out_path, dpi=300)
print(f"✅ Heatmap gespeichert als: {out_path}")
