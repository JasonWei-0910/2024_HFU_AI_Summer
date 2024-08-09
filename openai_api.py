from openai import OpenAI
import os 

def chat_with_chatgpt(user_message, openai_api_key):
    client = OpenAI(api_key=openai_api_key)
    chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content":user_message +'請用作家的方式回答'
                }
            ],
            model="gpt-3.5-turbo",
        )
        
    response = chat_completion.choices[0].message.content
    return response if response else 'No Content'




if __name__=='__main__':
  user_message = '加速世界好好看'
  api_key = os.getenv('OPENAI_API_KEY',None)
  if api_key and user_message:
     response = chat_with_chatgpt(user_message, api_key)
     print(response)
    
 
   



    