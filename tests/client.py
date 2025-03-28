import asyncio

from hh import HHClient


async def main():
    client = HHClient("client_id", "client_secret")
    employer = client.employer
    res = await employer.resume.search(text="python")
    print(res)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
