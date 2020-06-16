import string, random
from time import strftime
from tkinter import *
from tkinter.ttk import *

class Alice():


    """ This is a class that creates a bot called Alice """
    def remove_punctuation(self, input_string):

        out_string = ''

        for character in input_string:

            if character not in string.punctuation:
                out_string = out_string + character

        return out_string

    def prepare_text(self, input_string):

        for characters in input_string:
            temp_string = input_string.lower()
            temp_string = self.remove_punctuation(temp_string)
            out_list = temp_string.split()

        return out_list

    def selector(self, input_list, check_list, return_list):

        output = None

        for items in input_list:

            if items in check_list:
                output = random.choice(return_list)
                break

        return output

    def is_in_list(self, list_one, list_two):

        for items in list_one:
            if items in list_two:
                return True

        return False

    def end_chat(self, input_list):

        end = ['bye', 'goodbye', 'quit', 'goodnight']
        for items in end:

            if self.is_in_list(input_list, end):
                return True

            else:
                return False

    def have_a_chat(self):

        ## Lists for inputs and outputs
        input_greetings = ['hello', 'hi', 'hey', 'heyy', 'good morning', 'good afternoon', 'good evening']
        input_thanks = ['thanks', 'thank you', 'ty', 'thx']

        output_thanks = ["You're welcome.", 'No problem.', 'Anytime.']
        output_greetings = ['Welcome. How may I help you today?', 'Hello, how can I help you?',
                            'Good to see you. How can I help?']

        time_request = ['what time is it', 'time', 'tell me the time', 'nanji']
        clock_request = ['clock']

        end_chat = ['bye', 'goodbye', 'quit', 'goodnight']
        random_responses = ['Did you know there are 1 trillion stars in the Andromeda galaxy?', 'mhm', "Let's move on"]

        combined_list = input_greetings + input_thanks + output_thanks + output_greetings + \
                        time_request + clock_request + end_chat

        """Chat status and counter to check whether Alice has been greeted """
        status = True
        greeting_cntr = 0

        """Shows who is talking"""
        while status:

            input_text = input('You : ')
            output_text = None

            """Prepares text entered for dissemination"""
            input_text = self.prepare_text(input_text)

            """If output_text is none, will start the conversation"""
            if not output_text:

                outputs = []

                outputs.append(self.selector(input_text, input_greetings, output_greetings))

                response = list(filter(None, outputs))

                """Checks for a greeting"""
                if not self.is_in_list(input_text, input_greetings) and greeting_cntr == 0:
                    output_text = 'No greeting? How disappointing.'

                elif self.is_in_list(input_text, input_greetings):
                    greeting_cntr +=1

                """Will only talk to you if greeting has been made"""
                if greeting_cntr > 0:

                    if response:
                        output_text = random.choice(response)

                    if self.is_in_list(input_text, input_thanks):
                        output_text = random.choice(output_thanks)

                    if self.is_in_list(input_text, time_request):
                        current_time = strftime('%H:%M:%S %p')
                        output_text = 'The current time is: ' + current_time

                    if self.is_in_list(input_text, clock_request):
                        DigiClock().current_time()

                    if not self.is_in_list(input_text, combined_list):
                        output_text = "I don't understand, please type something else."

                    if output_text == None:
                        output_text = random.choice(random_responses)

                    if self.end_chat(input_text):
                        output_text = 'Until next time.'
                        status = False

            print('Alice:', output_text)

"""Makes a digial clock using tkinter"""
class DigiClock():


    """create a tkinter window"""
    root = Tk()
    root.title('Digital Clock')

    def __init__(self):

        """create the label for displaying the time"""
        self.time_label = Label(self.root, font=('arial black', 40, 'bold'),
                                background='black',
                                foreground='red')  # makes it look more like a digital clock

        """updates label every 1000ms"""
        self.time_label.after(1000, self.current_time)

    """method to get time from PC"""
    def current_time(self):

        display_time = strftime('%H:%M:%S %p') # gets time from system
        self.time_label.config(text=display_time)
        self.time_label.pack(anchor='center')  # anchors time to top right
        self.time_label.after(1000, self.current_time)  # updates time displayed

        self.root.mainloop()

"""Starts the chat"""
Alice().have_a_chat()