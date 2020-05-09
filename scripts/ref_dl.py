import sys, os
import DLFCN

if hasattr(sys, "setdlopenflags"):
    dlopen_flags = sys.getdlopenflags()
    sys.setdlopenflags(dlopen_flags | DLFCN.RTLD_GLOBAL)

try:
    import hou
except ImportError:
    sys.path.append("/opt/hfs18.0.416/houdini/python2.7libs")
    import hou
    print hou.houdiniPath()
finally:
    if hasattr(sys, "setdlopenflags"):
        sys.setdlopenflags(dlopen_flags)