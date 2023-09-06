import socket

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем адрес и порт сервера
server_address = ('localhost', 8888)
server_socket.bind(server_address)

# Начинаем прослушивать входящие соединения
server_socket.listen(1)
print("Сервер запущен. Ожидание подключений...")

# Принимаем входящее соединение
client_socket, client_address = server_socket.accept()
print("Подключено клиентское соединение:", client_address)

# Получаем данные от клиента
data = client_socket.recv(1024)
print("Получены данные от клиента:", data.decode())

# Отправляем ответ клиенту
response = "Привет, клиент!"
client_socket.send(response.encode())

# Закрываем соединение
client_socket.close()
server_socket.close()


#     Создаем сокет: server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM).
#         socket.AF_INET указывает, что используется семейство протоколов IPv4.
#         socket.SOCK_STREAM указывает, что используется протокол TCP для надежной передачи потока данных.
#
#     Устанавливаем адрес и порт сервера: server_address = ('localhost', 8888).
#
#     Привязываем сокет к указанному адресу и порту: server_socket.bind(server_address).
#
#     Начинаем прослушивать входящие соединения: server_socket.listen(1).
#         Аргумент 1 указывает на количество максимальных ожидаемых входящих соединений.
#
#     Принимаем входящее соединение: client_socket, client_address = server_socket.accept().
#         accept() блокирует выполнение программы, пока не будет получено входящее соединение.
#         При успешном принятии соединения возвращается новый сокет client_socket, представляющий соединение с клиентом, и адрес клиента client_address.
#
#     Получаем данные от клиента: data = client_socket.recv(1024).
#         recv(1024) читает до 1024 байтов данных из сокета.
#
#     Отправляем ответ клиенту: response = "Привет, клиент!"; client_socket.send(response.encode()).
#         encode() преобразует строку в байтовый формат перед отправкой через сокет.
#
#     Закрываем соединение: client_socket.close(); server_socket.close().
#         close() закрывает сокеты клиента и сервера, освобождая ресурсы.
#
# Этот код создает простой сервер, который принимает входящие соединения, получает данные от клиента, отправляет ответ и закрывает соединение.