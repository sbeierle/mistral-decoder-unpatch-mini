# 🧠 Environment Notes – Mistral Decoder Patch (RX 7900 XTX)

## English 🇬🇧

This file documents the real hardware and environment setup used throughout the decoder patching showcase (Phases 4–6). It is intended to provide full transparency about the technical context, limitations, and achievements.

![Hardware Setup](https://github.com/sbeierle/mistral-decoder-unpatch-mini/blob/main/config_RX7900.png)

---

### 🧰 Hardware and Platform
- **Machine:** Local gaming/workstation PC
- **GPU:** AMD Radeon RX 7900 XTX (non-enterprise)
- **CPU:** AMD Ryzen architecture
- **OS:** Linux (Ubuntu-based, custom-tuned)
- **RAM:** 96 GB

---

### ⚙️ Python & Library Environment
- PyTorch with ROCm (HIP) backend for AMD GPU acceleration
- Python 3.10+ with isolated `venv`
- Custom inference scripts: deterministic (via `do_sample=False`)
- Torch warnings (e.g., `hipBLASLt`) are expected due to unofficial PyTorch support for AMD

---

### 🔥 Constraints and Solutions
- **No access to enterprise GPUs** (e.g. A100, H100, V100)
- **Long inference times** (25–40 seconds per prompt typical)
- **High VRAM consumption**, resolved via CPU/GPU split execution
- **Some visualizations were batched** or generated asynchronously

This setup proves that advanced decoder patching and neuron path manipulation can be executed on a locally available GPU – without cloud support, without LoRA, and without fine-tuning.

> “You don’t need a datacenter – you just need precision.”

---

## العربية 🇸🇦

يوثق هذا الملف البيئة والأجهزة الحقيقية المستخدمة أثناء عرض التعديلات على المشفر (المراحل 4–6). الهدف هو الشفافية الكاملة حول القيود والإنجازات التقنية.

![إعداد الجهاز](https://github.com/sbeierle/mistral-decoder-unpatch-mini/blob/main/config_RX7900.png)

---

### 🧰 الجهاز والنظام
- **الجهاز:** كمبيوتر مكتبي محلي (مخصص أو معدل)
- **بطاقة الرسوميات:** AMD RX 7900 XTX (ليست بطاقة احترافية)
- **المعالج:** AMD Ryzen
- **النظام:** لينوكس (توزيعة أوبونتو معدلة)
- **الذاكرة العشوائية:** 96 جيجابايت

---

### ⚙️ بيئة بايثون والمكتبات
- PyTorch باستخدام backend خاص بـ ROCm (HIP) لتشغيل GPU
- Python 3.10+ مع بيئة `venv` معزولة
- السكربتات تعتمد `do_sample=False` للحصول على إخراج حتمي
- بعض التحذيرات (`hipBLASLt`) طبيعية بسبب الدعم غير الرسمي لـ PyTorch على AMD

---

### 🔥 القيود والحلول
- **لا توجد بطاقات احترافية** مثل A100 أو V100
- **أوقات استدلال طويلة** (بين 25 و40 ثانية للطلب الواحد)
- **استهلاك كبير للذاكرة** تم حله عبر توزيع المعالجة بين CPU وGPU
- **بعض الرسوم البيانية تم توليدها على دفعات** أو بطريقة غير تزامنية

يثبت هذا العمل أن التعديلات العصبونية والتحكم في مسارات المشفر يمكن تنفيذها على جهاز شخصي بدون سحابة، بدون LoRA، وبدون إعادة تدريب.

> "لست بحاجة إلى مركز بيانات – فقط إلى الدقة والمنهجية."
