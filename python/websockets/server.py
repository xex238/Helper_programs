import asyncio
import websockets

ip_address = 'localhost' # ip-адрес для открытия сервера
main_port = 8772 # Порт для открытия сервера

# Метод приёма сообщения от клиента и вывода его на экран
async def data_exchange(websocket):
    file = await websocket.recv()
    print('Сообщение 1: ', file)

# Запуск сервера
main_server = websockets.serve(data_exchange, ip_address, main_port)
asyncio.get_event_loop().run_until_complete(main_server)
asyncio.get_event_loop().run_forever()