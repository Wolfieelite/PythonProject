from bleak import BleakScanner

KNOWN_AVALIBLE_DEVICES = {
    "TY": "38:2C:E5:1A:2E:04",
    "TV Samsung 6 Series 55":  "28:39:5E:5F:E0:13"
}

async def scan_for_devices():
    devices = await BleakScanner.discover()
    near_by_devices = {}

    for d in devices:
        if d.name == None:
            continue
        if d.address in KNOWN_AVALIBLE_DEVICES.values():
            device_name = [name for name, address in KNOWN_AVALIBLE_DEVICES.items() if address == d.address][0]
            print(f"{device_name} is nearby!")
            near_by_devices[device_name] = d.address
    return near_by_devices
