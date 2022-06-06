# Monopoly
__AUTHOR__ = "Adrian Jahraus"
__VERSION__ = "0.0.1"

from calendar import c
import socket
from unicodedata import name
import pygame as pg
import os
import threading
from threading import Thread

HOST = socket.gethostname()
IP = socket.gethostbyname(HOST)
PORT = 5050
FORMAT = "utf-8"
MAXPLAYERS = 4


class player:
    status = 0 # 0=none, 1=prison, 2=lost(0money)
    position = 0
    money = 1500
    owned_streets = []

    def __init__(self, name, conn):
        self.name = name
        self.conn = conn

    def checkmoney(self):
        if self.money <= 0:
            self.status = 2
            return False
        return True

    def edit_money(self, amount):
        self.money += amount
        if not self.checkmoney():
            
        



def sendall(conn, msg):
    try:
        conn.sendall(msg.encode(FORMAT))
        return True
    except:
        return False


def recv(conn):
    try:
        data = conn.recv(1024).decode(FORMAT)
        return data
    except:
        return None


def connection(conn, addr):
    try:
        while 1:
            with conn:
                if len(threading.enumerate()) > MAXPLAYERS:
                    print(f"[SERVER] Server is full disconnectingm {conn} {addr}")
                    sendall(conn, "Server is full")
                    return
                print(f"[SERVER] Connected {conn} {addr}")
                sendall(conn, "Connected")
                client_version = recv(conn)
                if client_version != __VERSION__:
                    print(f"[SERVER] Client version not matching\nDisconnecting {conn} {addr}")
                    return
                p_name = recv(conn)    
                p = player(p_name, conn)
    except Exception as e:
        print(e)


def main():
    pg.init()
    print(f"[STARTING SERVER] HOST: {HOST} {IP}")
    while 1:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((IP,PORT))
            s.listen()
            conn, addr = s.accept()


    


if __name__ == "__main__":
    main()
