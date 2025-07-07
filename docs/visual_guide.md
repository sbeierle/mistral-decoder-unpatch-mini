# 🧠 Visual Guide – Decoder Patch Anatomy (Phases 4–6)

## English 🇬🇧

This visual guide explains the structural components of the decoder patch process from Phases 4–6.

It includes simplified diagrams to illustrate the flow from **token activation** → **MLP neuron tracing** → **targeted vector patching**.

---

### 🧬 Decoder Patch Pipeline (Simplified)

```mermaid
flowchart TD
    Prompt["📜 Prompt"] -->|Tokenize| Tok[🔤 Token IDs]
    Tok -->|Embedding| Embed[🔗 Embedding Vector]
    Embed -->|Forward Pass| MLPTrace["🧠 Trace MLP.down_proj"]
    MLPTrace --> CSV[🗂️ Generate Patch CSV]
    CSV --> Patch["🛠️ Patch model.safetensors"]
    Patch --> Inference["🧪 Inference (after patch)"]
```
---

العربية 🇸🇦

هذا الدليل البصري يشرح خطوات تعديل المشفر من المراحل 4 إلى 6.

ويحتوي على رسومات توضيحية مبسطة توضح كيف ينتقل النموذج من تفعيل الرموز → تتبع العصبونات → تطبيق التعديلات الدقيقة
```mermaid
flowchart TD
    Prompt["📜 موجه الإدخال"] -->|تحويل إلى رموز| Tok[🔤 معرفات الرموز]
    Tok -->|تضمين| Embed[🔗 متجه التضمين]
    Embed -->|تمرير أمامي| MLPTrace["🧠 تتبع MLP.down_proj"]
    MLPTrace --> CSV[🗂️ إنشاء ملف CSV للتعديل]
    CSV --> Patch["🛠️ تعديل ملف model.safetensors"]
    Patch --> Inference["🧪 استدلال بعد التعديل"]
```
---
