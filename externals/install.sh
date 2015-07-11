#!/bin/bash
#install Runtimes libs

logFilePath="/var/log/f2c-install-eventagent.log"

cwd=$(cd "$(dirname "$0")"; pwd)
external_libs=`ls -l | grep -v total | grep -v install | awk '{print $9}'`
if [ ! -n "$external_libs" ]; then
    external_libs=`ls -l | grep -v total | grep -v install | awk '{print $8}'`
else
    echo "external libs exist"
fi

which python2.7 > /dev/null 2>&1
if [ $? == 0 ];then
    echo "python2.7 exists"
else
    ln -sv `which python` /usr/bin/python2.7
fi
for lib_dir_path in $external_libs
do
    echo installing $lib_dir_path
    echo $lib_dir_path
    cd $cwd/$lib_dir_path
    python2.7 setup.py install 2>&1 >> $logFilePath
    echo $lib_dir_path install done!
done