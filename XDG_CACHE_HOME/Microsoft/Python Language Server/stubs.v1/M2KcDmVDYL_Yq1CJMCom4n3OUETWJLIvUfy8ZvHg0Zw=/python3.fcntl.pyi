DN_ACCESS = 1
DN_ATTRIB = 32
DN_CREATE = 4
DN_DELETE = 8
DN_MODIFY = 2
DN_MULTISHOT = 2147483648
DN_RENAME = 16
FASYNC = 8192
FD_CLOEXEC = 1
F_DUPFD = 0
F_DUPFD_CLOEXEC = 1030
F_EXLCK = 4
F_GETFD = 1
F_GETFL = 3
F_GETLEASE = 1025
F_GETLK = 5
F_GETLK64 = 5
F_GETOWN = 9
F_GETSIG = 11
F_NOTIFY = 1026
F_RDLCK = 0
F_SETFD = 2
F_SETFL = 4
F_SETLEASE = 1024
F_SETLK = 6
F_SETLK64 = 6
F_SETLKW = 7
F_SETLKW64 = 7
F_SETOWN = 8
F_SETSIG = 10
F_SHLCK = 8
F_UNLCK = 2
F_WRLCK = 1
I_ATMARK = 21279
I_CANPUT = 21282
I_CKBAND = 21277
I_FDINSERT = 21264
I_FIND = 21259
I_FLUSH = 21253
I_FLUSHBAND = 21276
I_GETBAND = 21278
I_GETCLTIME = 21281
I_GETSIG = 21258
I_GRDOPT = 21255
I_GWROPT = 21268
I_LINK = 21260
I_LIST = 21269
I_LOOK = 21252
I_NREAD = 21249
I_PEEK = 21263
I_PLINK = 21270
I_POP = 21251
I_PUNLINK = 21271
I_PUSH = 21250
I_RECVFD = 21262
I_SENDFD = 21265
I_SETCLTIME = 21280
I_SETSIG = 21257
I_SRDOPT = 21254
I_STR = 21256
I_SWROPT = 21267
I_UNLINK = 21261
LOCK_EX = 2
LOCK_MAND = 32
LOCK_NB = 4
LOCK_READ = 64
LOCK_RW = 192
LOCK_SH = 1
LOCK_UN = 8
LOCK_WRITE = 128
__doc__ = 'This module performs file control and I/O control on file \ndescriptors.  It is an interface to the fcntl() and ioctl() Unix\nroutines.  File descriptors can be obtained with the fileno() method of\na file or socket object.'
__name__ = 'fcntl'
__package__ = ''
def fcntl(fd, cmd, arg):
    'Perform the operation `cmd` on file descriptor fd.\n\nThe values used for `cmd` are operating system dependent, and are available\nas constants in the fcntl module, using the same names as used in\nthe relevant C header files.  The argument arg is optional, and\ndefaults to 0; it may be an int or a string.  If arg is given as a string,\nthe return value of fcntl is a string of that length, containing the\nresulting value put in the arg buffer by the operating system.  The length\nof the arg string is not allowed to exceed 1024 bytes.  If the arg given\nis an integer or if none is specified, the result value is an integer\ncorresponding to the return value of the fcntl call in the C code.'
    pass

def flock(fd, operation):
    'Perform the lock operation `operation` on file descriptor `fd`.\n\nSee the Unix manual page for flock(2) for details (On some systems, this\nfunction is emulated using fcntl()).'
    pass

def ioctl(fd, request, arg, mutate_flag):
    'Perform the operation `request` on file descriptor `fd`.\n\nThe values used for `request` are operating system dependent, and are available\nas constants in the fcntl or termios library modules, using the same names as\nused in the relevant C header files.\n\nThe argument `arg` is optional, and defaults to 0; it may be an int or a\nbuffer containing character data (most likely a string or an array).\n\nIf the argument is a mutable buffer (such as an array) and if the\nmutate_flag argument (which is only allowed in this case) is true then the\nbuffer is (in effect) passed to the operating system and changes made by\nthe OS will be reflected in the contents of the buffer after the call has\nreturned.  The return value is the integer returned by the ioctl system\ncall.\n\nIf the argument is a mutable buffer and the mutable_flag argument is false,\nthe behavior is as if a string had been passed.\n\nIf the argument is an immutable buffer (most likely a string) then a copy\nof the buffer is passed to the operating system and the return value is a\nstring of the same length containing whatever the operating system put in\nthe buffer.  The length of the arg buffer in this case is not allowed to\nexceed 1024 bytes.\n\nIf the arg given is an integer or if none is specified, the result value is\nan integer corresponding to the return value of the ioctl call in the C\ncode.'
    pass

def lockf(fd, cmd, len, start, whence):
    'A wrapper around the fcntl() locking calls.\n\n`fd` is the file descriptor of the file to lock or unlock, and operation is one\nof the following values:\n\n    LOCK_UN - unlock\n    LOCK_SH - acquire a shared lock\n    LOCK_EX - acquire an exclusive lock\n\nWhen operation is LOCK_SH or LOCK_EX, it can also be bitwise ORed with\nLOCK_NB to avoid blocking on lock acquisition.  If LOCK_NB is used and the\nlock cannot be acquired, an OSError will be raised and the exception will\nhave an errno attribute set to EACCES or EAGAIN (depending on the operating\nsystem -- for portability, check for either value).\n\n`len` is the number of bytes to lock, with the default meaning to lock to\nEOF.  `start` is the byte offset, relative to `whence`, to that the lock\nstarts.  `whence` is as with fileobj.seek(), specifically:\n\n    0 - relative to the start of the file (SEEK_SET)\n    1 - relative to the current buffer position (SEEK_CUR)\n    2 - relative to the end of the file (SEEK_END)'
    pass

