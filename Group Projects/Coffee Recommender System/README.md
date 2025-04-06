# ☕ 零壹咖啡師 - Coffee Recommender System
## 🧾 Project Overview
零壹咖啡師 is a coffee recommender system built with Tkinter in Python.
The app offers a fullscreen, image-driven interface that helps users choose the perfect coffee based on their personal preferences, including:
- Production time 
- Sweetness
- Caffeine level
- Milk / Foam / Whipped cream



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


