import sys
import os

# Defining dash, because in windows it is '\' while in linux&mac it is '/'
if os.name == 'nt':
    dash = "\\"
else:
    dash = "/"

# Changing path to another directory to import functions from it
sys.path.append("functions{}".format(dash))
from quiz import main_quiz
from read import main_read

try:
    while True:
        print('''                        ######################################
                        #                                    #
                        #                                    #
                        #            WELCOME TO              #
                        #                                    #
                        #               QUIZ                 #
                        #                                    #
                        #                                    #
                        ######################################
            ''')
        print('''

                            INSTRUCTION ARE AS FOLLOWS:

                                 1. TO START THE QUIZ - start
                                 2. TO CHECK YOUR SCORE - score
                                 3. TO STOP THE QUIZ - exit

            ''')
        while True:
            choice = input('Enter your choice: ').lower()
            if choice == 'start':
                main_quiz()
                break
            elif choice == 'score':
                main_read()
                break
            elif choice == 'exit':
                sys.exit()
            else:
                print("Wrong input! Try again.")
                continue
        continue
except KeyboardInterrupt:
    print("Shutdown requested...exiting")
