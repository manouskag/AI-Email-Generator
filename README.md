🎯 Objectives
To Demonstrate CrewAI Agent Collaboration

🏗️ System Architecture
                     USER
                       │
                       ▼
              ┌─────────────────┐
              │    Streamlit    │
              │   Web Interface │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Email Generator │
              └────────┬────────┘
                       │
                       ▼
                ┌─────────────┐
                │   CrewAI    │
                │     Crew    │
                └──────┬──────┘
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
     Strategist      Writer      Reviewer
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
               Google Gemini
                       │
                       ▼
                Final Email
                       │
                       ▼
                     USER


📂 Project Structure
AI Email Generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── src/
│   ├── email_crew.py
│   ├── email_generator.py
│   └── prompts.py
│
└── venv/


--> app.py

The main Streamlit application.

It provides:

Email settings
User input fields
Generate Email button
Generated email display
Download functionality


--> email_crew.py

Contains:

Gemini configuration
CrewAI agents
CrewAI tasks
Crew definition
Sequential processing


--> email_generator.py

Acts as the connection between the Streamlit interface and the CrewAI system.


--> prompts.py

Contains predefined options such as:

Email types
Tones
Formality levels
Recipient types
Email lengths
Languages

1. Create Virtual Environment


2. Install Dependencies

Install the required packages:

pip install -r requirements.txt

The Gemini provider integration is included through:

crewai[google-genai]


3. Google Gemini API Configuration

The application uses Google Gemini as the LLM.

Create a Gemini API key using Google AI Studio.

Create a .env file in the project root:

AI Email Generator/
├── .env
├── app.py
└── src/

Add:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY

Replace YOUR_GEMINI_API_KEY with your actual API key.
