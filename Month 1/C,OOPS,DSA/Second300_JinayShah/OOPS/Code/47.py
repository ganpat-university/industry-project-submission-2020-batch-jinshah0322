import asyncio

async def state_machine():
    state = "start"
    
    async def state_start():
        nonlocal state
        print("Entering state: start")
        await asyncio.sleep(1)
        state = "processing"
    
    async def state_processing():
        nonlocal state
        print("Entering state: processing")
        await asyncio.sleep(2)
        state = "end"
    
    async def state_end():
        nonlocal state
        print("Entering state: end")
    
    while state != "end":
        if state == "start":
            await state_start()
        elif state == "processing":
            await state_processing()
        elif state == "end":
            await state_end()
        else:
            raise ValueError("Invalid state")

async def main():
    await state_machine()

if __name__ == "__main__":
    asyncio.run(main())
