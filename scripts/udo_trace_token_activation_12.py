# Please note that this is NOT a functional code !!!
# If you are interested in original files feel free to contact and tell me reason for usage


import torch, argparse, json
from safetensors.torch import load_file
from transformers import AutoTokenizer, AutoModelForCausalLM

def scan(d, p, l, s):
    with open(p) as f: prm = f.read()
    tok = AutoTokenizer.from_pretrained(d)
    mdl = AutoModelForCausalLM.from_pretrained(d, torch_dtype=torch.float16).eval()
    ipt = tok(prm, return_tensors="pt").to(mdl.device)
    mdl(ipt.input_ids)  # warmup

    r = []
    for i in range(*map(int, l.split("-"))):
        k = f"model.layers.{i}.mlp.down_proj.weight"
        t = load_file(mdl.model.config._name_or_path)[k]
        v = torch.norm(t, dim=0)
        idx = (v > v.mean()).nonzero(as_tuple=True)[0]
        for j in idx:
            r.append({"Tensor": k, "Dim": int(j), "scale": float(s)})
    return r

if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--model", required=True)
    a.add_argument("--prompt", required=True)
    a.add_argument("--out", default="patch.csv")
    a.add_argument("--layers", default="22-31")
    a.add_argument("--scale", default="0.04")
    o = a.parse_args()

    out = scan(o.model, o.prompt, o.layers, o.scale)
    import csv
    with open(o.out, "w") as f:
        w = csv.DictWriter(f, fieldnames=["Tensor", "Dim", "scale"])
        w.writeheader()
        w.writerows(out)
