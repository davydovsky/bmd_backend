#!/bin/sh

set -e

PROJECTNAME=bmd
HOMEDIR=/opt/$PROJECTNAME

if ! getent group $PROJECTNAME 2>/dev/null ; then
    groupadd -r $PROJECTNAME 2>/dev/null
fi

if ! getent passwd $PROJECTNAME 2>/dev/null ; then
    useradd -r -g $PROJECTNAME -m -d $HOMEDIR $PROJECTNAME 2>/dev/null
fi

if [ ! -d $HOMEDIR ] ; then
    mkdir -p $HOMEDIR
fi
chown $PROJECTNAME:$PROJECTNAME $HOMEDIR

mkdir -p /var/log/$PROJECTNAME
chown -R $PROJECTNAME:$PROJECTNAME /var/log/$PROJECTNAME