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

'''

///////////////////////////
// System control functions
#define e_reset e_reset_system
int     e_reset_system();
int     e_reset_chip();
int     e_reset_group(e_epiphany_t *dev);
int     e_start(e_epiphany_t *dev, unsigned row, unsigned col);
int     e_start_group(e_epiphany_t *dev);
int     e_signal(e_epiphany_t *dev, unsigned row, unsigned col);
int     e_halt(e_epiphany_t *dev, unsigned row, unsigned col);
int     e_resume(e_epiphany_t *dev, unsigned row, unsigned col);


////////////////////
// Utility functions
unsigned e_get_num_from_coords(e_epiphany_t *dev, unsigned row, unsigned col);
void     e_get_coords_from_num(e_epiphany_t *dev, unsigned corenum, unsigned *row, unsigned *col);
//
e_bool_t e_is_addr_on_chip(void *addr);
e_bool_t e_is_addr_on_group(e_epiphany_t *dev, void *addr);
//
e_hal_diag_t e_set_host_verbosity(e_hal_diag_t verbose);
'''