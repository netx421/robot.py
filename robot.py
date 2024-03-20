import openai
import speech_recognition as sr
import pyttsx3

# Function to record audio from the user
def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Robot: Listening...")
        audio = recognizer.listen(source)
    try:
        voice_data = recognizer.recognize_google(audio).lower()
        print(f"You: {voice_data}")
        return voice_data
    except sr.UnknownValueError:
        print("Robot: Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError as e:
        print(f"Robot: Apologies, there was an error recognizing the speech: {e}")
        return ""

# Function for text-to-speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE!"  # Replace with your actual OpenAI API key

# Initial conversation setup
print("Robot: Initiating system startup sequence.")
print("Robot: Hello there! How can I assist you today?")
conversation = [{"role": "system", "content": "DIRECTIVE_FOR_gpt-3.5-turbo"}]

# Main loop for conversation
while True:
    # Process user input through voice
    voice_data = record_audio()
    message = {"role": "user", "content": voice_data}
    conversation.append(message)
    
    # Get AI response
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)
    ai_response = completion.choices[0].message.content
    print(f"Robot: {ai_response}")
    
    # Speak AI response
    speak(ai_response)
    
    # Prompt for next user input
    print("Robot: Listening...")
