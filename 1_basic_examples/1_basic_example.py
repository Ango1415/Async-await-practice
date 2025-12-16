import asyncio

# asynchronous function
async def fun():
    print("Hello")
    await asyncio.sleep(1)  # Simulate an asynchronous task
    print("World")

asyncio.run(fun()) # calling fun()