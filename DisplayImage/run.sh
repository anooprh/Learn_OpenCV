#!/bin/bash

#############################
# Helper Debug function
# _DEBUG="on" 

function _ECHO_MSG() {
 [ "$_DEBUG" == "on" ] &&  echo $@
}

#############################
# Find the base directory and project name
pushd `dirname $0` > /dev/null

PROJDIR=`pwd -P`
PROJECT_NAME=$(basename "$PROJDIR")

popd > /dev/null
_ECHO_MSG "Project Directory: $PROJDIR"
_ECHO_MSG "Project Name: $PROJECT_NAME"

#############################
# Build the project if not built

pushd `pwd` > /dev/null
if [ ! -d "$PROJDIR/build" ]; then
  _ECHO_MSG "Not built previously, building project: $PROJECT_NAME"
  mkdir $PROJDIR/build
  cd $PROJDIR/build
  cmake ..
  make
else
  _ECHO_MSG "Project $PROJECT_NAME built previously, skipping build"
  cd $PROJDIR/build
fi

popd > /dev/null
#############################
# Determine if any inputs args are passed

if [ ! $# -eq 0 ]; then
    _ECHO_MSG "Input arguments supplied, passing it to the binary executable ${PROJECT_NAME}"
	ARGS="$@"
else
    _ECHO_MSG "No input arguments supplied, supplying default input(s)"	
	ARGS="$PROJDIR/../data/images/cat_sample.jpg"  #This is the only thing specific to this project

fi
#############################
# Execute Command
CMD="${PROJDIR}/build/${PROJECT_NAME} ${ARGS}"

_ECHO_MSG "Executing $CMD"

`$CMD`

_ECHO_MSG "Done..."
#############################

