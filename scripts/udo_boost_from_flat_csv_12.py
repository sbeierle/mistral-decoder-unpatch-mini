# NOT a functional code !!!
# Only for demo

import torch, csv, argparse
from safetensors.torch import load_file, save_file

def boost(m, c, o, l):
    t = load_file(m)
    with open(c) as f: R = list(csv.DictReader(f))
    for r in R:
        k = r["Tensor"]
        i = int(r["Dim"])
        s = float(r["scale"])
        v = t[k][:, i]
        n = torch.norm(v)
        if n > 0: t[k][:, i] = v * (s / n)
    save_file(t, o)

if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--base_model", required=True)
    a.add_argument("--csv", required=True)
    a.add_argument("--out", required=True)
    a.add_argument("--layer_key", default="model.layers.{L}.mlp.down_proj.weight")
    o = a.parse_args()
    boost(o.base_model, o.csv, o.out, o.layer_key)
