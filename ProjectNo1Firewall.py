import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 8080

blocked_ips = ['127.0.0.2']

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print(" Python Personal Firewall ")
print(" Listening on Port:", PORT)

while True:
    client_socket, addr = server.accept()
    client_ip = addr[0]
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n[{current_time}] Connection attempt from {client_ip}")

    if client_ip in blocked_ips:
        print(" BLOCKED:", client_ip)
        body = "Access Denied by Firewall!"
        status = "403 Forbidden"
    else:
        print(" ALLOWED:", client_ip)
        body = "Access Granted!"
        status = "200 OK"

    response = f"""HTTP/1.1 {status}
Content-Type: text/plain
Content-Length: {len(body)}
Connection: close

{body}"""

    client_socket.sendall(response.encode())
    client_socket.close()
