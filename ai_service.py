from groq import Groq
from dotenv import load_dotenv
import os

from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def get_ai_response(user_text):

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_text,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    answer = get_ai_response("Я люблю математику, комп'ютери і логічні задачі. Яку професію мені обрати?")
    print(answer)