from pptx import Presentation
from pptx.util import Inches, Pt
prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
def slide(title, bullets, sub=None):
    s = prs.slides.add_slide(BLANK)
    t = s.shapes.add_textbox(Inches(0.6), Inches(0.4), Inches(12), Inches(1))
    t.text_frame.word_wrap = True; t.text_frame.text = title
    t.text_frame.paragraphs[0].font.size = Pt(36); t.text_frame.paragraphs[0].font.bold = True
    y = 1.6
    if sub:
        b = s.shapes.add_textbox(Inches(0.6), Inches(y), Inches(12), Inches(0.7)); b.text_frame.word_wrap=True; b.text_frame.text=sub; b.text_frame.paragraphs[0].font.size=Pt(20); y += 0.9
    for line in bullets:
        b = s.shapes.add_textbox(Inches(0.8), Inches(y), Inches(11.8), Inches(0.8)); b.text_frame.word_wrap=True; b.text_frame.text="•  "+line; b.text_frame.paragraphs[0].font.size=Pt(20); y += 0.85
    return s
slide("HeartRisk", ["Heart Disease Risk Predictor"], "An AI/ML project by Vikranth Reddy — B.Tech CSE (AI & ML), Woxsen University")
slide("The Problem", ["Heart disease is a leading cause of death, yet early risk often goes unnoticed", "Check-ups produce numbers — age, blood pressure, cholesterol — but patients cannot read what they mean together", "A simple, explainable risk score helps people decide when to see a doctor sooner"])
slide("The Solution", ["HeartRisk estimates heart-disease risk (0–100%) from 8 health readings", "Age, sex, resting blood pressure, cholesterol, max heart rate, fasting blood sugar, exercise angina, ST depression", "Interactive demo: change any reading, see the risk instantly — fully in the browser"])
slide("Tech Stack", ["Python + scikit-learn: logistic regression", "Synthetic dataset: 900 patient records (seed 42)", "HTML + CSS + vanilla JavaScript demo", "GitHub + Vercel hosting"])
slide("Architecture", ["Inputs: 8 health features → standardization (train mean / std) → logistic regression → sigmoid → risk probability", "Model exported as model.json; the browser demo reproduces it exactly", "Strongest drivers: ST depression, low max heart rate and high cholesterol"])
slide("Demo", ["Try the presets: typical middle-aged profile, young healthy profile, high-risk profile", "Typical middle-aged profile (55, BP 140, cholesterol 260) → 10.6% risk", "High-risk profile (70, BP 180, cholesterol 380, angina) → 95.5% risk"])
slide("Results", ["5-fold cross-validated accuracy = 75.1%", "AUC = 0.83 (majority-class baseline: 50.3% — about 1.5x better)", "Disease rate in training data: 50.3%", "Strongest drivers match known cardiac risk factors: ST depression, low max heart rate, high cholesterol"])
slide("Future Scope", ["Train on a real clinical dataset with doctor-validated labels", "Add per-feature explanations: which reading raised or lowered this person's risk", "Add lifestyle inputs: smoking, exercise, family history", "Track risk over time: log readings monthly and chart the trend"])
slide("Thank You", ["HeartRisk — know your number, see a doctor sooner."], "Vikranth Reddy · github.com/HVRGAMING2705/heartrisk")
out = "/home/hatch/workspace/goals/daily-ai-ml-project-factory/files/AIML_HeartRisk_2026-10-28.pptx"
prs.save(out); print("saved", out, "slides:", len(prs.slides._sldIdLst))
