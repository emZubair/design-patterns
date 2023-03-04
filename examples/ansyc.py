import asyncio


async def task(name, work_queue):
    while not work_queue.empty():
        delay = await work_queue.get()
        print(f"Task '{name} for {delay}' is running...")
        await asyncio.sleep(delay)
        # await asyncio.sleep(delay) is non-blocking


async def main():
    """
    This is the main entry point for the program
    """
    # Create the queue of work
    work_queue = asyncio.Queue()

    # Put some work in the queue
    for work in [3, 1, 5, 2, 4, 6, 7]:
        await work_queue.put(work)

    # Run the tasks
    await asyncio.gather(
        asyncio.create_task(task("One", work_queue)),
        asyncio.create_task(task("Four", work_queue)),
        asyncio.create_task(task("Seven", work_queue)),
        asyncio.create_task(task("Ten", work_queue)),
        asyncio.create_task(task("Two", work_queue)),
    )

if __name__ == "__main__":
    asyncio.run(main())
