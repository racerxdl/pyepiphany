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
	return True if _elib.e_init(buff) == E_TRUE else False

def e_get_platform_info():
	platform = e_platform_t()
	return platform if _elib.e_get_platform_info(byref(platform)) == E_TRUE else False

def e_finalize():
	return True if _elib.e_finalize() == E_TRUE else False

## Epiphany access
def e_open(dev, row, col, rows,cols):
	return True if _elib.e_open(byref(dev), row, col, rows, cols) == E_TRUE else False

def e_close(dev):
	return True if _elib.e_close(byref(dev)) == E_TRUE else False

## External Memory Access
def e_alloc(base, size):
	mbuf = e_mem_t()
	return mbuf if _elib.e_close(byref(mbuf), base, size) == E_TRUE else False

def e_free(mbuf):
	return True if _elib.e_free(byref(mbuf)) == E_TRUE else False

## Data Transfer
def e_read(dev, row, col, from_addr, buf, size):
	return True if _elib.e_read(byref(dev), row, col, from_addr, byref(buf), size) == E_TRUE else False

def e_write(dev, row, col, to_addr, buf, size):
	return True if _elib.e_write(byref(dev), row, col, to_addr, byref(buf), size) == E_TRUE else False

###########################
## System control functions

def e_reset_system():
	return True if _elib.e_reset_system() else False

e_reset = e_reset_system

def e_reset_chip():
	return True if _elib.e_reset_chip() else False

def e_reset_group(dev):
	return True if _elib.e_reset_group(byref(dev)) else False

def e_start(dev, row, col):
	return True if _elib.e_start(byref(dev), row, col) else False

def e_start_group(dev):
	return True if _elib.e_start_group(byref(deb)) else False

def e_signal(dev, row, col):
	return True if _elib.e_signal(byref(dev), row, col) else False

def e_halt(dev, row, col):
	return True if _elib.e_halt(byref(dev), row, col) else False

def e_resume(dev, row, col):
	return True if _elib.e_resume(byref(dev), row, col) else False


####################
## Utility functions
def e_get_num_from_coords(dev, row, col):
	return True if _elib.e_get_num_from_coords(byref(dev), row, col) else False

def e_get_coords_from_num(dev, corenum):
	row = c_int()
	col = c_int()
	return (row.value,col.value) if _elib.e_get_coords_from_num(byref(dev), corenum, byref(row), byref(col)) else False

def e_is_addr_on_chip(addr):
	return True if _elib.e_is_addr_on_chip(addr) else False

def e_is_addr_on_group(dev, addr):
	return True if _elib.e_is_addr_on_group(byref(dev), addr) else False


def e_set_host_verbosity(verbose):
	return _elib.e_set_host_verbosity(verbose)

####################
## e-Loader

def e_load(executable, dev, row, col, start):
	execs = create_string_buffer(executable)
	return True if _elib.e_load(byref(execs), byref(dev), row, col, start) else False

def e_load_group(executable, dev, row, col, rows, cols, start):
	execs = create_string_buffer(executable)
	return True if _elib.e_load_group(byref(execs), byref(dev), row, col, rows, cols, start) else False

def e_set_loader_verbosity(verbose):
	return _elib.e_set_loader_verbosity(verbose)