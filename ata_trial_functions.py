import openai
from openai import OpenAI

def genereer_afbeelding(apik, vraagtekst):
    client = OpenAI(api_key=apik)
    invoer = vraagtekst
    response = client.images.generate(
    model="dall-e-3",
    prompt=invoer,
    n=1,
    size="1792x1024",
    quality="hd"
    )
    return response.data[0].url




