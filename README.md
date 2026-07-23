# Wilsun AI Voice Assistant 

Wilsun is a lightweight, responsive desktop AI voice assistant built entirely in Python. It features a modern, clean graphical user interface, real-time speech recognition, fast cloud AI processing, and file-less in-memory text-to-speech streaming.

##  Features
- **Modern UI:** Clean split-screen design built using CustomTkinter.
- **Push-to-Talk:** Simple button-triggered active microphone listening.
- **Instant Processing:** Connected to Groq's high-speed cloud AI engine.
- **In-Memory Audio:** Streams voice responses directly through memory buffers, leaving zero temporary files on your hard drive.

##  Tech Stack
- **Language:** Python
- **GUI Engine:** CustomTkinter
- **Speech-to-Text:** SpeechRecognition (Google API)
- **AI Engine:** Groq API (Llama 3.3)
- **Text-to-Speech:** Edge-TTS & Pygame Mixer

##  How to Install & Run

1. Clone this repository to your computer.
2. Install the required Python dependencies:
   ```bash
   pip install customtkinter speechrecognition pygame edge-tts groq
   ```
3. Go to the Groq Website and grab an API Key and use this **EXACT** code below in your terminal:
   ```bash
   setx GROQ_API_KEY "your_actual_copied_key_here"
   ```
4. Run the application:
   ```bash
   python main.py
   ```