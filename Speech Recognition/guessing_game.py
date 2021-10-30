import random
import time
import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
    '''
    this function will return a dictionary object. İn dictionary;
        Success: If our program can reach google speech API this key will
            has True value; otherwise, it will be false.
        Error: If our program throw an error then this key has a value that explain
            the type of the error; otherwise, it will return none.
        Transcription: It's value will be recorded speech's text; otherwise, it
            will be none.
    '''

    # First we need to be sure that recognizer object is an instance of Recognizer class
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("'recognizer' must be 'Recognizer' instance")
    # Second we need to be sure that microphone object is an instance of Microphone class
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("'microphone' must be 'Microphone' instance")

    # we need to adjust the noise every time we speak
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # we should set response object
    response = {
        "success" : True,
        "error" : None,
        "transcription" : None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.WaitTimeoutError:
        response["error"] = "You need to speak within 2 seconds"
    except sr.UnknownValueError:
        response["error"] = "Couldn't understand what you said"
    except sr.RequestError:
        response["error"] = "API is unavailable"
        response["success"] = False

    return  response

if __name__ == "__main__":

    # set the words that need to be guessed, max number of guess, prompt limit
    WORDS = ["Yellow", "Red", "Purple", "Black", "White", "Blue", "Pink"]
    NUM_GUESSES = 3
    PROMPT_LIMIT = 5

    # create recognizer and microphone instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # get a random word from WORDS list
    word = random.choice(WORDS)

    # explain game
    explanation = (
        "I'm thinking of one of these words:\n"
        "{words}\n"
        "You have {n} tries to guess which one. \n"
    ).format(words = ', '.join(WORDS), n=NUM_GUESSES)

    # print explanation and wait 3 secs before starting the game
    print(explanation)
    time.sleep(3)

    # 3 guess trial
    for i in range(NUM_GUESSES):
        for j in range(PROMPT_LIMIT):
            print("Guess {}. Speak!".format(i+1))
            guess = recognize_speech_from_mic(recognizer, microphone)
            # If a transcription returned than break out of the looop
            if guess["transcription"]:
                break
            # If no transcription returned because of API unavailability break
            # out of loop and continue
            if not guess["success"]:
                break
            # If API is reached but no transcription returned then re-prompt
            print("Sorry, I couldn't catch what you said. Please repeat")

        #If there was an error stop the game
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break

        # show the user the transcription
        print("You said: {}".format(guess["transcription"]))

        # determine if the guess is correct
        guess_is_correct = guess["transcription"].lower() == word.lower()

        # determine if there is any attempts
        attempts_remain = i < NUM_GUESSES - 1

        # determine if player has won the game
        if guess_is_correct:
            #if guess is correct stop the game
            print("Congratulations!  You won the game.")
            break
        elif attempts_remain:
            #if the guess is wrong and the player has more attempts
            print("Incorrectç Try again!\n")
        else:
            # if guess is wrong and the player has no more attemps stop game
            print("Sorry, you lose!\nI was thinking of '{}'".format(word))



