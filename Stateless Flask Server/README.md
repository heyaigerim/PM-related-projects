 # Chatbot Server with Terminal Interface
 ## INFO 253B: Back-End Web Architecture
 ## UC Berkeley, 2025

## Stateless Flask Server | Command Parsing | APIs & Data Processing

## Overview
This project is a **stateless Flask-based chatbot server** that parses user messages and processes commands in a structured format. It connects with a Terminal-based chat interface (TerminalChat), handling various user inputs and returning formatted responses.

## Why It’s Interesting:
### ✔ Problem-Solving Approach: Demonstrates user interaction handling & structured command processing.
### ✔ Technical Understanding: API-driven chat experience, message parsing, and structured response handling.
### ✔ End-to-End Execution: Covers architecture, API design, and integration with an existing chat interface.

## Why This Project Matters for Product Management:
### ✔ User-Centered Thinking: Builds structured chat interactions based on user intent.
### ✔ API-Driven Workflow: Demonstrates knowledge of backend communication & product APIs.
### ✔ Scalability Considerations: Stateless architecture allows easy deployment & scaling.
### ✔ Data-Driven Decisions: Could extend into AI/NLP-based interactions.

## Key Features
1. Stateless Flask API
- Receives user messages via POST /chat.
- Parses messages based on command structure.
Returns structured JSON responses.
2. Natural Command Processing
- Commands start with / and extract keywords for task execution.
- General messages return a default response.

## Example:
json
Copy
Edit
{
  "chat": "/remind me to submit my application"
}

Response:
json
Copy
Edit
{
  "chat": "remind: me to submit my application"
}

3. Integration with TerminalChat
- Terminal-based chat system (terminal_chatbot.py)
- API-driven real-time interaction

4. Runs on Custom Port (5003)
- Flexible port configuration for deployment.

## Tech Stack
1. Python 
2. Flask (API framework)
3. TerminalChat (Client interface)
4. Git & GitHub (Version control & collaboration)

## Getting Started
### 1️⃣ Clone the Repository
- bash
- Copy
- Edit
### 2️⃣ Set Up the Chat Server
- bash
- Copy
- Edit
- cd terminal-chat/chat_server
- python3 -m venv venv
- source venv/bin/activate
- pip install Flask
### 3️⃣ Run the Flask Server
- bash
- Copy
- Edit
- python server.py

### Expected Output: **Running on http://127.0.0.1:5003/**

### 4️⃣ Run the Chat Client
- In a new terminal window:
bash
Copy
Edit
cd terminal-chat
python3 terminal_chatbot.py http://localhost:5003
TerminalChat will now interact with your Flask API!

### Testing Commands
User Input	Expected Output
/remind me to submit my resume	-->remind: me to submit my resume
/start	-->start:
Hello, how are you?	-->None: Hello, how are you?
/notify user about the deadline	-->notify: user about the deadline


## Future Enhancements
Integrate with LLMs (e.g., GPT-4) for smart response suggestions
Deploy API as a microservice (AWS, GCP, etc.)
Expand to a web-based UI for real-time interaction

## License
This project is open-source and available under the MIT License.