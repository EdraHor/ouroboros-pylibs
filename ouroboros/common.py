import os
import sys
import io
import json
import time
import struct
import shutil
import asyncio
import traceback
import configparser
import xml.etree.ElementTree as ET
try:
    import xmltodict
except ImportError:    # only used by XML helpers the decompiler does not call
    xmltodict = None

from ctypes import cdll, byref

if sys.platform == 'win32':
    from ctypes import windll
    from ctypes import wintypes
    from ctypes.wintypes import *

ANSI_CODE_PAGE = 'mbcs'
