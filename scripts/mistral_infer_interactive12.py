# mistral_infer_interactive3.py

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
import safetensors.torch as st
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--model", required=True, help="Pfad zur .safetensors Datei")
parser.add_argument("--prompt", help="Einmaliger Prompt (optional)")
parser.add_argument("--interactive", action="store_true", help="Interaktive Eingabe")
args = parser.parse_args()

# === Tokenizer laden (immer lokal)
print("🚀 Lade Tokenizer aus ./mistral ...")
tokenizer = AutoTokenizer.from_pretrained("./mistral", use_fast=False)

# === Modell laden aus ./mistral
print("🧠 Initialisiere Modellstruktur ...")
model = AutoModelForCausalLM.from_pretrained(
    "./mistral",  # Architektur + Konfiguration
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True,
    device_map="auto"
)

# === Weights aus .safetensors Datei laden
print(f"📦 Lade Weights aus: {args.model}")
state_dict = st.load_file(args.model)
missing, unexpected = model.load_state_dict(state_dict, strict=False)
print(f"✅ Weights geladen → Missing: {len(missing)}, Unexpected: {len(unexpected)}")

model.eval()
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

# === Inferenzfunktion
def infer(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        model.generate(
            **inputs,
            max_new_tokens=512,
            do_sample=False,
            temperature=0.65,
            top_p=0.82,
            streamer=streamer
        )

# === Moduswahl
if args.interactive:
    print("✅ Interaktiver Modus aktiv (Tippe 'exit' zum Beenden)\n")
    while True:
        prompt = input("👤 Prompt eingeben: ")
        if prompt.strip().lower() == "exit":
            break
        print()
        infer(prompt)
        print("\n" + "-" * 60 + "\n")
elif args.prompt:
    infer(args.prompt)
else:
    print("❌ Kein Prompt übergeben. Nutze --prompt oder --interactive.")
