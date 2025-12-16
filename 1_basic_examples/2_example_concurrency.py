import asyncio

async def task_1():
    print("Task 1 started")
    await asyncio.sleep(2)  # Simulate a 2-second task
    print("Task 1 completed")

async def task_2():
    print("Task 2 started")
    await asyncio.sleep(1)  # Simulate a 1-second task
    print("Task 2 completed")

async def main():
    await asyncio.gather(task_1(), task_2())  # Run both tasks concurrently

asyncio.run(main())