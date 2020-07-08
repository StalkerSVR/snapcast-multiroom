#!/usr/bin/python3
import asyncio
import snapcast.control
from time import sleep

client_conf = [
["speaker1",[["Radio",6,16]]],
["speaker2",[["Radio",6,24]]],
["kodi-2",[["Radio",6,16]]]
]


def get_client_friendly_name(server, client_id):
  for client in server.clients:
    if client.identifier==client_id:
      return client.friendly_name
  return ""

def get_volume(client, group):
  for cfg in client_conf:
    if cfg[0]==get_client_friendly_name(server,client):
      for stream in cfg[1]:
        if stream[0]==group:
           return(stream[2])
  return(None)



def check_muted(client_name):
  for client in server.clients:
    if client.identifier==client_name:
       return client.muted

def set_low_volume(stream_name):
  for group in server.groups:
    if group.stream==stream_name:
      for client in group.clients:
         if check_muted(client)==False:
           volume=get_volume(client,stream_name)
           print("Set volume for " + client + " to " + str(int(volume/2.5)))
#           loop.run_until_complete(server.client_volume(client, {'muted': True}))
           loop.run_until_complete(server.client_volume(client, {'percent': int(volume/3.5)}))

def set_def_volume(stream_name):
  for group in server.groups:
    if group.stream==stream_name:
      for client in group.clients:
         if check_muted(client)==False:
           volume=get_volume(client,stream_name)
           print("Set volume for " + client + " to " + str(volume))
#           loop.run_until_complete(server.client_volume(client, {'muted': True}))
           loop.run_until_complete(server.client_volume(client, {'percent': volume}))


loop = asyncio.get_event_loop()
server = loop.run_until_complete(snapcast.control.create_server(loop, 'snapserver.local', reconnect=False))

set_low_volume("Radio")

