import os
from huggingface_hub import InferenceClient

## You need a token from https://hf.co/settings/tokens. If you run this on Google Colab, you can set it up in the "settings" tab under "secrets". Make sure to call it "HF_TOKEN"
#os.environ["HF_TOKEN"]="hf_xxxxxxxxxxxxxx"

#client = InferenceClient("meta-llama/Llama-3.2-3B-Instruct")
# if the outputs for next cells are wrong, the free model may be overloaded. You can also use this public endpoint that contains Llama-3.2-3B-Instruct
client = InferenceClient("https://jc26mwg228mkj8dw.us-east-1.aws.endpoints.huggingface.cloud") 


# Here there is not EOS (End of sequence of the token)
'''
output = client.text_generation(
    "The capital of France is",
    max_new_tokens=100,
)

print(output)

Output -> Paris. The capital of Italy is Rome. The capital of Spain is Madrid. The capital of Germany is Berlin. The capital of the United Kingdom is London. The capital of Australia is Canberra. The capital of China is Beijing. The capital of Japan is Tokyo. The capital of India is New Delhi. The capital of Brazil is Brasília. The capital of Russia is Moscow. The capital of South Africa is Pretoria. The capital of Egypt is Cairo. The capital of Turkey is Ankara. The
'''


#Here there is the submission of the request through the chhat template related to the model https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct
'''prompt="""<|begin_of_text|><|start_header_id|>user<|end_header_id|>
The capital of France is<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""
output = client.text_generation(
    prompt,
    max_new_tokens=100,
)

print(output)

Output -> ...Paris!

'''


#This is the simplest way to use the chat template

output = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "The capital of France is"},
    ],
    stream=False,
    max_tokens=1024,
)
print(output.choices[0].message.content)

"Output -> Paris."

