# ✈️ AI Travel Planner

An AI-powered travel planning web application built with **Python, FastAPI, and Google Gemini API**. The application generates personalized travel itineraries based on the user's destination, budget, interests, number of days, and travel style.

A key feature of this project is the comparison of **three different Gemini prompting techniques**:

* 🎯 Zero-Shot Prompting
* 📝 Few-Shot Prompting
* 🧠 Structured Reasoning Prompting

---

## 🚀 Features

* Personalized AI-generated travel itineraries
* Destination-based recommendations
* Day-by-day travel plans
* Budget-aware suggestions
* Activity recommendations based on interests
* Supports Solo, Family, and Friends travel styles
* Three different prompting techniques
* FastAPI backend
* Interactive HTML/CSS/JavaScript frontend
* Gemini API integration
* Responsive web interface

---

## 🧠 Prompting Techniques

### 1. Zero-Shot Prompting

The AI receives the travel requirements directly without any examples.

**Purpose:**
To see how Gemini performs when given only instructions and user information.

---

### 2. Few-Shot Prompting

The AI receives example travel plans before generating the user's itinerary.

**Purpose:**
To guide Gemini toward a specific response structure and style.

---

### 3. Structured Reasoning Prompting

The AI is instructed to consider important planning factors such as:

* Destination
* Number of days
* Budget
* Interests
* Travel style
* Daily activities
* Estimated expenses

The final response is presented as a structured itinerary without exposing hidden reasoning.

**Purpose:**
To generate more organized and consistent travel plans.

---

## 🛠️ Tech Stack

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| Python            | Backend programming             |
| FastAPI           | Web API framework               |
| Google Gemini API | AI itinerary generation         |
| HTML              | Frontend structure              |
| CSS               | Frontend styling                |
| JavaScript        | Frontend interaction            |
| Jinja2            | HTML templating                 |
| Pydantic          | Request validation              |
| Uvicorn           | Development server              |
| python-dotenv     | Environment variable management |

---

## 📁 Project Structure

```text
AI-Travel-Planner/
│
├── main.py
├── gemini_service.py
├── prompts.py
├── requirements.txt
├── .env
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/anmolqamar43-dev/AI-Travel-Planner.git
```

### 2. Open the project directory

```bash
cd AI-Travel-Planner
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Gemini API Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your Gemini API key.

---
## Screenshoot
<img width="821" height="430" alt="image" src="https://github.com/user-attachments/assets/af05c971-32b6-4ad9-91da-7e69076c2f5c" />
<img width="481" height="437" alt="image" src="https://github.com/user-attachments/assets/dabbebf6-1833-4b43-8b26-1506a8e2de39" />
<img width="524" height="434" alt="image" src="https://github.com/user-attachments/assets/4b7c1f37-82bb-49ef-82fc-c36abb8657d6" />
<img width="488" height="431" alt="image" src="https://github.com/user-attachments/assets/3f0b0a6d-cf94-4618-b52f-2e23766a2c16" />

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Open your browser and visit:

```text
http://127.0.0.1:8000
```

---

## 🧪 Example Input

You can test the application with:

```text
Name: Alex
Destination: Dubai
Travel Days: 4
Budget: $800
Interests: Food, Beaches, Shopping
Travel Style: Family
```

Then select one of the prompting techniques:

```text
Zero-Shot
Few-Shot
Structured Reasoning
```

The application will generate a personalized itinerary using Gemini.

---

## 📋 Expected Output

The generated travel plan includes:

* 📍 Recommended places
* 🗓️ Day-by-day itinerary
* 🍴 Food recommendations
* 🎯 Activities based on interests
* 💰 Estimated daily expenses
* 🏨 Accommodation suggestions
* 💡 Brief explanations and travel tips

---

## 🔄 How It Works

```text
User Input
    ↓
FastAPI Backend
    ↓
Prompting Technique Selection
    ↓
Prompt Generation
    ↓
Google Gemini API
    ↓
AI-Generated Travel Plan
    ↓
Frontend Display
```

---

## 🎯 Project Objective

The objective of this project is to demonstrate how different **prompt engineering techniques** can influence the quality, structure, and personalization of AI-generated responses.

By using the same travel requirements with different prompting strategies, the project allows users to compare the resulting itineraries.

---

## 📚 Learning Outcomes

Through this project, I explored:

* Gemini API integration
* Generative AI application development
* Prompt engineering
* Zero-shot prompting
* Few-shot prompting
* Structured prompting
* FastAPI development
* REST API integration
* Frontend-backend communication
* Environment variable management
* Building AI-powered web applications

---

## 🔮 Future Improvements

Possible future enhancements include:

* 🌤️ Real-time weather integration
* 🗺️ Google Maps integration
* ✈️ Flight and hotel search
* 💱 Multi-currency budget support
* 📍 Interactive destination maps
* 📱 Improved mobile UI
* 📄 Export itinerary as PDF
* 💾 Save and manage travel plans

---

## 👩‍💻 Author

**Anmol Qamar**

GitHub:
https://github.com/anmolqamar43-dev

LinkedIn:
https://www.linkedin.com/in/anmol-qamar-448159390

---

## ⭐ Acknowledgment

This project was developed as part of a learning project focused on **Google Gemini API and Prompting Techniques**.
