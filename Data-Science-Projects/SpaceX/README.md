# IBM Data Science Capstone Project - Falcon 9 First Stage Landing Prediction

## 🚀 Introduction
SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage. Therefore if we can determine if the first stage will land, we can determine the cost of a launch. This information can be used if an alternate company wants to bid against SpaceX for a rocket launch.

## 📌 Project Goal
To build a machine learning model that predicts whether the Falcon 9 first stage will land successfully, based on launch-related features such as payload mass, orbit type, launch site, and booster version. 

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
