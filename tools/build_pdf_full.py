# -*- coding: utf-8 -*-
from weasyprint import HTML

# ================= SCALES =================
FREQ = ["دائماً", "أحياناً", "نادراً"]
APPLY = ["تنطبق تماماً", "تنطبق جزئياً", "لا تنطبق"]
AGREE = ["موافق", "محايد", "غير موافق"]

# ================= PART 1 (AI topics) =================
topic1_items = [
    "أفكّر في مدى شرعية وأمانة استخدام النصوص المولّدة بالذكاء الاصطناعي في أبحاثي قبل تقديمها.",
    "أتحقّق ممّا إذا كانت تطبيقات الذكاء الاصطناعي تنتهك خصوصية البيانات الشخصية للآخرين.",
    "أحرص على الإشارة بوضوح إلى اعتمادي على أدوات الذكاء الاصطناعي في الأجزاء التي ساعدتني بها.",
    "أتجنّب استخدام مخرجات الذكاء الاصطناعي إذا شعرت أنها تروّج لأفكار متحيّزة أو غير عادلة.",
    "أحلّل الآثار التربوية والنفسية البعيدة المدى لاعتماد زملائي الكلّي على تفكير الآلة الجاهز.",
]
topic2_items = [
    "أستطيع تغيير طريقة تفكيري ودراستي التقليدية بسرعة لتتناسب مع أدوات التعلّم الذكية.",
    "لا أشعر بالإحباط الفكري عندما تُطرح تقنيات ذكاء اصطناعي جديدة تتطلّب مهارات مختلفة.",
    "أتقبّل فكرة أن الذكاء الاصطناعي يمكن أن يشارك في عمليات التحليل النفسي الإحصائي بكفاءة.",
    "أبحث دائماً عن طرق تفكير بديلة لتطوير مهاراتي النفسية بما يتلاءم مع سوق العمل الرقمي.",
    "أستمتع بدمج النظريات النفسية التقليدية مع خوارزميات التفكير الاصطناعي في التطبيقات العملية.",
]
refs1 = [
    "العتيبي، بندر نايف (2025). أخلاقيات الذكاء الاصطناعي في التعليم العالي: رؤية تربوية معاصرة. مجلة التربية والابتكار الرقمي، 4(2)، 112–135.",
    "القحطاني، سارة محمد (2026). التفكير الأخلاقي الرقمي وتطبيقاته لدى طلبة العلوم الإنسانية. دار المناهج للنشر والتوزيع.",
]
refs2 = [
    "الشمري، هدى ضاري (2025). السيكولوجيا الرقمية: المرونة الذهنية وأساليب التفكير الحديثة. المكتبة الأكاديمية.",
    "عبد الرحمن، طارق مدحت (2026). التكيف المعرفي والابتكار في عصر الذكاء الاصطناعي. مجلة الدراسات النفسية والتربوية المعاصرة، 18(3)، 210–239.",
]

# ================= PART 2 (classic options 01-03) =================
options = [
    {"no": "01", "title": "التفكير التأمّلي", "en": "Reflective Thinking",
     "desc": "يركّز هذا النوع على قدرة الطالب على مراجعة طريقة تعلّمه، وتقييم أدائه، وحلّ المشكلات بناءً على الخبرات السابقة.",
     "rows": [("العنوان المقترح", "«مستوى التفكير التأمّلي لدى طلبة الجامعة في ضوء بعض المتغيرات»"),
              ("المتغير المستقل", "التخصص الدراسي (علمي / إنساني) أو الجنس (ذكور / إناث)."),
              ("الأداة (المقياس)", "مقياس التفكير التأمّلي (مثل مقياس «كمبر Kember» المترجَم للعربية)، ويقيس أربعة أبعاد: العمل المعتاد، الفهم، التأمّل، التأمّل النقدي.")],
     "refs": ["عفانة، عزو، والجيش، يوسف (2009). التدريس والتعلم بالذكاءات المتعددة. غزة: آفاق للنشر والتوزيع.",
              "صبري، ماهر، والرافعي، محب (2021). التقويم التربوي: أسسه وإجراءاته. الرياض: مكتبة الرشد."]},
    {"no": "02", "title": "التفكير فوق المعرفي", "en": "Metacognition",
     "desc": "يركّز على وعي الطالب بخطوات تفكيره وقدرته على التخطيط والمراقبة والتقييم الذاتي أثناء الدراسة.",
     "rows": [("العنوان المقترح", "«درجة ممارسة مهارات التفكير فوق المعرفي لدى طلاب المرحلة الثانوية»"),
              ("المتغير المستقل", "المعدّل الدراسي (متفوّقين / عاديين) لمعرفة أثر التحصيل في وعيهم بتفكيرهم."),
              ("الأداة (المقياس)", "مقياس الوعي بالعمليات فوق المعرفية (مثل مقياس «شراو ودِنيسون Schraw & Dennison» المعرَّب)، ويقيس: التخطيط، المراقبة، التقييم، إدارة المعلومات.")],
     "refs": ["جروان، فتحي (2016). تعليم التفكير: مفاهيم وتطبيقات. عمّان: دار الفكر.",
              "عبيد، وليم، وعفانة، عزو (2007). التفكير والمنهاج المدرسي. القاهرة: دار الفكر العربي."]},
    {"no": "03", "title": "التفكير الإيجابي", "en": "Positive Thinking",
     "desc": "يركّز على الجانبين النفسي والتربوي معاً، وكيف ينظر الطالب إلى التحديات الدراسية بنظرة تفاؤلية تدفعه إلى الإنجاز.",
     "rows": [("العنوان المقترح", "«التفكير الإيجابي وعلاقته بالتحصيل الدراسي لدى طلبة المرحلة الثانوية»"),
              ("المتغير المستقل", "مستوى التحصيل الدراسي."),
              ("الأداة (المقياس)", "مقياس التفكير الإيجابي (مثل مقياس عبد الستار إبراهيم، أو مقياس التفكير الإيجابي للشباب المعرَّب)، ويقيس: التفاؤل، الثقة بالنفس، الرضا عن الحياة الدراسية.")],
     "refs": ["إبراهيم، عبد الستار (2012). آفاق جديدة في العلاج المعرفي والتفكير الإيجابي. القاهرة: دار رغد للنشر.",
              "المليجي، رضا (2018). علم النفس التربوي وتطبيقاته الصفية. عمّان: دار الإعصار العلمي."]},
]

# ================= PART 3 (daily habits study) =================
p3_routine = [
    "ألتزم بجدول زمني محدّد ومنظَّم للأنشطة اليومية (دراسة، ترفيه، رياضة).",
    "أتناول وجبات الطعام الأساسية في أوقات ثابتة يومياً.",
    "أخصّص ساعات محدّدة وثابتة للمذاكرة اليومية دون تأجيل.",
]
p3_sleep = [
    "أجد صعوبة في النوم خلال ٣٠ دقيقة من ذهابي إلى الفراش.",
    "أستيقظ في منتصف الليل أو في الصباح الباكر ولا أستطيع العودة للنوم.",
    "أشعر بالخمول والتعب خلال ساعات النهار بانتظام.",
    "ألتزم بموعد ثابت للنوم والاستيقاظ يومياً (حتى في عطلة نهاية الأسبوع).",
]
p3_perf = [
    "أشعر أنّ قدرتي على التركيز واستيعاب المحاضرات مرتفعة.",
    "أحصل على درجات تتوافق مع طموحي في الاختبارات الدورية.",
]
p3_refs_sleep = [
    "الصبحي، منال بنت شداد (2021). اضطرابات النوم وعلاقتها بالتحصيل الدراسي واليقظة الذهنية لدى طالبات الجامعة. مجلة العلوم التربوية والنفسية، جامعة أم القرى.",
    "باوزير، رائد أحمد (2019). جودة النوم وعلاقتها بالاضطرابات النفسية والأداء الأكاديمي لدى طلاب الكليات الطبية. المجلة الطبية السعودية (ملخّص بالعربية).",
]
p3_refs_routine = [
    "العبد الله، خالد محمد (2022). تنظيم الروتين اليومي وعلاقته بالاستقرار النفسي والتحصيل الدراسي لدى طلبة الثانوية. مجلة التربية للبحوث التربوية والنفسية.",
    "الخالدي، مريم (2020). عادات الاستذكار والروتين اليومي وعلاقتها بدافعية الإنجاز لدى طلبة الجامعة. دار وائل للنشر.",
]

# ================= PART 4 (metacognition applied) =================
p4_refs = [
    "جروان، فتحي (2016). تعليم التفكير: مفاهيم وتطبيقات. عمّان: دار الفكر ناشرون وموزعون.",
    "قطامي، يوسف (2013). علم النفس التربوي للمعلّمين. عمّان: دار المسيرة للنشر والتوزيع.",
    "العتوم، عدنان، والجراح، عبد الناصر، وبشارة، موفق (2014). تنمية مهارات التفكير: نماذج نظرية وتطبيقات عملية. عمّان: دار المسيرة.",
    "أبو جادو، صالح، ونوفل، محمد (2017). تعليم التفكير: النظرية والتطبيق. عمّان: دار المسيرة.",
]
p4_axis1 = [
    "أعرف جيداً ما هي نقاط قوّتي ونقاط ضعفي في المذاكرة.",
    "أستطيع تحديد المعلومات المهمّة والتركيز عليها أثناء الشرح.",
    "أميل إلى مراجعة وتذكّر المعلومات السابقة قبل البدء في موضوع جديد.",
    "أعرف متى أستعين بمصادر خارجية (كالإنترنت أو الأصدقاء) لفهم الدرس.",
    "أثق بقدرتي العقلية على استيعاب المواد الدراسية الصعبة.",
]
p4_axis2 = [
    "أضع خطة زمنية محدّدة أو أهدافاً واضحة قبل البدء في الدراسة.",
    "أبحث عن أمثلة من الواقع لمساعدتي في فهم الأفكار المجرّدة.",
    "أقوم بتلخيص المادة وتدوين الملاحظات بأسلوبي الخاص لضمان الفهم.",
    "أسأل نفسي أسئلة حول المادة أثناء المذاكرة لأتأكّد من استيعابي لها.",
    "أتوقّف عن القراءة وأعيد المذاكرة من جديد إذا شعرت بالتشتّت أو عدم الفهم.",
    "أقوم بتحليل أخطائي السابقة في الاختبارات لتجنّب تكرارها مستقبلاً.",
    "أقيّم مدى إنجازي وخطة المذاكرة بعد انتهائي من الاختبارات مباشرة.",
]

# ================= PART 5 (psychological topics 04-07) =================
options2 = [
    {"no": "04", "title": "القلق الأكاديمي", "en": "Academic Anxiety",
     "desc": "يدرس الأثر النفسي لضغط الامتحانات والواجبات في أداء الطلاب.",
     "rows": [("العنوان المقترح", "«مستوى قلق الامتحان لدى طلبة المرحلة الثانوية في ضوء متغير الجنس (ذكور / إناث)»"),
              ("المتغير المستقل", "الجنس (ذكور / إناث)."),
              ("الأداة (المقياس)", "مقياس قلق الامتحان لـ«سبيلبيرجر Spielberger» (تعريب د. أحمد محمد عبد الخالق).")],
     "refs": ["عبد الخالق، أحمد (2000). قلق الامتحان. الإسكندرية: دار المعرفة الجامعية.",
              "دويدار، عبد الفتاح (2018). مقدمة في علم النفس التربوي. بيروت: دار النهضة العربية."]},
    {"no": "05", "title": "الدافعية للإنجاز", "en": "Achievement Motivation",
     "desc": "يدرس القوة الداخلية التي تدفع الطالب للنجاح والتفوّق الأكاديمي وتخطّي العقبات.",
     "rows": [("العنوان المقترح", "«درجة دافعية الإنجاز الأكاديمي لدى طلبة الجامعة وفقاً لمتغير التخصص الدراسي»"),
              ("المتغير المستقل", "التخصص الدراسي (علمي / إنساني)."),
              ("الأداة (المقياس)", "مقياس الدافعية للإنجاز المطوَّر للبيئة العربية (مثل مقياس د. جابر عبد الحميد ود. علاء الدين كفافي).")],
     "refs": ["قطامي، يوسف (2012). سيكولوجية التعلم والتعليم. عمّان: دار المسيرة.",
              "منصور، طلعت (2015). أسس علم النفس التربوي. القاهرة: مكتبة الأنجلو المصرية."]},
    {"no": "06", "title": "التنظيم الذاتي للتعلّم", "en": "Self-Regulated Learning",
     "desc": "يدرس قدرة الطالب على إدارة وقته، وجدولة استذكاره، والاعتماد على نفسه دون توجيه مستمرّ من المعلّم أو الأهل.",
     "rows": [("العنوان المقترح", "«مستوى التعلّم المنظَّم ذاتياً لدى طلاب الكليات التربوية»"),
              ("المتغير المستقل", "المستوى الدراسي (سنة أولى / سنة رابعة) لمعرفة تطوّر المهارة مع الوقت."),
              ("الأداة (المقياس)", "مقياس الاستراتيجيات المُحفِّزة للتعلّم MSLQ لـ«بنتريتش Pintrich» (تعريب د. عماد الزغلول).")],
     "refs": ["الزغلول، عماد (2014). مبادئ علم النفس التربوي. عمّان: دار المسيرة.",
              "أبو غزال، معاوية (2016). نظريات التعلم وتطبيقاتها التربوية. عمّان: دار وائل للنشر."]},
    {"no": "07", "title": "الاحتراق النفسي الأكاديمي", "en": "Academic Burnout",
     "desc": "يدرس حالة الإجهاد العاطفي والجسدي الناتجة عن الضغوط الدراسية المستمرّة وفقدان الشغف بالتعلّم.",
     "rows": [("العنوان المقترح", "«درجة الاحتراق الأكاديمي لدى طلبة الجامعة وعلاقته بمتغير المعدّل الدراسي»"),
              ("المتغير المستقل", "المعدّل الدراسي (مرتفع / منخفض)."),
              ("الأداة (المقياس)", "مقياس «ماسلاش Maslach» للاحتراق النفسي (نسخة الطلاب المعرَّبة بتعريب د. بشير معمرية).")],
     "refs": ["معمرية، بشير (2012). بحوث ودراسات في علم النفس التربوي والنفسي. الجزائر: منشورات الحبر.",
              "الخالدي، أديب (2019). المرجع في الصحة النفسية. عمّان: دار وائل."]},
]


# ================= HELPERS =================
def scale_head(scale):
    return "".join(f"<th class='opt'>{s}</th>" for s in scale)


def questionnaire(items, scale, start=1, head="العبارة"):
    rows = ""
    for i, it in enumerate(items, start):
        cells = "".join("<td class='mark'><span class='circle'></span></td>" for _ in scale)
        rows += f"<tr><td class='num'>{i}</td><td class='stmt'>{it}</td>{cells}</tr>"
    return ("<table class='q'><thead><tr><th class='num'>م</th>"
            f"<th class='stmt'>{head}</th>{scale_head(scale)}</tr></thead>"
            f"<tbody>{rows}</tbody></table>")


def reflist(refs):
    return "<ul class='refs'>" + "".join(f"<li>{r}</li>" for r in refs) + "</ul>"


def subhead(text, axis="", hint=""):
    a = f"<em class='axis'>{axis}</em>" if axis else ""
    h = f"<em class='schint'>{hint}</em>" if hint else ""
    return f"<div class='subhead'><span>{text}</span>{a}{h}</div>"


def sec_head(no, title, en):
    return (f"<div class='sec-head'><span class='sec-no'>{no}</span>"
            f"<div class='sec-titles'><h2>{title}</h2><span class='en'>{en}</span></div></div>")


def brief(desc):
    return (f"<div class='brief'><span class='brief-label'>نبذة عن المتغيّر</span>"
            f"<p>{desc}</p></div>")


def topic_block(no, title, en, desc, axis, items, scale, refs):
    return f"""<section class="topic">{sec_head(no, title, en)}{brief(desc)}
      {subhead('المراجع العربية الحديثة')}{reflist(refs)}
      {subhead('الاستبيان (المقياس)', f'المحور: {axis}', 'مقياس ثلاثي: ' + ' · '.join(scale))}
      {questionnaire(items, scale)}</section>"""


def part_label(text):
    return f"<div class='part-label'><span class='dot'></span> {text}</div>"


def option_card(o):
    rows = "".join(f"<tr><td class='lbl'>{l}</td><td class='val'>{v}</td></tr>" for l, v in o["rows"])
    return f"""<div class="card"><div class="card-head"><span class="card-no">{o['no']}</span>
      <div class="card-titles"><h3>{o['title']}</h3><span class="en">{o['en']}</span></div></div>
      <p class="card-desc">{o['desc']}</p><table class="meta">{rows}</table>
      <div class="card-refs"><span class="rlabel">أبرز المراجع</span>{reflist(o['refs'])}</div></div>"""


# ----- assemble parts -----
part1 = (topic_block("١", "مستوى الوعي بالتفكير الأخلاقي الرقمي", "Digital Ethical Thinking",
                     "يقيس عمليات التفكير والتحليل الذاتي التي يقوم بها الطالب لضمان الاستخدام الأخلاقي والآمن للذكاء الاصطناعي عند استخدام تطبيقاته (مثل تجنّب الانتحال العلمي، والتحيّز، وحماية الخصوصية الرقمية) لدى طلبة الجامعة.",
                     "الأمانة الفكرية والمسؤولية الرقمية", topic1_items, FREQ, refs1)
         + topic_block("٢", "المرونة الذهنية الرقمية", "Digital Mental Flexibility",
                       "متغيّر نفسي يقيس مدى قدرة الطالب على تعديل وتطوير أساليب تفكيره النفسي والمعرفي ليتواكب بسرعة وكفاءة مع التغيّرات المتسارعة التي تفرضها التقنيات الذكية، في مواجهة تحديات الذكاء الاصطناعي لدى طلبة تخصص علم النفس.",
                       "التكيّف الفكري مع التحوّل الذكي", topic2_items, APPLY, refs2))

part2 = "".join(option_card(o) for o in options)

# ----- Part 3 -----
part3 = f"""<section class="topic">{sec_head("٣", "العادات اليومية وأثرها الأكاديمي", "Daily Habits & Academic Performance")}
  <div class="brief"><span class="brief-label">نبذة عن الدراسة</span>
  <p>دراسة تتناول العلاقة بين ثلاثة أبعاد مترابطة لدى طلبة الجامعة: الروتين اليومي وتنظيم الوقت، وجودة النوم، والأداء الأكاديمي.</p></div>
  <div class="note-box"><span class="note-label">ملاحظة منهجية</span>
  <p>يضمّ هذا البحث بصياغته الحالية <strong>ثلاثة متغيرات</strong> (الروتين اليومي، جودة النوم، الأداء الأكاديمي) لا متغيّراً واحداً. ويمكن اعتماده كما هو ببناء استبيانٍ واحدٍ مقسَّمٍ إلى محاور، أو اختزاله إلى متغيّرٍ مستقلٍّ واحد وجعل الباقي متغيّراً تابعاً.</p></div>
  {subhead('المراجع العربية للدراسات السابقة')}
  <div class="ref-group"><h5>حول جودة النوم والأداء الأكاديمي</h5>{reflist(p3_refs_sleep)}</div>
  <div class="ref-group"><h5>حول الروتين اليومي وإدارة الوقت</h5>{reflist(p3_refs_routine)}</div>
  {subhead('الاستبيان · استبيانٌ واحد مقسَّم إلى ثلاثة محاور')}
  {subhead('المحور الأول: الروتين اليومي وتنظيم الوقت', '', 'مقياس ثلاثي: ' + ' · '.join(FREQ))}
  {questionnaire(p3_routine, FREQ)}
  {subhead('المحور الثاني: جودة النوم', 'مقتبس من مقياس بيتسبرغ العالمي PSQI', 'مقياس ثلاثي: ' + ' · '.join(FREQ))}
  {questionnaire(p3_sleep, FREQ)}
  {subhead('المحور الثالث: الأداء الأكاديمي', 'التقييم الذاتي والسجل الدراسي', 'مقياس ثلاثي: ' + ' · '.join(AGREE))}
  {questionnaire(p3_perf, AGREE)}
  <p class="inote">ويمكن قياس الأداء الأكاديمي أيضاً بسؤال الطالب مباشرةً عن معدّله التراكمي الأخير (GPA) ضمن قسم البيانات الديموغرافية.</p>
</section>"""

# ----- Part 4 -----
part4 = f"""<section class="topic">{sec_head("٤", "التفكير فوق المعرفي · نموذج تطبيقي", "Metacognition (Applied)")}
  <div class="proposed"><span class="prop-label">العنوان المقترح</span>
  <p>«مستوى التفكير فوق المعرفي لدى طلبة الجامعة في ضوء متغير التخصص الدراسي».</p>
  <span class="prop-note">ويمكن استبدال «طلبة الجامعة» بـ«طلبة المرحلة الثانوية»، أو «التخصص الدراسي» بـ«الجنس: ذكور / إناث» وفق المتاح.</span></div>
  {subhead('المصادر العربية المعتمدة للتوثيق')}{reflist(p4_refs)}
  {subhead('الاستبيان · مقياس التفكير فوق المعرفي', 'مقتبس ومطوَّر من مقياس «شراو ودِنيسون»')}
  <div class="instructions"><span class="ins-label">تعليمات المقياس</span>
  <p>عزيزي الطالب / عزيزتي الطالبة: يُرجى قراءة العبارات الآتية بدقّة، ووضع علامة (✓) أمام الاختيار الذي ينطبق عليك: <strong>موافق · محايد · غير موافق</strong>.</p></div>
  <div class="demo"><span class="demo-label">الجزء الأول · البيانات الديموغرافية (المتغير المستقل)</span>
  <div class="demo-row"><span class="demo-q">التخصص الدراسي:</span>
  <span class="opt-box"><span class="chk"></span> علمي</span>
  <span class="opt-box"><span class="chk"></span> إنساني</span></div></div>
  {subhead('الجزء الثاني · فقرات المقياس')}
  {subhead('المحور الأول: تنظيم وفهم المعرفة', 'الوعي العقلي', 'مقياس ثلاثي: ' + ' · '.join(AGREE))}
  {questionnaire(p4_axis1, AGREE, start=1)}
  {subhead('المحور الثاني: إدارة وتنظيم السلوك', 'التحكّم والتوجيه', 'مقياس ثلاثي: ' + ' · '.join(AGREE))}
  {questionnaire(p4_axis2, AGREE, start=6)}
</section>"""

# ----- Part 5 -----
part5 = "".join(option_card(o) for o in options2)


# ================= CSS =================
CSS = """
@page {
  size: A4; margin: 16mm 15mm 18mm 15mm;
  @bottom-center { content: "بحوث التخرّج — قسم علم النفس التربوي · كلية التربية للبنات · جامعة الكوفة";
    font-family:'Tajawal'; font-size:7.6pt; color:#9a8f7a; letter-spacing:.2px; }
  @bottom-left { content: counter(page); font-family:'Tajawal'; font-size:8.5pt; color:#13505B; font-weight:700; }
}
@page cover { margin:0; @bottom-center{content:none;} @bottom-left{content:none;} }
* { box-sizing:border-box; }
html { direction:rtl; }
body { font-family:'Amiri',serif; color:#25201a; font-size:12pt; line-height:1.95; margin:0; }
h1,h2,h3,h5 { margin:0; font-weight:700; }

/* COVER */
.cover { page:cover; height:297mm; position:relative; overflow:hidden; background:#0B3A42; color:#fff; }
.cover .band-top { position:absolute; top:0; left:0; right:0; height:118mm; background:linear-gradient(160deg,#13505B 0%,#0B3A42 70%); }
.cover .ornament { position:absolute; top:0; right:0; width:0;height:0; border-top:70mm solid rgba(200,162,75,.14); border-left:70mm solid transparent; }
.cover .ornament2 { position:absolute; top:0; left:0; width:0;height:0; border-top:46mm solid rgba(255,255,255,.05); border-right:46mm solid transparent; }
.cover-inner { position:relative; padding:20mm 22mm; height:100%; display:flex; flex-direction:column; }
.uni { text-align:center; }
.uni .l1 { font-size:17pt; font-weight:700; }
.uni .l2 { font-size:13pt; margin-top:3mm; color:#d8e6e8; }
.uni .l3 { font-size:12pt; color:#c8a24b; font-weight:700; margin-top:1.5mm; }
.rule { width:52mm; height:2px; background:#c8a24b; margin:7mm auto; opacity:.9; }
.emblem { width:34mm; height:34mm; border-radius:50%; margin:4mm auto 0; border:1.6mm solid #c8a24b; display:flex; align-items:center; justify-content:center; background:rgba(255,255,255,.05); }
.emblem span { font-size:30pt; font-weight:700; color:#fff; }
.title-wrap { margin-top:26mm; text-align:center; }
.kicker { font-family:'Tajawal'; font-size:11pt; color:#c8a24b; letter-spacing:3px; font-weight:500; }
.maintitle { font-size:30pt; font-weight:700; line-height:1.5; margin-top:6mm; color:#fff; }
.subtitle { font-size:13.5pt; color:#d8e6e8; margin-top:6mm; line-height:1.8; }
.cover-foot { margin-top:auto; }
.present { background:rgba(255,255,255,.07); border:1px solid rgba(200,162,75,.4); border-radius:3mm; padding:6mm 8mm; text-align:center; }
.present .to { font-family:'Tajawal'; font-size:10.5pt; color:#c8a24b; letter-spacing:1px; }
.present .who { font-size:15pt; font-weight:700; margin-top:2mm; color:#fff; }
.meta-row { display:flex; justify-content:space-between; margin-top:7mm; font-family:'Tajawal'; font-size:9.5pt; color:#bcae93; }

/* PAGE TITLE / TOC */
.page-title { display:flex; align-items:center; gap:5mm; margin:0 0 5mm; }
.page-title .bar { width:7mm; height:13mm; background:#c8a24b; border-radius:2px; }
.page-title h1 { font-size:21pt; color:#0B3A42; }
.page-title .sub { font-family:'Tajawal'; font-size:9.5pt; color:#8a8270; margin-top:1mm; }
.lead { font-size:11.2pt; line-height:1.72; color:#3a342c; text-align:justify; background:#F6F2E9; border-right:3px solid #c8a24b; padding:3.5mm 6mm; border-radius:0 3mm 3mm 0; }
.toc { margin-top:5mm; }
.toc h4 { font-family:'Tajawal'; font-size:10.5pt; color:#13505B; font-weight:700; border-bottom:2px solid #e7dcc2; padding-bottom:1.5mm; margin-bottom:2.5mm; }
.toc ul { list-style:none; margin:0 0 1mm; padding:0; }
.toc li { display:flex; align-items:baseline; gap:3mm; padding:0.7mm 0; font-size:10.8pt; }
.toc .part-label { font-size:10.6pt; padding:2mm 5mm; margin:2.6mm 0 2mm; }
.toc .part-label:first-of-type { margin-top:0; }
.toc .tnum { font-family:'Tajawal'; font-weight:700; color:#c8a24b; font-size:10pt; min-width:9mm; }
.toc .dots { flex:1; border-bottom:1px dotted #cbbfa3; transform:translateY(-3px); }
.toc .ten { font-family:'Tajawal'; font-size:8.2pt; color:#9a8f7a; }

/* PART LABEL */
.part-label { font-family:'Tajawal'; font-weight:700; font-size:12.5pt; color:#fff; background:linear-gradient(90deg,#13505B,#0B3A42); padding:3.5mm 6mm; border-radius:2mm; display:flex; align-items:center; gap:4mm; margin:0 0 7mm; }
.part-label .dot { width:4mm; height:4mm; background:#c8a24b; border-radius:50%; display:inline-block; }

/* TOPIC */
.topic { margin-bottom:9mm; }
.sec-head { display:flex; align-items:center; gap:5mm; margin-bottom:4mm; }
.sec-no { font-size:17pt; font-weight:700; color:#fff; background:#13505B; width:12mm; height:12mm; border-radius:50%; display:flex; align-items:center; justify-content:center; box-shadow:inset 0 0 0 1.4mm #c8a24b; }
.sec-titles h2 { font-size:17.5pt; color:#0B3A42; line-height:1.3; }
.sec-titles .en { font-family:'Tajawal'; font-size:9.5pt; color:#b8902f; letter-spacing:.5px; }
.brief { background:#EEF3F2; border-radius:3mm; padding:4mm 6mm; margin:3mm 0 4mm; border-right:3px solid #13505B; }
.brief-label { font-family:'Tajawal'; font-weight:700; font-size:9.5pt; color:#13505B; display:block; margin-bottom:1mm; }
.brief p { margin:0; font-size:11.6pt; text-align:justify; color:#33302a; }
.subhead { display:flex; align-items:baseline; gap:4mm; margin:5mm 0 3mm; }
.subhead span { font-family:'Tajawal'; font-weight:700; font-size:11pt; color:#13505B; position:relative; padding-right:5mm; }
.subhead span::before { content:""; position:absolute; right:0; top:50%; transform:translateY(-50%); width:3mm; height:3mm; background:#c8a24b; border-radius:50%; }
.subhead .axis { font-family:'Amiri'; font-style:normal; font-size:10.5pt; color:#6a6354; }
.subhead .schint { font-family:'Tajawal'; font-style:normal; font-size:8.3pt; color:#9a8f7a; margin-right:auto; }
ul.refs { list-style:none; margin:0; padding:0; }
ul.refs li { position:relative; padding:2mm 7mm 2mm 0; font-size:11pt; line-height:1.8; color:#34302a; text-align:justify; border-bottom:1px dashed #e7dcc2; }
ul.refs li:last-child { border-bottom:none; }
ul.refs li::before { content:"\\2756"; position:absolute; right:0; top:2mm; color:#c8a24b; font-size:10pt; }

/* QUESTIONNAIRE */
table.q { width:100%; border-collapse:collapse; margin-top:2mm; border:1px solid #cdd9d7; border-radius:2mm; overflow:hidden; }
table.q thead th { background:linear-gradient(90deg,#13505B,#1c6675); color:#fff; font-family:'Tajawal'; font-weight:700; font-size:9.6pt; padding:3mm 2mm; text-align:center; }
table.q th.stmt { text-align:right; padding-right:5mm; }
table.q td { padding:2.6mm 2mm; font-size:11pt; border-top:1px solid #e2e9e8; }
table.q td.num { text-align:center; width:9mm; font-family:'Tajawal'; font-weight:700; color:#13505B; background:#f2f6f5; }
table.q th.num { width:9mm; }
table.q td.stmt { text-align:right; padding-right:5mm; line-height:1.7; color:#2c2822; }
table.q th.opt { width:21mm; }
table.q td.mark { text-align:center; width:21mm; }
table.q tbody tr:nth-child(even) td { background:#f7faf9; }
.circle { display:inline-block; width:4.6mm; height:4.6mm; border:1.3px solid #9bb0ad; border-radius:50%; }

/* CARDS */
.cards-intro { font-size:12pt; color:#3a342c; text-align:justify; margin-bottom:6mm; background:#F6F2E9; border-right:3px solid #c8a24b; padding:4mm 6mm; border-radius:0 3mm 3mm 0; }
.card { border:1px solid #ddd3bd; border-radius:3mm; margin-bottom:6mm; overflow:hidden; break-inside:avoid; }
.card-head { display:flex; align-items:center; gap:4mm; background:#EEF3F2; padding:3.5mm 5mm; border-bottom:1px solid #ddd3bd; }
.card-no { font-family:'Tajawal'; font-weight:700; font-size:13pt; color:#fff; background:#c8a24b; width:10mm; height:10mm; border-radius:2mm; display:flex; align-items:center; justify-content:center; }
.card-titles h3 { font-size:15pt; color:#0B3A42; }
.card-titles .en { font-family:'Tajawal'; font-size:9pt; color:#b8902f; }
.card-desc { margin:4mm 5mm 2mm; font-size:11.3pt; color:#33302a; text-align:justify; }
table.meta { width:calc(100% - 10mm); margin:1mm 5mm 3mm; border-collapse:collapse; }
table.meta td { padding:2.2mm 0; vertical-align:top; border-top:1px dashed #e7dcc2; font-size:11pt; }
table.meta tr:first-child td { border-top:none; }
table.meta td.lbl { font-family:'Tajawal'; font-weight:700; font-size:9.6pt; color:#13505B; width:33mm; padding-left:4mm; }
table.meta td.val { color:#2f2b25; text-align:justify; line-height:1.75; }
.card-refs { background:#faf8f2; padding:3mm 5mm 2mm; border-top:1px solid #eee3cb; }
.card-refs .rlabel { font-family:'Tajawal'; font-weight:700; font-size:9pt; color:#b8902f; }
.card-refs ul.refs li { font-size:10.4pt; padding-top:1.4mm; padding-bottom:1.4mm; }
.note { margin-top:4mm; font-family:'Tajawal'; font-size:8.8pt; color:#8a8270; text-align:center; border-top:1px solid #e7dcc2; padding-top:3mm; }

/* NEW: methodological note, ref-group, proposed, instructions, demo */
.note-box { background:#FBF3E2; border:1px solid #ecd9a8; border-right:4px solid #c8a24b; border-radius:0 3mm 3mm 0; padding:4mm 6mm; margin:0 0 5mm; }
.note-label { font-family:'Tajawal'; font-weight:700; font-size:9.5pt; color:#9a7414; display:block; margin-bottom:1mm; }
.note-box p { margin:0; font-size:11.4pt; text-align:justify; color:#4a3f25; }
.note-box strong { color:#8a5e0c; }
.ref-group { margin-bottom:2mm; }
.ref-group h5 { font-family:'Tajawal'; font-size:9.6pt; color:#1c6675; margin:3mm 0 0; padding-right:5mm; position:relative; }
.ref-group h5::before { content:"\\25C8"; position:absolute; right:0; color:#c8a24b; font-size:8pt; top:1px; }
.inote { font-family:'Tajawal'; font-size:9pt; color:#7a7264; margin:3mm 0 0; padding:2.5mm 5mm; background:#f4f6f5; border-radius:2mm; text-align:justify; }
.proposed { background:linear-gradient(90deg,#EEF3F2,#f7faf9); border:1px solid #cdd9d7; border-right:4px solid #13505B; border-radius:0 3mm 3mm 0; padding:4mm 6mm; margin:0 0 4mm; }
.prop-label { font-family:'Tajawal'; font-weight:700; font-size:9.5pt; color:#13505B; display:block; }
.proposed p { margin:1.5mm 0; font-size:13.5pt; font-weight:700; color:#0B3A42; }
.prop-note { font-family:'Tajawal'; font-size:8.8pt; color:#7a7264; }
.instructions { background:#F6F2E9; border-radius:3mm; padding:3.5mm 6mm; margin:0 0 4mm; }
.ins-label { font-family:'Tajawal'; font-weight:700; font-size:9.5pt; color:#b8902f; display:block; margin-bottom:.5mm; }
.instructions p { margin:0; font-size:11pt; color:#3a342c; text-align:justify; }
.demo { border:1px dashed #b9c8c6; border-radius:3mm; padding:3.5mm 6mm; margin:0 0 4mm; background:#fbfdfc; }
.demo-label { font-family:'Tajawal'; font-weight:700; font-size:9.6pt; color:#13505B; display:block; margin-bottom:2mm; }
.demo-row { display:flex; align-items:center; gap:8mm; font-size:11.5pt; }
.demo-q { color:#2f2b25; }
.opt-box { display:inline-flex; align-items:center; gap:2mm; }
.chk { display:inline-block; width:4.2mm; height:4.2mm; border:1.4px solid #13505B; border-radius:1mm; }
"""

# ================= DOCUMENT =================
HTML_DOC = f"""<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<style>{CSS}</style></head><body>

<div class="cover">
  <div class="band-top"></div><div class="ornament"></div><div class="ornament2"></div>
  <div class="cover-inner">
    <div class="uni"><div class="l1">جامعة الكوفة</div><div class="l2">كلية التربية للبنات</div><div class="l3">قسم علم النفس التربوي</div></div>
    <div class="rule"></div><div class="emblem"><span>ﻧﻔﺲ</span></div>
    <div class="title-wrap">
      <div class="kicker">دليل مقترحات بحوث التخرّج</div>
      <div class="maintitle">مصادر ومتغيرات ومقاييس<br>لبحوث التخرّج</div>
      <div class="subtitle">مقترحاتٌ بحثية في التفكير والذكاء الاصطناعي والمواضيع النفسية<br>مع المراجع الحديثة وأدواتِ القياس الجاهزة</div>
    </div>
    <div class="cover-foot">
      <div class="present"><div class="to">مُقدَّم إلى</div><div class="who">الدكتورة المشرفة على بحوث التخرّج</div></div>
      <div class="meta-row"><span>إعداد طالبات قسم علم النفس التربوي</span><span>العام الدراسي ٢٠٢٥ – ٢٠٢٦</span></div>
    </div>
  </div>
</div>

<div class="page-title"><span class="bar"></span><div><h1>تمهيد ومحتويات الدليل</h1><div class="sub">Overview &amp; Contents</div></div></div>
<p class="lead">يضمّ هذا الدليل مجموعةً منظَّمةً من المقترحات البحثية الصالحة لبحوث التخرّج في تخصص علم النفس التربوي،
موزَّعةً على خمسة محاور تتدرّج من المقترحات الحديثة المرتبطة بالذكاء الاصطناعي، إلى الخيارات التأصيلية في أنواع التفكير،
ثم دراسة العادات اليومية وأثرها الأكاديمي، فنموذجٍ تطبيقيٍّ متكاملٍ للتفكير فوق المعرفي، وأخيراً باقةٍ من المواضيع النفسية بمتغيّرٍ واحد.
وقد رُوعي في كلّ مقترح تحديدُ المتغيّر، ونبذةٍ تعريفية، وأحدثِ المراجع العربية، وأداةِ القياس المناسبة.</p>

<div class="toc"><h4>محتويات الدليل</h4>
  {part_label('المحور الأول · مقترحات قائمة على الذكاء الاصطناعي')}
  <ul>
    <li><span class="tnum">١</span> مستوى الوعي بالتفكير الأخلاقي الرقمي <span class="dots"></span><span class="ten">Digital Ethical Thinking</span></li>
    <li><span class="tnum">٢</span> المرونة الذهنية الرقمية <span class="dots"></span><span class="ten">Digital Mental Flexibility</span></li>
  </ul>
  {part_label('المحور الثاني · خيارات تأصيلية في أنواع التفكير')}
  <ul>
    <li><span class="tnum">٠١</span> التفكير التأمّلي <span class="dots"></span><span class="ten">Reflective Thinking</span></li>
    <li><span class="tnum">٠٢</span> التفكير فوق المعرفي <span class="dots"></span><span class="ten">Metacognition</span></li>
    <li><span class="tnum">٠٣</span> التفكير الإيجابي <span class="dots"></span><span class="ten">Positive Thinking</span></li>
  </ul>
  {part_label('المحور الثالث · العادات اليومية وأثرها الأكاديمي')}
  <ul>
    <li><span class="tnum">٣</span> الروتين وجودة النوم والأداء الأكاديمي <span class="dots"></span><span class="ten">Daily Habits &amp; Performance</span></li>
  </ul>
  {part_label('المحور الرابع · التفكير فوق المعرفي (نموذج تطبيقي)')}
  <ul>
    <li><span class="tnum">٤</span> مقياس التفكير فوق المعرفي المتكامل <span class="dots"></span><span class="ten">Metacognition — Applied</span></li>
  </ul>
  {part_label('المحور الخامس · مواضيع نفسية إضافية بمتغير واحد')}
  <ul>
    <li><span class="tnum">٠٤</span> القلق الأكاديمي <span class="dots"></span><span class="ten">Academic Anxiety</span></li>
    <li><span class="tnum">٠٥</span> الدافعية للإنجاز <span class="dots"></span><span class="ten">Achievement Motivation</span></li>
    <li><span class="tnum">٠٦</span> التنظيم الذاتي للتعلّم <span class="dots"></span><span class="ten">Self-Regulated Learning</span></li>
    <li><span class="tnum">٠٧</span> الاحتراق النفسي الأكاديمي <span class="dots"></span><span class="ten">Academic Burnout</span></li>
  </ul>
</div>

<div style="break-before:page;"></div>
{part_label('المحور الأول · مقترحات قائمة على الذكاء الاصطناعي')}
{part1}

<div style="break-before:page;"></div>
{part_label('المحور الثاني · خيارات تأصيلية في أنواع التفكير')}
<p class="cards-intro">ثلاثة خيارات بحثية راسخة، يصلح كلٌّ منها لبحث تخرّج بمتغيّر مستقلّ واحد. يعرض كلُّ خيار: تعريفه المختصر، والعنوان المقترح، والمتغيّر المستقل، وأداة القياس بأبعادها، وأبرز المراجع العربية المعتمدة.</p>
{part2}

<div style="break-before:page;"></div>
{part_label('المحور الثالث · العادات اليومية وأثرها الأكاديمي')}
{part3}

<div style="break-before:page;"></div>
{part_label('المحور الرابع · التفكير فوق المعرفي (نموذج تطبيقي)')}
{part4}

<div style="break-before:page;"></div>
{part_label('المحور الخامس · مواضيع نفسية إضافية بمتغير مستقل واحد')}
<p class="cards-intro">أربعة مواضيع نفسية إضافية، يصلح كلٌّ منها لبحث تخرّج بمتغيّرٍ مستقلٍّ واحد، ولكلٍّ منها مقياسٌ عربيٌّ معرَّبٌ ومتوفّر. ويتيح هذا التنوّع — مع التفكير فوق المعرفي — اختيار المقترح الأنسب لظروف الباحثة وعيّنتها.</p>
{part5}
<div class="note">انتهى الدليل — أُعِدّ بعنايةٍ ليكون مرجعاً موجزاً وأنيقاً لمناقشة مقترحات بحوث التخرّج.</div>

</body></html>"""

with open("/tmp/research_full.html", "w", encoding="utf-8") as f:
    f.write(HTML_DOC)
HTML(string=HTML_DOC).write_pdf("/tmp/research_full.pdf")
print("PDF written: /tmp/research_full.pdf")
