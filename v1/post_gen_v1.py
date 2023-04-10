
import openai

openai.api_key = "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"

model_engine = "text-davinci-002"
prompt = "Monastyr M15 \nJest FINAŁ!!! \nDzisiaj pokonałem Simone Roncalli 6:2 6:2 💪💪 \nJestem mega zadowolony a jutro zawalczę o tytuł. \nTrzymajcie kciuki ✊️"
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

