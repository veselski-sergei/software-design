import sys
from pytest import mark
from telethon import TelegramClient
from telethon.tl.custom.message import Message
from messages import *


@mark.asyncio
async def test_start(client: TelegramClient):
    # Create a conversation
    async with client.conversation("@PolySmartHomeBot", timeout=100) as conv:
        # Send a command
        await conv.send_message("/start")
        # Get response
        resp: Message = await conv.get_response()
        # Make assertions
        assert "чем воспользуешься?" in resp.raw_text

@mark.asyncio
async def test_menu(client: TelegramClient):
    # Create a conversation
    async with client.conversation("@PolySmartHomeBot", timeout=100) as conv:
        # Send a command
        await conv.send_message("главное меню")
        # Get response
        resp: Message = await conv.get_response()
        # Make assertions
        assert "выбери раздел" in resp.raw_text
 

@mark.asyncio
async def test_info(client: TelegramClient):
    # Create a conversation
    async with client.conversation("@PolySmartHomeBot", timeout=100) as conv:
        # Send a command
        await conv.send_message("инфо")
        # Get response
        resp: Message = await conv.get_response()
        # Make assertions
        assert "выбери объект" in resp.raw_text

@mark.asyncio
async def test_info_temp(client: TelegramClient):
    # Create a conversation
    async with client.conversation("@PolySmartHomeBot", timeout=100) as conv:
        # Send a command
        await conv.send_message("инфо")
        await conv.send_message("темпиратура")
        # Get response
        resp: Message = await conv.get_response()
        # Make assertions
        assert "Текущая температура:" in resp.raw_text

@mark.asyncio
async def test_info_hum(client: TelegramClient):
    # Create a conversation
    async with client.conversation("@PolySmartHomeBot", timeout=100) as conv:
        # Send a command
        await conv.send_message("инфо")
        await conv.send_message("влажность")
        # Get response
        resp: Message = await conv.get_response()
        # Make assertions
        assert "Текущая влажность:" in resp.raw_text

@mark.asyncio
async def test_info_relay(client: TelegramClient):
    # Create a conversation
    async with client.conversation("@PolySmartHomeBot", timeout=100) as conv:
        # Send a command
        await conv.send_message("инфо")
        await conv.send_message("розетка")
        # Get response
        resp: Message = await conv.get_response()
        # Make assertions
        assert "Состояние розетки (реле):" in resp.raw_text

@mark.asyncio
async def test_manage(client: TelegramClient):
    # Create a conversation
    async with client.conversation("@PolySmartHomeBot", timeout=100) as conv:
        # Send a command
        await conv.send_message("управление")
        # Get response
        resp: Message = await conv.get_response()
        # Make assertions
        assert "Что сделать с розеткой?" in resp.raw_text

@mark.asyncio
async def test_manage_ON_relay(client: TelegramClient):
    # Create a conversation
    async with client.conversation("@PolySmartHomeBot", timeout=100) as conv:
        # Send a command
        await conv.send_message("управление")
        await conv.send_message("включить")
        # Get response
        resp: Message = await conv.get_response()
        # Make assertions
        assert ("Включаю реле" in resp.raw_text) or ("реле уже под напряжением" in resp.raw_text)

@mark.asyncio
async def test_manage_OFF_relay(client: TelegramClient):
    # Create a conversation
    async with client.conversation("@PolySmartHomeBot", timeout=100) as conv:
        # Send a command
        await conv.send_message("управление")
        await conv.send_message("выключить")
        # Get response
        resp: Message = await conv.get_response()
        # Make assertions
        assert ("Отключаю реле" in resp.raw_text) or ("реле уже обесточено" in resp.raw_text)

@mark.asyncio
async def test_manage_state(client: TelegramClient):
    # Create a conversation
    async with client.conversation("@PolySmartHomeBot", timeout=100) as conv:
        # Send a command
        await conv.send_message("управление")
        await conv.send_message("текущее состояние")
        # Get response
        resp: Message = await conv.get_response()
        # Make assertions
        assert ("Состояние розетки (реле): Реле включено" in resp.raw_text) or ("Состояние розетки (реле): Реле обесточено" in resp.raw_text)


@mark.asyncio
async def test_signaling(client: TelegramClient):
    # Create a conversation
    async with client.conversation("@PolySmartHomeBot", timeout=100) as conv:
        # Send a command
        await conv.send_message("сигнализация")
        # Get response
        resp: Message = await conv.get_response()
        # Make assertions
        assert "какой раздел необходим?" in resp.raw_text

