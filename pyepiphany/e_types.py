#!/usr/bin/env python

from ctypes import *

'''
	Most of these is got from epiphany-hal-data.h and epiphany-hal-data-local.h
'''

#	e_bool_t enum
E_FALSE 				= 	False
E_TRUE 					= 	True 


#	e_hal_diag_t enum
H_D0 					= 	0
H_D1 					= 	1
H_D2 					= 	2
H_D3 					= 	3
H_D4 					= 	4

#	e_return_stat_t enum
E_OK   					=  	0
E_ERR  					= 	-1
E_WARN 					= 	-2

#	e_gp_reg_id_t enum
E_CORE_GP_REG_BASE     = 0xf0000
E_REG_R0               = E_CORE_GP_REG_BASE + 0x0000
E_REG_R1               = E_CORE_GP_REG_BASE + 0x0004
E_REG_R2               = E_CORE_GP_REG_BASE + 0x0008
E_REG_R3               = E_CORE_GP_REG_BASE + 0x000c
E_REG_R4               = E_CORE_GP_REG_BASE + 0x0010
E_REG_R5               = E_CORE_GP_REG_BASE + 0x0014
E_REG_R6               = E_CORE_GP_REG_BASE + 0x0018
E_REG_R7               = E_CORE_GP_REG_BASE + 0x001c
E_REG_R8               = E_CORE_GP_REG_BASE + 0x0020
E_REG_R9               = E_CORE_GP_REG_BASE + 0x0024
E_REG_R10              = E_CORE_GP_REG_BASE + 0x0028
E_REG_R11              = E_CORE_GP_REG_BASE + 0x002c
E_REG_R12              = E_CORE_GP_REG_BASE + 0x0030
E_REG_R13              = E_CORE_GP_REG_BASE + 0x0034
E_REG_R14              = E_CORE_GP_REG_BASE + 0x0038
E_REG_R15              = E_CORE_GP_REG_BASE + 0x003c
E_REG_R16              = E_CORE_GP_REG_BASE + 0x0040
E_REG_R17              = E_CORE_GP_REG_BASE + 0x0044
E_REG_R18              = E_CORE_GP_REG_BASE + 0x0048
E_REG_R19              = E_CORE_GP_REG_BASE + 0x004c
E_REG_R20              = E_CORE_GP_REG_BASE + 0x0050
E_REG_R21              = E_CORE_GP_REG_BASE + 0x0054
E_REG_R22              = E_CORE_GP_REG_BASE + 0x0058
E_REG_R23              = E_CORE_GP_REG_BASE + 0x005c
E_REG_R24              = E_CORE_GP_REG_BASE + 0x0060
E_REG_R25              = E_CORE_GP_REG_BASE + 0x0064
E_REG_R26              = E_CORE_GP_REG_BASE + 0x0068
E_REG_R27              = E_CORE_GP_REG_BASE + 0x006c
E_REG_R28              = E_CORE_GP_REG_BASE + 0x0070
E_REG_R29              = E_CORE_GP_REG_BASE + 0x0074
E_REG_R30              = E_CORE_GP_REG_BASE + 0x0078
E_REG_R31              = E_CORE_GP_REG_BASE + 0x007c
E_REG_R32              = E_CORE_GP_REG_BASE + 0x0080
E_REG_R33              = E_CORE_GP_REG_BASE + 0x0084
E_REG_R34              = E_CORE_GP_REG_BASE + 0x0088
E_REG_R35              = E_CORE_GP_REG_BASE + 0x008c
E_REG_R36              = E_CORE_GP_REG_BASE + 0x0090
E_REG_R37              = E_CORE_GP_REG_BASE + 0x0094
E_REG_R38              = E_CORE_GP_REG_BASE + 0x0098
E_REG_R39              = E_CORE_GP_REG_BASE + 0x009c
E_REG_R40              = E_CORE_GP_REG_BASE + 0x00a0
E_REG_R41              = E_CORE_GP_REG_BASE + 0x00a4
E_REG_R42              = E_CORE_GP_REG_BASE + 0x00a8
E_REG_R43              = E_CORE_GP_REG_BASE + 0x00ac
E_REG_R44              = E_CORE_GP_REG_BASE + 0x00b0
E_REG_R45              = E_CORE_GP_REG_BASE + 0x00b4
E_REG_R46              = E_CORE_GP_REG_BASE + 0x00b8
E_REG_R47              = E_CORE_GP_REG_BASE + 0x00bc
E_REG_R48              = E_CORE_GP_REG_BASE + 0x00c0
E_REG_R49              = E_CORE_GP_REG_BASE + 0x00c4
E_REG_R50              = E_CORE_GP_REG_BASE + 0x00c8
E_REG_R51              = E_CORE_GP_REG_BASE + 0x00cc
E_REG_R52              = E_CORE_GP_REG_BASE + 0x00d0
E_REG_R53              = E_CORE_GP_REG_BASE + 0x00d4
E_REG_R54              = E_CORE_GP_REG_BASE + 0x00d8
E_REG_R55              = E_CORE_GP_REG_BASE + 0x00dc
E_REG_R56              = E_CORE_GP_REG_BASE + 0x00e0
E_REG_R57              = E_CORE_GP_REG_BASE + 0x00e4
E_REG_R58              = E_CORE_GP_REG_BASE + 0x00e8
E_REG_R59              = E_CORE_GP_REG_BASE + 0x00ec
E_REG_R60              = E_CORE_GP_REG_BASE + 0x00f0
E_REG_R61              = E_CORE_GP_REG_BASE + 0x00f4
E_REG_R62              = E_CORE_GP_REG_BASE + 0x00f8
E_REG_R63              = E_CORE_GP_REG_BASE + 0x00fc

#	e_core_reg_id_t enum
E_CORE_SP_REG_BASE     = 0xf0000
# Control registers
E_REG_CONFIG           = E_CORE_SP_REG_BASE + 0x0400
E_REG_STATUS           = E_CORE_SP_REG_BASE + 0x0404
E_REG_PC               = E_CORE_SP_REG_BASE + 0x0408
E_REG_DEBUGSTATUS      = E_CORE_SP_REG_BASE + 0x040c
E_REG_LC               = E_CORE_SP_REG_BASE + 0x0414
E_REG_LS               = E_CORE_SP_REG_BASE + 0x0418
E_REG_LE               = E_CORE_SP_REG_BASE + 0x041c
E_REG_IRET             = E_CORE_SP_REG_BASE + 0x0420
E_REG_IMASK            = E_CORE_SP_REG_BASE + 0x0424
E_REG_ILAT             = E_CORE_SP_REG_BASE + 0x0428
E_REG_ILATST           = E_CORE_SP_REG_BASE + 0x042C
E_REG_ILATCL           = E_CORE_SP_REG_BASE + 0x0430
E_REG_IPEND            = E_CORE_SP_REG_BASE + 0x0434
E_REG_CTIMER0          = E_CORE_SP_REG_BASE + 0x0438
E_REG_CTIMER1          = E_CORE_SP_REG_BASE + 0x043C
E_REG_FSTATUS          = E_CORE_SP_REG_BASE + 0x0440
E_REG_DEBUGCMD         = E_CORE_SP_REG_BASE + 0x0448

# DMA Registers
E_REG_DMA0CONFIG       = E_CORE_SP_REG_BASE + 0x0500
E_REG_DMA0STRIDE       = E_CORE_SP_REG_BASE + 0x0504
E_REG_DMA0COUNT        = E_CORE_SP_REG_BASE + 0x0508
E_REG_DMA0SRCADDR      = E_CORE_SP_REG_BASE + 0x050C
E_REG_DMA0DSTADDR      = E_CORE_SP_REG_BASE + 0x0510
E_REG_DMA0AUTODMA0     = E_CORE_SP_REG_BASE + 0x0514
E_REG_DMA0AUTODMA1     = E_CORE_SP_REG_BASE + 0x0518
E_REG_DMA0STATUS       = E_CORE_SP_REG_BASE + 0x051C
E_REG_DMA1CONFIG       = E_CORE_SP_REG_BASE + 0x0520
E_REG_DMA1STRIDE       = E_CORE_SP_REG_BASE + 0x0524
E_REG_DMA1COUNT        = E_CORE_SP_REG_BASE + 0x0528
E_REG_DMA1SRCADDR      = E_CORE_SP_REG_BASE + 0x052C
E_REG_DMA1DSTADDR      = E_CORE_SP_REG_BASE + 0x0530
E_REG_DMA1AUTODMA0     = E_CORE_SP_REG_BASE + 0x0534
E_REG_DMA1AUTODMA1     = E_CORE_SP_REG_BASE + 0x0538
E_REG_DMA1STATUS       = E_CORE_SP_REG_BASE + 0x053C

# Memory Protection Registers
E_REG_MEMPROTECT       = E_CORE_SP_REG_BASE + 0x0608

# Node Registers
E_REG_MESHCFG          = E_CORE_SP_REG_BASE + 0x0700
E_REG_COREID           = E_CORE_SP_REG_BASE + 0x0704
E_REG_CORE_RESET       = E_CORE_SP_REG_BASE + 0x070c

# Chip registers enum ( e_chips_regs_t)
E_CHIP_REG_BASE        = 0xf0000
E_REG_IO_LINK_MODE_CFG = E_CHIP_REG_BASE + 0x0300
E_REG_IO_LINK_TX_CFG   = E_CHIP_REG_BASE + 0x0304
E_REG_IO_LINK_RX_CFG   = E_CHIP_REG_BASE + 0x0308
E_REG_IO_GPIO_CFG      = E_CHIP_REG_BASE + 0x030c
E_REG_IO_FLAG_CFG      = E_CHIP_REG_BASE + 0x0318
E_REG_IO_SYNC_CFG      = E_CHIP_REG_BASE + 0x031c
E_REG_IO_HALT_CFG      = E_CHIP_REG_BASE + 0x0320
E_REG_IO_RESET         = E_CHIP_REG_BASE + 0x0324
E_REG_IO_LINK_DEBUG    = E_CHIP_REG_BASE + 0x0328


# Epiphany system registers enum ( e_sys_reg_id_t )
E_SYS_REG_BASE  = 0x00000000
E_SYS_CONFIG    = E_SYS_REG_BASE + 0x0000
E_SYS_RESET     = E_SYS_REG_BASE + 0x0004
E_SYS_VERSION   = E_SYS_REG_BASE + 0x0008
E_SYS_FILTERL   = E_SYS_REG_BASE + 0x000c
E_SYS_FILTERH   = E_SYS_REG_BASE + 0x0010
E_SYS_FILTERC   = E_SYS_REG_BASE + 0x0014

#	e_signal_t enum
E_SYNC     = 0
E_USER_INT = 9

# 	e_memtype_t enum
E_RD   = 1
E_WR   = 2
E_RDWR = 3

#	e_objtype_t enum

E_NULL         = 0
E_EPI_PLATFORM = 1
E_EPI_CHIP     = 2
E_EPI_GROUP    = 3
E_EPI_CORE     = 4
E_EXT_MEM      = 5
E_MAPPING      = 6


#	e_chiptype_t enum
E_E16G301 = 0
E_E64G401 = 1


#	e_platformtype_t enum
E_GENERIC        = 0
E_EMEK301        = 1
E_EMEK401        = 2
E_ZEDBOARD1601   = 3
E_ZEDBOARD6401   = 4
E_PARALLELLA1601 = 5
E_PARALLELLA6401 = 6

SIZEOF_IVT = 0x28

#	e_loader_diag_t enum
L_D0 = 0
L_D1 = 1
L_D2 = 2
L_D3 = 3
L_D4 = 40


class e_mem_t(Structure):
	'''
		e_objtype_t      objtype;     // object type identifier
		off_t            phy_base;    // physical global base address of external memory buffer as seen by host side
		off_t            page_base;   // physical base address of memory page
		off_t            page_offset; // offset of memory region base to memory page base
		size_t           map_size;    // size of eDRAM allocated buffer for host side
		off_t            ephy_base;   // physical global base address of external memory buffer as seen by device side
		size_t           emap_size;   // size of eDRAM allocated buffer for device side
		void            *mapped_base; // for mmap
		void            *base;        // application (virtual) space base address of external memory buffer
		int              memfd;       // for mmap
	'''
	_fields_ 	= 	[	("objtype"		, 	c_int),
						("phy_base"		, 	c_int),
						("page_base"	, 	c_int),
						("page_offset"	,	c_int),
						("map_size"		,	c_int),
						("ephy_base"	,	c_int),
						("emap_size"	,	c_int),
						("mapped_base"	,	c_void_p),
						("base"			,	c_void_p),
						("memfd"		,	c_int)
					]	


class e_mmap_t(Structure):
	'''
	typedef struct {
		e_objtype_t      objtype;     // object type identifier
		off_t            phy_base;    // physical global base address of memory region
		off_t            page_base;   // physical base address of memory page
		off_t            page_offset; // offset of memory region base to memory page base
		size_t           map_size;    // size of mapped region
		void            *mapped_base; // for mmap
		void            *base;        // application space base address of memory region
	} e_mmap_t;
	'''
	_fields_ 	= 	[	("objtype"		, 	c_int),
						("phy_base"		, 	c_int),
						("page_base"	, 	c_int),
						("page_offset"	,	c_int),
						("map_size"		,	c_int),
						("mapped_base"	,	c_void_p),
						("base"			,	c_void_p)
					]	

class e_core_t(Structure):
	'''
	typedef struct {
		e_objtype_t      objtype;     // object type identifier
		unsigned int     id;          // core ID
		unsigned int     row;         // core absolute row number
		unsigned int     col;         // core absolute col number
		e_mmap_t         mems;        // core's SRAM data structure
		e_mmap_t         regs;        // core's e-regs data structure
	} e_core_t;
	'''
	_fields_ 	= 	[	("objtype"		, 	c_int),
						("id"			, 	c_uint),
						("row"			, 	c_uint),
						("col"			,	c_uint),
						("mems"			,	e_mmap_t),
						("regs"			,	e_mmap_t)
					]

class e_epiphany_t(Structure):
	'''
		e_objtype_t      objtype;     // object type identifier
		e_chiptype_t     type;        // Epiphany chip part number
		unsigned int     num_cores;   // number of cores group
		unsigned int     base_coreid; // group base core ID
		unsigned int     row;         // group absolute row number
		unsigned int     col;         // group absolute col number
		unsigned int     rows;        // number of rows group
		unsigned int     cols;        // number of cols group
		e_core_t       **core;        // e-cores data structures array
		int              memfd;       // for mmap
	'''
	_fields_ 	= 	[	("objtype"		, 	c_int),
						("type"			, 	c_int),
						("num_cores"	, 	c_uint),
						("base_coreid"	, 	c_uint),
						("row"			, 	c_uint),
						("col"			, 	c_uint),
						("rows"			, 	c_uint),
						("cols"			, 	c_uint),
						("core"			,	POINTER(POINTER(e_core_t))),
						("memfd"		,	c_int)
					]

# Platform data structures
class e_chip_t(Structure):
	'''
		e_objtype_t      objtype;     // object type identifier
		e_chiptype_t     type;        // Epiphany chip part number
		char             version[32]; // version number of Epiphany chip
		unsigned int     arch;        // architecture generation
		unsigned int     base_coreid; // chip base core ID
		unsigned int     row;         // chip absolute row number
		unsigned int     col;         // chip absolute col number
		unsigned int     rows;        // number of rows in chip
		unsigned int     cols;        // number of cols in chip
		unsigned int     num_cores;   // number of cores in chip
		unsigned int     sram_base;   // base offset of core SRAM
		unsigned int     sram_size;   // size of core SRAM
		unsigned int     regs_base;   // base offset of core registers
		unsigned int     regs_size;   // size of core registers segment
		off_t            ioregs_n;    // base address of north IO register
		off_t            ioregs_e;    // base address of east IO register
		off_t            ioregs_s;    // base address of south IO register
		off_t            ioregs_w;    // base address of west IO register
	'''
	_fields_ 	= 	[	("objtype"		, 	c_int),
						("type"			, 	c_int),
						("version"		, 	c_char * 32),
						("arch"			,	c_uint),
						("base_coreid"	,	c_uint),
						("row"			,	c_uint),
						("col"			,	c_uint),
						("rows"			,	c_uint),
						("cols"			,	c_uint),
						("num_cores"	,	c_uint),
						("sram_base"	,	c_uint),
						("sram_size"	,	c_uint),
						("regs_base"	,	c_uint),
						("regs_size"	,	c_uint),
						("ioregs_n"		,	c_int),
						("ioregs_e"		,	c_int),
						("ioregs_s"		,	c_int),
						("ioregs_w"		,	c_int)
					]


class e_memseg_t(Structure):
	'''
	e_objtype_t      objtype;     // object type identifier
	off_t            phy_base;    // physical global base address of external memory segment as seen by host side
	off_t            ephy_base;   // physical global base address of external memory segment as seen by device side
	size_t           size;        // size of eDRAM allocated buffer for host side
	e_memtype_t      type;        // type of memory RD/WR/RW
	'''
	_fields_ 	= 	[	("objtype"		, 	c_int),
						("phy_base"		, 	c_int),
						("ephy_base"	,	c_int),
						("size"			,	c_int),
						("type"			,	c_int)
					]

class e_platform_t(Structure):
	'''
	e_objtype_t      objtype;     // object type identifier
	e_platformtype_t type;        // platform part number
	char             version[32]; // version number of platform
	unsigned int     hal_ver;     // version number of the E-HAL
	int              initialized; // platform initialized?

	unsigned int     regs_base;   // base address of platform registers

	int              num_chips;   // number of Epiphany chips in platform
	e_chip_t        *chip;        // array of Epiphany chip objects
	unsigned int     row;         // platform absolute minimum row number
	unsigned int     col;         // platform absolute minimum col number
	unsigned int     rows;        // number of rows in platform
	unsigned int     cols;        // number of cols in platform

	int              num_emems;   // number of external memory segments in platform
	e_memseg_t      *emem;        // array of external memory segments
	'''
	_fields_ 	= 	[	("objtype"		, 	c_int),
						("type"			, 	c_int),
						("version"		,	c_char * 32),
						("hal_ver"		,	c_uint),
						("initialized"	,	c_int),

						("regs_base"	,	c_uint),

						("num_chips"	,	c_int),
						("chip"			,	POINTER(e_chip_t)),
						("row"			,	c_uint),
						("col"			,	c_uint),
						("rows"			,	c_uint),
						("cols"			,	c_uint),

						("num_emems"	,	c_int),
						("emem"			,	POINTER(e_memseg_t))
					]	

class e_group_config_t(Structure):
	'''
	e_objtype_t  objtype;           // 0x28
	e_chiptype_t chiptype;          // 0x2c
	e_coreid_t   group_id;          // 0x30
	unsigned     group_row;         // 0x34
	unsigned     group_col;         // 0x38
	unsigned     group_rows;        // 0x3c
	unsigned     group_cols;        // 0x40
	unsigned     core_row;          // 0x44
	unsigned     core_col;          // 0x48
	unsigned     alignment_padding; // 0x4c
	'''
	_fields_ 	= 	[	("objtype"				, 	c_int),
						("chiptype"				, 	c_int),
						("group_id"				,	c_uint),
						("group_row"			,	c_uint),
						("group_col"			,	c_uint),
						("group_rows"			,	c_uint),
						("group_cols"			,	c_uint),
						("core_row"				,	c_uint),
						("core_col"				,	c_uint),
						("alignment_padding"	,	c_uint),
					]	

class e_mem_config_t(Structure):
	'''
	e_objtype_t objtype;            // 0x50
	unsigned    base;               // 0x54
	'''
	_fields_	=	[	("objtype"	,	c_int),
						("base"		,	c_uint)
					]