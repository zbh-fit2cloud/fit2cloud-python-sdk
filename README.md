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
    listClusterVms
    listClusterVmGroupVms

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

输出示例
======================================

 ./f2cs.py listClusters
 [
  {
    "status": "TERMINATED",
    "credentialName": "default-key",
    "serverNumber": null,
    "name": "autotest-cluster",
    "cloudName": "default-test",
    "envType": "development",
    "cloudId": 3,
    "clusterType": "autotest",
    "id": 7,
    "credentialId": 3,
    "rabbitmqExchange": "exchange_down_7_1cedc8e5",
    "roleNumber": null,
    "created": 1404285505000,
    "totalFee": 36.085,
    "price": null,
    "groupId": 32,
    "launched": 1417302000000,
    "description": "\u81ea\u52a8\u5316\u9a8c\u6536\u6d4b\u8bd5\u96c6\u7fa4"
  },
  {
    "status": "TERMINATED",
    "credentialName": "default-key",
    "serverNumber": null,
    "name": "stability-test",
    "cloudName": "default-dev",
    "envType": "development",
    "cloudId": 2,
    "clusterType": "stability-test",
    "id": 16,
    "credentialId": 3,
    "rabbitmqExchange": "exchange_down_16_ae850ca5",
    "roleNumber": null,
    "created": 1405261884000,
    "totalFee": 881.84,
    "price": null,
    "groupId": 32,
    "launched": 1417366122000,
    "description": "\u7a33\u5b9a\u6027\u6d4b\u8bd5\u96c6\u7fa4"
  },
  {
    "status": "TERMINATED",
    "credentialName": "default-key",
    "serverNumber": null,
    "name": "ecommerce0922",
    "cloudName": "default-dev",
    "envType": "development",
    "cloudId": 2,
    "clusterType": "ecommerce",
    "id": 10042,
    "credentialId": 3,
    "rabbitmqExchange": "exchange_down_10042_2402839b",
    "roleNumber": null,
    "created": 1411391056000,
    "totalFee": 121.83,
    "price": null,
    "groupId": 32,
    "launched": 1415840881000,
    "description": ""
  },
  {
    "status": "TERMINATED",
    "credentialName": "default-key",
    "serverNumber": null,
    "name": "autoscaling",
    "cloudName": "default-dev",
    "envType": "development",
    "cloudId": 2,
    "clusterType": "test",
    "id": 10043,
    "credentialId": 3,
    "rabbitmqExchange": "exchange_down_10043_7d932f43",
    "roleNumber": null,
    "created": 1411472145000,
    "totalFee": 253.8,
    "price": null,
    "groupId": 32,
    "launched": 1417227130000,
    "description": ""
   }
 ]

 ./f2cs.py listClusterVMGroups --cluster-id=16
 [
  {
    "vmNumber": 1,
    "loadBalancerBandwidth": 1000,
    "serverRoleId": 30,
    "clusterId": 16,
    "imageId": "ubuntu1204_64_20G_aliaegis_20140926.vhd",
    "loadBalancerId": "\u65e0",
    "serverRoleName": "ubuntu-beijing",
    "lastScaleTime": null,
    "id": 64,
    "zone": "",
    "launchDelay": 0,
    "instanceType": "ecs.t1.xsmall",
    "imageName": "ubuntu1204-20140926",
    "image": 3,
    "internetBandwidth": 100,
    "autoscaleStatus": null,
    "description": "",
    "clusterName": "stability-test",
    "internetType": "PayByTraffic",
    "launchInterval": 0,
    "groupId": 32,
    "serverRole": null,
    "name": "ubuntu-beijing",
    "loadBalancerPublicIp": null,
    "created": 1405261902000,
    "region": "cn-beijing"
  },
  {
    "vmNumber": 1,
    "loadBalancerBandwidth": 1000,
    "serverRoleId": 31,
    "clusterId": 16,
    "imageId": "centos6u5_64_20G_aliaegis_20140926.vhd",
    "loadBalancerId": "\u65e0",
    "serverRoleName": "centos-qingdao",
    "lastScaleTime": null,
    "id": 65,
    "zone": "cn-qingdao-b",
    "launchDelay": 0,
    "instanceType": "ecs.t1.xsmall",
    "imageName": "centos6u5-20140926",
    "image": 15,
    "internetBandwidth": 100,
    "autoscaleStatus": null,
    "description": "",
    "clusterName": "stability-test",
    "internetType": "PayByTraffic",
    "launchInterval": 0,
    "groupId": 32,
    "serverRole": null,
    "name": "centos-qingdao",
    "loadBalancerPublicIp": null,
    "created": 1405261943000,
    "region": "cn-qingdao"
  },
  {
    "vmNumber": 0,
    "loadBalancerBandwidth": 1000,
    "serverRoleId": 5002,
    "clusterId": 16,
    "imageId": "ubuntu1404_64_20G_aliaegis_20140926.vhd",
    "loadBalancerId": "\u65e0",
    "serverRoleName": "ubuntu1404",
    "lastScaleTime": null,
    "id": 5012,
    "zone": null,
    "launchDelay": 0,
    "instanceType": "ecs.t1.xsmall",
    "imageName": "ubuntu1404-20140926",
    "image": 22,
    "internetBandwidth": 100,
    "autoscaleStatus": null,
    "description": "",
    "clusterName": "stability-test",
    "internetType": "PayByTraffic",
    "launchInterval": 0,
    "groupId": 32,
    "serverRole": null,
    "name": "ubuntu1404",
    "loadBalancerPublicIp": null,
    "created": 1406130081000,
    "region": "cn-hangzhou"
  },
  {
    "vmNumber": 0,
    "loadBalancerBandwidth": 1000,
    "serverRoleId": 5033,
    "clusterId": 16,
    "imageId": "centos6u5_64_20G_aliaegis_20140926.vhd",
    "loadBalancerId": "\u65e0",
    "serverRoleName": "centos-shenzhen",
    "lastScaleTime": null,
    "id": 5083,
    "zone": null,
    "launchDelay": 0,
    "instanceType": "ecs.t1.xsmall",
    "imageName": "centos6u5-20140926",
    "image": 17,
    "internetBandwidth": 100,
    "autoscaleStatus": null,
    "description": "",
    "clusterName": "stability-test",
    "internetType": "PayByTraffic",
    "launchInterval": 0,
    "groupId": 32,
    "serverRole": null,
    "name": "centos-shenzhen",
    "loadBalancerPublicIp": null,
    "created": 1409406678000,
    "region": "cn-shenzhen"
   }
 ]

 ./f2cs.py listClusterVms --cluster-id=16
 [
  {
    "backendCreated": false,
    "serverRoleId": 31,
    "vmId": "i-287pja0mk",
    "imageId": "centos6u5_64_20G_aliaegis_20140926.vhd",
    "localIP": "10.164.11.222",
    "rabbitmqQueue": "queue_down_16_12167_13acb6ff",
    "id": 12167,
    "alertType": "OK",
    "zone": "cn-qingdao-b",
    "cloudName": "default-dev",
    "backendCreating": false,
    "failedCause": null,
    "clusterRoleName": "centos-qingdao",
    "clusterType": "stability-test",
    "workId": 24385,
    "vmType": "ecs.t1.xsmall",
    "imageName": "centos6u5-20140926",
    "heartbeatStatus": "ONLINE",
    "image": 15,
    "internetBandwidth": 100,
    "status": "startResponse",
    "description": null,
    "clusterName": "stability-test",
    "clusterId": 16,
    "price": 0.18,
    "internetType": "PayByTraffic",
    "excludeVmStatus": null,
    "runningTime": null,
    "remoteIP": "114.215.149.211",
    "password": null,
    "groupId": 32,
    "vmStatus": "Running",
    "agentRetried": 1,
    "name": "stability-test--centos-qingdao--12167",
    "terminateFlag": false,
    "created": 1417366135000,
    "clusterRoleId": 65,
    "region": "cn-qingdao",
    "cloudId": 2,
    "deleted": null
  },
  {
    "backendCreated": false,
    "serverRoleId": 30,
    "vmId": "i-25e3mowze",
    "imageId": "ubuntu1204_64_20G_aliaegis_20140926.vhd",
    "localIP": "10.173.36.215",
    "rabbitmqQueue": "queue_down_16_12168_08d615f9",
    "id": 12168,
    "alertType": "OK",
    "zone": "cn-beijing-a",
    "cloudName": "default-dev",
    "backendCreating": false,
    "failedCause": null,
    "clusterRoleName": "ubuntu-beijing",
    "clusterType": "stability-test",
    "workId": 24386,
    "vmType": "ecs.t1.xsmall",
    "imageName": "ubuntu1204-20140926",
    "heartbeatStatus": "ONLINE",
    "image": 3,
    "internetBandwidth": 100,
    "status": "startResponse",
    "description": null,
    "clusterName": "stability-test",
    "clusterId": 16,
    "price": 0.2,
    "internetType": "PayByTraffic",
    "excludeVmStatus": null,
    "runningTime": null,
    "remoteIP": "123.57.67.57",
    "password": null,
    "groupId": 32,
    "vmStatus": "Running",
    "agentRetried": 0,
    "name": "stability-test--ubuntu-beijing--12168",
    "terminateFlag": false,
    "created": 1417366135000,
    "clusterRoleId": 64,
    "region": "cn-beijing",
    "cloudId": 2,
    "deleted": null
  }
 ]

 ./f2cs.py listClusterVMGroupVMs --cluster-id=16 --cluster-vmgroup-id=64
 [
  {
    "backendCreated": false,
    "serverRoleId": 30,
    "vmId": "i-25e3mowze",
    "imageId": "ubuntu1204_64_20G_aliaegis_20140926.vhd",
    "localIP": "10.173.36.215",
    "rabbitmqQueue": "queue_down_16_12168_08d615f9",
    "id": 12168,
    "alertType": "OK",
    "zone": "cn-beijing-a",
    "cloudName": "default-dev",
    "backendCreating": false,
    "failedCause": null,
    "clusterRoleName": "ubuntu-beijing",
    "clusterType": "stability-test",
    "workId": 24386,
    "vmType": "ecs.t1.xsmall",
    "imageName": "ubuntu1204-20140926",
    "heartbeatStatus": "ONLINE",
    "image": 3,
    "internetBandwidth": 100,
    "status": "startResponse",
    "description": null,
    "clusterName": "stability-test",
    "clusterId": 16,
    "price": 0.2,
    "internetType": "PayByTraffic",
    "excludeVmStatus": null,
    "runningTime": null,
    "remoteIP": "123.57.67.57",
    "password": null,
    "groupId": 32,
    "vmStatus": "Running",
    "agentRetried": 0,
    "name": "stability-test--ubuntu-beijing--12168",
    "terminateFlag": false,
    "created": 1417366135000,
    "clusterRoleId": 64,
    "region": "cn-beijing",
    "cloudId": 2,
    "deleted": null
   }
 ]

 ./f2cs.py getServerInfo --cluster-id=16 --server-id=12168
 {
  "backendCreated": false,
  "serverRoleId": 30,
  "vmId": "i-25e3mowze",
  "imageId": "ubuntu1204_64_20G_aliaegis_20140926.vhd",
  "vmType": "ecs.t1.xsmall",
  "rabbitmqQueue": "queue_down_16_12168_08d615f9",
  "id": 12168,
  "alertType": "OK",
  "zone": "cn-beijing-a",
  "cloudName": "default-dev",
  "backendCreating": false,
  "failedCause": null,
  "clusterRoleName": "ubuntu-beijing",
  "clusterType": "stability-test",
  "workId": 24386,
  "localIP": "10.173.36.215",
  "imageName": "ubuntu1204-20140926",
  "heartbeatStatus": "ONLINE",
  "image": 3,
  "internetBandwidth": 100,
  "status": "startResponse",
  "description": null,
  "clusterName": "stability-test",
  "clusterId": 16,
  "price": 0.2,
  "internetType": "PayByTraffic",
  "excludeVmStatus": null,
  "runningTime": null,
  "remoteIP": "123.57.67.57",
  "password": "6a6f4fa0a9d9492b81bfc3a",
  "groupId": 32,
  "name": "stability-test--ubuntu-beijing--12168",
  "agentRetried": 0,
  "vmStatus": "Running",
  "terminateFlag": false,
  "created": 1417366135000,
  "clusterRoleId": 64,
  "region": "cn-beijing",
  "cloudId": 2,
  "deleted": null
 }

