from huggingface_hub import InferenceClient

client = InferenceClient("https://jc26mwg228mkj8dw.us-east-1.aws.endpoints.huggingface.cloud") 

prompt = f'''
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
    Answer the following questions as best you can. You have access to the following tools:

get_weather: Get the current weather in a given location

The way you use the tools is by specifying a json blob.
Specifically, this json should have a `action` key (with the name of the tool to use) and a `action_input` key (with the input to the tool going here).

The only values that should be in the "action" field are:
get_weather: Get the current weather in a given location, args: {{"location": {{"type": "string"}}}}
example use : 

{{
  "action": "get_weather",
  "action_input": {{"location": "New York"}}
}}

ALWAYS use the following format:

Question: the input question you must answer
Thought: you should always think about one action to take. Only one action at a time in this format:
Action:

$JSON_BLOB (inside markdown cell)

Observation: the result of the action. This Observation is unique, complete, and the source of truth.
... (this Thought/Action/Observation can repeat N times, you should take several steps when needed. The $JSON_BLOB must be formatted as markdown and only use a SINGLE action at a time.)

You must always end your output with the following format:

Thought: I now know the final answer
Final Answer: the final answer to the original input question

Now begin! Reminder to ALWAYS use the exact characters `Final Answer:` when you provide a definitive answer. 
<|eot_id|><|start_header_id|>user<|end_header_id|>
What's the weather in London ?
<|eot_id|><|start_header_id|>assistant<|end_header_id|>

Action:
{{ "action": "get_weather", "action_input": {{"location": {{"type": "string", "value": "London"}}}} }}

Thought: I will check the weather in London.
Observation: the weather in London is sunny with low temperatures. 
'''

output = client.text_generation(
    prompt,
    max_new_tokens=100,
)

print(output)

# Dummy function
def get_weather(location):
    return f"the weather in {location} is sunny with low temperatures.\n"

print(get_weather('London'))

print("""
Possible outputs 

Final Answer: The current weather in London is sunny with low temperatures.
the weather in London is sunny with low temperatures.

""")