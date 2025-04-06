# ☕ 零壹咖啡師 - Coffee Recommender System
**零壹咖啡師** is a full-screen interactive coffee recommendation system, built with **Python**, **Tkinter**, and **Pillow**.  
It allows users to customize their coffee based on personal taste and preferences, then browse beautiful visual recipe cards — just like a virtual barista.

### 🧾 Users can filter by:
- Brew time (製作時間)
- Sweetness level (甜度)
- Caffeine level (咖啡因濃度)
- Milk / Foam / Whipped cream (牛奶 / 奶泡 / 鮮奶油)

All recipes are matched from a custom dataset and presented with full-screen visual cards designed for intuitive navigation.

## 🎬 Demo
[![Watch the demo](https://img.youtube.com/vi/08I_F10XkKg/maxresdefault.jpg)](https://youtu.be/08I_F10XkKg?si=7BYNIbqrBmiiPnoJ)

---

## 💡 Key Features
- **Interactive GUI**: Built using Tkinter, with fullscreen visuals and stylized buttons.
- **Personalized Filtering**: Filters coffee recipes based on user-selected preferences.
- **Recipe Browsing**: Each result includes a dedicated illustrated recipe card.
- **Visual Design**: Integrates Pillow to load and resize recipe images.
- **Sound Effects**: Uses `pygame` for background music and button sound feedback.

---

## ✨ Tech Stack
- **Python**
- **Tkinter** (GUI framework)
- **Pillow** (Image rendering and resizing)
- **Pandas** (Data filtering and recipe logic)
- **Pygame** (Sound effects and background music)

---

## 🚀 How It Works
1. **Start Screen**: Users enter a fullscreen mode and interact with a visual questionnaire.
2. **Filter Logic**: The app filters a dataset (`select.csv`) to find coffees that match the input.
3. **Recommendation List**: Displays results as stylized buttons.
4. **Recipe Display**: Each coffee opens a full image of the recipe with navigation buttons.
5. **No Match Handling**: A fallback page is shown if no match is found.

---

## 😎 My Role
I worked on simplifying and optimizing the original group project by:
- Streamlining image loading and layout using loops
- Rewriting the GUI for better structure and readability


---

## 🔗 Folder Structure
```
.
├── pics/                   # All recipe and UI images
├── audio/                 # Sound effects and background music
├── select.csv             # Dataset for coffee filtering
├── main.py                # Main Python file
├── README.md              # This file
```


