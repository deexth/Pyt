import openai

# from django.core.paginator import Paginator



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

# def Home(question):
#     prompt = question
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt},
#         ],
#         stream=True,
#     )
#     for chunk in response:
#         return chunk.choices[0].delta
#         # return chunk


# chat = input("Enter your question: ")
# print(Home(chat))