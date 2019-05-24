#!/usr/bin/env python3
import sys
import os
import struct
import socket
import re

from hashlib import sha256
from base64 import b32encode, b64decode, b64encode
from multiprocessing import Process, Queue

def get_sam_address():
    value = os.getenv("I2P_SAM_ADDRESS")
    if value:
        value = value.split(":")
        return (value[0], int(value[1]))
    else:
        return ("127.0.0.1", 7656)

def vain(data, prefix, q):
    cert_len = struct.unpack("!H", data[385:387])[0]

    public_data = data[:387+cert_len]
    data_tail = data[387+cert_len:]

    head = public_data[:256] + os.urandom(88)
    tail = public_data[352:]
    head_hash = sha256(head)

    while True:
        padding = os.urandom(8)
        new_hash = head_hash.copy() 
        new_hash.update(padding + tail)
        if b32encode(new_hash.digest()).startswith(prefix):
            new_data = head + padding + tail
            address = b32encode(new_hash.digest()).decode()[:52].lower()
            break

    q.put({"address": address, "data": new_data+data_tail})

def get_new_destination(sam_address):
    sam_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sam_socket.connect(sam_address)
    except ConnectionRefusedError:
        print("SAM API is unavailable. Make sure SAM is enabled on your I2P router.")
        exit()

    sam_socket.send(b"HELLO VERSION MIN=3.1 MAX=3.1\n")
    reply = sam_socket.recv(4096)
    if reply == b"HELLO REPLY RESULT=OK VERSION=3.1\n":
        sam_socket.send(b"DEST GENERATE SIGNATURE_TYPE=7\n")
        reply = sam_socket.recv(4096)
        dest = reply.split(b" ")[3][5:-1]
        sam_socket.close()
        return b64decode(dest, altchars="-~", validate=True)
    else:
        print(reply)
        exit()

def generate_address(prefix):
    prefix = prefix.upper().encode()

    data = get_new_destination(get_sam_address())

    processes = []
    q = Queue()
    for x in range(os.cpu_count()):
        p = Process(target=vain, args=(data, prefix, q))
        p.start()
        processes.append(p)

    new_key = q.get()
    for x in processes: x.terminate()

    return new_key

def main():
    if len(sys.argv) < 2:
        print("Usage: {} PREFIX [FILE]".format(sys.argv[0]))
        return

    prefix = sys.argv[1]

    if not re.match("^[a-zA-Z0-9]+$", prefix):
        print("Prefix must be alphanumeric string")
        return

    if len(sys.argv) == 3:
        outfile = sys.argv[2]
    else:
        outfile = "key.dat"

    new_key = generate_address(prefix)

    print(new_key["address"] + ".b32.i2p")
    print(b64encode(new_key["data"], altchars=b"-~").decode())

    if os.access(os.path.dirname(outfile) or ".", os.W_OK):
        with open(outfile, 'wb') as f: 
            f.write(new_key["data"])

        print("Key saved to -->", outfile)



if __name__ == "__main__":
    main()
