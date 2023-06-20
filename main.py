import subprocess
import os
import socket

from threading import Thread
from get_folders_and_files import list_dir, read_file, read_file_str

SERVER_ADDRES = "0.0.0.0"  # socket.gethostbyname("localhost")
SERVER_PORT = 8080


def process_request(client_socket, address):
    print(f"Connection from {address} has been established!")

    received_data = client_socket.recv(1024)
    received_data = received_data.decode()
    headers = received_data.split("\r\n")
    header_get = headers[0]

    requested_page = header_get.split(" ")[1][1:]
    # requested_page = "/" + requested_page

    text_extensions = ["html", "css", "js", "pdf", "txt"]
    executable_extensions = ["py-run"]
    byte_flag = False
    print("test %s", requested_page)

    response_body = ""
    response_header = "HTTP/1.1 200 OK\r\n\r\n"

    if requested_page:
        if requested_page == "HEADER":
            response_body = received_data

        elif requested_page.split(".")[-1] in executable_extensions:
            if requested_page in [
                "get_folders_and_files.py-run",
                "main.py-run",
            ]:
                response_body = "Sorry can't run this program"
            else:
                requested_page = requested_page.replace("-run", "")
                process = subprocess.run(
                    ["python3", requested_page], stdout=subprocess.PIPE, text=True
                )
                response_body = process.stdout

        elif os.path.exists(requested_page):
            if os.path.isdir(requested_page):
                response_body = list_dir(requested_page)
            elif requested_page.split(".")[-1] in text_extensions:
                response_body, response_header = read_file_str(requested_page)
            else:
                response_body, response_header = read_file(requested_page)
                byte_flag = True

        else:
            file = open("not_found.html", "r", encoding="utf-8")
            response_header = "HTTP/1.1 404 NOT FOUND\r\n\r\n"
    else:
        response_body = list_dir(".")

    if byte_flag is False:
        response = response_header + response_body
        client_socket.send(response.encode("utf-8"))
    else:
        response = response_header.encode("utf-8") + response_body
        client_socket.send(response)

    client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDRES, SERVER_PORT))
server_socket.listen(10)
print(f"server listening {SERVER_ADDRES}:{SERVER_PORT}")

while True:
    client_socket, address = server_socket.accept()

    Thread(target=process_request, args=(client_socket, address)).start()

server_socket.close()
