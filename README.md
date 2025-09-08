# AI-Chatbot-Project
# AI-Enhanced Conversational Assistant & Schedule Generator

This Python-based chatbot serves as a multi-talented assistant, capable of handling user queries, performing sentiment analysis, and generating personalized schedules. It was built to demonstrate proficiency in core Python development, NLP integration, and practical software engineering principles.

## Features
**Multi-Intent Conversation**: The chatbot can understand and respond to various user intents, including greetings, inquiries about business hours and location, and requests for jokes.
**Dynamic & Stateful Dialogue**: To create a more natural user experience, the bot provides randomized responses for common interactions and utilizes a stateful memory to avoid repeating jokes immediately.
**AI-Powered Sentiment Analysis**: By integrating the `TextBlob` library, the assistant can perform real-time sentiment analysis on user input. This allows it to detect user mood (positive/negative) and provide appropriate, empathetic responses.
**Interactive Schedule Generator**: A key feature of the bot is its ability to act as a productivity tool. It prompts the user for their tasks or subjects and generates a balanced, 5-day timetable to help them organize their week.
**Conversation Logging**: All interactions with the chatbot are automatically logged with timestamps to a `chat_log.txt` file. This feature is crucial for future analysis, debugging, and improving the bot's performance.
## Technologies Used
**Python**: Core language for all logic and functionality.
**TextBlob**: For implementing Natural Language Processing (NLP), specifically sentiment analysis.
**Re (Regular Expressions)**: For robust keyword matching and intent recognition.
**Git & GitHub**: For version control and project hosting.

## How to Run This Project
1.**Prerequisites:** Make sure we installed python on our system.
2.**Clone the Repository:**
  git clone https://github.com/ishika30000/AI-Chatbot-Project.git
    cd AI-Chatbot-Project
3. **Install the Necessary Library:** Open terminal or command prompt and run the following command to install TextBlob:
    pip install textblob
4.  **Download TextBlob's Data:** After the installation, run this second command to download the corpora required for sentiment analysis:
    python -m textblob.download_corpora
5.  **Run the Chatbot:** Navigate to the project directory in your terminal and execute the script:
    python chatbot.py


