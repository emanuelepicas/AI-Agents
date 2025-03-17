from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel

# Initialize the LiteLLMModel with Ollama's mistral model
model = LiteLLMModel(model_id='ollama_chat/mistral')

# Set up the agent with the DuckDuckGo search tool
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

# Run the agent with your query
agent.run("Search for the best music recommendations for a party at Wayne's mansion.")
