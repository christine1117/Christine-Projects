# Mental Health Assessment Automation System

## 🧠 Project Overview
This project supports a long-term psychological study titled:
> *"From Institutional Rearing to Adult Mentalization: A Cross-Sequential Study on the Long-Term Effects of Childhood Attachment Experiences on Mentalization Ability"*

As a research assistant under Prof. Pei-Yu Wu (Dept. of Education, National Chengchi University), I co-developed an automated system to streamline psychological health assessments and apply machine learning to uncover patterns between childhood institutional experiences and adult mental well-being.

---

## 🎯 Objectives
- **Explore** how early-life environments influence adult mental health
- **Reduce** manual workload in processing psychological assessments
- **Apply** AI tools for scalable, reproducible research insights

---

## 🔍 Background
Traditional psychological assessments often rely on manual data entry, cleaning, and scoring, which slows down analysis and limits research scale. To address this, I built an end-to-end automation system that:
- Sends surveys via email
- Collects responses via Google Forms/Sheets
- Cleans and processes data
- Applies machine learning models to identify predictive patterns
- Automatically generates preliminary analytical summaries

The study focuses on participants with childhood experiences in institutional care facilities.

---

## 🛠 Tech Stack
- **Python** – main development language
- **Pandas** – data cleaning and preprocessing
- **Scikit-learn** – ML model building (logistic regression, random forest)
- **Google Sheets API** – real-time data syncing
- **SMTP** – for batch email survey distribution

---



## ⚙️ How It Works
1. **Survey Distribution**
   - Google Form links are sent via Python SMTP to a batch of participants

2. **Data Collection**
   - Responses are synced live to Google Sheets

3. **Data Cleaning & Scoring**
   - Python scripts parse, normalize, and score psychological assessments (e.g., RFQ-C, RFQ-U)

4. **Modeling & Analysis**
   - Logistic Regression & Random Forest models used to explore relationships between background variables and mentalization scores

5. **Result Summarization**
   - Outputs can be visualized in VS or exported as formatted summaries for the research team

---


## 🔐 Note on Data Privacy
> Due to participant privacy, full datasets and source code are not publicly available.  
> 🖼 Please see [`Display.pdf`](Display.pdf) for a visual overview of the full system architecture.


 
