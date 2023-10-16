import openai


def Home(question):
    prompt = question
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful cooking assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content


chat = input("Enter your question: ")
print(Home(chat))
