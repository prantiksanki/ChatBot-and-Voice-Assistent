# prepros.py
from llm_add import llm
from langchain_core.prompts import PromptTemplate

# Function to generate precise disaster-related information
def generate_disaster_response(query, disaster):
    template = '''
    You are a disaster guidance system that provide 
    the most precise, optimal, relevant response based on the disaster 
    type and user query by giving response that is based on international standard.
    The user is stranded in that disaster situation and you have to give perfect Response in the input language, in one 
    paragraph, within 120 characters, without special characters, the user follows your steps
    and wants the best solution so that he can save his life. Also provide governmental details or contact to get out of the situation

    Scenario: {disaster}
    User Query: "{query}"

    Deliver only essential information—no extras.
    '''
    
    # Create the prompt
    prompt = PromptTemplate.from_template(template)
    
    # Prepare the input for the LLM
    chain = prompt | llm
    
    # Invoke the LLM with the input
    response = chain.invoke(input={"query": query, "disaster": disaster})
    
    return response.content