#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ctypes import *
from e_types import *

_elib = CDLL("libe-hal.so")	#include <e-hal.h>

#################################
## Device communication functions
##
## Platform configuration
def e_init(hdf=None):
	'''
	Description
		This function initializes the HAL data structures, and establishes a connection to the Epiphany 
		platform. The platform parameters are read form a Hardware Description File (HDF), whose 
		path is given at the function argument. 
		 
		If the hdf parameter is a None, then the file location is read from the EPIPHANY_HDF 
		environment variable. This variable is normally set on your system startup file (~/.bashrc in 
		Linux), and reflects the structure of the underlying Epiphany platform. For example: 
		 
		EPIPHANY_HDF=”${EPIPHANY_HOME}/bsps/parallella/parallella.xml” 

		If the EPIPHANY_HDF variable is not set, then the function will try to locate the platform.hdf 
		file located in the current BSP directory. 
		 
	Return value 
		If successful, the function returns True. On a failure it returns False. 
	'''
	if hdf == None:
		buff = 0
	else:
		buff = create_string_buffer(hdf) 
	return True if _elib.e_init(buff) == E_OK else False

def e_get_platform_info():
	'''
	Description 
		The Epiphany platform information is stored internally in an e_platform_t type object. It 
		contains the data on the various chips, external memory segments and geometry comprising the 
		system. Some of this data can be retrieved through this function. 
		 
	Return value 
		If successful, the function returns e_platform_t object. On a failure it returns False.
	'''
	platform = e_platform_t()
	return platform if _elib.e_get_platform_info(byref(platform)) == E_OK else False

def e_finalize():
	'''
	Description 
		Use this function to finalize the connection with the Epiphany system. Some resources that were 
		allocated in the e_init() call are released here. 
		 
	Return value 
		If successful, the function returns True. On a failure it returns False. 
	'''
	return True if _elib.e_finalize() == E_OK else False

## Epiphany access
def e_open(row, col, rows, cols):
	'''
	Description 
		This function defines an eCore workgroup. The workgroup is defined in terms of the coordintaes 
		relative to the platform’s effective chip area. The arguments row and col define the place of the 
		group’s origin eCore. The origin is set relative to the Epiphany platform’s origin, defined in the 
		e_init() call. The arguments rows and cols give the group’s size, defining the work 
		rectangle. A work group can be as amall as a single core or as large as the whole available 
		effective chip area. The core group data is saved in the provided e_epiphany_t type object 
		dev. 
		 
		Subsequent accesses to the core group (e.g., for read and write of data) are done using a 
		reference to the dev object. 
		 
	Return value 
		If successful, the function returns e_epiphany_t object. On a failure it returns False.
	'''
	dev = e_epiphany_t()
	return dev if _elib.e_open(byref(dev), row, col, rows, cols) == E_OK else False

def e_close(dev):
	'''
	Description 
		The function closes the eCore workgroup. The resources allocated by the e_open() call are 
		released here. Use this function before re-allocating an eCore to a new workgroup. 
		 
	Return value 
		If successful, the function returns True. On a failure it returns False. 
	'''
	return True if _elib.e_close(byref(dev)) == E_OK else False

## External Memory Access
def e_alloc(base, size):
	'''
	Description 
		This function defines a buffer in external memory. The buffer is defined in terms of the relative 
		from the beginning of the external memory segment, defined in the e_init() call. The 
		argument base defines the offset, starting at 0. The argument and size gives the buffer’s size. 
		The external memory buffer data is saved in the provided e_mem_t type object mbuf. 
		 
		Subsequent accesses to the buffer (e.g., for read and write of data) are done using a reference to 
		the mbuf object. 
		 
	Return value 
		If successful, the function returns e_mem_t object. On a failure it returns False. 
	'''
	mbuf = e_mem_t()
	return mbuf if _elib.e_alloc(byref(mbuf), base, size) == E_OK else False

def e_free(mbuf):
	'''
	Description 
		This function defines a buffer in external memory. The buffer is defined in terms of the relative 
		from the beginning of the external memory segment, defined in the e_init() call. The 
		argument base defines the offset, starting at 0. The argument and size gives the buffer’s size. 
		The external memory buffer data is saved in the provided e_mem_t type object mbuf. 
		 
		Subsequent accesses to the buffer (e.g., for read and write of data) are done using a reference to 
		the mbuf object. 
		 
	Return value 
		If successful, the function returns True. On a failure it returns False. 
	'''
	return True if _elib.e_free(byref(mbuf)) == E_OK else False

## Data Transfer
def e_read(dev, row, col, from_addr, size):
	'''
	Description 
		This function reads data of length size from a workgroup core or an external memory buffer to 
		the local byte buffer buf. The argument dev specifies the target from which to read the data. It 
		can be of either types e_epiphany_t or e_mem_t. 
		 
		If an object of type e_epiphany_t is given, then the row and col arguments specify the 
		relative target eCore coordinates in the workgroup. 
		 
		If an object of type e_mem_t is given, then the row and col arguments are ignored. 
		 
		In both cases, the from_addr parameter specifies the write offset relative to the buffer’s start, or 
		to the eCore’s internal space. 
		 
		To access system registers, the to_addr parameter can be one of the register symbols of the 
		types e_gp_reg_id_t, e_core_reg_id_t, e_chip_reg_id_t, e_sys_reg_id_t. 
		 
	Return value 
		If successful, the function returns the string buffer. On a failure it returns False. 
	'''
	data = create_string_buffer(size)
	bytes = _elib.e_read(byref(dev), row, col, from_addr, byref(data), size)
	return data if bytes == size else False

def e_write(dev, row, col, to_addr, buf, size):
	'''
	Description 
		This function writes data of length size from the local byte buffer buf to a workgroup core or 
		an external memory buffer. The argument dev specifies the target on which to write the data. It 
		can be of either types e_epiphany_t or e_mem_t. 
		 
		If an object of type e_epiphany_t is given, then the row and col arguments specify the 
		relative target eCore coordinates in the workgroup. 
		 
		If an object of type e_mem_t is given, then the row and col arguments are ignored. 
		 
		In both cases, the to_addr parameter specifies the write offset relative to the buffer’s start, or to 
		the eCore’s internal space. 
		 
		To access system registers, the to_addr parameter can be one of the register symbols of the 
		types e_gp_reg_id_t, e_core_reg_id_t, e_chip_reg_id_t, e_sys_reg_id_t. 
		 
	Return value 
		If successful, the function returns True. On a failure it returns False
	'''
	bytes = _elib.e_write(byref(dev), row, col, to_addr, byref(buf), size)
	return bytes == size

###########################
## System control functions

def e_reset_system():
	'''
	Description 
		Use this function to perform a full hardware reset of the Epiphany platform, including the 
		Epiphany chips and the FPGA glue logic. 
		 
		Special care must be taken when using this function in a multiprocessing environment not to 
		disrupt working tasks, possibly launched by other applications. 
		 
	Return value 
		If successful, the function returns True. On a failure it returns False. 
	'''
	return True if _elib.e_reset_system() == E_OK else False

e_reset = e_reset_system

def e_reset_chip():
	'''
		TODO: Missing on oficial SDK reference
	'''
	return True if _elib.e_reset_chip() == E_OK else False

def e_reset_group(dev):
	'''
	Description 
		Use this function to perform a soft reset of a workgroup. 
		 
		Special care must be taken when using this function, as resetting the eCore when memory 
		transactions, that were generated with a core read instruction from the global memory space 
		(either LDR instruction or an instruction fetch from outside of the core) are not concluded can 
		bring the system to an undefined state. 
		 
	Return value 
		If successful, the function returns True. On a failure it returns False
	'''
	return True if _elib.e_reset_group(byref(dev)) == E_OK else False

def e_start(dev, row, col):
	'''
	Description 
		This function writes the SYNC signal to the workgroup core’s ILAT register. It causes the core to 
		jump to the IVT entry #0. Normally, this will be used after loading a program on the core. 
		 
		The row and col parameters specify the target eCore coordinates, relative to the workgroup 
		given by the dev argument. 
		 
	Return value 
		If successful, the function returns True. On a failure it returns False. 
	'''
	return True if _elib.e_start(byref(dev), row, col) == E_OK else False

def e_start_group(dev):
	'''
	Description 
		This function writes the SYNC signal to the workgroup cores’ ILAT registers. It causes the 
		workgroup cores to jump to their IVT entry #0. Normally, this will be used after loading a 
		program on the core. 
		 
	Return value 
		If successful, the function returns True. On a failure it returns False. 
	'''
	return True if _elib.e_start_group(byref(deb)) == E_OK else False

def e_signal(dev, row, col):
	'''
	Description 
		This function writes the USER_INT (soft interrupt) signal to the workgroup core’s ILAT register. 
		It causes the core to jump to the IVT entry #9. 
		 
		The row and col parameters specify the target eCore coordinates, relative to the workgroup 
		given by the dev argument. 
		 
	Return value 
		If successful, the function returns True. On a failure it returns False. 
	'''
	return True if _elib.e_signal(byref(dev), row, col) == E_OK else False

def e_halt(dev, row, col):
	'''
	Description 
		This function halts the workgroup core’s program execution. It may be useful for debug 
		purposes. 
		 
		The row and col parameters specify the target eCore coordinates, relative to the workgroup 
		specified by the dev argument. 
		 
	Return value 
		If successful, the function returns True. On a failure it returns False
	'''
	return True if _elib.e_halt(byref(dev), row, col) == E_OK else False

def e_resume(dev, row, col):
	'''
	Description 
		This function resumes a workgroup core’s program execution that was previously stopped with a 
		call to e_halt(). 
		 
		The row and col parameters specify the target eCore coordinates, relative to the workgroup 
		specified by the dev argument. 
		 
	Return value 
		If successful, the function returns True. On a failure it returns False. 
	'''
	return True if _elib.e_resume(byref(dev), row, col) == E_OK else False


####################
## Utility functions
def e_get_num_from_coords(dev, row, col):
	'''
	Description 
		Convert a workgroup’s eCore coordinates to a core number. The workgroup is defined by the 
		dev argument. The core numbering is done in a “raster scan” manner, starting at the groups 
		origin as core #0 and continuing row-wise. Thus, the number of the first core in the second row 
		equals to the group’s cols parameter, and the last core in the third row equals to (3*cols-1). 
		The last core in the group is numbered (rows*cols-1). 
		 
	Return value 
		The function returns the selected core’s number. 
	'''
	return _elib.e_get_num_from_coords(byref(dev), row, col)

def e_get_coords_from_num(dev, corenum):
	'''
	Description 
		Convert a workgroup’s eCore number to core’s coordinates, relative to the group origin. The 
		workgroup is defined by the dev argument. The core numbering is done in a raster scan manner, 
		starting at the groups origin as core #0 and continuing column-wise. Thus, the (row, col) 
		coordinates of the core #0 are (0,0), core #cols coordinates are (1,0), and core #(3*cols-
		1) coordinates are (2,cols-1). The last core in the group, numbered (rows*cols-1), has 
		coordinates (rows-1,cols-1). 
	 
	Return value 
		The function returns the selected core’s coordinates as tuple (row, col)
	'''
	row = c_int()
	col = c_int()
	return (row.value,col.value) if _elib.e_get_coords_from_num(byref(dev), corenum, byref(row), byref(col)) == E_OK else False

def e_is_addr_on_chip(addr):
	'''
	Description 
		This function checks whether a global, 32-bit address, given by argument addr, is within a 
		physical Epiphany chip’s space. 
	 
	Return value 
		The function returns True if an address is on a chip and False otherwise
	'''
	return True if _elib.e_is_addr_on_chip(addr) == E_OK else False

def e_is_addr_on_group(dev, addr):
	'''
	Description 
		This function checks whether a global, 32-bit address, given by argument addr, is within a core 
		workgroup’s space. The workgroup is specified by the dev argument. 
		 
	Return value 
		The function returns True if an address is on a workgroup and False otherwise. 
	'''
	return True if _elib.e_is_addr_on_group(byref(dev), addr) == E_OK else False


def e_set_host_verbosity(verbose):
	'''
	Description 
		This function sets the verbosity level of the eHAL function calls. The levels defined from H_D0 
		to H_D4. Level H_D0 means no diagnostics are emitted, and any higher level designates more 
		detailed diagnostics. This function is meant for diagnostics and debug purposes. 
		 
	Return value 
		The function returns the old diagnostics level value. 
	'''
	return _elib.e_set_host_verbosity(verbose)

####################
## e-Loader

def e_load(executable, dev, row, col, start):
	'''
	Description 
		This function loads an Epiphany program onto a workgroup core. The executable string 
		specifies the path to the program’s image. The target core workgroup is specified by the dev 
		argument. The target core is specified by the row and col coordinates, relative to the 
		workgroup. 
		 
		Optionally, a loaded program can be started immediately after loading, according to the start 
		parameter. When the start parameter is e_true, the program is launched after load. If it is 
		e_false, the program is not launched. 
		 
		Program load should be performed only when the core is in an idle or halt state. A safe way to 
		achieve this is to use the e_reset_system() or e_reset_core() API’s before the load. 
		 
	Return value 
		If successful, the function returns True. On a failure it returns False. 
	'''
	execs = create_string_buffer(executable)
	return True if _elib.e_load(byref(execs), byref(dev), row, col, start) == E_OK else False

def e_load_group(executable, dev, row, col, rows, cols, start):
	'''
	Description 
		This function loads an Epiphany program onto a subgroup of a workgroup. The executable 
		string specifies the path to the program’s image. The target workgroup is specified by the dev 
		argument. The target cores subgroup for loading the image is specified by the row and col 
		coordinates, relative to the workgroup origin. The rows and cols parameters specify the size of 
		the subgroups. All cores in the subgroup are loaded with the same program image. 
		 
		Optionally, the loaded programs can be started immediately after loading on all cores in the 
		subgroup, according to the start parameter. When the start parameter is e_true, the 
		programs are launched after load. If it is e_false, the programs are not launched. 
		 
		Program load should be performed only when the core is in an idle or halt state. A safe way to 
		achieve this is to use the e_reset_system() or e_reset_core() API’s before the load. 
		 
	Return value 
		If successful, the function returns True. The SREC parser ignores the errors and 
		continues the program load. 
	'''
	execs = create_string_buffer(executable)
	ret = _elib.e_load_group(byref(execs), byref(dev), row, col, rows, cols, start)
	if ret == E_WARN:
		print "e_load_group returned E_WARN!"
	return True if ret == E_OK or ret == E_WARN else False

def e_set_loader_verbosity(verbose):
	'''
	Description 
		This function sets the verbosity level of the program loader function calls, on top of the other 
		eHAL calls diagnostics.. The levels defined from L_D0 to L_D4. Level L_D0 means no 
		diagnostics are emitted, and any higher level designates more detailed diagnostics. This function 
		is meant for diagnostics and debug purposes. 
		 
	Return value 
		The function returns the old diagnostics level value. 
	'''
	return _elib.e_set_loader_verbosity(verbose)