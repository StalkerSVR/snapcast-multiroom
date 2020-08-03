#!/usr/bin/python3
import asyncio
import snapcast.control
from time import sleep
#import mpd

client_conf = [
["speaker2",[["default",1,100],["default_Kitchen",1,60],["AirPlay",3,100],["Mopidy",5,100],["Plexamp",4,100],["uPnP",6,100],["Radio",7, 100]]],
["speaker1",[["default",1, 50],["default_Hall",1,60],["AirPlay",3,100],["Mopidy",5,100],["Plexamp",4,100],["uPnP",6,100],["Radio",7,100]]],
["kodi-2",  [["default",1, 50],["default_Room",1,60],["AirPlay",3,100],["Mopidy",5,100],["Plexamp",4,100],["uPnP",6,100],["Radio",7,100]]],
["kodi-1",  [["default",1, 50],["default_Zal",1,60],["AirPlay",2,100],["Mopidy",4,100],["Plexamp",3,100]]]]

def check_stream(server, stream_name):
  for stream in server.streams:
    if stream.name == stream_name:
      if stream.status == "playing":
        return (True)
  return(False)


def get_client_friendly_name(server, client_id):
  for client in server.clients:
    if client.identifier==client_id:
      return client.friendly_name
  return ""

def get_new_stream(server, group):
  new_stream=""
  new_stream_priority=9999
  for client in group.clients:
    for cfg in client_conf:
      if cfg[0]==get_client_friendly_name(server,client):
        for stream in cfg[1]:
          if check_stream(server,stream[0])==True:
             if stream[1]<new_stream_priority:
                new_stream_priority=stream[1]
                new_stream=stream[0]
  return(new_stream)

def update_streams():
  for group in server.groups:
    new_stream=get_new_stream(server,group)
    if (new_stream != group.stream) and (new_stream != ""):
      print("change "+ group.identifier+" from " + group.stream + " to " + new_stream)
      for gclient in group.clients:
        for sclient in server.clients:
          if sclient.identifier==gclient:
            for i in range(len(client_conf)):
              if client_conf[i][0]==gclient:
                for j in range(len(client_conf[i][1])):
                  if client_conf[i][1][j][0]==group.stream:
                    client_conf[i][1][j][2]=sclient.volume
      for client in group.clients:
        for cfg in client_conf:
          if cfg[0]==get_client_friendly_name(server,client):
            for stream in cfg[1]:
              if stream[0]==new_stream:
                print("Change volume for " + client)
                loop.run_until_complete(server.client_volume(client, {'percent': stream[2]}))
      loop.run_until_complete(server.group_stream(group.identifier,new_stream))

#for client in server.clients:
#  print(client.friendly_name)


# set volume for client #0 to 50%
#client = server.clients[0]
#loop.run_until_complete(server.client_volume(client.identifier, {'percent': 50, 'muted': False}))

try:
  loop = asyncio.get_event_loop()
  server = loop.run_until_complete(snapcast.control.create_server(loop, 'snapserver.local', reconnect=True))
  update_streams()
except:
  a=1
sleep(0.1)
