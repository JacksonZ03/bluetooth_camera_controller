import asyncio
from bleak import BleakScanner
from tabulate import tabulate

async def scan_devices():
    devices = await BleakScanner.discover()
    device_list = []
    for device in devices:
        # Some devices might not have a name, so we handle that case
        name = device.name if device.name else "Unknown Device"
        device_list.append([device.address, name])
    
    # Sort by device name for better readability
    device_list.sort(key=lambda x: x[1])
    print("\nBluetooth Devices Found:")
    print(tabulate(device_list, headers=['Address', 'Device Name'], tablefmt='grid'))

async def main():
    await scan_devices()

asyncio.run(main())