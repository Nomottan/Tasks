import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for ball in range(1, 6):
        await asyncio.sleep(12/power)
        print(f"Силач {name} поднял {ball} шар")
    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    participant_1 = asyncio.create_task(start_strongman('Pasha', 2))
    participant_2 = asyncio.create_task(start_strongman('Denis', 3))
    participant_3 = asyncio.create_task(start_strongman('Apollon', 4))
    await participant_1
    await participant_2
    await participant_3

asyncio.run(start_tournament())
