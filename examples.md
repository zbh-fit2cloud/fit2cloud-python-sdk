
示例:
======================================

./f2cs.py config --cloud-provider=aliyun --id=c2glcnNqZHVhbirbnbmdAZ21haWwuY29t --secret=15xxxxx4ff-xxxx-4727-8xxx-045dxxx59484
./f2cs.py listClusters
./f2cs.py listClusterVmGroups --cluster-name=wordpress-all-in-one
./f2cs.py listClusterVms --cluster-name=wordpress-all-in-one
./f2cs.py getCluster --cluster-name=wordpress-all-in-one
./f2cs.py getClusterVmGroup --cluster-name=wordpress-all-in-one --vmgroup-name=wd-all-in-one
./f2cs.py setClusterVmGroupSize --cluster-name=wordpress-all-in-one --vmgroup-name=wd-all-in-one --size=2
./f2cs.py shutdownCluster --cluster-name=wordpress-all-in-one
./f2cs.py launchCluster --cluster-name=wordpress-all-in-one


1. 配置命令行的API Key和Secret
======================================

```
$./f2cs.py config --cloud-provider=aliyun --id=c2glcnNqZHVhbirbnbmdAZ21haWwuY29t --secret=15xxxxx4ff-xxxx-4727-8xxx-045dxxx59484
{
  "secretKey": "15xxxxx4ff-xxxx-4727-8xxx-045dxxx59484",
  "endpoint": "https://aliyun.fit2cloud.com:8443/rest/",
  "accessKeyId": "c2glcnNqZHVhbirbnbmdAZ21haWwuY29t"
}
```

2. 列出用户的某CloudProvider下所有集群
======================================

```
$ ./f2cs.py listClusters
[
  {
    "status": "CREATED",
    "credentialName": "default-key",
    "serverNumber": null,
    "name": "wordpress-dev",
    "cloudName": "default-dev",
    "envType": "development",
    "cloudId": 279,
    "clusterType": "default",
    "id": 1,
    "credentialId": 74,
    "rabbitmqExchange": "exchange_down_1_687d3c26",
    "roleNumber": null,
    "created": 1417932914000,
    "totalFee": 0.0,
    "price": null,
    "groupId": 10090,
    "launched": null,
    "description": ""
  }
]
```

3. 获取某集群虚拟机组信息
======================================

```
$ ./f2cs.py getClusterVmGroup --cluster-name=wordpress-all-in-one --vmgroup-name=wd-all-in-one
[
  {
    "vmNumber": 1,
    "hostnameStart": 1,
    "serverRoleId": 5078,
    "clusterId": 10068,
    "imageId": "centos6u5_64_20G_aliaegis_20140926.vhd",
    "serverRoleName": "wd-all-in-one",
    "instanceType": "ecs.t1.xsmall",
    "zone": "",
    "hostnameType": 2,
    "launchDelay": 0,
    "id": 5211,
    "imageName": "centos6u5-20140926",
    "image": 15,
    "hostnameData": "wordpress-bj",
    "description": "\u5355\u673a\u7248Wordpress\u865a\u673a\u7ec4",
    "clusterName": "wordpress-all-in-one",
    "internetType": "PayByTraffic",
    "launchInterval": 0,
    "groupId": 34,
    "name": "wd-all-in-one",
    "created": "Oct 30, 2014 3:38:09 PM",
    "region": "cn-qingdao",
    "internetBandwidth": 100
  }
]
```

4. 设置某集群虚拟机组大小，即虚拟机数量
======================================

```
$ ./f2cs.py setClusterVmGroupSize --cluster-name=wordpress-all-in-one --vmgroup-name=wd-all-in-one --size=2
{
  "message": "Set cluster wordpress-all-in-one vmgroup wd-all-in-one vm number to 2 successfully!",
  "code": 0
}
```

5. 获取集群信息，通过集群名称
======================================

```
$ ./f2cs.py getCluster --cluster-name=wordpress-all-in-one
{
  "status": "RUNNING",
  "credentialName": "default-key",
  "name": "wordpress-all-in-one",
  "cloudName": "default-dev",
  "envType": "development",
  "cloudId": 10,
  "clusterType": "wordpress",
  "created": "Oct 30, 2014 3:38:09 PM",
  "credentialId": 5,
  "rabbitmqExchange": "exchange_down_10068_605bc48e",
  "totalFee": 7.585,
  "id": 10068,
  "groupId": 34,
  "launched": "Dec 6, 2014 4:07:05 PM",
  "description": "\u5355\u673a\u7248Wordpress\u96c6\u7fa4"
}

集群不存在的情况:
$ ./f2cs.py getCluster --cluster-name=wordpress-dev1
{
  "errorcode": 1000,
  "message": "Cluster wordpress-dev1 doesn't exist!"
}
```

5. 列出集群内虚拟机组信息，通过集群名称
============================================================================

```
$ ./f2cs.py listClusterVmGroups --cluster-name=wordpress-all-in-one
[
  {
    "vmNumber": 2,
    "hostnameStart": 1,
    "serverRoleId": 5078,
    "clusterId": 10068,
    "imageId": "centos6u5_64_20G_aliaegis_20140926.vhd",
    "serverRoleName": "wd-all-in-one",
    "instanceType": "ecs.t1.xsmall",
    "zone": "",
    "hostnameType": 2,
    "launchDelay": 0,
    "id": 5211,
    "imageName": "centos6u5-20140926",
    "image": 15,
    "hostnameData": "wordpress-bj",
    "description": "\u5355\u673a\u7248Wordpress\u865a\u673a\u7ec4",
    "clusterName": "wordpress-all-in-one",
    "internetType": "PayByTraffic",
    "launchInterval": 0,
    "groupId": 34,
    "name": "wd-all-in-one",
    "created": "Oct 30, 2014 3:38:09 PM",
    "region": "cn-qingdao",
    "internetBandwidth": 100
  },
  {
    "vmNumber": 0,
    "hostnameStart": 1,
    "serverRoleId": 5209,
    "clusterId": 10068,
    "imageId": "ubuntu1404_64_20G_aliaegis_20140926.vhd",
    "serverRoleName": "wd-all-in-one-ubuntu",
    "instanceType": "ecs.t1.xsmall",
    "zone": "",
    "hostnameType": 2,
    "launchDelay": 0,
    "id": 5384,
    "imageName": "ubuntu1404-20140926",
    "image": 24,
    "hostnameData": "wd-bj",
    "description": "",
    "clusterName": "wordpress-all-in-one",
    "internetType": "PayByTraffic",
    "launchInterval": 0,
    "groupId": 34,
    "name": "wd-all-in-one-ubuntu",
    "created": "Dec 3, 2014 2:51:30 PM",
    "region": "cn-beijing",
    "internetBandwidth": 100
  }
]
```

6. 列出集群内所有虚拟机，通过集群名称
============================================================================

```
$ ./f2cs.py listClusterVms --cluster-name=wordpress-all-in-one
[
  {
    "backendCreated": false,
    "serverRoleId": 5078,
    "vmId": "i-28hhijukm",
    "imageId": "centos6u5_64_20G_aliaegis_20140926.vhd",
    "localIP": "10.144.161.231",
    "rabbitmqQueue": "queue_down_10068_12387_cdb7ef9e",
    "id": 12387,
    "alertType": "OK",
    "zone": "cn-qingdao-b",
    "cloudName": "default-dev",
    "backendCreating": false,
    "hostname": "wordpress-bj1",
    "clusterRoleName": "wd-all-in-one",
    "clusterType": "wordpress",
    "workId": 26026,
    "vmType": "ecs.t1.xsmall",
    "imageName": "centos6u5-20140926",
    "heartbeatStatus": "ONLINE",
    "image": 15,
    "internetBandwidth": 100,
    "status": "startResponse",
    "clusterName": "wordpress-all-in-one",
    "clusterId": 10068,
    "price": 0.1881,
    "internetType": "PayByTraffic",
    "remoteIP": "115.28.180.51",
    "groupId": 34,
    "vmStatus": "Running",
    "agentRetried": 0,
    "hostnameNumber": 1,
    "name": "wordpress-all-in-one--wd-all-in-one--12387",
    "terminateFlag": false,
    "created": "Dec 7, 2014 3:29:24 PM",
    "clusterRoleId": 5211,
    "region": "cn-qingdao",
    "cloudId": 10
  },
  {
    "backendCreated": false,
    "serverRoleId": 5078,
    "clusterId": 10068,
    "imageId": "centos6u5_64_20G_aliaegis_20140926.vhd",
    "localIP": "10.144.46.102",
    "rabbitmqQueue": "queue_down_10068_12388_b0e75e6d",
    "id": 12388,
    "zone": "cn-qingdao-b",
    "cloudName": "default-dev",
    "backendCreating": false,
    "hostname": "wordpress-bj2",
    "clusterRoleName": "wd-all-in-one",
    "clusterType": "wordpress",
    "workId": 26031,
    "vmType": "ecs.t1.xsmall",
    "imageName": "centos6u5-20140926",
    "heartbeatStatus": "OFFLINE",
    "image": 15,
    "internetBandwidth": 100,
    "status": "ready",
    "clusterName": "wordpress-all-in-one",
    "vmId": "i-28h9v55i2",
    "price": 0.1881,
    "internetType": "PayByTraffic",
    "remoteIP": "115.28.37.136",
    "groupId": 34,
    "vmStatus": "Running",
    "agentRetried": 0,
    "hostnameNumber": 2,
    "name": "wordpress-all-in-one--wd-all-in-one--12388",
    "terminateFlag": false,
    "created": "Dec 7, 2014 3:35:42 PM",
    "clusterRoleId": 5211,
    "region": "cn-qingdao",
    "cloudId": 10
  }
]
```

7. 获取集群信息
========================================

```
$ ./f2cs.py getCluster --cluster-name=wordpress-all-in-one
{
  "status": "RUNNING",
  "credentialName": "default-key",
  "name": "wordpress-all-in-one",
  "cloudName": "default-dev",
  "envType": "development",
  "cloudId": 10,
  "clusterType": "wordpress",
  "created": "Oct 30, 2014 3:38:09 PM",
  "credentialId": 5,
  "rabbitmqExchange": "exchange_down_10068_605bc48e",
  "totalFee": 7.585,
  "id": 10068,
  "groupId": 34,
  "launched": "Dec 6, 2014 4:07:05 PM",
  "description": "\u5355\u673a\u7248Wordpress\u96c6\u7fa4"
}
```

8. 关闭集群
========================================

```
$ ./f2cs.py shutdownCluster --cluster-name=wordpress-all-in-one
{
  "message": "Shutdown cluster wordpress-all-in-one successfully!",
  "code": 0
}
```

9. 启动集群
========================================

```
$ ./f2cs.py launchCluster --cluster-name=wordpress-all-in-one
{
  "message": "launch cluster wordpress-all-in-one successfully!",
  "code": 0
}
```




