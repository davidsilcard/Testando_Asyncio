import asyncio

async def printar_1():
    await asyncio.sleep(2)
    print(1)


async def printar_2():
    print(2)

async def main():
    task1 = asyncio.create_task(printar_1())
    task2 = asyncio.create_task(printar_2())

    await asyncio.gather(task1,task2)

if __name__ == '__main__':
    asyncio.run(main())