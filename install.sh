#!/bin/bash

function validateRunAsRoot
{
  currentuser=`whoami`
  if [ "$currentuser" == "root" ];then
      echo `date "+%Y-%m-%d %H:%M:%S"`": 运行用户检查通过，当前用户为root"
  else
      echo `date "+%Y-%m-%d %H:%M:%S"`": 错误: 当前导入主机脚本需要以root用户运行，请切换到root用户下再执行!"
      exit 1
  fi
}
validateRunAsRoot

cwd=$(cd "$(dirname "$0")"; pwd)

cp $cwd/f2cs.py /usr/bin/f2cs
cp $cwd/cacert.pem /usr/bin/cacert.pem 
