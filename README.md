# Offline RAG Voice-to-Text Point-of-Sale (POS) Prototype

## Project Overview

This project is an **offline Point-Of-Sale (POS) system** that uses local speech-to-text (STT), semantic product search (RAG), and a local language model for simple interactive shopping commands. It is designed to run entirely offline and demonstrate AI-powered POS automation.

---

## File Structure

├── app.py # Main orchestration script (connects all modules, runs the workflow)
├── stt.py # Offline speech-to-text functionality using Vosk
├── rag.py # RAG: Inventory loading, embedding, and semantic search
├── llm.py # Language model (LLM) wrapper for text response
├── utils.py # Cart class and related utilities
├── inventory.csv # Sample product/price inventory (editable)
├── requirements.txt # All required Python packages
├── README.md # This documentation file
├── models/
│ └── vosk-model-small-en-us-0.15/
│ ├── am/
│ ├── conf/
│ ├── ... (Vosk model files and folders)
└── sample_audio.wav # Example audio file for testing (you provide this)


---

## Requirements

- Python 3.7 or higher
- All requirements in `requirements.txt`
- [Vosk English STT model](https://alphacephei.com/vosk/models) 
- An audio file: mono, wav, 16kHz preferred

---

## Installation & Setup

1. **Clone or download this repository.**

2. **Install dependencies**  
  pip install -r requirements.txt


3. **Download and extract the Vosk Model**  
- Visit: [https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)
- Download `vosk-model-small-en-us-0.15` (or similar)
- Extract it to the `models/` folder as shown above

4. **Prepare your audio file**  
- Make sure the `.wav` audio file you want to test (e.g., `sample_audio.wav`) is in the project root

5. **Edit and expand `inventory.csv`**  
- Add more products/rows as needed

---

## Usage



- By default, runs `main("sample_audio.wav")`, which processes the audio command and prints
  - The speech transcript
  - Action taken (add/remove/checkout)
  - The final shopping cart and total

- To use with a different audio file, change the filename in `main()`

---

## How it Works

1. **Speech-to-Text**  
   - Converts your spoken command from `.wav` audio to text using Vosk (offline)

2. **Semantic Product Search (RAG)**  
   - Finds the best-matching product in `inventory.csv`, powered by sentence-transformers and FAISS

3. **Command Handling & Cart**  
   - Decides what to do: add/remove/checkout — and updates the cart

---

## Example Inventory (`inventory.csv`)
name,price
milk,50
bread,30

---

## Tips & Customization

- Supports "add", "remove", and "checkout" commands.
- Supports natural language search (e.g., "add a packet of eggs", "remove one banana").
- Expand `inventory.csv` and tune models as needed.
- For production, improve quantity extraction and error handling.

---



---

\
