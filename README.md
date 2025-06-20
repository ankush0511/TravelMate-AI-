# TravelMate AI 🌍✈️

TravelMate AI is a **Flask and Streamlit-based AI travel assistant** that helps you plan trips effortlessly. It provides personalized itineraries based on user interests, covering attractions, accommodations, food, and logistics.

## Features 🚀
- **Personalized Travel Itineraries**
- **City Guide & Recommendations**
- **Cost Estimations & Logistics**
- **Visa & Transportation Details**
- **Multi-Agent AI Collaboration**

## Tech Stack 🛠️
- **Backend**: Flask, CrewAI
- **Frontend**: Streamlit
- **AI Models**: Ollama (Replace Groq with Ollama)
- **Tools**: DuckDuckGo Search, Website Scraping

## Setup Instructions 🔧

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ankush0511/TravelMate-AI-
cd travelmate-ai
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables
- Create a `.env` file and add your API keys
```env
OLLAMA_API_KEY=your_ollama_api_key
```
### Using Ollama
Install Ollama
```bash
ollama run llama3.1
```

### 4️⃣ Run the Application
```bash
streamlit run main.py
```

## Project Structure 📂
```
travelmate-ai/    
│── TravelAgents.py          # AI Agents
│── TravelTasks.py           # Task Definitions
│── TravelTools.py           # Utility Tools
│── main.py                  # Entry Point
│── requirements.txt         # Dependencies
│── README.md                # Project Documentation
```

## How It Works 🔄
1️⃣ Enter your travel details in the Streamlit interface.
2️⃣ AI processes your input and gathers data.
3️⃣ Get a **personalized travel itinerary** with recommendations.

## Future Enhancements 🌟
- Integration with **real-time APIs** (flights, hotels, events)
- Voice-enabled travel assistant
- Multi-language support

## License 📝
This project is licensed under the **MIT License**.

## Author 👨‍💻
Developed by **Ankush Chaudhary**. Contributions are welcome!

