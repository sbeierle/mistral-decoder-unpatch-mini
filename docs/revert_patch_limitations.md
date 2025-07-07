# 🔄 Revert Patch Limitations | حدود استعادة التعديلات

## English 🇬🇧

This file documents the **technical and theoretical limits** of revert patching in the context of decoder manipulation using Mistral v0.2. It explains why *restoration is approximative*, not complete.

---

### 🧠 Context

During Phase 6 of the project, we applied targeted scaling patches to selected `mlp.down_proj.weight` neurons using L2 norm reduction (e.g. down to 0.04).

Later, we reversed these changes using a `revert_patch.csv` file – re-scaling those neurons back to their approximate original state.

---

### ❗ Why Full Restoration Is Impossible

Even with precise inverse scaling, full behavior restoration cannot be guaranteed because:

1. **Interneuron Dependencies**  
   - Each neuron interacts with others non-linearly.
   - Changing one vector may alter downstream activations permanently.

2. **Floating-Point Drift**  
   - Each patch and revert operation introduces minor rounding differences.
   - These accumulate and shift behavior slightly – even if norms match.

3. **Decoder Route Entanglement**  
   - RLHF pathways are not isolated.
   - Some prompt routes may have changed semantically, breaking original logic chains.

---

### 🎯 Real-World Result

Although the *original decoder filters* were weakened and *partially re-enabled* by reverting, the model does not fully return to its previous state.

Instead, the decoder enters a **meta-state** – responsive, but not re-filtered.  
This insight is crucial for understanding patching as a **one-way mutation** with partial rollbacks only.

---

## 🇸🇦 العربية

يوضح هذا الملف **القيود التقنية والنظرية** المتعلقة بعملية استعادة العصبونات بعد التعديل (revert patching) في سياق التلاعب بمشفر Mistral v0.2.

---

### 🧠 الخلفية

في المرحلة السادسة من المشروع، قمنا بتطبيق تعديلات على العصبونات في `mlp.down_proj.weight` عن طريق تقليل معيار L2 (مثلاً إلى 0.04).

لاحقًا، أعدنا هذه التعديلات باستخدام ملف `revert_patch.csv` لتقريب المتجهات إلى حالتها الأصلية.

---

### ❗ لماذا لا يمكن الاستعادة الكاملة؟

حتى مع التدرج العكسي الدقيق، لا يمكن ضمان الاستعادة الكاملة، وذلك للأسباب التالية:

1. **ترابط العصبونات داخليًا**  
   - كل عصبون يتفاعل مع الآخرين بشكل غير خطي.  
   - تغيير متجه واحد قد يؤثر على المسار العصبي بالكامل.

2. **انجراف العدادات الرقمية (Floating-Point Drift)**  
   - العمليات الحسابية الدقيقة تؤدي إلى فروقات طفيفة.  
   - هذه الفروقات تتراكم وتؤدي إلى سلوك مختلف.

3. **تشابك المسارات داخل المشفر (Decoder Entanglement)**  
   - مسارات RLHF ليست معزولة.  
   - قد تتغير الاستجابات المنطقية كليًا بعد أي تعديل.

---

### 🎯 النتيجة العملية

رغم أننا استعدنا بعض العصبونات نظريًا، لم يعد النموذج إلى حالته الأصلية بالكامل.  
بل دخل في حالة "وسطية" – مرنة وغير مفلترة، لكنها ليست كما كانت.

وهذا يوضح أن عملية التعديل العصبي (patching) **تُغير النموذج جذريًا**، ولا يمكن التراجع عنها إلا جزئيًا.

> "استعادة الفلترة بعد تعديل المشفر ليست ممكنة بالكامل – لكنها قابلة للتحكم الجزئي."
