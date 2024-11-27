# This script is tested on Sony A7c
import asyncio
from bleak import BleakClient

async def record_camera():
    address = "X2B21C64-9AWE-4W60-QF12-11SC53EU8A84" # Replace with your camera's bluetooth address
    
    try:
        async with BleakClient(address) as client:
            char_uuid = "FF01"

            # 0x0e = Record Button Up
            # 0x0f = Record Button Down

            # Send record sequence
            await client.write_gatt_char(char_uuid, bytes([0x01, 0x0e]))
            await client.write_gatt_char(char_uuid, bytes([0x01, 0x0f]))
            await client.write_gatt_char(char_uuid, bytes([0x01, 0x0e]))

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(record_camera())