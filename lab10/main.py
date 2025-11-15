from log_device import log_nearby_devices
from scan_device import scan_for_devices
import asyncio
import shelve


async def scan():
    nearby_devices = await scan_for_devices()
    if nearby_devices:
        log_nearby_devices(nearby_devices)
    else:
        print("No known devices nearby.")


def main():
    while True:
        print("scanning...")
        asyncio.run(scan())
        print("sleeping till next scan...")
        asyncio.sleep(3600)

        #varifying
        with shelve.open("device_log.db") as db:
            for name, address in db.items():
                print(f"{name}: {address}")


if __name__ == "__main__":
    main()
