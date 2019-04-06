import socket
import json
import sys


def run_server(host, port):
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)
    print('running on ', host, port)

    while True:
        try:
            client, addr = sock.accept()
            print(f'{addr} connected')

            try:
                json_data = client.recv(1024)
                data = json.loads(json_data)
                print(data)
            except Exception as err:
                print(err)

        except KeyboardInterrupt:
            print('=' * 50 + '\n', 'Сервер недоступен')
            sock.close()
            sys.exit()


run_server('127.0.0.1', 8080)
