#!/usr/bin/python3
import asyncio
import mpd
import arrow
from time import sleep
import snapcast.control

radio_stream = "Radio"
snapserver = "snapserver.local"

def check_stream(server, stream_name):
  for stream in server.streams:
    if stream.name == stream_name:
      if stream.status == "playing":
        return (True)
  return(False)

loop = asyncio.get_event_loop()
server = loop.run_until_complete(snapcast.control.create_server(loop, snapserver, reconnect=False))

if (check_stream(server,radio_stream)==False):
  client = mpd.MPDClient(use_unicode=True)
  print ("Connecting to mpd-radio:6600")
  client.connect("mpd", 6600)
  print ("Connected")
  if client.status()['state'] == "play":
    print ("Stopping")
    client.stop()
    client.clear()

  sleep(0.3)
  client.disconnect()


