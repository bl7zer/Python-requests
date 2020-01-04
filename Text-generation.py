from requests import post
from json import loads

url = 'https://models.dobro.ai/gpt2/medium/' #link to post request (link to neural network: "https://porfirevich.ru")
data = ({
    "prompt": "your text (begin story)",
    "length": 50, #text max lendth
    "num_samples": 5 #nums of examples
})

text = post(url, json=data).text
text = loads(text)["replies"] #transform json to py_dict
