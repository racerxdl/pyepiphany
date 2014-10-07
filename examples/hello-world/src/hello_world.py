#!/usr/bin/env python

'''
  This is based on hello world example of Yaniv Sapir <yaniv@adapteva.com>
  Contributed by Lucas Teske <lucas@teske.net.br>
'''

from pyepiphany.e_hal import *
import random
from time import sleep

_BufSize    =   128
_BufOffset  =   0x01000000
_SeqLen     =   20

e_init()
e_reset_system()
platform = e_get_platform_info()

if platform == False:
  print "Error getting plataform info!"
  exit(1)

emem = e_alloc(_BufOffset, _BufSize)
random.seed(1)  

for i in range(_SeqLen):
  # Draw a random core
  row = random.randint(0, platform.rows-1)
  col = random.randint(0, platform.cols-1)
  coreid = (row + platform.row) * 64 + col + platform.col

  # Open the single-core workgroup and reset the core, in
  # case a previous process is running. Note that we used
  # core coordinates relative to the workgroup.
  dev = e_open(row, col, 1, 1)
  e_reset_group(dev)

  # Load the device program onto the selected eCore
  # and launch after loading.
  e_load("e_hello_world.srec", dev, 0, 0, E_TRUE)

  # Wait for core program execution to finish, then
  # read message from shared buffer.
  sleep(0.01);
  emsg = e_read(emem, 0, 0, 0x0, _BufSize);

  # Print the message and close the workgroup.
  print "{:3d}: Message from eCore 0x{:03x} ({:2d},{:2d}): {:s}".format(i, coreid, row, col, str(emsg.raw))
  e_close(dev)

# Release the allocated buffer and finalize the
# e-platform connection.
e_free(emem)
e_finalize()

