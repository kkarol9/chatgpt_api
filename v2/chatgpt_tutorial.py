import openai

# load and set our key
openai.api_key = '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'

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", # this is "ChatGPT" $0.002 per 1k tokens
  messages=[{"role": "user", "content": "Hej, czy pomożesz mi stworzyć post na facebooka podsumowujący mój udział w turnieju tenisowym? Turniej był rozgrywany w sharm el sheikh w egipcie. Był to turniej itf word tour na nawierzchni twardej,. W pierwszej rundzie wygrałem 6-3 2-6 6-2 z Petrem Nestorem, w drugiej wygrałem 6-7 7-6 7-6 z Petrem Benjaminem Privara, w w QF przegrałem z Mohamedem Safatem 6-3 2-6 5-7. Był to udany występ dzięki któremu zdobyłem trzy punkty do rankingu.?"}]
)

print(completion)



reply_content = completion.choices[0].message.content
print(reply_content)


message_history = []
# What is the moon's circumference in km?
user_input = input("> ")
print("User's input was: ", user_input)