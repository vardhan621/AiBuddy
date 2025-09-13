from openai import OpenAI
import requests
client = OpenAI(api_key="Enter your Api key here")
def chat_with_gpt(user_message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # free-tier friendly
        messages=[
            {"role": "system", "content": "You are a helpful chatbot."},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content
def image_gen(user_message):
    result = client.images.generate(
      model="gpt-image-1",
      prompt=user_message,
      size="1024x1024"  # Options: 256x256, 512x512, 
      
    )
    image_url = result.data[0].url
    print("Image URL:", image_url)
    img_data=requests.get(image_url).content 
    with open("robo.png","wb")as f:
       f.write(img_data)
    print("imagesaved")
def link_gen(user_message):
    response =  client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": user_message}]
    )

    print(response['choices'][0]['message']['content'])
