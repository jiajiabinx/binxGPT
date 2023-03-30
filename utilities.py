import re
import openai

def extract_language(response_text):
    pattern = r'```(\w+)?((?:(?!```)[\s\S])+)?```|`([^`]+)`'
    match = re.search(pattern, response_text)

    if match:
        if match.group(1):
            return True, match.group(1)
        elif match.group(3):
            return True,'text'
        else:
            return True,'text'
    else:
        return False, None


def chat_gpt(message,global_messages):
    
    if not global_messages:
        global_messages.append({"role": "system", "content": "You are ChatGPT, an AI assistant trained by OpenAI."})
    
    global_messages.append({"role": "user", "content": message})
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=global_messages,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )

        gpt_response = response.choices[0].message.content.strip()
        global_messages.append({"role": "assistant", "content": gpt_response})
        return gpt_response
    except Exception as e:
        return f"Error: {str(e)}"