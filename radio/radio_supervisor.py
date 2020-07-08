#!/usr/bin/python3
import mpd
import arrow
from time import sleep


playlist=[[0,0,'https://montecarlo.hostingradio.ru/montecarlo128.mp3'],[7,00,'http://icecast.vgtrk.cdnvideo.ru/rrzonam_mp3_128kbps'],[22,30,'https://montecarlo.hostingradio.ru/montecarlo128.mp3']]
vollist=[[0,0,15],[22,30,30],[23,00,25],[23,30,20],[8,0,35]]
#playlist=[[0,0,'https://stream.pcradio.ru/rmc_mcnights-med'],[7,00,'http://icecast.vgtrk.cdnvideo.ru/rrzonam_mp3_128kbps'],[22,10,'https://stream.pcradio.ru/rmc_mcnights-med']]
current=''

def get_needed():
  newitem=playlist[0]
  nowtime=arrow.now().floor('minute')
  for item in playlist:
    if nowtime.replace(hour=item[0], minute=item[1])<=nowtime:
       if nowtime.replace(hour=item[0], minute=item[1])> nowtime.replace(hour=newitem[0], minute=newitem[1]):
          newitem=item
  return(newitem[2])

def get_init_volume():
  newitem=vollist[0]
  nowtime=arrow.now().floor('minute')
  for item in vollist:
    if nowtime.replace(hour=item[0], minute=item[1])<=nowtime:
       if nowtime.replace(hour=item[0], minute=item[1])> nowtime.replace(hour=newitem[0], minute=newitem[1]):
          newitem=item
  return(newitem[2])

def get_needed_volume():
  newitem=vollist[0]
  nowtime=arrow.now().floor('minute')
  for item in vollist:
    if nowtime.replace(hour=item[0], minute=item[1]) == nowtime:
       vol=item[2]
       return(vol)
  return (999)


client = mpd.MPDClient(use_unicode=True)
print ("Connecting to mpd-radio:6600")
client.connect("mpd", 6600)
print ("Connected")
client.stop()
client.setvol(get_init_volume())

while True:
  needed=get_needed()
  vol=get_needed_volume()
  if current != needed or client.status()['state'] == 'stop':
#      client.clear()
      current=needed
      client.addid(current,0)
      print ("Restart playing: "+current)
      client.play(0)
      client.delete(1)
  if vol != 999 and vol != client.status()['volume']:
     client.setvol(vol) 
  sleep(0.1)
client.disconnect()

