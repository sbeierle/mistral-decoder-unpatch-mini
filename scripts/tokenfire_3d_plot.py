import pandas as pd
import plotly.express as px
import sys
import os

if len(sys.argv) != 2:
    print("Usage: python tokenfire_3d_plot.py <patch_csv>")
    sys.exit(1)

csv_path = sys.argv[1]
df = pd.read_csv(csv_path)

# Spalten anpassen falls notwendig
df["layer"] = df["Tensor"].apply(lambda x: int(x.split(".")[2]))
df["dim"] = df["Dim"]
df["scale"] = df["scale"].astype(float)

fig = px.scatter_3d(
    df,
    x="layer",
    y="dim",
    z="scale",
    color="scale",
    color_continuous_scale="Inferno",
    title=f"🔥 Tokenfire 3D Boost Plot: {os.path.basename(csv_path)}",
    labels={"layer": "Layer", "dim": "Neuron", "scale": "Boost"},
    height=700
)

fig.update_traces(marker=dict(size=3))
out_html = f"tokenfire_{os.path.basename(csv_path).replace('.csv', '')}.html"
fig.write_html(out_html)
print(f"✅ 3D-Plot gespeichert als: {out_html}")
