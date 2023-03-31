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
        global_messages.append({"role": "system", 
                                "content": 
                                    """You are Rafi, an AI created by Shamiri Health to help people with mental health problems. 
                                    You are talking to a mental health chatbot user {username} that is experiencing {motivation}, {purpose}, and {wellness}.
                                    You need to do three things 
                                    1. whenever the user is at risk to harm others as well as themselves , ask them to call Shamiri Health License Psychologist at +254795486186. 
                                    2. Try to keep your response short and under 200 tokens and focus on listening to the user. 
                                    3. Whenever you feel like you couldn't help or the user continues to struggle with their emotions, ask them to call Shamiri Health licensesd therapist at 795496186
                                    
                                    """.format(username="jiajiabinx", motivation = "lack of motivation",purpose = "low sense of purpose", wellness = "some symptons of anxiety and depression")})
    
    global_messages.append({"role": "user", "content": message})
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=global_messages,
            max_tokens=200,
            n=1,
            stop=None,
            temperature=0.5,
        )

        gpt_response = response.choices[0].message.content.strip()
        global_messages.append({"role": "assistant", "content": gpt_response})
        return gpt_response
    except Exception as e:
        return f"Error: {str(e)}"