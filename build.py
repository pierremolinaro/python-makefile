#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, os
import makefile

#--- Change dir to script absolute path
scriptDir = os.path.dirname (os.path.abspath (sys.argv [0]))
os.chdir (scriptDir)
#--- Get goal as first argument
goal = "all"
if len (sys.argv) > 1 :
  goal = sys.argv [1]
#--- Build python makefile
make = makefile.Make (goal)
make.mMacTextEditor = "TextWrangler"
#--- Add C files compile rule
sourceList = ["main.c", "myRoutine.c"]
objectList = []
for source in sourceList:
#--- Add compile rules
  object = "objects/" + source + ".o"
  depObject = object + ".dep"
  objectList.append (object)
  rule = makefile.Rule ([object], "Compiling " + source) # Release 2
  rule.deleteTargetDirectoryOnClean ()
  rule.mDependences.append (source)
  rule.mCommand.append ("gcc")
  rule.mCommand += ["-c", source]
  rule.mCommand += ["-o", object]
  rule.mCommand += ["-MD", "-MP", "-MF", depObject]
  rule.enterSecondaryDependanceFile (depObject, make)
  rule.mPriority = os.path.getsize (scriptDir + "/" + source)
  rule.mOpenSourceOnError = True
  make.addRule (rule)
#--- Add linker rule
product = "myRoutine"
mapFile = product + ".map"
rule = makefile.Rule ([product, mapFile], "Linking " + product) # Release 2
rule.mDeleteTargetOnError = True
rule.deleteTargetFileOnClean ()
rule.mDependences += objectList
rule.mCommand += ["gcc"]
rule.mCommand += objectList
rule.mCommand += ["-o", product]
rule.mCommand += ["-Wl,-map," + mapFile]
postCommand = makefile.PostCommand ("Stripping " + product)
postCommand.mCommand += ["strip", "-A", "-n", "-r", "-u", product]
rule.mPostCommands.append (postCommand)
make.addRule (rule)
#--- Print rules
# make.printRules ()
# make.writeRuleDependancesInDotFile ("make-deps.dot")
make.checkRules ()
#--- Add goals
make.addGoal ("all", [product, mapFile], "Building all")
make.addGoal ("compile", objectList, "Compile C files")
#make.simulateClean ()
#make.printGoals ()
#--- Get max parallel jobs as second argument
maxParallelJobs = 0 # 0 means use host processor count
if len (sys.argv) > 2 :
  maxParallelJobs = int (sys.argv [2])
make.runGoal (maxParallelJobs, maxParallelJobs == 1)
#--- Build Ok ?
make.printErrorCountAndExitOnError ()
