def main_quiz():
    import json
    import os
    from operator import itemgetter
    from random import shuffle

    # Prints out questions and options from question sets
    def Def_Question(message, a, b, c, d, correct):
        # Prints question
        print('\n> ' + message)

        # Prints possible answers
        print('\na: {} \nb: {} \nc: {} \nd: {}'.format(a, b, c, d))

        # Checks if the answer is correct, and then gives points accordingly
        response = input('Enter your answer: ')
        return response== correct

    print(''' 
    			       LET'S BEGIN

    			WE HAVE TWO CATEGORY OF QUIZ
			1. MATHS
			2. SPORTS

    			SELECT THE SUITABLE OPTION


    	''')
    category = input('Choose category [maths/sports]: ').lower()
    questionsets=[]
    ques_math=[]
    questiondict_maths=[]
    ques_sports=[]
    questiondict_sports=[]
    # Chooses which language to initialize
    while True:
        with open(os.path.join('question_sets', 'quiz.json'), 'r') as f:
                data = json.load(f)
                questionsets=data['quiz']
        if category == 'maths':
            ques_math=questionsets["maths"]
            questiondict_maths=[]  
            break
        elif category == 'sports':
            ques_sports=questionsets["sport"]
            questiondict_sports=[]
            break
    #   elif language == 'enter abbreviation of your questionset here':
    #       with open('question_sets{}your question set name here.json'.format(dash), 'r') as f:
    #           questionsets = json.load(f)
    #           questiondict = []
    #       break
        else:
            print('Sorry, I don\'t have such quiz in my database. Try again.')
            continue

    
    l_maths=len(ques_math)
    l_sports=len(ques_sports) 
    if category=='maths':
            for i in range(1,l_maths+1):
            	item=ques_math['q'+str(i)]
            	question = item['question']
            	a = item['options'][0]
            	b = item['options'][1]
            	c = item['options'][2]
            	d = item['options'][3]
            	answer = item['answer']             
            	questiondict_maths.append((question, a, b, c, d, answer))
            shuffle(questiondict_maths)

    elif category=='sports':
            for i in range(1,l_sports+1):
                item=ques_sports['q'+str(i)]
                question = item['question']
                a = item['options'][0]
                b = item['options'][1]
                c = item['options'][2]
                d = item['options'][3]
                answer = item['answer']
                questiondict_sports.append((question, a, b, c, d, answer))
            shuffle(questiondict_sports)
    data_store=[]
    # Quiz loop
    while True:
        name = input('Enter your name: ')
        score_maths = 0
        score_sports = 0

        # For each question in question sets, it calls Def_Question,
        # and adds scosre for correct answer
        if category=='maths':
            for q in questiondict_maths:
                score_maths += Def_Question(*q)
        elif category=='sports':
            for q in questiondict_sports:
                score_sports += Def_Question(*q)

        data_store.append({'Name: ': name, 'Maths: ' : score_maths, "Sport: ":score_sports})
        print('''
        				!!!!CONGRAULATIONS!!!!

        				YOU HAD COMPLETED QUIZ

        		    DO AGAIN WANT TO ATTEMPT THE QUIZ

        	''')
        again = input('[y/n] ').lower()
        if again == 'y':
            os.system('cls')
            continue
        else:
            # Saves data into json file
            with open('data_scores.json', 'w') as f:
                json.dump(data_store, f, indent=2)
            break
