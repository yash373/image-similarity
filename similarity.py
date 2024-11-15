from dotenv import load_dotenv
from groq import Groq

load_dotenv(".env.local")

client = Groq()

# Function that send two images, Image1 and Image2
# It returns the similarity score between the two images by prompting llm

def similarity(image1, image2):
    model = "llama3-groq-70b-8192-tool-use-preview"
    system_prompt = f"""
        You are an elite artist that compares art pieces and returns a similarity score between 0 and 10000.
        Return number only. You must be realistic and not lie. You must think like an elite artist while grading the similarity of art pieces.
        Colour should be a big component in your judging criteria. For Ex: https://i.imgur.com/62ZnMny.jpeg and https://i.imgur.com/epE7S1R.jpeg have a similarity of 7000
        If the images are completely unrealated then you must return a score of 0. You have to give me a definite answer that is objectively true.
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
                        "text": f"Image 1: {image1}\nImage 2: {image2}"
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

    return int(completion.choices[0].message.content)

# Test

# image1 = "https://plus.unsplash.com/premium_photo-1673002094195-f18084be89ce?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# image2 = "https://images.unsplash.com/photo-1460627390041-532a28402358?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# print(similarity(image1, image2))
