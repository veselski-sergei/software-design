import pytest
import os
from app_auth import *
from telethon import TelegramClient
from telethon.sessions import StringSession

@pytest.fixture(scope="function")
async def client() -> TelegramClient:
    client = TelegramClient(None, api_id, api_hash)
    client.session.set_dc(2, '149.154.167.40', 443)
    # Connect to the server
    #
    await client.start(phone='9996621234', code_callback=lambda: '22222')
    #await client.connect()

    # Issue a high level command to start receiving message
    await client.get_me()
    # Fill the entity cache
    await client.get_dialogs()

    yield client

    async with client.conversation("@PolySmartHomeBot", timeout=100) as conv:
        await conv.send_message("Главное меню")
        
    await client.disconnect()
    await client.disconnected