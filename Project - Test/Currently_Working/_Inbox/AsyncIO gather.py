import asyncio
import requests
from time import sleep

async def f1():
    print("f1 ran")
    url = "https://img.freepik.com/free-photo/majestic-mountain-peak-tranquil-winter-landscape-generated-by-ai_188544-15662.jpg"
    respond = requests.get(url)
    with open("image.jpg","wb") as f:
        f.write(respond.content)

async def f2():
    print("f2 ran")
    url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYkI__WCZy0vYn4BVFcftAOv1kZgH-2QFgizkw-piqkgEnltP4UkJQ9k7U5T6NXwrct7A&usqp=CAU"
    respond = requests.get(url)
    with open("image2.jpg","wb") as f:
        f.write(respond.content)
    
async def f3():
    print("f3 ran")
    url = "https://images.unsplash.com/photo-1556379092-dca659792591?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8fA%3D%3D"
    respond = requests.get(url)
    with open("image3.jpg","wb") as f:
        f.write(respond.content)

async def main():
    l = await asyncio.gather(
            f1(),
            f2(),
            f3())
    print (l)

asyncio.run(main())