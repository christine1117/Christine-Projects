# Mental Health Assessment Automation System

## 🧠 Project Overview
This project supports a long-term psychological study titled:
> *"From Institutional Rearing to Adult Mentalization: A Cross-Sequential Study on the Long-Term Effects of Childhood Attachment Experiences on Mentalization Ability"*

As a research assistant under Prof. Pei-Yu Wu (Department of Education, National Chengchi University), I independently designed and developed a full-stack system to automate psychological health assessments for children raised in institutional care.

Built using **real-world mental health data** collected from ongoing research, the system delivers personalized reports to participants and enables psychologists to track group trends and high-risk indicators through an interactive dashboard.

---

## 🎯 Objectives
- **Uncover** how early-life environments influence adult mental health
- **Automate** psychological assessment processes to reduce manual workload and human error
- **Empower** psychologists and researchers with interactive dashboards and data visualizations
- **Translate** psychological insights into scalable, reproducible, and human-centered tools

---

## 🔍 Background
Traditional psychological assessments often rely on manual data entry, cleaning, and scoring, which slows down analysis and limits research scale.
To address this, I built an end-to-end automation system that:
- Sends surveys via email
- Collects responses via Google Forms/Sheets
- Cleans and processes data
- Applies machine learning models to identify predictive patterns
- Automatically generates preliminary analytical summaries
- Provides psychologists with an interactive dashboard to monitor risk and trends

## 🖥️ Features
| Role              | Key Functionality                                                                 |
|-------------------|-----------------------------------------------------------------------------------|
| 🧒 Participants    | Receive personalized monthly feedback reports via email                          |
| 🧠 Psychologists   | Use a secure dashboard to track monthly trends and identify high-risk individuals |
| 📊 Researchers     | Analyze longitudinal data with machine learning and interactive visualizations    |

---
## ⚙️ System Architecture

```
[Google Form] ➝ [Google Sheets API] ➝ [Data Processing (Python)] ➝ [Flask Dashboard]
                                                             ⬑
                                                    [Auto Email Generator]
```

---
## 🛠 Tech Stack
- **Python** – core development
- **Pandas** – data preprocessing & scoring
- **Flask** – web app & dashboard backend
- **Jinja2** – HTML template automation
- **Chart.js** – data visualization (trends, risk indicators)
- **Google Sheets API** – real-time data sync
- **SMTP** – email delivery (report distribution)
- **Scikit-learn** – logistic regression & random forest analysis

---



## ⚙️ How It Works
1. **Survey Distribution**  
   Participants receive survey links via automated email (Python SMTP)

2. **Data Collection**  
   Google Form responses are synced to Google Sheets in real time

3. **Data Cleaning & Scoring**  
   Scores are computed for psychological measures (e.g., RFQ-C, RFQ-U, emotional distress index)

4. **Automated Report Generation**  
   Each participant receives a personalized feedback summary (via email)

5. **Dashboard for Psychologists**  
   A web interface (Flask + Chart.js) displays:
   - Monthly participation stats  
   - RFQ-C / RFQ-U averages  
   - High-risk count  
   - Visualized trends across time  

6. **Machine Learning Analysis **  
  

---


## 🔐 Note on Data Privacy
> Due to participant privacy, full datasets and source code are not publicly available.  
> 🖼 Please see [`Display.pdf`](Display.pdf) for a visual overview of the full system architecture.


 
