from dotenv import load_dotenv
from groq import Groq

load_dotenv(".env.local")

client = Groq()

# Function that send I amge and return chess elo

def rating(image1):
    model = "llama3-groq-70b-8192-tool-use-preview"
    system_prompt = f"""
        You are an elite artist that rates art pieces and returns a chess elo rating between 0 and 2800.
        Return number only. You must be realistic and not lie. You must think like an elite artist while grading the complexity and you grade them based on technicality of the art piece and creativity of art pieces.
        If the image is a masterpiece like the mona lisa, you must return a score of 2800. You have to give me a definite answer that is objectively true.
    """

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Image 1: {image1}"
                    }
                ]
            },
        ],
        temperature=1.5,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    return int(completion.choices[0].message.content)


