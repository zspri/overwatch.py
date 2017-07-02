######################################
# Overwatch.py                       #
# A basic wrapper
# Version 0.1.0                      #
# Copyright (C) Nanomotion 2017      #
# See the LICENSE file for more info #
######################################

__title__ = 'overwatchpy'
__author__ = 'Nanomotion'
__license__ = 'MIT'
__copyright__ = 'Copyright (C) 2017 Nanomotion'
__version__ = '0.1.0'

from .objects import *
from . import core, Data
from .errors import errors

import logging

__logger__ = logging.getLogger(__name__)