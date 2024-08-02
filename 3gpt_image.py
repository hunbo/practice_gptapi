from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

os.environ.get("OPEN_API_KEY")


api_key = os.environ.get("OPEN_API_KEY")
client = OpenAI(
    api_key= api_key
)

#response = client.images.generate(
    #model="dall-e-3",
    #prompt="겨울, 우주, 마녀, 판타지, 코어, 생물, 초현실적, 어두운이미지를 그려줘",
    #size = "1024x1024",
    #quality="standard",
    #n=1,)
  

#image_url = response.data[0].url
#print(image_url)

#from PIL import Image
#import urllib.request
#def display_jpeg_image(url):
    #try:
        #image_path, _ = urllib.request.urlretrieve(url, "test.jpg")
        #print(image_path)
        #image = Image.open(image_path)
        #image.show()
   # except Exception as e:
   #     print("Error:", e)

#jpeg_image_path =  "https://cdn.kbmaeil.com/news/photo/201904/811074_839900_5653.jpg"
#display_jpeg_image(jpeg_image_path)
#이해완료

#response = client.images.edit(
#    model="dall-e-2",
#    image=open("assets/background.png", "rb"), #rb: read binary, 이 모드는 텍스트 파일이 아닌 바이너리 파일(예: 이미지, 비디오, 실행 파일 등)을 열 때 사용.
#    mask=open("assets/mask.png", "rb"),
#    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
#    n=1,
#    size="1024x1024",
#)
#image_url = response.data[0].url
#print(image_url)
#이해 완료

response = client.images.create_variation(
    image=open("assets/cat-and-dog.png", "rb"),
    n=2,
    size="1024x1024"
)
image_url = response.data[0].url
print(image_url)