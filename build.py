#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, os
import makefile

#--- Change dir to script absolute path
scriptDir = os.path.dirname (os.path.abspath (sys.argv [0]))
os.chdir (scriptDir)
#--- Build python makefile
make = makefile.Make ()
#--- Add C files compile rule
sourceList = ["main.c", "myRoutine.c"]
objectList = []
for source in sourceList:
#--- Compile
  object = "objects/" + source + ".o"
  depObject = object + ".dep"
  objectList.append (object)
  rule = makefile.Rule (object, "Compiling " + source)
  rule.mDependences.append (source)
  rule.mCommand.append ("gcc")
  rule.mCommand += ["-c", source]
  rule.mCommand += ["-o", object]
  rule.mCommand += ["-MD", "-MP", "-MF", depObject]
  rule.enterSecondaryDependanceFile (depObject)
  rule.mPriority = os.path.getsize (scriptDir + "/" + source)
  make.addRule (rule)
#--- Add linker rule
product = "myRoutine"
rule = makefile.Rule (product, "Linking " + product)
rule.mDependences += objectList
rule.mCommand += ["gcc"]
rule.mCommand += objectList
rule.mCommand += ["-o", product]
make.addRule (rule)
#--- Print rules
#make.printRules ()
#--- Add goals
make.addGoal ("all", [product], "Building all")
make.addGoal ("compile", objectList, "Compile C files")
#make.printGoals ()
#--- Get goal as first argument
goal = "all"
if len (sys.argv) > 1 :
  goal = sys.argv [1]
#--- Get max parallel jobs as second argument
maxParallelJobs = 0 # 0 means use host processor count
if len (sys.argv) > 2 :
  maxParallelJobs = int (sys.argv [2])
make.runGoal (goal, maxParallelJobs, maxParallelJobs == 1)
#--- Build Ok ?
make.printErrorCountAndExitOnError ()
