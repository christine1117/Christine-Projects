# IBM Data Science Capstone Project - Falcon 9 First Stage Landing Prediction

## 🚀 Introduction
SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage. Therefore if we can determine if the first stage will land, we can determine the cost of a launch. This information can be used if an alternate company wants to bid against SpaceX for a rocket launch.

## 📌 Project Goal
Build a machine learning model to predict **Falcon 9 first stage landing success**, based on features such as:
- Payload mass
- Orbit type
- Launch site
- Booster version

## 🔍 Methodology  
This project follows a complete data science lifecycle, from data collection to model evaluation:

### 🟣 Data Collection  
- [01_Data_Collection_API.ipynb](01_Data_Collection_Api.ipynb)  
  Used SpaceX's API to collect structured launch data  
- [02_Webscraping.ipynb](02_Webscraping.ipynb)  
  Scraped additional launch information from Wikipedia

### 🟠 Data Wrangling  
- [03_Data_Wrangling.ipynb](03_Data_Wrangling.ipynb)  
  Standardized formats, calculated counts per site/orbit, and prepared data for EDA

### 🔵 Exploratory Data Analysis (EDA)  
- [04_SpaceX_EDA_SQL.ipynb](04_SpaceX_EDA_SQL.ipynb)  
  SQL-based queries to summarize patterns  
- [05_EDA_With_Data_Visualization.ipynb](05_EDA_With_Data_Visualization.ipynb)  
  Visual analysis of payload mass, launch success, and orbit types

### 🟢 Geospatial Visualization  
- [06_SpaceX_Interactive_Visual_Analytics_Folium.ipynb](06_SpaceX_Interactive_Visual_Analytics_Folium.ipynb)  
  Built an interactive map of launch sites and payloads using Folium

### 🔴 Modeling & Evaluation  
- [07_Machine_Learning_Prediction.ipynb](07_Machine_Learning_Prediction.ipynb)  
  Trained 4 classification models and evaluated using F1 Score and Accuracy


## 📊 Key Insights
- **Mission success rates increased over time**, especially after 2015 when reusability became a focus.
- Surprisingly, **missions with heavier payloads had higher success rates**, likely due to improved technology and planning in later years.
- **VLEO and ISS orbits** had high success rates and often carried large payloads.
- Most failures occurred during **early missions** or at sites like **CCAFS SLC 40**.
- **F9 Block 5 boosters** carried the largest payloads and showed strong reliability.
- From **2010–2017**, most missions did not attempt booster recovery; the **first successful ground landing** happened in **2015**.

---
📽️ A visual summary of this project is also available as a [Slide Deck](00_Falcon9_Landing_Prediction_SlideDeck.pdf).
> This presentation was designed as a **comprehensive, stakeholder-ready report** —  
> covering the full data science lifecycle, key insights, and model results in a clear, digestible format.  
> It's suitable for both technical and non-technical audiences who want to understand  
> the value and decision-making potential behind the predictive model.
