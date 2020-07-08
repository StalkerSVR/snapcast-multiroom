#!/usr/bin/python3
import asyncio
import snapcast.control
from time import sleep

def check_muted(client_name):
  for client in server.clients:
    if client.identifier==client_name:
       return client.muted

def unmute_streams():
  for group in server.groups:
#    if group.stream==stream_name:
      for client in group.clients:
         if check_muted(client):
           print("Unmute " + client)
           loop.run_until_complete(server.client_volume(client, {'muted': False}))


loop = asyncio.get_event_loop()
server = loop.run_until_complete(snapcast.control.create_server(loop, 'snapserver.local', reconnect=False))

unmute_streams()

