#!/usr/bin/env python

from ctypes import *

_elib = CDLL("libe-hal.so")	#include <e-hal.h>

def e_init(hdf=None):
	if hdf == None:
		buff = 0
	else:
		buff = create_string_buffer(hdf) 
	return True if _elib.e_init(buff) == 0 else False

'''

/////////////////////////////////
// Device communication functions
//
// Platform configuration
int     e_init(char *hdf);
int     e_get_platform_info(e_platform_t *platform);
int     e_finalize();
// Epiphany access
int     e_open(e_epiphany_t *dev, unsigned row, unsigned col, unsigned rows, unsigned cols);
int     e_close(e_epiphany_t *dev);
// External memory access
int     e_alloc(e_mem_t *mbuf, off_t base, size_t size);
int     e_free(e_mem_t *mbuf);
//
// Data transfer
ssize_t e_read(void *dev, unsigned row, unsigned col, off_t from_addr, void *buf, size_t size);
ssize_t e_write(void *dev, unsigned row, unsigned col, off_t to_addr, const void *buf, size_t size);


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