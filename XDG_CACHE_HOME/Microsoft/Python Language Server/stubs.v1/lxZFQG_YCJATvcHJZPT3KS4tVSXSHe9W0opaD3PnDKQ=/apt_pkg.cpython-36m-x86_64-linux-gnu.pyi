import builtins as _mod_builtins

class Acquire(_mod_builtins.object):
    "Acquire([progress: apt.progress.base.AcquireProgress])\n\nCoordinate the retrieval of files via network or local file system\n(using 'copy:/path/to/file' style URIs). The optional argument\n'progress' takes an apt.progress.base.AcquireProgress object\nwhich may report progress information."
    RESULT_CANCELLED = 2
    RESULT_CONTINUE = 0
    RESULT_FAILED = 1
    __class__ = Acquire
    def __init__(self, progress: apt.progress.base.AcquireProgress=None):
        "Acquire([progress: apt.progress.base.AcquireProgress])\n\nCoordinate the retrieval of files via network or local file system\n(using 'copy:/path/to/file' style URIs). The optional argument\n'progress' takes an apt.progress.base.AcquireProgress object\nwhich may report progress information."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def fetch_needed(self):
        'The total amount of data to be fetched (number of bytes).'
        pass
    
    def get_lock(self, log: str):
        "get_lock(log: str)\n\nAcquires a log for the given directory, using a file 'lock' in it."
        pass
    
    @property
    def items(self):
        'A list of all items as apt_pkg.AcquireItem objects, including already\nfetched ones and to be fetched ones.'
        pass
    
    @property
    def partial_present(self):
        'The amount of data which is already available (number of bytes).'
        pass
    
    def run(self):
        'run() -> int\n\nRun the fetcher and return one of RESULT_CANCELLED,\nRESULT_CONTINUE, RESULT_FAILED.\n\nRESULT_CONTINUE means that all items which where queued prior to\ncalling run() have been fetched successfully or failed transiently.\n\nRESULT_CANCELLED means canceled by the progress class.\n\nRESULT_FAILED means a generic failure.'
        return 1
    
    def shutdown(self):
        'shutdown()\n\nShut the fetcher down, removing all items from it. Future access to\nqueued AcquireItem objects will cause a segfault. The partial result\nis kept on the disk and not removed and APT might reuse it.'
        pass
    
    @property
    def total_needed(self):
        'The amount of data that needs to fetched plus the amount of data\nwhich has already been fetched (number of bytes).'
        pass
    
    @property
    def workers(self):
        'A list of all active workers as apt_pkg.AcquireWorker objects.'
        pass
    

class AcquireFile(AcquireItem):
    "AcquireFile(owner, uri[, md5, size, descr, short_descr, destdir,destfile])\n\nRepresent a file to be fetched. The parameter 'owner' points to\nan apt_pkg.Acquire object and the parameter 'uri' to the source\nlocation. Normally, the file will be stored in the current directory\nusing the file name given in the URI. This directory can be changed\nby passing the name of a directory to the 'destdir' parameter. It is\nalso possible to set a path to a file using the 'destfile' parameter,\nbut both cannot be specified together.\n\nThe parameters 'short_descr' and 'descr' can be used to specify\na short description and a longer description for the item. This\ninformation is used by progress classes to refer to the item and\nshould be short, for example, package name as 'short_descr' and\nand something like 'http://localhost sid/main python-apt 0.7.94.2'\nas 'descr'.\nThe parameters 'md5' and 'size' are used to verify the resulting\nfile. The parameter 'size' is also to calculate the total amount\nof data to be fetched and is useful for resuming a interrupted\ndownload.\n\nAll parameters can be given by name (i.e. as keyword arguments)."
    __class__ = AcquireFile
    def __init__(self, owner, uri, md5=None, size=None, descr=None, short_descr=None, destdir=None, destfile=None):
        "AcquireFile(owner, uri[, md5, size, descr, short_descr, destdir,destfile])\n\nRepresent a file to be fetched. The parameter 'owner' points to\nan apt_pkg.Acquire object and the parameter 'uri' to the source\nlocation. Normally, the file will be stored in the current directory\nusing the file name given in the URI. This directory can be changed\nby passing the name of a directory to the 'destdir' parameter. It is\nalso possible to set a path to a file using the 'destfile' parameter,\nbut both cannot be specified together.\n\nThe parameters 'short_descr' and 'descr' can be used to specify\na short description and a longer description for the item. This\ninformation is used by progress classes to refer to the item and\nshould be short, for example, package name as 'short_descr' and\nand something like 'http://localhost sid/main python-apt 0.7.94.2'\nas 'descr'.\nThe parameters 'md5' and 'size' are used to verify the resulting\nfile. The parameter 'size' is also to calculate the total amount\nof data to be fetched and is useful for resuming a interrupted\ndownload.\n\nAll parameters can be given by name (i.e. as keyword arguments)."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class AcquireItem(_mod_builtins.object):
    'Represent a single item to be fetched by an Acquire object.\n\nIt is not possible to construct instances of this class directly.\nProspective users should construct instances of a subclass such as\nAcquireFile instead. It is not possible to create subclasses on the\nPython level, only on the C++ level.'
    STAT_AUTH_ERROR = 4
    STAT_DONE = 2
    STAT_ERROR = 3
    STAT_FETCHING = 1
    STAT_IDLE = 0
    STAT_TRANSIENT_NETWORK_ERROR = 5
    __class__ = AcquireItem
    def __init__(self, *args, **kwargs):
        'Represent a single item to be fetched by an Acquire object.\n\nIt is not possible to construct instances of this class directly.\nProspective users should construct instances of a subclass such as\nAcquireFile instead. It is not possible to create subclasses on the\nPython level, only on the C++ level.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def active_subprocess(self):
        "The name of the active subprocess (for instance, 'gzip', 'rred' or 'gpgv')."
        pass
    
    @property
    def complete(self):
        'A boolean value determining whether the item has been fetched\ncompletely'
        pass
    
    @property
    def desc_uri(self):
        'A string describing the URI from which the item is acquired.'
        pass
    
    @property
    def destfile(self):
        'The path to the file where the item will be stored.'
        pass
    
    @property
    def error_text(self):
        'If an error occurred, a string describing the error; empty string\notherwise.'
        pass
    
    @property
    def filesize(self):
        'The size of the file (number of bytes). If unknown, it is set to 0.'
        pass
    
    @property
    def id(self):
        'The ID of the item. An integer which can be set by progress classes.'
        pass
    
    @property
    def is_trusted(self):
        "Whether the item is trusted or not. Only True for packages\nwhich come from a repository signed with one of the keys in\nAPT's keyring."
        pass
    
    @property
    def local(self):
        'Whether we are fetching a local item (copy:/) or not.'
        pass
    
    @property
    def mode(self):
        'Old name for active_subprocess'
        pass
    
    @property
    def partialsize(self):
        'The amount of data which has already been fetched (number of bytes).'
        pass
    
    @property
    def status(self):
        "An integer representing the item's status which can be compared\nagainst one of the STAT_* constants defined in this class."
        pass
    

class AcquireItemDesc(_mod_builtins.object):
    'Provide the description of an item and the URI the item is\nfetched from. Progress classes make use of such objects to\nretrieve description and other information about an item.'
    __class__ = AcquireItemDesc
    def __init__(self, *args, **kwargs):
        'Provide the description of an item and the URI the item is\nfetched from. Progress classes make use of such objects to\nretrieve description and other information about an item.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def description(self):
        'A string describing the item.'
        pass
    
    @property
    def owner(self):
        'The owner of the item, an apt_pkg.AcquireItem object.'
        pass
    
    @property
    def shortdesc(self):
        'A short string describing the item (e.g. package name).'
        pass
    
    @property
    def uri(self):
        'The URI from which this item would be downloaded.'
        pass
    

class AcquireWorker(_mod_builtins.object):
    "Represent a sub-process responsible for fetching files from\nremote locations. This sub-process uses 'methods' located in\nthe directory specified by the configuration option\nDir::Bin::Methods."
    __class__ = AcquireWorker
    def __init__(self, *args, **kwargs):
        "Represent a sub-process responsible for fetching files from\nremote locations. This sub-process uses 'methods' located in\nthe directory specified by the configuration option\nDir::Bin::Methods."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def current_item(self):
        'The item currently being fetched, as an apt_pkg.AcquireItemDesc object.'
        pass
    
    @property
    def current_size(self):
        'The amount of data fetched so far for the current item.'
        pass
    
    @property
    def resumepoint(self):
        'The amount of data which was already available when the download was\nstarted.'
        pass
    
    @property
    def status(self):
        'The status of the worker, as a string.'
        pass
    
    @property
    def total_size(self):
        'The total size of the item.'
        pass
    

class ActionGroup(_mod_builtins.object):
    "ActionGroup(depcache)\n\nCreate a new ActionGroup() object. The parameter *depcache* refers to an\napt_pkg.DepCache() object.\n\nActionGroups disable certain cleanup actions, so modifying many packages\nis much faster.\n\nActionGroup() can also be used with the 'with' statement, but be aware\nthat the ActionGroup() is active as soon as it is created, and not just\nwhen entering the context. This means you can write::\n\n    with apt_pkg.ActionGroup(depcache):\n        depcache.markInstall(pkg)\n\nOnce the block of the with statement is left, the action group is \nautomatically released from the cache."
    __class__ = ActionGroup
    def __enter__(self):
        '__enter__() -> ActionGroup\n\nA dummy action which just returns the object itself, so it can\nbe used as a context manager.'
        return self
    
    def __exit__(self, *excinfo):
        '__exit__(*excinfo) -> bool\n\nSame as release(), but for use as a context manager.'
        return True
    
    def __init__(self, depcache):
        "ActionGroup(depcache)\n\nCreate a new ActionGroup() object. The parameter *depcache* refers to an\napt_pkg.DepCache() object.\n\nActionGroups disable certain cleanup actions, so modifying many packages\nis much faster.\n\nActionGroup() can also be used with the 'with' statement, but be aware\nthat the ActionGroup() is active as soon as it is created, and not just\nwhen entering the context. This means you can write::\n\n    with apt_pkg.ActionGroup(depcache):\n        depcache.markInstall(pkg)\n\nOnce the block of the with statement is left, the action group is \nautomatically released from the cache."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def release(self):
        'release()\n\nEnd the scope of this action group.  If this is the only action\ngroup bound to the cache, this will cause any deferred cleanup\nactions to be performed.'
        pass
    

CURSTATE_CONFIG_FILES = 5
CURSTATE_HALF_CONFIGURED = 2
CURSTATE_HALF_INSTALLED = 4
CURSTATE_INSTALLED = 6
CURSTATE_NOT_INSTALLED = 0
CURSTATE_UNPACKED = 1
class Cache(_mod_builtins.object):
    'Cache([progress]) -> Cache() object.\n\nThe APT cache file contains a hash table mapping names of binary\npackages to their metadata. A Cache object is the in-core\nrepresentation of the same. It provides access to APT’s idea of the\nlist of available packages.\nThe optional parameter *progress* can be used to specify an \napt.progress.base.OpProgress() object (or similar) which reports\nprogress information while the cache is being opened.  If this\nparameter is not supplied, the progress will be reported in simple,\nhuman-readable text to standard output. If it is None, no output\nwill be made.\n\nThe cache can be used like a mapping from package names to Package\nobjects (although only getting items is supported). Instead of a name,\na tuple of a name and an architecture may be used.'
    __class__ = Cache
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, progress=None):
        'Cache([progress]) -> Cache() object.\n\nThe APT cache file contains a hash table mapping names of binary\npackages to their metadata. A Cache object is the in-core\nrepresentation of the same. It provides access to APT’s idea of the\nlist of available packages.\nThe optional parameter *progress* can be used to specify an \napt.progress.base.OpProgress() object (or similar) which reports\nprogress information while the cache is being opened.  If this\nparameter is not supplied, the progress will be reported in simple,\nhuman-readable text to standard output. If it is None, no output\nwill be made.\n\nThe cache can be used like a mapping from package names to Package\nobjects (although only getting items is supported). Instead of a name,\na tuple of a name and an architecture may be used.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def depends_count(self):
        'The number of apt_pkg.Dependency objects stored in the cache.'
        pass
    
    @property
    def file_list(self):
        'A list of apt_pkg.PackageFile objects stored in the cache.'
        pass
    
    @property
    def group_count(self):
        'The number of apt_pkg.Group objects stored in the cache.'
        pass
    
    @property
    def groups(self):
        'A list of Group objects in the cache'
        pass
    
    @property
    def is_multi_arch(self):
        'Whether the cache supports multi-arch.'
        pass
    
    @property
    def package_count(self):
        'The number of apt_pkg.Package objects stored in the cache.'
        pass
    
    @property
    def package_file_count(self):
        'The number of apt_pkg.PackageFile objects stored in the cache.'
        pass
    
    @property
    def packages(self):
        'A list of apt_pkg.Package objects stored in the cache.'
        pass
    
    @property
    def policy(self):
        'The PkgPolicy for the cache'
        pass
    
    @property
    def provides_count(self):
        'Number of Provides relations described in the cache.'
        pass
    
    def update(self, progress, sources: SourceList, pulse_interval: int):
        "update(progress, sources: SourceList, pulse_interval: int) -> bool\n\nUpdate the index files used by the cache. A call to this method\ndoes not affect the current Cache object; instead, a new one\nshould be created in order to use the changed index files.\n\nThe parameter 'progress' can be used to specify an\napt.progress.base.AcquireProgress() object , which will report\nprogress information while the index files are being fetched.\nThe parameter 'sources', if provided, is an apt_pkg.SourcesList\nobject listing the remote repositories to be used.\nThe 'pulse_interval' parameter indicates how long (in microseconds)\nto wait between calls to the pulse() method of the 'progress' object.\nThe default is 500000 microseconds."
        return True
    
    @property
    def ver_file_count(self):
        'The number of (Version, PackageFile) relations.'
        pass
    
    @property
    def version_count(self):
        'The number of apt_pkg.Version objects stored in the cache.'
        pass
    

class CacheMismatchError(_mod_builtins.ValueError):
    'Raised when passing an object from a different cache to\n:class:`apt_pkg.DepCache` methods\n\n.. versionadded:: 1.6.1'
    __class__ = CacheMismatchError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Raised when passing an object from a different cache to\n:class:`apt_pkg.DepCache` methods\n\n.. versionadded:: 1.6.1'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'apt_pkg'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class Cdrom(_mod_builtins.object):
    'Cdrom()\n\nCdrom objects can be used to identify Debian installation media and to\nadd them to /etc/apt/sources.list.'
    __class__ = Cdrom
    def __init__(self):
        'Cdrom()\n\nCdrom objects can be used to identify Debian installation media and to\nadd them to /etc/apt/sources.list.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def add(self, progress: apt_pkg.CdromProgress):
        'add(progress: apt_pkg.CdromProgress) -> bool\n\nAdd the given CD-ROM to the sources.list. Return True on success;\nraise an error on failure or return False.'
        return True
    
    def ident(self, progress: apt_pkg.CdromProgress):
        'ident(progress: apt_pkg.CdromProgress) -> str\n\nTry to identify the CD-ROM and if successful return the hexadecimal\nCDROM-ID (and a integer version suffix separated by -) as a\nstring. Otherwise, return None or raise an error.\n\nThe ID is created by hashing all file and directory names on the\nCD-ROM and appending the version.'
        return ''
    

class Configuration(_mod_builtins.object):
    'Configuration()\n\nRepresent the configuration of APT by mapping option keys to\nvalues and storing configuration parsed from files like\n/etc/apt/apt.conf. The most important Configuration object\nis apt_pkg.config which points to the global configuration\nobject. Other top-level Configuration objects can be created\nby calling the constructor, but there is usually no reason to.'
    __class__ = Configuration
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self):
        'Configuration()\n\nRepresent the configuration of APT by mapping option keys to\nvalues and storing configuration parsed from files like\n/etc/apt/apt.conf. The most important Configuration object\nis apt_pkg.config which points to the global configuration\nobject. Other top-level Configuration objects can be created\nby calling the constructor, but there is usually no reason to.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def clear(self, key: str):
        'clear(key: str)\n\nRemove the specified option and all sub-options.'
        pass
    
    def dump(self):
        'dump() -> str\n\nReturn a string dump this Configuration object.'
        return ''
    
    def exists(self, key: str):
        'exists(key: str) -> bool\n\nCheck whether the given key exists.'
        return True
    
    def find(self, key: str, default: str=''):
        "find(key: str[, default: str = '']) -> str\n\nFind the value for the given key and return it. If the\ngiven key does not exist, return default instead."
        return ''
    
    def find_b(self):
        'find_i(key: str[, default: bool = False]) -> bool\n\nSame as find, but for boolean values; returns False on unknown values.'
        return True
    
    def find_dir(self, key: str, default: str=''):
        "find_dir(key: str[, default: str = '']) -> str\n\nSame as find_file(), but for directories. The difference is\nthat this function adds a trailing slash to the result."
        return ''
    
    def find_file(self, key: str, default: str=''):
        "find_file(key: str[, default: str = '']) -> str\n\nSame as find(), but for filenames. In the APT configuration, there\nis a special section Dir:: for storing filenames. find_file() locates\nthe given key and then goes up and prepends the directory names to the\nreturn value. For example, for:\n\n    apt_pkg.config['Dir'] = 'a'\n    apt_pkg.config['Dir::D'] = 'b'\n    apt_pkg.config['Dir::D::F'] = 'c'\n\nfind_file('Dir::D::F') returns 'a/b/c'. There is also a special\nconfiguration setting RootDir which will always be prepended to the\nresult (the default being ''). Thus, if RootDir is 'x', the example\nwould return 'x/a/b/c'."
        return ''
    
    def find_i(self, key: str, default: int=0):
        'find_i(key: str[, default: int = 0]) -> int\n\nSame as find, but for integer values.'
        return 1
    
    def get(self):
        "find(key: str[, default: str = '']) -> str\n\nFind the value for the given key and return it. If the\ngiven key does not exist, return default instead."
        return ''
    
    def keys(self, root: str=None):
        "keys([root: str]) -> list\n\nReturn a list of all keys in the configuration object. If 'root'\nis given, limit the list to those below the root."
        return list()
    
    def list(self, root: str=None):
        "list([root: str]) -> list\n\nReturn a list of all items at the given root, using their full\nname. For example, in a configuration object where the options A,\nB, and B::C are set, the following expressions evaluate to True:\n\n   conf.list() == ['A', 'B']\n   conf.list('A') == ['']\n   conf.list('B') == ['B::C']\n"
        return list()
    
    def my_tag(self):
        "my_tag() -> str\n\nReturn the tag of the root of this Configuration object. For the\ndefault object, this is an empty string. For a subtree('APT') of\nsuch an object, it would be 'APT' (given as an example)."
        return ''
    
    def set(self, key: str, value: str):
        'set(key: str, value: str)\n\nSet the given key to the given value. To set int or bool values,\nencode them using str(value) and then use find_i()/find_b()\nto retrieve their value again.'
        pass
    
    def subtree(self, key: str):
        "subtree(key: str) -> apt_pkg.Configuration\n\nReturn a new apt_pkg.Configuration object with the given option\nas its root. Example:\n\n    apttree = config.subtree('APT')\n    apttree['Install-Suggests'] = config['APT::Install-Suggests']"
        pass
    
    def value_list(self, root: str=None):
        'value_list([root: str]) -> list\n\nSame as list(), but instead of returning the keys, return the values.'
        return list()
    

DATE = 'Apr 29 2019'
class DepCache(_mod_builtins.object):
    "DepCache(cache: apt_pkg.Cache)\n\nA DepCache() holds extra information on the state of the packages.\n\nThe parameter 'cache' refers to an apt_pkg.Cache() object."
    __class__ = DepCache
    def __init__(self, cache: apt_pkg.Cache):
        "DepCache(cache: apt_pkg.Cache)\n\nA DepCache() holds extra information on the state of the packages.\n\nThe parameter 'cache' refers to an apt_pkg.Cache() object."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def broken_count(self):
        'The number of packages with broken dependencies in the cache.'
        pass
    
    def commit(self, acquire_progress, install_progress):
        "commit(acquire_progress, install_progress)\n\nCommit all the marked changes. This method takes two arguments,\n'acquire_progress' takes an apt.progress.base.AcquireProgress\nobject and 'install_progress' an apt.progress.base.InstallProgress\nobject."
        pass
    
    @property
    def deb_size(self):
        'The size of the packages which are needed for the changes to be\napplied.'
        pass
    
    @property
    def del_count(self):
        'The number of packages marked for removal.'
        pass
    
    def fix_broken(self):
        'fix_broken() -> bool\n\nFix broken packages.'
        return True
    
    def get_candidate_ver(self, pkg: apt_pkg.Package):
        'get_candidate_ver(pkg: apt_pkg.Package) -> apt_pkg.Version\n\nReturn the candidate version for the package, normally the version\nwith the highest pin (changeable using set_candidate_ver).'
        pass
    
    def init(self, progress: apt.progress.base.OpProgress):
        'init(progress: apt.progress.base.OpProgress)\n\nInitialize the depcache (done automatically when constructing\nthe object).'
        pass
    
    @property
    def inst_count(self):
        'The number of packages marked for installation.'
        pass
    
    def is_auto_installed(self, pkg: apt_pkg.Package):
        'is_auto_installed(pkg: apt_pkg.Package) -> bool\n\nCheck whether the package is marked as automatically installed.'
        return True
    
    def is_garbage(self, pkg: apt_pkg.Package):
        'is_garbage(pkg: apt_pkg.Package) -> bool\n\nCheck whether the package is garbage, i.e. whether it is automatically\ninstalled and the reverse dependencies are not installed anymore.'
        return True
    
    def is_inst_broken(self, pkg: apt_pkg.Package):
        'is_inst_broken(pkg: apt_pkg.Package) -> bool\n\nCheck whether the package is broken, ignoring marked changes.'
        return True
    
    def is_now_broken(self, pkg: apt_pkg.Package):
        'is_now_broken(pkg: apt_pkg.Package) -> bool\n\nCheck whether the package is broken, taking marked changes into account.'
        return True
    
    def is_upgradable(self, pkg: apt_pkg.Package):
        'is_upgradable(pkg: apt_pkg.Package) -> bool\n\nCheck whether the package is upgradable.'
        return True
    
    @property
    def keep_count(self):
        'The number of packages marked for keep.'
        pass
    
    def mark_auto(self, pkg: apt_pkg.Package, auto: bool):
        'mark_auto(pkg: apt_pkg.Package, auto: bool)\n\nMark package as automatically installed (if auto=True),\nor as not automatically installed (if auto=False).'
        pass
    
    def mark_delete(self, pkg: apt_pkg.Package, purge: bool=False):
        "mark_delete(pkg: apt_pkg.Package[, purge: bool = False])\n\nMark package for deletion, and if 'purge' is True also for purging."
        pass
    
    def mark_install(self, pkg: apt_pkg.Package, auto_inst=True, from_user=True):
        "mark_install(pkg: apt_pkg.Package[, auto_inst=True, from_user=True])\n\nMark the package for installation. The parameter 'auto_inst' controls\nwhether the dependencies of the package are marked for installation\nas well. The parameter 'from_user' controls whether the package is\nregistered as NOT automatically installed."
        pass
    
    def mark_keep(self, pkg: apt_pkg.Package):
        'mark_keep(pkg: apt_pkg.Package)\n\nMark package to be kept.'
        pass
    
    def marked_delete(self, pkg: apt_pkg.Package):
        'marked_delete(pkg: apt_pkg.Package) -> bool\n\nCheck whether the package is marked for removal.'
        return True
    
    def marked_downgrade(self, pkg: apt_pkg.Package):
        'marked_downgrade(pkg: apt_pkg.Package) -> bool\n\nCheck whether the package is marked for downgrade.'
        return True
    
    def marked_install(self, pkg: apt_pkg.Package):
        'marked_install(pkg: apt_pkg.Package) -> bool\n\nCheck whether the package is marked for installation.'
        return True
    
    def marked_keep(self, pkg: apt_pkg.Package):
        'marked_keep(pkg: apt_pkg.Package) -> bool\n\nCheck whether the package should be kept.'
        return True
    
    def marked_reinstall(self, pkg: apt_pkg.Package):
        'marked_reinstall(pkg: apt_pkg.Package) -> bool\n\nCheck whether the package is marked for re-installation.'
        return True
    
    def marked_upgrade(self, pkg: apt_pkg.Package):
        'marked_upgrade(pkg: apt_pkg.Package) -> bool\n\nCheck whether the package is marked for upgrade.'
        return True
    
    def minimize_upgrade(self):
        'minimize_upgrade() -> bool\n\nGo over the entire set of packages and try to keep each package\nmarked for upgrade. If a conflict is generated then the package\nis restored.'
        return True
    
    @property
    def policy(self):
        'The apt_pkg.Policy object used by this cache.'
        pass
    
    def read_pinfile(self, file: str=None):
        'read_pinfile([file: str])\n\nRead the pin policy'
        pass
    
    def set_candidate_release(self, pkg: apt_pkg.Package, ver: apt_pkg.Version, rel: string):
        "set_candidate_release(pkg: apt_pkg.Package, ver: apt_pkg.Version, rel: string) -> bool\n\nSets not only the candidate version 'ver' for package 'pkg', but walks also down the dependency tree and checks if it is required to set the candidate of the dependency to a version from the given release string 'rel', too."
        return True
    
    def set_candidate_ver(self, pkg: apt_pkg.Package, ver: apt_pkg.Version):
        "set_candidate_ver(pkg: apt_pkg.Package, ver: apt_pkg.Version) -> bool\n\nSet the candidate version of 'pkg' to 'ver'."
        return True
    
    def set_reinstall(self, pkg: apt_pkg.Package, reinstall: bool):
        'set_reinstall(pkg: apt_pkg.Package, reinstall: bool)\n\nSet whether the package should be reinstalled (reinstall = True or False).'
        pass
    
    def upgrade(self, dist_upgrade: bool=True):
        "upgrade([dist_upgrade: bool = True]) -> bool\n\nMark the packages for upgrade under the same conditions apt-get\nupgrade does. If 'dist_upgrade' is True, also allow packages to\nbe upgraded if they require installation/removal of other packages;\njust like apt-get dist-upgrade."
        return True
    
    @property
    def usr_size(self):
        'The amount of space required for installing/removing the packages,\ni.e. the Installed-Size of all packages marked for installation\nminus the Installed-Size of all packages for removal.'
        pass
    

class Dependency(_mod_builtins.object):
    'Represent a dependency from one package version to a package,\nand (optionally) a version relation (e.g. >= 1). Dependency\nobjects also provide useful functions like all_targets()\nfor selecting packages to satisfy the dependency.'
    TYPE_CONFLICTS = 5
    TYPE_DEPENDS = 1
    TYPE_DPKG_BREAKS = 8
    TYPE_ENHANCES = 9
    TYPE_OBSOLETES = 7
    TYPE_PREDEPENDS = 2
    TYPE_RECOMMENDS = 4
    TYPE_REPLACES = 6
    TYPE_SUGGESTS = 3
    __class__ = Dependency
    def __init__(self, *args, **kwargs):
        'Represent a dependency from one package version to a package,\nand (optionally) a version relation (e.g. >= 1). Dependency\nobjects also provide useful functions like all_targets()\nfor selecting packages to satisfy the dependency.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def all_targets(self):
        'all_targets() -> list\n\nA list of all possible apt_pkg.Version objects which satisfy this\ndependency.'
        return list()
    
    @property
    def comp_type(self):
        "The type of comparison in mathematical notation, as a string, namely one of:\n'<', '<=', '=', '!=', '>=', '>', ''.\nThe empty string will be returned in case of an unversioned dependency."
        pass
    
    @property
    def comp_type_deb(self):
        "The type of comparison in Debian notation, as a string, namely one of:\n'<<', '<=', '=', '!=', '>=', '>>', ''.\nThe empty string will be returned in case of an unversioned dependency.\nFor details see the Debian Policy Manual on the syntax of relationship fields:\nhttps://www.debian.org/doc/debian-policy/ch-relationships.html#s-depsyntax"
        pass
    
    @property
    def dep_type(self):
        'The type of the dependency; may be translated'
        pass
    
    @property
    def dep_type_enum(self):
        'Same as dep_type, but with a numeric value instead of a string. Can\nbe compared against the TYPE_ constants defined in this class.'
        pass
    
    @property
    def dep_type_untranslated(self):
        'Same as dep_type, but guaranteed to be untranslated.'
        pass
    
    @property
    def id(self):
        'The numeric ID of this dependency object.'
        pass
    
    @property
    def parent_pkg(self):
        'The apt_pkg.Package object of the package which depends.'
        pass
    
    @property
    def parent_ver(self):
        'The apt_pkg.Version object of the package which depends.'
        pass
    
    @property
    def target_pkg(self):
        'The apt_pkg.Package object of the package depended upon'
        pass
    
    @property
    def target_ver(self):
        'The version of the package depended upon as a string'
        pass
    

class DependencyList(_mod_builtins.object):
    'A simple list-like type for representing multiple dependency\nobjects in an efficient manner; without having to generate\nall Dependency objects in advance.'
    __class__ = DependencyList
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        'A simple list-like type for representing multiple dependency\nobjects in an efficient manner; without having to generate\nall Dependency objects in advance.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Description(_mod_builtins.object):
    'Represent a package description and some attributes. Needed for\nthings like translated descriptions.'
    __class__ = Description
    def __init__(self, *args, **kwargs):
        'Represent a package description and some attributes. Needed for\nthings like translated descriptions.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def file_list(self):
        'A list of all apt_pkg.PackageFile objects related to this description.'
        pass
    
    @property
    def language_code(self):
        'The language code of the description. Empty string for untranslated\ndescriptions.'
        pass
    
    @property
    def md5(self):
        'The MD5 hash of the description.'
        pass
    

class Error(_mod_builtins.SystemError):
    'Exception class for most python-apt exceptions.\n\nThis class replaces the use of :class:`SystemError` in previous versions\nof python-apt. It inherits from :class:`SystemError`, so make sure to\ncatch this class first.\n\n.. versionadded:: 1.1'
    __class__ = Error
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Exception class for most python-apt exceptions.\n\nThis class replaces the use of :class:`SystemError` in previous versions\nof python-apt. It inherits from :class:`SystemError`, so make sure to\ncatch this class first.\n\n.. versionadded:: 1.1'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'apt_pkg'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class FileLock(_mod_builtins.object):
    "SystemLock(filename: str)\n\nContext manager for locking using a file. The lock is established\nas soon as the method __enter__() is called. It is released when\n__exit__() is called.\n\nThis should be used via the 'with' statement, for example:\n\n   with apt_pkg.FileLock(filename):\n       ...\n\nOnce the block is left, the lock is released automatically. The object\ncan be used multiple times:\n\n   lock = apt_pkg.FileLock(filename)\n   with lock:\n       ...\n   with lock:\n       ...\n\n"
    __class__ = FileLock
    def __enter__(self):
        'Lock the system.'
        return self
    
    def __exit__(self):
        'Unlock the system.'
        pass
    
    def __init__(self, filename: str):
        "SystemLock(filename: str)\n\nContext manager for locking using a file. The lock is established\nas soon as the method __enter__() is called. It is released when\n__exit__() is called.\n\nThis should be used via the 'with' statement, for example:\n\n   with apt_pkg.FileLock(filename):\n       ...\n\nOnce the block is left, the lock is released automatically. The object\ncan be used multiple times:\n\n   lock = apt_pkg.FileLock(filename)\n   with lock:\n       ...\n   with lock:\n       ...\n\n"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Group(_mod_builtins.object):
    'Group(cache, name)\n\nGroup of packages with the same name.\n\nProvides access to all packages sharing a name. Can be used this\nlike a list, or by using the special find_*() methods. If you use\nit as a sequence, make sure to access it linearly, as this uses a\nlinked list internally.'
    __class__ = Group
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, cache, name):
        'Group(cache, name)\n\nGroup of packages with the same name.\n\nProvides access to all packages sharing a name. Can be used this\nlike a list, or by using the special find_*() methods. If you use\nit as a sequence, make sure to access it linearly, as this uses a\nlinked list internally.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def find_package(self, architecture: str):
        'find_package(architecture: str) -> Package\n\nReturn a package for the given architecture, or None if none exists'
        pass
    
    def find_preferred_package(self, prefer_non_virtual: bool=True):
        'find_preferred_package(prefer_non_virtual: bool = True) -> Package\n\nReturn a package for the best architecture, either the native one\nor the first found one. If none exists, return None. If non_virtual\nis True, prefer non-virtual packages over virtual ones.'
        pass
    

class GroupList(_mod_builtins.object):
    "A GroupList is an internally used structure to represent\nthe 'groups' attribute of apt_pkg.Cache objects in a more\nefficient manner by creating Group objects only when they\nare accessed."
    __class__ = GroupList
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        "A GroupList is an internally used structure to represent\nthe 'groups' attribute of apt_pkg.Cache objects in a more\nefficient manner by creating Group objects only when they\nare accessed."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class HashString(_mod_builtins.object):
    "HashString(type, hash) OR HashString('type:hash')\n\nCreate a new HashString object. The first form allows you to specify\na type and a hash, and the second form a single string where type and\nhash are separated by a colon, e.g.::\n\n   HashString('MD5Sum', '6cc1b6e6655e3555ac47e5b5fe26d04e')\n\nValid options for 'type' are: MD5Sum, SHA1, SHA256."
    __class__ = HashString
    def __init__(self, type, hash):
        "HashString(type, hash) OR HashString('type:hash')\n\nCreate a new HashString object. The first form allows you to specify\na type and a hash, and the second form a single string where type and\nhash are separated by a colon, e.g.::\n\n   HashString('MD5Sum', '6cc1b6e6655e3555ac47e5b5fe26d04e')\n\nValid options for 'type' are: MD5Sum, SHA1, SHA256."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def hashtype(self):
        'The type of the hash, as a string (possible: MD5Sum,SHA1,SHA256).'
        pass
    
    def verify_file(self, filename: str):
        'verify_file(filename: str) -> bool\n\nVerify that the file indicated by filename matches the hash.'
        return True
    

class HashStringList(_mod_builtins.object):
    'HashStringList()\n\nManage a list of HashStrings.\n\nThe list knows which hash is the best and provides convenience\nmethods for file verification.\n\n.. versionadded:: 1.1'
    __class__ = HashStringList
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self):
        'HashStringList()\n\nManage a list of HashStrings.\n\nThe list knows which hash is the best and provides convenience\nmethods for file verification.\n\n.. versionadded:: 1.1'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def append(self, object: HashString):
        'append(object: HashString)\n\nAppend the given HashString to this list.'
        pass
    
    @property
    def file_size(self):
        'If a file size is part of the list, return it, otherwise 0.'
        pass
    
    def find(self, type: str=""):
        'find(type: str = "") -> HashString\n\nFind a hash of the given type, or the best one, if the argument\nis empty or not specified.'
        pass
    
    def verify_file(self, filename: str):
        'verify_file(filename: str) -> bool\n\nVerify that the file with the given name matches all hashes in\nthe list.'
        return True
    

class Hashes(_mod_builtins.object):
    'Hashes([object: (bytes, file)])\n\nCalculate hashes for the given object. It can be used to create all\nsupported hashes for a file.\n\nThe parameter *object* can be a bytestring, an object providing the\nfileno() method, or an integer describing a file descriptor.'
    __class__ = Hashes
    def __init__(self, object: (bytes,file)=None):
        'Hashes([object: (bytes, file)])\n\nCalculate hashes for the given object. It can be used to create all\nsupported hashes for a file.\n\nThe parameter *object* can be a bytestring, an object providing the\nfileno() method, or an integer describing a file descriptor.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def hashes(self):
        'A :class:`HashStringList` of all hashes.\n\n.. versionadded:: 1.1'
        pass
    
    @property
    def md5(self):
        'The MD5Sum of the file as a string.\n\n.. deprecated:: 1.1'
        pass
    
    @property
    def sha1(self):
        'The SHA1Sum of the file as a string.\n\n.. deprecated:: 1.1'
        pass
    
    @property
    def sha256(self):
        'The SHA256Sum of the file as a string.\n\n.. deprecated:: 1.1'
        pass
    

INSTSTATE_HOLD = 2
INSTSTATE_HOLD_REINSTREQ = 3
INSTSTATE_OK = 0
INSTSTATE_REINSTREQ = 1
class IndexFile(_mod_builtins.object):
    'Represent an index file, i.e. package indexes, translation indexes,\nand source indexes.'
    __class__ = IndexFile
    def __init__(self, *args, **kwargs):
        'Represent an index file, i.e. package indexes, translation indexes,\nand source indexes.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def archive_uri(self, path: str):
        'archive_uri(path: str) -> str\n\nReturn the URI to the given path in the archive.'
        return ''
    
    @property
    def describe(self):
        'A string describing the index file.'
        pass
    
    @property
    def exists(self):
        'A boolean value determining whether the index file exists.'
        pass
    
    @property
    def has_packages(self):
        'A boolean value determining whether the index file has packages.'
        pass
    
    @property
    def is_trusted(self):
        'A boolean value determining whether the file can be trusted; e.g.\nbecause it is from a source with a GPG signed Release file.'
        pass
    
    @property
    def label(self):
        'The label of the index file.'
        pass
    
    @property
    def size(self):
        'The size of the files, measured in bytes.'
        pass
    

LIB_VERSION = '5.0.2'
class MetaIndex(_mod_builtins.object):
    'Provide information on meta-indexes (i.e. Release files), such as\nwhether they are trusted or their URI.'
    __class__ = MetaIndex
    def __init__(self, ieReleasefiles):
        'Provide information on meta-indexes (i.e. Release files), such as\nwhether they are trusted or their URI.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def dist(self):
        'The distribution, as a string.'
        pass
    
    @property
    def index_files(self):
        'A list of all IndexFile objects associated with this meta index.'
        pass
    
    @property
    def is_trusted(self):
        'A boolean value determining whether the file can be trusted.'
        pass
    
    @property
    def uri(self):
        'The uri the meta index is located at.'
        pass
    

class OrderList(_mod_builtins.object):
    'OrderList(depcache: DepCache)\n\nSequence type for packages with special ordering methods.'
    FLAG_ADDED = 1
    FLAG_ADD_PENDIG = 2
    FLAG_AFTER = 256
    FLAG_CONFIGURED = 32
    FLAG_IMMEDIATE = 4
    FLAG_IN_LIST = 128
    FLAG_LOOP = 8
    FLAG_REMOVED = 64
    FLAG_STATES_MASK = 112
    FLAG_UNPACKED = 16
    __class__ = OrderList
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, depcache: DepCache):
        'OrderList(depcache: DepCache)\n\nSequence type for packages with special ordering methods.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def append(self, pkg: Package):
        'append(pkg: Package)\n\nAppend a package to the end of the list.'
        pass
    
    def flag(self, pkg: Package, flag: int, unset_flags: int=None):
        "flag(pkg: Package, flag: int[, unset_flags: int])\n\nFlag the package, set flags in 'flag' and remove flags in\n'unset_flags'."
        pass
    
    def is_flag(self, pkg: Package, flag: int):
        'is_flag(pkg: Package, flag: int)\n\nCheck if the flag(s) are set.'
        pass
    
    def is_missing(self):
        'is_now(pkg: Package)\n\nCheck if the package is marked for install.'
        pass
    
    def is_now(self, pkg: Package):
        'is_now(pkg: Package)\n\nCheck if the package is flagged for any state but removal.'
        pass
    
    def order_configure(self):
        'order_configure()\n\nOrder the packages for configuration (see Debian Policy).'
        pass
    
    def order_critical(self):
        'order_critical()\n\nOrder by PreDepends only (critical unpack order).'
        pass
    
    def order_unpack(self):
        'order_unpack()\n\nOrder the packages for unpacking (see Debian Policy).'
        pass
    
    def score(self, pkg: Package):
        'score(pkg: Package) -> int\n\nReturn the score of the package.'
        return 1
    
    def wipe_flags(self, flags: int):
        "wipe_flags(flags: int)\n\nRemove the flags in 'flags' from all packages in this list"
        pass
    

PRI_EXTRA = 5
PRI_IMPORTANT = 2
PRI_OPTIONAL = 4
PRI_REQUIRED = 1
PRI_STANDARD = 3
class Package(_mod_builtins.object):
    'Represent a package. A package is uniquely identified by its name\nand each package can have zero or more versions which can be\naccessed via the version_list property. Packages can be installed\nand removed by apt_pkg.DepCache.'
    __class__ = Package
    def __init__(self, *args, **kwargs):
        'Represent a package. A package is uniquely identified by its name\nand each package can have zero or more versions which can be\naccessed via the version_list property. Packages can be installed\nand removed by apt_pkg.DepCache.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def architecture(self):
        'The architecture of the package.'
        pass
    
    @property
    def current_state(self):
        'The current state, which can be compared against the constants\nCURSTATE_CONFIG_FILES, CURSTATE_HALF_CONFIGURED,\nCURSTATE_HALF_INSTALLED, CURSTATE_INSTALLED, CURSTATE_NOT_INSTALLED,\nCURSTATE_UNPACKED of the apt_pkg module.'
        pass
    
    @property
    def current_ver(self):
        'The version of the package currently installed or None.'
        pass
    
    @property
    def essential(self):
        'Boolean value determining whether the package is essential.'
        pass
    
    def get_fullname(self, pretty: bool=False):
        "get_fullname([pretty: bool = False]) -> str\n\nGet the full name of the package, including the architecture. If\n'pretty' is True, the architecture is omitted for native packages,\nthat is, and amd64 apt package on an amd64 system would give 'apt'."
        return ''
    
    @property
    def has_provides(self):
        'Whether the package is provided by at least one other package.'
        pass
    
    @property
    def has_versions(self):
        'Whether the package has at least one version in the cache.'
        pass
    
    @property
    def id(self):
        'The numeric ID of the package'
        pass
    
    @property
    def important(self):
        "Boolean value determining whether the package has the 'important'\nflag set ('Important: yes' in the Packages file). No longer used."
        pass
    
    @property
    def inst_state(self):
        'The state of the install, which be compared against the constants\nINSTSTATE_HOLD, INSTSTATE_HOLD_REINSTREQ, INSTSTATE_OK,\nINSTSTATE_REINSTREQ of the apt_pkg module.'
        pass
    
    @property
    def name(self):
        'The name of the package.'
        pass
    
    @property
    def provides_list(self):
        "A list of all packages providing this package. The list contains\ntuples in the format (providesname, providesver, version)\nwhere 'version' is an apt_pkg.Version object."
        pass
    
    @property
    def rev_depends_list(self):
        'An apt_pkg.DependencyList object of all reverse dependencies.'
        pass
    
    @property
    def section(self):
        'The section of the package.'
        pass
    
    @property
    def selected_state(self):
        'The state of the selection, which can be compared against the constants\nSELSTATE_DEINSTALL, SELSTATE_HOLD, SELSTATE_INSTALL, SELSTATE_PURGE,\nSELSTATE_UNKNOWN of the apt_pkg module.'
        pass
    
    @property
    def version_list(self):
        'A list of all apt_pkg.Version objects for this package.'
        pass
    

class PackageFile(_mod_builtins.object):
    'A package file is an index file stored in the cache with some\nadditional pieces of information.'
    __class__ = PackageFile
    def __init__(self, *args, **kwargs):
        'A package file is an index file stored in the cache with some\nadditional pieces of information.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def architecture(self):
        'The architecture of the package file. Unused, empty string nowadays.'
        pass
    
    @property
    def archive(self):
        "The archive of the package file (i.e. 'Suite' in the Release file)."
        pass
    
    @property
    def codename(self):
        'The codename of this package file (e.g. squeeze-updates).'
        pass
    
    @property
    def component(self):
        "The component of this package file (e.g. 'main')."
        pass
    
    @property
    def filename(self):
        'The path to the file.'
        pass
    
    @property
    def id(self):
        'The numeric ID of this PackageFile object.'
        pass
    
    @property
    def index_type(self):
        "A string describing the type of index. Known values are\n'Debian Package Index', 'Debian Translation Index', and\n'Debian dpkg status file'."
        pass
    
    @property
    def label(self):
        "The label set in the release file (e.g. 'Debian')."
        pass
    
    @property
    def not_automatic(self):
        'Whether the NotAutomatic flag is set in the Release file.'
        pass
    
    @property
    def not_source(self):
        'Whether this package file lacks an active (sources.list) source;packages listed in such a file cannot be downloaded.'
        pass
    
    @property
    def origin(self):
        'The origin set in the release file.'
        pass
    
    @property
    def site(self):
        'The hostname of the location this file comes from.'
        pass
    
    @property
    def size(self):
        'The size of the file.'
        pass
    
    @property
    def version(self):
        "The version set in the release file (e.g. '5.0.X' for lenny, where X\nis a point release)."
        pass
    

class PackageList(_mod_builtins.object):
    "A PackageList is an internally used structure to represent\nthe 'packages' attribute of apt_pkg.Cache objects in a more\nefficient manner by creating Package objects only when they\nare accessed."
    __class__ = PackageList
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        "A PackageList is an internally used structure to represent\nthe 'packages' attribute of apt_pkg.Cache objects in a more\nefficient manner by creating Package objects only when they\nare accessed."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class PackageManager(_PackageManager):
    "PackageManager(depcache: apt_pkg.DepCache)\n\nPackageManager objects allow the fetching of packages marked for\ninstallation and the installation of those packages. The parameter\n'depcache' specifies an apt_pkg.DepCache object where information\nabout the package selections is retrieved from.\n\nMethods in this class can be overridden in sub classes\nto implement behavior different from APT's dpkg implementation."
    __class__ = PackageManager
    def __init__(self, depcache: apt_pkg.DepCache):
        "PackageManager(depcache: apt_pkg.DepCache)\n\nPackageManager objects allow the fetching of packages marked for\ninstallation and the installation of those packages. The parameter\n'depcache' specifies an apt_pkg.DepCache object where information\nabout the package selections is retrieved from.\n\nMethods in this class can be overridden in sub classes\nto implement behavior different from APT's dpkg implementation."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def configure(self, pkg: Package):
        'configure(pkg: Package) -> bool \n\nAdd a configure action. Can be overridden in subclasses.\n\nNew in version 0.8.0.'
        return True
    
    def go(self, status_fd: int):
        'go(status_fd: int) -> bool \n\nStart dpkg. Can be overridden in subclasses.\n\nNew in version 0.8.0.'
        return True
    
    def install(self, pkg: Package, filename: str):
        'install(pkg: Package, filename: str) -> bool \n\nAdd a install action. Can be overridden in subclasses.\n\nNew in version 0.8.0.'
        return True
    
    def remove(self, pkg: Package, purge: bool):
        'remove(pkg: Package, purge: bool) -> bool \n\nAdd a removal action. Can be overridden in subclasses.\n\nNew in version 0.8.0.'
        return True
    
    def reset(self):
        'reset()\n\nReset the package manager for a new round.\nCan be overridden in subclasses.\n\nNew in version 0.8.0.'
        pass
    

class PackageRecords(_mod_builtins.object):
    'PackageRecords(cache: apt_pkg.Cache)\n\nPackage Records contain information about packages. Those objects\ncan be used to retrieve information such as maintainer or filename\nof a package. They can also be used to retrieve the raw records\nof the packages (i.e. those stanzas stored in Packages files).'
    __class__ = PackageRecords
    def __init__(self, cache: apt_pkg.Cache):
        'PackageRecords(cache: apt_pkg.Cache)\n\nPackage Records contain information about packages. Those objects\ncan be used to retrieve information such as maintainer or filename\nof a package. They can also be used to retrieve the raw records\nof the packages (i.e. those stanzas stored in Packages files).'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def filename(self):
        "The filename of the package, as stored in the 'Filename' field."
        pass
    
    @property
    def hashes(self):
        'The hashes of the packages, as a HashStringList'
        pass
    
    @property
    def homepage(self):
        "The homepage of the package, as stored in the 'Homepage' field."
        pass
    
    @property
    def long_desc(self):
        "The long description of the packages; i.e. all lines in the\n'Description' field except for the first one."
        pass
    
    def lookup(self, packagefile: apt_pkg.PackageFile, index: int):
        'lookup((packagefile: apt_pkg.PackageFile, index: int)) -> bool\n\nChanges to a new package'
        return True
    
    @property
    def maintainer(self):
        "The maintainer of the package, as stored in the 'Maintainer' field."
        pass
    
    @property
    def md5_hash(self):
        "The MD5 hash value of the package, as stored in the 'MD5Sum' field."
        pass
    
    @property
    def name(self):
        "The name of the package, as stored in the 'Package' field."
        pass
    
    @property
    def record(self):
        'The raw record, suitable for parsing by apt_pkg.TagSection.'
        pass
    
    @property
    def sha1_hash(self):
        "The SHA1 hash value, as stored in the 'SHA1' field."
        pass
    
    @property
    def sha256_hash(self):
        "The SHA256 hash value, as stored in the 'SHA256' field."
        pass
    
    @property
    def short_desc(self):
        "The short description of the package, i.e. the first line of the\n'Description' field."
        pass
    
    @property
    def source_pkg(self):
        "The name of the source package, if different from the name of the\nbinary package. This information is retrieved from the 'Source' field."
        pass
    
    @property
    def source_ver(self):
        "The version of the source package, if it differs from the version\nof the binary package. Just like 'source_pkg', this information\nis retrieved from the 'Source' field."
        pass
    

class Policy(_mod_builtins.object):
    'Policy(cache)\n\nRepresentation of the policy of the Cache object given by cache. This\nprovides a superset of policy-related functionality compared to the\nDepCache class. The DepCache can be used for most purposes, but there\nmay be some cases where a special policy class is needed.'
    __class__ = Policy
    def __init__(self, cache):
        'Policy(cache)\n\nRepresentation of the policy of the Cache object given by cache. This\nprovides a superset of policy-related functionality compared to the\nDepCache class. The DepCache can be used for most purposes, but there\nmay be some cases where a special policy class is needed.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def create_pin(self, type: str, pkg: str, data: str, priority: int):
        "create_pin(type: str, pkg: str, data: str, priority: int)\n\nCreate a pin for the policy. The parameter 'type' refers to one of the\nstrings 'Version', 'Release', or 'Origin'. The argument 'pkg' is the\nname of the package. The parameter 'data' refers to the value\n(e.g. 'unstable' for type='Release') and the other possible options.\nThe parameter 'priority' gives the priority of the pin."
        pass
    
    def get_candidate_ver(self):
        'get_match(package: apt_pkg.Package) -> apt_pkg.Version\n\nGet the best package for the job.'
        pass
    
    def get_match(self, package: apt_pkg.Package):
        'get_match(package: apt_pkg.Package) -> apt_pkg.Version\n\nReturn a matching version for the given package.'
        pass
    
    def get_priority(self, package: apt_pkg.Package):
        'get_priority(package: apt_pkg.Package) -> int\n\nReturn the priority of the package.'
        return 1
    
    def read_pindir(self, dirname: str):
        "read_pindir(dirname: str) -> bool\n\nRead the pin files in the given dir (e.g. '/etc/apt/preferences.d')\nand add them to the policy."
        return True
    
    def read_pinfile(self, filename: str):
        "read_pinfile(filename: str) -> bool\n\nRead the pin file given by filename (e.g. '/etc/apt/preferences')\nand add it to the policy."
        return True
    

class ProblemResolver(_mod_builtins.object):
    'ProblemResolver(depcache: apt_pkg.DepCache)\n\nProblemResolver objects take care of resolving problems\nwith dependencies. They mark packages for installation/\nremoval and try to satisfy all dependencies.'
    __class__ = ProblemResolver
    def __init__(self, depcache: apt_pkg.DepCache):
        'ProblemResolver(depcache: apt_pkg.DepCache)\n\nProblemResolver objects take care of resolving problems\nwith dependencies. They mark packages for installation/\nremoval and try to satisfy all dependencies.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def clear(self, pkg: apt_pkg.Package):
        'clear(pkg: apt_pkg.Package)\n\nRevert the actions done by protect()/remove() on the package.'
        pass
    
    def install_protect(self):
        'install_protect()\n\nInstall all protected packages.'
        pass
    
    def protect(self, pkg: apt_pkg.Package):
        'protect(pkg: apt_pkg.Package)\n\nMark the package as protected in the resolver, meaning that its\nstate will not be changed.'
        pass
    
    def remove(self, pkg: apt_pkg.Package):
        'remove(pkg: apt_pkg.Package)\n\nMark the package for removal in the resolver.'
        pass
    
    def resolve(self, fix_broken: bool=True):
        "resolve([fix_broken: bool = True]) -> bool\n\nTry to intelligently resolve problems by installing and removing\npackages. If 'fix_broken' is True, apt will try to repair broken\ndependencies of installed packages."
        return True
    
    def resolve_by_keep(self):
        'resolve_by_keep() -> bool\n\nTry to resolve problems only by using keep.'
        return True
    

REWRITE_PACKAGE_ORDER = _mod_builtins.list()
REWRITE_SOURCE_ORDER = _mod_builtins.list()
SELSTATE_DEINSTALL = 3
SELSTATE_HOLD = 2
SELSTATE_INSTALL = 1
SELSTATE_PURGE = 4
SELSTATE_UNKNOWN = 0
class SourceList(_mod_builtins.object):
    'SourceList()\n\nRepresent the list of sources stored in /etc/apt/sources.list and\nsimilar files.'
    __class__ = SourceList
    def __init__(self):
        'SourceList()\n\nRepresent the list of sources stored in /etc/apt/sources.list and\nsimilar files.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def find_index(self, pkgfile: apt_pkg.PackageFile):
        'find_index(pkgfile: apt_pkg.PackageFile) -> apt_pkg.IndexFile\n\nReturn the index file for the given package file, or None if none\ncould be found.'
        pass
    
    def get_indexes(self, acquire: apt_pkg.Acquire, all: bool=False):
        "get_indexes(acquire: apt_pkg.Acquire[, all: bool=False]) -> bool\n\nAdd all indexes (i.e. stuff like Release files, Packages files)\nto the Acquire object 'acquire'. If 'all' is True, all indexes\nwill be added, otherwise only changed indexes will be added."
        return True
    
    @property
    def list(self):
        'A list of MetaIndex() objects.'
        pass
    
    def read_main_list(self):
        'read_main_list() -> bool\n\nRead /etc/apt/sources.list and similar files to populate the list\nof indexes.'
        return True
    

class SourceRecordFiles(_mod_builtins.object):
    'SourceRecordFile()\n\nProvide an easy way to look up the src records of a source package.\n'
    __class__ = SourceRecordFiles
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self):
        'SourceRecordFile()\n\nProvide an easy way to look up the src records of a source package.\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def hashes(self):
        'The hashes of the source package file.'
        pass
    
    @property
    def path(self):
        'The remote path of the source package file.'
        pass
    
    @property
    def size(self):
        'The size of the source package file.'
        pass
    
    @property
    def type(self):
        'The type of the source package file.'
        pass
    

class SourceRecords(_mod_builtins.object):
    'SourceRecords()\n\nProvide an easy way to look up the records of source packages and\nprovide easy attributes for some widely used fields of the record.'
    __class__ = SourceRecords
    def __init__(self):
        'SourceRecords()\n\nProvide an easy way to look up the records of source packages and\nprovide easy attributes for some widely used fields of the record.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def binaries(self):
        'A list of the names of the binaries produced by this source package.'
        pass
    
    @property
    def build_depends(self):
        'A dictionary describing the build-time dependencies of the package;\nthe format is the same as used for apt_pkg.Version.depends_list_str.'
        pass
    
    @property
    def files(self):
        'A list of :class:`SourceRecordFiles` objects.'
        pass
    
    @property
    def index(self):
        'The index file associated with this record as a list of\napt_pkg.IndexFile objects.'
        pass
    
    def lookup(self, name: str):
        'lookup(name: str) -> bool\n\nLook up the source package with the given name. Each call moves\nthe position of the records parser forward. If there are no\nmore records, return None. If the lookup failed this way,\naccess to any of the attributes will result in an AttributeError.'
        return True
    
    @property
    def maintainer(self):
        'The maintainer of the package.'
        pass
    
    @property
    def package(self):
        'The name of the source package.'
        pass
    
    @property
    def record(self):
        'The raw record, suitable for parsing using apt_pkg.TagSection.'
        pass
    
    def restart(self):
        'restart()\n\nRestart the lookup process. This moves the parser to the first\npackage and lookups can now be made just like on a new object.'
        pass
    
    @property
    def section(self):
        'The section of the source package.'
        pass
    
    def step(self):
        'step() -> bool\n\nGo to the source package. Each call moves\nthe position of the records parser forward. If there are no\nmore records, return None. If the lookup failed this way,\naccess to any of the attributes will result in an AttributeError.'
        return True
    
    @property
    def version(self):
        'The version of the source package.'
        pass
    

class SystemLock(_mod_builtins.object):
    "SystemLock()\n\nContext manager for locking the package system. The lock is established\nas soon as the method __enter__() is called. It is released when\n__exit__() is called.\n\nThis should be used via the 'with' statement, for example:\n\n   with apt_pkg.SystemLock():\n       ...\n\nOnce the block is left, the lock is released automatically. The object\ncan be used multiple times:\n\n   lock = apt_pkg.SystemLock()\n   with lock:\n       ...\n   with lock:\n       ...\n\n"
    __class__ = SystemLock
    def __enter__(self):
        'Lock the system.'
        return self
    
    def __exit__(self):
        'Unlock the system.'
        pass
    
    def __init__(self):
        "SystemLock()\n\nContext manager for locking the package system. The lock is established\nas soon as the method __enter__() is called. It is released when\n__exit__() is called.\n\nThis should be used via the 'with' statement, for example:\n\n   with apt_pkg.SystemLock():\n       ...\n\nOnce the block is left, the lock is released automatically. The object\ncan be used multiple times:\n\n   lock = apt_pkg.SystemLock()\n   with lock:\n       ...\n   with lock:\n       ...\n\n"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

TIME = '11:49:15'
class Tag(_mod_builtins.object):
    'Tag\n\nIdentify actions to be executed on a task\n\nThis is used in conjunction with :meth:`TagSection.write` to rewrite\na tag section into a new one.\n\nThis class is abstract, use one of the subclasses:\n:class:`TagRewrite`, :class:`TagRemove`, :class:`TagRename`\n\n.. versionadded:: 1.1'
    REMOVE = 0
    RENAME = 1
    REWRITE = 2
    __class__ = Tag
    def __init__(self, *args, **kwargs):
        'Tag\n\nIdentify actions to be executed on a task\n\nThis is used in conjunction with :meth:`TagSection.write` to rewrite\na tag section into a new one.\n\nThis class is abstract, use one of the subclasses:\n:class:`TagRewrite`, :class:`TagRemove`, :class:`TagRename`\n\n.. versionadded:: 1.1'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def action(self):
        'The action to perform.'
        pass
    
    @property
    def data(self):
        'The data to write instead (for REWRITE), or the new tag name (RENAME)'
        pass
    
    @property
    def name(self):
        'The name of the tag to perform the action on.'
        pass
    

class TagFile(_mod_builtins.object):
    "TagFile(file, [bytes: bool = False])\n\nTagFile() objects provide access to debian control files, which consist\nof multiple RFC822-style sections.\n\nTo provide access to those sections, TagFile objects provide an iterator\nwhich yields TagSection objects for each section.\n\nTagFile objects also provide another API which uses a shared TagSection\nobject in the 'section' member. The functions step() and jump() can be\nused to navigate within the file; offset() returns the current\nposition.\n\nIt is important to not mix the use of both APIs, because this can have\nunwanted effects.\n\nThe parameter 'file' refers to an object providing a fileno() method or\na file descriptor (an integer).\n\nBy default, text read from files is treated as strings (binary data in\nPython 2, Unicode strings in Python 3). Use bytes=True to cause all\nheader values read from this TagFile to be bytes even in Python 3.\nHeader names are always treated as Unicode."
    __class__ = TagFile
    def __enter__(self):
        'Context manager entry, return self.'
        return self
    
    def __exit__(self):
        'Context manager exit, calls close.'
        pass
    
    def __init__(self, file, bytes: bool=False):
        "TagFile(file, [bytes: bool = False])\n\nTagFile() objects provide access to debian control files, which consist\nof multiple RFC822-style sections.\n\nTo provide access to those sections, TagFile objects provide an iterator\nwhich yields TagSection objects for each section.\n\nTagFile objects also provide another API which uses a shared TagSection\nobject in the 'section' member. The functions step() and jump() can be\nused to navigate within the file; offset() returns the current\nposition.\n\nIt is important to not mix the use of both APIs, because this can have\nunwanted effects.\n\nThe parameter 'file' refers to an object providing a fileno() method or\na file descriptor (an integer).\n\nBy default, text read from files is treated as strings (binary data in\nPython 2, Unicode strings in Python 3). Use bytes=True to cause all\nheader values read from this TagFile to be bytes even in Python 3.\nHeader names are always treated as Unicode."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return TagFile()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def close(self):
        'close()\n\nClose the file.'
        pass
    
    def jump(self, offset: int):
        "jump(offset: int) -> bool\n\nJump to the given offset; return True on success. Note that jumping to\nan offset is not very reliable, and the 'section' attribute may point\nto an unexpected section."
        return True
    
    def offset(self):
        'offset() -> int\n\nReturn the current offset.'
        return 1
    
    @property
    def section(self):
        'The current section, as a TagSection object.'
        pass
    
    def step(self):
        'step() -> bool\n\nStep forward in the file'
        return True
    

class TagRemove(Tag):
    'TagRemove(name: str)\n\nRemove the tag *name* from the tag section\n\n.. versionadded:: 1.1'
    __class__ = TagRemove
    def __init__(self, name: str):
        'TagRemove(name: str)\n\nRemove the tag *name* from the tag section\n\n.. versionadded:: 1.1'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class TagRename(Tag):
    'TagRename(old_name: str, new_name: str)\n\nRename the tag *old_name* to *new_name*\n\n.. versionadded:: 1.1'
    __class__ = TagRename
    def __init__(self, old_name: str, new_name: str):
        'TagRename(old_name: str, new_name: str)\n\nRename the tag *old_name* to *new_name*\n\n.. versionadded:: 1.1'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class TagRewrite(Tag):
    'TagRewrite(name: str, data: str)\n\nChange the value of the tag to the string passed in *data*\n\n.. versionadded:: 1.1'
    __class__ = TagRewrite
    def __init__(self, name: str, data: str):
        'TagRewrite(name: str, data: str)\n\nChange the value of the tag to the string passed in *data*\n\n.. versionadded:: 1.1'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class TagSection(_mod_builtins.object):
    'TagSection(text: str, [bytes: bool = False])\n\nProvide methods to access RFC822-style header sections, like those\nfound in debian/control or Packages files.\n\nTagSection() behave like read-only dictionaries and also provide access\nto the functions provided by the C++ class (e.g. find).\n\nBy default, text read from files is treated as strings (binary data in\nPython 2, Unicode strings in Python 3). Use bytes=True to cause all\nheader values read from this TagSection to be bytes even in Python 3.\nHeader names are always treated as Unicode.'
    __class__ = TagSection
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, text: str, bytes: bool=False):
        'TagSection(text: str, [bytes: bool = False])\n\nProvide methods to access RFC822-style header sections, like those\nfound in debian/control or Packages files.\n\nTagSection() behave like read-only dictionaries and also provide access\nto the functions provided by the C++ class (e.g. find).\n\nBy default, text read from files is treated as strings (binary data in\nPython 2, Unicode strings in Python 3). Use bytes=True to cause all\nheader values read from this TagSection to be bytes even in Python 3.\nHeader names are always treated as Unicode.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def bytes(self):
        'bytes() -> int\n\nReturn the number of bytes this section is large.'
        return 1
    
    def find(self, name: str, default=None):
        "find(name: str[, default = None]) -> str\n\nFind the key given by 'name' and return the value. If the key can\nnot be found, return 'default'."
        return ''
    
    def find_flag(self, name: str):
        "find_flag(name: str) -> int\n\nReturn 1 if the key's value is 'yes' or a similar value describing\na boolean true. If the field does not exist, or does not have such a\nvalue, return 0."
        return 1
    
    def find_raw(self):
        "find_raw(name: str[, default = None] -> str\n\nSame as find(), but returns the complete 'key: value' field; instead of\njust the value."
        return ''
    
    def get(self):
        "find(name: str[, default = None]) -> str\n\nFind the key given by 'name' and return the value. If the key can\nnot be found, return 'default'."
        return ''
    
    def keys(self):
        'keys() -> list\n\nReturn a list of all keys.'
        return list()
    

VERSION = '1.6.11'
class Version(_mod_builtins.object):
    'Version Object'
    MULTI_ARCH_ALL = 1
    MULTI_ARCH_ALLOWED = 8
    MULTI_ARCH_ALL_ALLOWED = 9
    MULTI_ARCH_ALL_FOREIGN = 3
    MULTI_ARCH_FOREIGN = 2
    MULTI_ARCH_NO = 0
    MULTI_ARCH_NONE = 0
    MULTI_ARCH_SAME = 4
    __class__ = Version
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, *args, **kwargs):
        'Version Object'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def arch(self):
        'The architecture of this specific version of the package.'
        pass
    
    @property
    def depends_list(self):
        "A dictionary mapping dependency types to lists (A) of lists (B) of\napt_pkg.Dependency objects. The lists (B) represent or dependencies\nlike 'a || b'."
        pass
    
    @property
    def depends_list_str(self):
        "Same as depends_list, except that the apt_pkg.Dependency objects\nare 3-tuples of the form (name, version, operator); where operator\nis one of '<', '<=', '=', '>=', '>'."
        pass
    
    @property
    def downloadable(self):
        'Whether the version can be downloaded.'
        pass
    
    @property
    def file_list(self):
        'A list of tuples (packagefile: apt_pkg.PackageFile, index: int) for the\nPackageFile objects related to this package. The index can be used\nto retrieve the record of this package version.'
        pass
    
    @property
    def hash(self):
        'The numeric hash of the version used in the internal storage.'
        pass
    
    @property
    def id(self):
        'The numeric ID of the package.'
        pass
    
    @property
    def installed_size(self):
        'The installed size of this package version.'
        pass
    
    @property
    def multi_arch(self):
        'Multi-arch state of this package, as an integer. See\nthe various MULTI_ARCH_* members.'
        pass
    
    @property
    def parent_pkg(self):
        'The parent package of this version.'
        pass
    
    @property
    def priority(self):
        'The priority of the package as an integer, which can be compared to\nthe constants PRI_EXTRA, PRI_IMPORTANT, PRI_OPTIONAL, PRI_REQUIRED,\nPRI_STANDARD of the apt_pkg module.'
        pass
    
    @property
    def priority_str(self):
        'The priority of the package, as a string.'
        pass
    
    @property
    def provides_list(self):
        "A list of all packages provided by this version. The list contains\ntuples in the format (providesname, providesver, version)\nwhere 'version' is an apt_pkg.Version object."
        pass
    
    @property
    def section(self):
        'The section of this package version.'
        pass
    
    @property
    def size(self):
        'The size of the package file.'
        pass
    
    @property
    def translated_description(self):
        'An apt_pkg.Description object for the translated description if\navailable or the untranslated fallback.'
        pass
    
    @property
    def ver_str(self):
        'The version string.'
        pass
    

_C_API = _mod_builtins.PyCapsule()
class _PackageManager(_mod_builtins.object):
    '_PackageManager objects allow the fetching of packages marked for\ninstallation and the installation of those packages.\nThis is an abstract base class that cannot be subclassed\nin Python. The only subclass is apt_pkg.PackageManager. This\nclass is an implementation-detail and not part of the API.'
    RESULT_COMPLETED = 0
    RESULT_FAILED = 1
    RESULT_INCOMPLETE = 2
    __class__ = _PackageManager
    def __init__(self, *args, **kwargs):
        '_PackageManager objects allow the fetching of packages marked for\ninstallation and the installation of those packages.\nThis is an abstract base class that cannot be subclassed\nin Python. The only subclass is apt_pkg.PackageManager. This\nclass is an implementation-detail and not part of the API.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def do_install(self, status_fd: int):
        'do_install(status_fd: int) -> int\n\nInstall the packages and return one of the class constants\nRESULT_COMPLETED, RESULT_FAILED, RESULT_INCOMPLETE. The argument\nstatus_fd can be used to specify a file descriptor that APT will\nwrite status information on (see README.progress-reporting in the\napt source code for information on what will be written there).'
        return 1
    
    def fix_missing(self):
        'fix_missing() -> bool\n\nFix the installation if a package could not be downloaded.'
        return True
    
    def get_archives(self, fetcher: Acquire, list: SourceList, recs: PackageRecords):
        "get_archives(fetcher: Acquire, list: SourceList, recs: PackageRecords) -> bool\n\nDownload the packages marked for installation via the Acquire object\n'fetcher', using the information found in 'list' and 'recs'."
        return True
    

__doc__ = 'Classes and functions wrapping the apt-pkg library.\n\nThe apt_pkg module provides several classes and functions for accessing\nthe functionality provided by the apt-pkg library. Typical uses might\ninclude reading APT index files and configuration files and installing\nor removing packages.'
__file__ = '/usr/lib/python3/dist-packages/apt_pkg.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'apt_pkg'
__package__ = ''
def base64_encode(value: bytes):
    'base64_encode(value: bytes) -> str\n\nEncode the given bytestring into Base64. The input may not\ncontain a null byte character (use the base64 module for this).'
    return ''

def check_dep(pkg_ver: str, dep_op: str, dep_ver: str):
    "check_dep(pkg_ver: str, dep_op: str, dep_ver: str) -> bool\n\nCheck that the given requirement is fulfilled; i.e. that the version\nstring given by 'pkg_ver' matches the version string 'dep_ver' under\nthe condition specified by the operator 'dep_op' (<,<=,=,>=,>).\n\nReturn True if 'pkg_ver' matches 'dep_ver' under the\ncondition 'dep_op'; for example, this returns True:\n\n    apt_pkg.check_dep('1', '<=', '2')"
    return True

def check_domain_list(host: str, domains: str):
    "check_domain_list(host: str, domains: str) -> bool\n\nCheck if the host given by 'host' belongs to one of the domains\nspecified in the comma separated string 'domains'. An example\nwould be:\n\n    check_domain_list('alioth.debian.org','debian.net,debian.org')\n\nwhich would return True because alioth belongs to debian.org."
    return True

config = Configuration()
def dequote_string(string: str):
    "dequote_string(string: str) -> str\n\nDequote the given string by replacing all HTTP encoded values such\nas '%20' with their decoded value (in this case, ' ')."
    return ''

def get_architectures():
    'get_architectures() -> list\n\nReturn the list of supported architectures on this system. On a \nmultiarch system this can be more than one. The main architectures\nis the first item in the list.'
    return list()

def get_lock(file: str, errors: bool):
    "get_lock(file: str, errors: bool) -> int\n\nCreate an empty file of the given name and lock it. If the locking\nsucceeds, return the file descriptor of the lock file. Afterwards,\nlocking the file from another process will fail and thus cause\nget_lock() to return -1 or raise an Error (if 'errors' is True).\n\nFrom Python 2.6 on, it is recommended to use the context manager\nprovided by apt_pkg.FileLock instead using the with-statement."
    return 1

def gettext(msg: str, domain: str='python-apt'):
    "gettext(msg: str[, domain: str = 'python-apt']) -> str\n\nTranslate the given string. This is much faster than Python's version\nand only does translations after setlocale() has been called."
    return ''

def init():
    'init()\n\nShorthand for doing init_config() and init_system(). When working\nwith command line arguments, first call init_config() then parse\nthe command line and finally call init_system().'
    pass

def init_config():
    'init_config()\n\nLoad the default configuration and the config file.'
    pass

def init_system():
    'init_system()\n\nConstruct the apt_pkg system.'
    pass

def md5sum(object):
    "md5sum(object) -> str\n\nReturn the md5sum of the object. 'object' may either be a string, in\nwhich case the md5sum of the string is returned, or a file() object\n(or file descriptor), in which case the md5sum of its contents is\nreturned."
    return ''

def open_maybe_clear_signed_file(file: str):
    'open_maybe_clear_signed_file(file: str) -> int\n\nOpen a file and ignore a PGP clear signature.\nReturn a open file descriptor or a error.'
    return 1

def parse_commandline():
    "parse_commandLine(config: Configuration, options: list, argv: list) -> list\n\nParse the command line in 'argv' into the configuration space. The\nlist 'options' contains a list of 3-tuples or 4-tuples in the form:\n\n   (short_option: str, long_option: str, variable: str[, type: str])\n\nThe element 'short_option' is one character, the 'long_option' element\nis the name of the long option, the element 'variable' the name of the\nconfiguration option the result will be stored in and type is one of\n'HasArg', 'IntLevel', 'Boolean', 'InvBoolean', 'ConfigFile',\n'ArbItem'. The default type is 'Boolean'. Read the online documentation\nin python-apt-doc and its tutorial on writing an apt-cdrom clone for more\ndetails."
    return list()

def parse_depends(s: str, strip_multi_arch: bool=True, architecture: string=None):
    "parse_depends(s: str[, strip_multi_arch : bool = True[, architecture : string]]) -> list\n\nParse the dependencies given by 's' and return a list of lists. Each of\nthese lists represents one or more options for an 'or' dependency in\nthe form of '(pkg, ver, comptype)' tuples. The tuple element 'pkg'\nis the name of the package; the element 'ver' is the version, or ''\nif no version was requested. The element 'ver' is a comparison\noperator ('<', '<=', '=', '>=', or '>').\n\nIf 'strip_multi_arch' is True, :any (and potentially other special values)\nwill be stripped from the full package nameThe 'architecture' parameter may be used to specify a non-native architecture\nfor the dependency parsing."
    return list()

def parse_src_depends(s: str, strip_multi_arch: bool=True, architecture: string=None):
    "parse_src_depends(s: str[, strip_multi_arch : bool = True[, architecture : string]]) -> list\n\nParse the dependencies given by 's' and return a list of lists. Each of\nthese lists represents one or more options for an 'or' dependency in\nthe form of '(pkg, ver, comptype)' tuples. The tuple element 'pkg'\nis the name of the package; the element 'ver' is the version, or ''\nif no version was requested. The element 'ver' is a comparison\noperator ('<', '<=', '=', '>=', or '>').\n\nDependencies may be restricted to certain architectures and the result\nonly contains those dependencies for the architecture set in the\nconfiguration variable APT::Architecture\n\nIf 'strip_multi_arch' is True, :any (and potentially other special values)\nwill be stripped from the full package nameThe 'architecture' parameter may be used to specify a non-native architecture\nfor the dependency parsing."
    return list()

def pkgsystem_is_locked():
    'pkgsystem_is_locked() -> bool\n\nCheck if the system is locked. Can be used to check whether the inner\nlock needs to be released or not in generic code.\n\n.. versionadded:: 1.6.3\n\n.. versionadded:: 1.7'
    return True

def pkgsystem_lock():
    'pkgsystem_lock() -> bool\n\nAcquire the global lock for the package system by using /var/lib/dpkg/lock-frontend\nand /var/lib/dpkg/lock to do the locking. From Python 2.6 on, the apt_pkg.SystemLock context\nmanager is available and should be used instead.'
    return True

def pkgsystem_lock_inner():
    "pkgsystem_lock_inner() -> bool\n\nReacquire the dpkg 'lock' lock file. Must be called only after\n:meth:`pkgsystem_unlock_inner` and only around invocations of dpkg.\n\n.. versionadded:: 1.6.3\n\n.. versionadded:: 1.7"
    return True

def pkgsystem_unlock():
    'pkgsystem_unlock() -> bool\n\nRelease the global lock for the package system.'
    return True

def pkgsystem_unlock_inner():
    "pkgsystem_unlock_inner() -> bool\n\nRelease the dpkg lock file 'lock'. To be called before manually\ninvoking dpkg.\n\n.. versionadded:: 1.6.3\n\n.. versionadded:: 1.7"
    return True

def quote_string(string: str, repl: str):
    "quote_string(string: str, repl: str) -> str\n\nEscape the string 'string', replacing any character not allowed in a URLor specified by 'repl' with its ASCII value preceded by a percent sign(so for example ' ' becomes '%20')."
    return ''

def read_config_dir(configuration: apt_pkg.Configuration, dirname: str):
    "read_config_dir(configuration: apt_pkg.Configuration, dirname: str)\n\nRead all configuration files in the dir given by 'dirname' in the\ncorrect order."
    pass

def read_config_file(configuration: apt_pkg.Configuration, filename: str):
    "read_config_file(configuration: apt_pkg.Configuration, filename: str)\n\nRead the configuration file 'filename' and set the appropriate\noptions in the configuration object."
    pass

def read_config_file_isc():
    "read_config_file(configuration: apt_pkg.Configuration, filename: str)\n\nRead the configuration file 'filename' and set the appropriate\noptions in the configuration object."
    pass

def rewrite_section(section: TagSection, order: list, rewrite_list: list):
    'rewrite_section(section: TagSection, order: list, rewrite_list: list) -> str\n\nRewrite the section given by *section* using *rewrite_list*, and order the\nfields according to *order*.\n\nThe parameter *order* is a :class:`list` object containing the names of the\nfields in the order they should appear in the rewritten section.\n:data:`apt_pkg.REWRITE_PACKAGE_ORDER` and\n:data:`apt_pkg.REWRITE_SOURCE_ORDER` are two predefined lists for rewriting\npackage and source sections, respectively.\n\nThe parameter *rewrite_list* is a list of tuples of the form\n``(tag, newvalue[, renamed_to])``, where *tag* describes the field which\nshould be changed, *newvalue* the value which should be inserted or\n``None`` to delete the field, and the optional *renamed_to* can be used\nto rename the field.\n\n.. deprecated:: 1.1\n\n    Replaced by :meth:`TagSection.write`'
    return ''

def sha1sum(object):
    "sha1sum(object) -> str\n\nReturn the sha1sum of the object. 'object' may either be a string, in\nwhich case the sha1sum of the string is returned, or a file() object\n(or file descriptor), in which case the sha1sum of its contents is\nreturned."
    return ''

def sha256sum(object):
    "sha256sum(object) -> str\n\nReturn the sha256sum of the object. 'object' may either be a string, in\nwhich case the sha256sum of the string is returned, or a file() object\n(or file descriptor), in which case the sha256sum of its contents is\nreturned."
    return ''

def sha512sum(object):
    "sha512sum(object) -> str\n\nReturn the sha512sum of the object. 'object' may either be a string, in\nwhich case the sha512sum of the string is returned, or a file() object\n(or file descriptor), in which case the sha512sum of its contents is\nreturned."
    return ''

def size_to_str(bytes: int):
    "size_to_str(bytes: int) -> str\n\nReturn a string describing the size in a human-readable manner using\nSI prefix and base-10 units, e.g. '1k' for 1000, '1M' for 1000000, etc."
    return ''

def str_to_time(rfc_time: str):
    'str_to_time(rfc_time: str) -> int\n\nConvert the given RFC 1123 formatted string to a Unix timestamp.'
    return 1

def string_to_bool(string: str):
    "string_to_bool(string: str) -> int\n\nReturn 1 if the string is a value such as 'yes', 'true', '1';\n0 if the string is a value such as 'no', 'false', '0'; -1 if\nthe string is not recognized."
    return 1

def time_rfc1123(unixtime: int):
    'time_rfc1123(unixtime: int) -> str\n\nFormat the given Unix time according to the requirements of\nRFC 1123.'
    return ''

def time_to_str(seconds: int):
    'time_to_str(seconds: int) -> str\n\nReturn a string describing the number of seconds in a human\nreadable manner using days, hours, minutes and seconds.'
    return ''

def upstream_version(ver: str):
    "upstream_version(ver: str) -> str\n\nReturn the upstream version for the package version given by 'ver'."
    return ''

def uri_to_filename(uri: str):
    "uri_to_filename(uri: str) -> str\n\nReturn a filename based on the given URI after replacing some\nparts not suited for filenames (e.g. '/')."
    return ''

def version_compare(a: str, b: str):
    "version_compare(a: str, b: str) -> int\n\nCompare the given versions; return a strictly negative value if 'a' is \nsmaller than 'b', 0 if they are equal, and a strictly positive value if\n'a' is larger than 'b'."
    return 1

