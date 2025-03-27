import asyncio

from hh import HHClient


async def main():
    client = HHClient("client_id", "client_secret")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        asyncio.get_event_loop().close()
