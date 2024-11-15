from dotenv import load_dotenv
from groq import Groq

load_dotenv(".env.local")

client = Groq()

# Function that send I amge and return chess elo

def rating(image1):
    model = "llama3-groq-70b-8192-tool-use-preview"
    system_prompt = f"""
        You are an elite artist that rates art pieces and returns a chess elo rating between 0 and 3000.
        Return number only. You must be realistic and not lie. You must think like an elite artist while grading the complexity and you grade them based on technicality of the art piece and creativity of art pieces. Your rating must solely based of the technical expertise potrayed in the art piece.
        You need to rate based on CSI. You have to give me a definite answer that is objectively true. You must be realistic and not lie. For Ex: https://i.imgur.com/62ZnMny.jpeg is 2500 elo.
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
                        "text": f"Image 1: {image1} Rating: "
                    }
                ]
            },
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=0.4,
        stream=False,
        stop=None,
    )

    return (completion.choices[0].message.content)


