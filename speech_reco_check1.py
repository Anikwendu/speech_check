import streamlit as st
import speech_recognition as sr
import pickle

def transcribe_speech(api):
    r = sr.Recognizer()
    r.pause_threshold = 0.6

    if api == 'Google':
        recognizer_func = r.recognize_google
    elif api == 'Bing':
        recognizer_func = r.recognize_sphinx
    elif api == 'Amazon':
        recognizer_func = r.recognize_amazon
    elif api == "Watson":
        recognizer_func = r.recognize_ibm
    elif api == "DeepSpeech":
        recognizer_func = r.recognize_ds
    else:
        return "Invalid API selected."

        # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Speak now...")
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            # Use the selected API for recognition
            text = recognizer_func(audio_text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not get that.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

def save_text(obj):
    with open('audio_text.pickle', 'wb') as file:
        pickle.dump(obj, file)

    with sr.Microphone() as source:
        print("Please speak in the language you selected...")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio,
                                  language="es-ES")  # replace "es-ES" with the language code of the selected language
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def language(language):
    r = sr.Recognizer()
    language_choice = language
    if language_choice == 'English':
        language_func = r.recognize_google
    if language_choice == 'Hausa':
        language_func = r.recognize_google
    if language_choice == 'Yoruba':
        language_func = r.recognize_google
    if language_choice == 'Igbo':
        language_func = r.recognize_google
    else:
        return 'Language not recognized'

    with sr.Microphone() as source:
        st.info("Speak now...")
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            text = language_func(audio_text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not get that.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format)

def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    api_options = ['Google', 'Bing', 'Amazon', 'Watson', 'Deepspeech']
    selected_api = st.selectbox("Select API:", api_options)
    lang_choice = ['English', 'Hausa', 'Yoruba', 'Igbo']
    selected_language = st.selectbox('Select language:', lang_choice)

    # add a button to trigger speech recognition
    if st.button("Start Recording"):
        text = transcribe_speech(selected_api)
        languages = language(selected_language)
        st.write("Transcription:", text, languages)



if __name__ == "__main__":
    main()