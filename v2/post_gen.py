import openai

openai.api_key = "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"

model_engine = "text-davinci-002"
prompt = "Roger Federer won the US Open in 2008."
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

message = completions.choices[0].text
print(message)
print("JUZ")