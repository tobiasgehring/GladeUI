#!/usr/bin/env python

# Name: setup.py
# Purpose: GladeWindow distutils install program
# Author: Tobias Gehring <mail@tobiasgehring.de>
#
# Copyright 2015


NAME    = 'GladeWindow'
VERSION = '0.1'

AUTHOR       = 'Tobias Gehring'
AUTHOR_EMAIL = 'mail@tobiasgehring.de'

LICENSE    = 'LGPLv3'
DESCRPTION = 'A library for helping loading GTK3 GUIs from glade files easily'

PACKAGE_DIR = {'': 'lib'}
PY_MODULES  = ['GladeWindow']

execfile('metasetup.py')
