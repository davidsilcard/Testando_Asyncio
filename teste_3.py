import asyncio


class Impressora():

    async def printar_1(self):
        await asyncio.sleep(2)
        print(1)

    async def printar_2(self):
        print(2)


async def main():
    ip = Impressora()
    task1 = asyncio.ensure_future(ip.printar_1())
    task2 = asyncio.ensure_future(ip.printar_2())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
