# Mental Health Assessment Automation System

## 🧠 Project Overview
This project supports a long-term psychological study titled:
> *"From Institutional Rearing to Adult Mentalization: A Cross-Sequential Study on the Long-Term Effects of Childhood Attachment Experiences on Mentalization Ability"*

In collaboration with Prof. Pei-Yu Wu (Department of Education, National Chengchi University), I independently designed and developed a full-stack system that automates psychological health assessments for children raised in institutional care.

Built on real-world mental health data from ongoing research, the system generates personalized feedback reports with visualization for participants, aiming to support self-awareness and emotional understanding. It is designed with user autonomy in mind, providing regular updates via email and allowing for future expansion with AI-driven feedback and emotional analysis.

---

## 🎯 Objectives
- **Uncover** how early-life environments influence adult mental health
- **Automate** psychological assessment processes to reduce manual workload and human error
- **Empower** participants to access timely, personalized mental health feedback

---

## 🔍 Background
Psychological assessments often rely on manual scoring and delayed feedback, which can feel impersonal and disempowering for participants.

To address this, I built an end-to-end system that not only automates backend analysis but also prioritizes the participant experience—delivering monthly psychological feedback via email and encouraging self-awareness through data-driven insights.

## 🖥️ Features
| Role              | Key Functionality                                                                 |
|-------------------|-----------------------------------------------------------------------------------|
| 🧒 Participants   | Receive personalized monthly feedback reports via email                          |
| 🧠 Research Use   | 	Collects longitudinal data and supports scalable analysis for future studies    |


---
## 🛠 Tech Stack
- **Python** 
- **Pandas** – data preprocessing & scoring
- **NumPy**  – numerical operations 
- **Matplotlib** – generate visualizations for user reports
- **Google Sheets API** – real-time data sync
- **SMTP** – email delivery (report distribution)

---



## ⚙️ How It Works
1. **Survey Distribution**  
   Participants receive survey links via automated email (Python SMTP)

2. **Real-time Data Collection**  
   Google Form responses are synced to Google Sheets in real time

3. **Data Cleaning & Scoring**  
   Scores are computed for psychological measures (e.g., RFQ-C, RFQ-U, emotional distress index)
   
4. **Emotional Feedback** 
    Besides numerical scores, the system also generates warm, personalized feedback statements based on the user’s current results.
  
5.  **Data Visualization**
    - Heatmap shows the intensity of distress across five key psychological indicators, comparing the current month with past months.
    - Line chart compares the user's monthly distress trend with group averages, helping identify personal deviations or improvements over time

6. **Automated Report Generation**  
   Each participant receives a personalized feedback summary (via email)


---


## 🔐 Note on Data Privacy
> Due to participant privacy, full datasets and source code are not publicly available.  
> 🖼 Please see [`Display.pdf`](Display.pdf) for a visual overview of the ultimate result.


 
