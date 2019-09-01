import asyncio


async def printar_1():
    await asyncio.sleep(2)
    print(1)


async def printar_2():
    print(2)


async def main():
    task1 = asyncio.ensure_future(printar_1())
    task2 = asyncio.ensure_future(printar_2())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
