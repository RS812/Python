import asyncio
async def greetings():
    asyncio.create_task(disp())
    print("Good Morning")
    await asyncio.sleep(1)
    print("Good Byee..")
async def disp():
    print ("Good Afternoon")
    await asyncio.sleep(1)
    print("Good Byee..")
asyncio.run(greetings())
