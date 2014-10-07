#!/usr/bin/env python

from ctypes import *
from e_types import *

_elib = CDLL("libe-hal.so")	#include <e-hal.h>

#################################
## Device communication functions
##
## Platform configuration
def e_init(hdf=None):
	if hdf == None:
		buff = 0
	else:
		buff = create_string_buffer(hdf) 
	return True if _elib.e_init(buff) == 0 else False

def e_get_platform_info(platform):
	return _elib.e_get_platform_info(byref(platform)

def e_finalize():
	return _elib.e_finalize()

## Epiphany access
def e_open(dev, row, col, rows,cols):
	print "TODO: Not implemented!"
	pass

def e_close(dev):
	pass

## External Memory Access
def e_alloc(mbuf, base, size):
	print "TODO: Not implemented!"
	pass

def e_free(mbuf):
	print "TODO: Not implemented!"
	pass

## Data Transfer
def e_read(dev, row, col, from_addr, buf, size):
	print "TODO: Not implemented!"
	pass

def e_write(dev, row, col, to_addr, buf, size):
	print "TODO: Not implemented!"
	pass


###########################
## System control functions

def     e_reset_system():
	print "TODO: Not implemented!"
	pass

e_reset = e_reset_system

def     e_reset_chip():
	print "TODO: Not implemented!"
	pass
def     e_reset_group(dev):
	print "TODO: Not implemented!"
	pass
def     e_start(dev, row, col):
	print "TODO: Not implemented!"
	pass
def     e_start_group(dev):
	print "TODO: Not implemented!"
	pass
def     e_signal(dev, row, col):
	print "TODO: Not implemented!"
	pass
def     e_halt(dev, row, col):
	print "TODO: Not implemented!"
	pass
def     e_resume(dev, row, col):
	print "TODO: Not implemented!"
	pass


####################
## Utility functions
def e_get_num_from_coords(dev, row, col):
	print "TODO: Not implemented!"
	pass
def e_get_coords_from_num(dev, corenum, row, col):
	print "TODO: Not implemented!"
	pass
##
def e_is_addr_on_chip(addr):
	print "TODO: Not implemented!"
	pass
def e_is_addr_on_group(dev, addr):
	print "TODO: Not implemented!"
	pass
##
def e_set_host_verbosity(verbose):
	print "TODO: Not implemented!"
	pass
