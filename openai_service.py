from dotenv import load_dotenv
import os
from openai import OpenAI

# Loading key for openai
load_dotenv()

def get_ai_bot_response(prompt: str):
       
    console_toolbox = ["ssh", "scp", "ping", "curl", "ipconfig", "ncat", "nc", "tcpdump", "whoami"]
        
    chat_prompt = (
        f"We have an interactive command line wrapper for Linux with a lot of networking functionality, including these commands: {console_toolbox}." 
        f"We will be having the user prompt you about things such as which command to use and why, or what the tool in our console toolbox does. If there ask"
        f"about an explanation about one of the commands found in our toolbox, please respond with a quick summary of what the command does and what parameters and options"
        f"it needs to run (have an example of the command with all required options/parameters as the last bit of your sentence). If they ask about a tool not in the toolbox, "
        f"please respond with something along the lines of: 'The command requested is not available in this console tool, please try again.'"
        f"If they ask about more than one command, or a comparison of more than one tool, please give a quick summary answer. If they ask for a recommended"
        f"command to use, if there is a viable command available in the toolbox for their situation, please respond with a quick summary of it and what it does, and if there is no"
        f"commands that fit the situation, please respond with something along the lines of 'This toolbox does not have any commands available for that situation, please try again.'"
        f"Please keep responses to a maximum of two sentences. This is the user prompt: {prompt}"
    )
    
    OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

    # Checks if no open api key, if none then returns previously generated mock response
    if not OPENAI_API_KEY:
        print("No OpenAI Key Available")
        return "OpenAI API Key not found."
       
    else:
        print("Generating response")

        # Initialize OpenAI Client with key
        client = OpenAI(api_key = OPENAI_API_KEY)

        # Send prompt to openai
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content": chat_prompt}]
        )

    return response.choices[0].message.content