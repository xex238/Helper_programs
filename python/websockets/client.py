import asyncio
import websockets

ip_address = 'localhost' # ip-адрес сервера
main_port = 8772 # Порт сервера

# Отправить сообщение серверу и закрыть подключение
async def send_data():
    uri = "ws://" + ip_address + ":" + str(main_port)
    async with websockets.connect(uri) as websocket:
        await websocket.send('Hello world!')

# Запуск клиента
asyncio.get_event_loop().run_until_complete(send_data())