#! /usr/bin/env python
# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------*

import sys, os, shutil, filecmp

#-----------------------------------------------------------------------------*

#--- Get script absolute path
scriptDir = os.path.dirname (os.path.abspath (sys.argv [0]))
os.chdir (scriptDir)
#--- Destinations
destinations = [
  "/Volumes/dev-svn/dev-lpc2294/dev-files/python-scripts",
  "/Volumes/dev-svn/galgas/libpm/python-makefiles",
  "/Volumes/dev-svn/plm/embedded-sources"
]
#---
source = os.path.abspath (scriptDir + "/makefile.py")
for dest in destinations:
  destPath = dest + "/makefile.py"
  if (not os.path.exists (destPath)) or not filecmp.cmp (source, destPath) :
    print "Updating '" + destPath + "'"
    shutil.copyfile (source, destPath)


#-----------------------------------------------------------------------------*
