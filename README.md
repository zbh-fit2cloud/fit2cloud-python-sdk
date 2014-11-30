fit2cloud-python-sdk
====================

安装
======================================
git clone git@github.com:fit2cloud/fit2cloud-python-sdk.git
cd fit2cloud-python-sdk
./f2cs.py <command> [<args>]

用法
======================================
    ./f2cs.py <command> [<args>]
    
命令
======================================
    config
    listClusters
    listClusterVmGroups
    listClusterServers
    listClusterVmGroupServers

例子
======================================
    ./f2cs.py config --endpoint=<endpoint> --id=<access key id> --secret=<access key secret>
    ./f2cs.py listClusters
    ./f2cs.py listClusterVmGroups --cluster-id=<集群Id>
    ./f2cs.py listClusterVms --cluster-id=<集群Id>
    ./f2cs.py listClusterVmGroupVms --cluster-id=<集群Id> --cluster-vmgroup-id=<集群虚拟机组Id>
    ./f2cs.py getServerInfo --cluster-id=<集群Id> --server-id=<虚拟机Id>
    ./f2cs.py -h | --help
    ./f2cs.py -v | --version

说明
======================================

    集群Id可以从Web控制台找到
    虚拟机Id可以从listClusterVms命令结果中找到，或从Web控制台虚拟机列表页第一列，这个虚拟机Id为整数类型，如12168
    acccess key id和access key secret可以从Web控制台找到，点击右上角用户名，从下拉菜单中选择API信息.
    ./f2cs.py config --endpoint=https://aliyun.fit2cloud.com:8443/rest/ --id=Km20dL0jaJ91XebnbWFpbC5jb20= --secret=3e27563j-e362-4v11-b222-c453dyc70768
    ./f2cs.py listClusters
    ./f2cs.py listClusterVmGroups --cluster-id=16
    ./f2cs.py listClusterVms --cluster-id=16
    ./f2cs.py listClusterVmGroupVms --cluster-id=16 --cluster-vmgroup-id=64
    ./f2cs.py getServerInfo --cluster-id=16 --server-id=12168

