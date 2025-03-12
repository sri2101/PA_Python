from weather import fetch_weather
from news import fetch_news
from geminiQna import chat_with_gemini
from clock import display_time, set_alarm
from Filemanager import add_file, delete_file, open_file
from openapps import open_application
from speech_text import speech_to_text
from text_speech import text_to_speech
from text_image import text_to_image

def main():
    
    introduction = "Hello! I am Harley, your Personal Assistant. How can I assist you today?"
    print(f"\n{introduction}\n")
    text_to_speech(introduction)
    while True:
        print("\nPersonal Assistant Menu:")
        print("1. Check Weather")
        print("2. Get Latest News")
        print("3. Ask Gemini AI")
        print("4. Show Current Time")
        print("5. Set Alarm")
        print("6. Manage Files (Add/Delete/Open)")
        print("7. Open Applications")
        print("8. Speech to Text")
        print("9. Text to Speech")
        print("10. Text to Image")
        print("11. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            city = input("Enter city name: ")
            print(fetch_weather(city))
        elif choice == "2":
            for news in fetch_news():
                print(news)
        elif choice == "3":
            query = input("Ask Gemini AI a question: ")
            print(chat_with_gemini(query))
        elif choice == "4":
            print("Current Time:", display_time())
        elif choice == "5":
            alarm_time = input("Enter alarm time (HH:MM format): ")
            set_alarm(alarm_time)
        elif choice == "6":
            file_action = input("Choose action (add/delete/open): ").strip().lower()
            filename = input("Enter filename: ")
            if file_action == "add":
                content = input("Enter file content (optional): ")
                print(add_file(filename, content))
            elif file_action == "delete":
                print(delete_file(filename))
            elif file_action == "open":
                print(open_file(filename))
            else:
                print("Invalid file action.")
        elif choice == "7":
            app_name = input("Enter application name (chrome/notepad/calculator): ").strip().lower()
            print(open_application(app_name))
        elif choice == "8":
            print("You said:", speech_to_text())
        elif choice == "9":
            text = input("Enter text to convert to speech: ")
            text_to_speech(text)
        elif choice == "10":
            text = input("Enter prompt to convert to an image: ")
            text_to_image(text) 
        elif choice == "11":
            print("Exiting assistant...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
