import socket

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем адрес и порт сервера
server_address = ('localhost', 8888)

# Устанавливаем соединение с сервером
client_socket.connect(server_address)

# Отправляем данные серверу
message = "Привет, сервер!"
client_socket.send(message.encode())

# Получаем ответ от сервера
response = client_socket.recv(1024)
print("Получен ответ от сервера:", response.decode())

# Закрываем соединение
client_socket.close()

#
#     Создаем сокет: client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM).
#         socket.AF_INET указывает, что используется семейство протоколов IPv4.
#         socket.SOCK_STREAM указывает, что используется протокол TCP для надежной передачи потока данных.
#
#     Устанавливаем адрес и порт сервера: server_address = ('localhost', 8888).
#         'localhost' означает, что клиент будет подключаться к серверу на локальном компьютере.
#         8888 - это порт сервера, к которому клиент будет подключаться.
#
#     Устанавливаем соединение с сервером: client_socket.connect(server_address).
#         connect() устанавливает соединение с сервером по указанному адресу и порту.
#
#     Отправляем данные серверу: message = "Привет, сервер!"; client_socket.send(message.encode()).
#         encode() преобразует строку в байтовый формат перед отправкой через сокет.
#
#     Получаем ответ от сервера: response = client_socket.recv(1024).
#         recv(1024) читает до 1024 байтов данных из сокета.
#
#     Закрываем соединение: client_socket.close().
#         close() закрывает сокет клиента и освобождает ресурсы.
#
# Этот код создает простой клиент, который устанавливает соединение с сервером, отправляет ему сообщение, получает ответ и закрывает соединение.