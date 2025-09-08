# Import necessary libraries
import re
import random
import datetime
from textblob import TextBlob

# --- Global variable to remember the last joke told ---
last_joke_told = None

# --- Feature 3: Sentiment Analysis Function ---
def get_sentiment(user_input):
    """
    Analyzes the sentiment of the user's input.
    Returns 'positive', 'negative', or 'neutral'.
    """
    analysis = TextBlob(user_input)
    if analysis.sentiment.polarity > 0.1:
        return 'positive'
    elif analysis.sentiment.polarity < -0.1:
        return 'negative'
    else:
        return 'neutral'

# --- Feature 2: Conversation Logging Function ---
def log_interaction(user_input, bot_response):
    """
    Logs the user input and bot response to a file.
    """
    with open("chat_log.txt", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] You: {user_input}\n")
        log_file.write(f"[{timestamp}] Bot: {bot_response}\n\n")

# --- NEW FEATURE: Timetable Generator Function ---
def generate_timetable():
    """
    Asks the user for tasks and generates a balanced weekly timetable.
    """
    print("Bot: Great! What are the main subjects or tasks you want to include in your timetable? (Please enter them separated by commas, e.g., Math, Science, English, Project Work)")
    user_tasks_input = input("You: ")
    tasks = [task.strip() for task in user_tasks_input.split(',')]

    if not tasks or all(t == '' for t in tasks):
        return "You didn't provide any tasks. Please try again."

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    time_slots = ["9am - 11am", "11am - 1pm", "2pm - 4pm"]
    
    # Add a "Revision" task and a "Break" to make it more realistic
    schedule_pool = tasks + ["Revision", "Break"]
    
    timetable = "Here is a balanced timetable to get you started:\n\n"
    
    for day in days:
        timetable += f"--- {day.upper()} ---\n"
        daily_tasks = random.sample(schedule_pool, len(time_slots))
        for i, slot in enumerate(time_slots):
            timetable += f"  {slot}: {daily_tasks[i]}\n"
        timetable += "\n"
        
    return timetable

# --- Main Response Function ---
def get_response(user_input):
    """
    Analyzes the user's input and returns a response.
    """
    global last_joke_told
    user_words = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    
    # Add the new timetable intent
    rules = {
        'timetable_intent': [r'timetable', r'schedule', r'plan'],
        'hello_intent': [r'hello', r'hi', r'hey'],
        'hours_intent': [r'hours', r'open', r'time'],
        'location_intent': [r'location', r'address'],
        'joke_intent': [r'joke', r'funny', r'laugh'],
        'goodbye_intent': [r'bye', 'goodbye']
    }

    responses = {
        'timetable_intent': generate_timetable, # Link to our new function
        'hello_intent': ["Hello there! How can I assist you?", "Hi! What can I do for you today?"],
        'hours_intent': "We are open from 9 AM to 5 PM, Monday to Friday.",
        'location_intent': "You can find us at 123 AI Street, Tech City.",
        'joke_intent': [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the computer show up at work late? It had a hard drive!",
            "Why do programmers prefer dark mode? Because light attracts bugs!"
        ],
        'goodbye_intent': ["Goodbye! Have a wonderful day.", "Farewell!"],
        'sentiment_positive': "I'm glad you're feeling positive! That's great to hear.",
        'sentiment_negative': "I'm sorry to hear that. I hope things get better soon.",
        'default': "I'm not sure how to help with that. You can ask me to create a timetable, tell a joke, or ask about our hours."
    }

    # 1. Check for a matching intent
    for intent, patterns in rules.items():
        for pattern in patterns:
            if any(re.search(pattern, word) for word in user_words):
                response = responses[intent]
                
                # If the response is a function (like our timetable generator), call it
                if callable(response):
                    return response()
                
                if intent == 'joke_intent':
                    available_jokes = [j for j in responses['joke_intent'] if j != last_joke_told]
                    new_joke = random.choice(available_jokes)
                    last_joke_told = new_joke
                    return new_joke
                
                if isinstance(response, list):
                    return random.choice(response)
                else:
                    return response

    # 2. Check for sentiment if no rule matches
    sentiment = get_sentiment(user_input)
    if sentiment == 'positive':
        return responses['sentiment_positive']
    elif sentiment == 'negative':
        return responses['sentiment_negative']
    
    # 3. Return default response
    return responses['default']

# --- Main loop to run the chatbot ---
if __name__ == "__main__":
    try:
        from textblob import TextBlob
    except ImportError:
        print("TextBlob library not found. Please run:")
        print("pip install textblob && python -m textblob.download_corpora")
        exit()

    print("Bot: Hello! I'm an enhanced chatbot. I can create a timetable for you, tell a joke, or answer questions. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['bye', 'goodbye', 'farewell']:
            response = get_response(user_input)
            print(f"Bot: {response}")
            log_interaction(user_input, response)
            break
            
        response = get_response(user_input)
        print(f"Bot: {response}")
        
        log_interaction(user_input, response)
