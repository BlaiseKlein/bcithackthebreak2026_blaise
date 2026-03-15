from google import genai
from dotenv import load_dotenv


load_dotenv()

def get_ai_bot_response(prompt: str):
       
    console_toolbox = ["ssh", "scp", "ping", "curl", "ipconfig", "ncat", "nc", "tcpdump", "whoami", "groups", "id"]
        
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
    
    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=chat_prompt
    )

    return response.text
