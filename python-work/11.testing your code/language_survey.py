from survey import Anonymous


#define a question
question = "What language did you first learn to speak?"
my_survey = Anonymous(question)

#Show the question, and store responses to the question
my_survey.show_question()
print("Enter 'q' to quit any time.\n")
while True:
    response = input("Lnaguage: ")
    if response == 'q':
        break
    my_survey.store_responses(response)
    
#Show the survey results
my_survey.show_results()