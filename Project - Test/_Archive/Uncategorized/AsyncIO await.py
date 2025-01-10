import asyncio
from time import sleep

async def f1(a):
    print("f1 ran")
    sleep(1)
    print(a**3)

async def f2(a):
    print("f2 ran")
    sleep(3)
    print(a**4)
    
async def f3(a):
    print("f3 ran")
    sleep(5)
    print(a**6)

async def main():
    await f1(4)
    await f2(4)
    await f3(4)
    return "zyx"

asyncio.run(main())

# output:
# f1 ran
# 64
# f2 ran
# 256
# f3 ran
# 4096