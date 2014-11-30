#!/usr/bin/python
# coding=utf-8
'''
Created on Nov 29, 2014

@author: jason
'''

import json
import os
import oauth2 as oauth
import traceback

class Server(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass

    
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
    
    def getGroupId(self):
        return self.groupId
    
    def setGroupId(self, groupId):
        self.groupId = groupId
    
    def getCloudId(self):
        return self.cloudId
    
    def setCloudId(self, cloudId):
        self.cloudId = cloudId
    
    def getClusterId(self):
        return self.clusterId
    
    def setClusterId(self, clusterId):
        self.clusterId = clusterId
    
    def getClusterroleId(self):
        return self.clusterRoleId
    
    def setClusterroleId(self, clusterRoleId):
        self.clusterRoleId = clusterRoleId
    
    def getServerroleId(self):
        return self.serverRoleId
    
    def setServerroleId(self, serverRoleId):
        self.serverRoleId = serverRoleId
    
    def getLocalIP(self):
        return self.localIP
    
    def setLocalIP(self, localIP):
        self.localIP = localIP
    
    def getRemoteIP(self):
        return self.remoteIP
    
    def setRemoteIP(self, remoteIP):
        self.remoteIP = remoteIP
    
    def getClusterType(self):
        return self.clusterType
    
    def setClusterType(self, clusterType):
        self.clusterType = clusterType
    
    def getClusterName(self):
        return self.clusterName
    
    def setClusterName(self, clusterName):
        self.clusterName = clusterName
    
    def getClusterRoleName(self):
        return self.clusterRoleName
    
    def setClusterRoleName(self, clusterRoleName):
        self.clusterRoleName = clusterRoleName
    
    def getRegion(self):
        return self.region
    
    def setRegion(self, region):
        self.region = region
    
    def getVmId(self):
        return self.vmId
    
    def setVmId(self, vmId):
        self.vmId = vmId
        
    def getVmStatus(self):
        return self.vmStatus
    
    def setVmStatus(self, vmStatus):
        self.vmStatus = vmStatus
    
    def getRabbitmqQueue(self):
        return self.rabbitmqQueue
    
    def setRabbitmqQueue(self, rabbitmqQueue):
        self.rabbitmqQueue = rabbitmqQueue
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    @staticmethod
    def fromDict(dictServer):
        serverId = dictServer['id']
        groupId = dictServer['groupId']
        cloudId = dictServer['cloudId']
        clusterId = dictServer['clusterId']
        clusterRoleId = dictServer['clusterRoleId']
        serverRoleId = dictServer['serverRoleId']
        localIP = dictServer['localIP']
        remoteIP = dictServer['remoteIP']
        clusterType = dictServer['clusterType']
        clusterName = dictServer['clusterName']
        clusterRoleName = dictServer['clusterRoleName']
        region = dictServer['region']
        vmId = dictServer['vmId']
        vmStatus = dictServer['vmStatus']
        rabbitmqQueue = dictServer['rabbitmqQueue']
        name = dictServer['name']

        server = Server()
        server.setId(serverId)
        server.setGroupId(groupId)
        server.setCloudId(cloudId)
        server.setClusterId(clusterId)
        server.setClusterroleId(clusterRoleId)
        server.setServerroleId(serverRoleId)
        server.setLocalIP(localIP)
        server.setRemoteIP(remoteIP)
        server.setClusterType(clusterType)
        server.setClusterName(clusterName)
        server.setClusterRoleName(clusterRoleName)
        server.setRegion(region)
        server.setVmId(vmId)
        server.setVmStatus(vmStatus)
        server.setRabbitmqQueue(rabbitmqQueue)
        server.setName(name)
        
        return server
    
    @staticmethod
    def fromJSON(jsonServer):
        dictServer = json.loads(jsonServer)
        return Server.fromDict(dictServer) 

    def toJSON(self):
        dictServer = self.toDict()
        jsonServer = json.dumps(dictServer, indent=2)
        return jsonServer
    
    def toDict(self):
        dictServer = {}
        dictServer['id'] = self.id
        dictServer['groupId'] = self.groupId
        dictServer['cloudId'] = self.cloudId
        dictServer['clusterId'] = self.clusterId
        dictServer['clusterRoleId'] = self.clusterRoleId
        dictServer['serverRoleId'] = self.serverRoleId
        dictServer['localIP'] = self.localIP
        dictServer['remoteIP'] = self.remoteIP
        dictServer['clusterType'] = self.clusterType
        dictServer['clusterName'] = self.clusterName
        dictServer['clusterRoleName'] = self.clusterRoleName
        dictServer['region'] = self.region
        dictServer['vmId'] = self.vmId
        dictServer['vmStatus'] = self.vmStatus
        dictServer['rabbitmqQueue'] = self.rabbitmqQueue
        dictServer['name'] = self.name
        
        return dictServer

class F2CRestWSClient(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def setEndpoint(self, endPoint):
        self.endPoint = endPoint
    
    def setAccessKeyId(self, accessKeyId):
        self.accessKeyId = accessKeyId
    
    def setSecretKey(self, secretKey):
        self.secretKey = secretKey
        
    def getClusters(self):
        url='%sclusters' % (self.endPoint)
        content = self.get(url, self.accessKeyId, self.secretKey)
        return content
        pass
    
    def getServer(self, clusterId, serverId):
        url='%scluster/%s/server/%s' % (self.endPoint, clusterId, serverId)
        content = self.get(url, self.accessKeyId, self.secretKey)
        return content
        pass
    
    def getClusterVMGroups(self, clusterId):
        url='%scluster/%s/roles' % (self.endPoint, clusterId)
        content = self.get(url, self.accessKeyId, self.secretKey)
        return content
    
    def getClusterVms(self, clusterId):
        url='%scluster/%s/servers' % (self.endPoint, clusterId)
        #logger.info("url=%s" % url)
        
        content = self.get(url, self.accessKeyId, self.secretKey)
        
        dictReturnServers=[]
        
        dictServers = json.loads(content)
        if dictServers!=None and len(dictServers) > 0 :
            for dictServer in dictServers : 
                #print "--------------------------------"
                server = Server.fromDict(dictServer)
                if server.getVmStatus() == "Running" :
                    dictReturnServers.append(dictServer)
                    #print server.toJSON()
                    pass
            pass
        
        return json.dumps(dictReturnServers,indent=2) 
    
    def getClusterVmGroupVMs(self, clusterId, clusterVmGroupId):
        url='%scluster/%s/clusterrole/%s/servers' % (self.endPoint, clusterId, clusterVmGroupId)
        #logger.info("url=%s" % url)
        content = self.get(url, self.accessKeyId, self.secretKey)
        
        dictReturnVMs=[]
        
        dictServers = json.loads(content)
        if dictServers!=None and len(dictServers) > 0 :
            for dictServer in dictServers : 
                #print "--------------------------------"
                server = Server.fromDict(dictServer)
                if server.getVmStatus() == "Running" :
                    dictReturnVMs.append(dictServer)
                    #print server.toJSON()
                    pass
            pass
        
        return json.dumps(dictReturnVMs,indent=2) 
    
    def getClusterVmGroupId(self, cluster_vmgroup_name):
        clusterrole_id = None
        jsonClusterroles = self.getClusterRoles()
        if(jsonClusterroles!=None) :
            try:
                dictClusterroles = json.loads(jsonClusterroles)
                for dictClusterrole in dictClusterroles:
                    if(dictClusterrole.has_key("name")) :
                        name =  dictClusterrole["name"]
                        if(cluster_vmgroup_name==name) :
                            clusterrole_id = dictClusterrole["id"]
            except Exception, e:
                raise e
        return clusterrole_id
    
    def get(self,url,key,secret):
        consumer = oauth.Consumer(key=key, secret=secret)
        client = oauth.Client(consumer, None,  timeout=10)
        current_dir = os.path.dirname(__file__)
        client.ca_certs =  "%s/cacert.pem" % current_dir
        #print client.ca_certs
        http_headers = {}
        #http_headers['X-Tradeshift-TenantId'] = TENANT_ID
        http_headers['User-Agent'] = 'MegaPythonAPIster 2.0'
        http_headers['Accept'] = 'application/json'
        content = None
        try:
            resp, content = client.request(
                url,
                method="GET",
                headers=http_headers
                )
            #logger.info("resp['status']=%s" % resp['status'])
            #logger.debug("content=%s" % content)
        except Exception, e :
            #logger.error(e)
            traceback.print_exc()
            raise Exception(e)
            
        return content

import argparse
import textwrap
import sys

class F2csConfig :
    
    def setEndpoint(self, endpoint):
        self.endpoint = endpoint
        
    def setAccessKeyId(self, accessKeyId):
        self.accessKeyId = accessKeyId
    
    def setSecretKey(self, secretKey):
        self.secretKey = secretKey
        
    def getEndpoint(self):
        return self.endpoint
    
    def getAccessKeyId(self):
        return self.accessKeyId
    
    def getSecretKey(self):
        return self.secretKey
    
    @staticmethod
    def fromDict(dictF2csConfig):
        endpoint = dictF2csConfig['endpoint']
        accessKeyId = dictF2csConfig['accessKeyId']
        secretKey = dictF2csConfig['secretKey']

        f2csConfig = F2csConfig()
        f2csConfig.setEndpoint(endpoint)
        f2csConfig.setAccessKeyId(accessKeyId)
        f2csConfig.setSecretKey(secretKey)

        return f2csConfig
    
    @staticmethod
    def fromJSON(jsonF2csConfig):
        dictF2csConfig = json.loads(jsonF2csConfig)
        return F2csConfig.fromDict(dictF2csConfig) 

    def toJSON(self):
        dictF2csConfig = self.toDict()
        jsonF2csConfig = json.dumps(dictF2csConfig, indent=2)
        return jsonF2csConfig
    
    def toDict(self):
        dictF2csConfig = {}
        dictF2csConfig['endpoint'] = self.endpoint
        dictF2csConfig['accessKeyId'] = self.accessKeyId
        dictF2csConfig['secretKey'] = self.secretKey
        
        return dictF2csConfig
    pass

class FileUtil:
    
    @staticmethod
    def writeContent(file_path, content):
        dir_path = os.path.dirname(file_path)
        os.system("mkdir -p %s" % dir_path)
        config_file = file(file_path, 'w')
        config_file.write(content)
        config_file.close()
    
    @staticmethod
    def readContent(file_path):
        config_file = file(file_path, 'r')
        file_content = ""
        file_lines = config_file.readlines();
        for line in file_lines :
            file_content = file_content + line
        config_file.close()
        return file_content

class F2CS :
    F2CSCONFIG_PATH = os.path.expanduser('~') + "/.f2cs/config"
    
    def __init__(self):
        usage = '''
    ./f2cs.py <command> [<args>]
commands:
    config
    listClusters
    listClusterVmGroups
    listClusterServers
    listClusterVmGroupServers
    executeScript

examples:
    ./f2cs.py config --endpoint=<endpoint> --id=<access key id> --secret=<access key secret>
    ./f2cs.py listClusters
    ./f2cs.py listClusterVmGroups --cluster-id=<cluster id>
    ./f2cs.py listClusterVms --cluster-id=<cluster id>
    ./f2cs.py listClusterVmGroupVms --cluster-id=<cluster id> --cluster-vmgroup-id=<cluster vmgroup id>
    ./f2cs.py getServerInfo --cluster-id=<cluster id> --server-id=<server id>
    ./f2cs.py executeScript --cluster-id=<cluster id> --cluster-vmgroup-id=<cluster vmgroup id> --cluster-server-id=<cluster server id> --script-file=<script file path> 
    ./f2cs.py -h | --help
    ./f2cs.py -v | --version
        '''
        
        parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     #description=textwrap.dedent(description),
                                     #epilog=textwrap.dedent(epilog),
                                     usage=usage
                                     )
        parser.add_argument('command', metavar='command', help='命令, config|listClusters|listClusterVmGroups|listClusterVms|listClusterVmGroupVms')
        parser.add_argument('-v', '--version', action='version', version='f2cs 1.0')
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print '不支持该命令: %s' % args.command
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)(args)
        
    def getF2CWSClient(self):
        #read from ~/.f2cs/config
        f2cWSClient = None
        if os.path.exists(self.F2CSCONFIG_PATH) :
            jsonF2csConfig = FileUtil.readContent(self.F2CSCONFIG_PATH)
            f2csConfig = F2csConfig.fromJSON(jsonF2csConfig)
            
            endPoint=f2csConfig.getEndpoint()
            accessKeyId=f2csConfig.getAccessKeyId()
            secretKey=f2csConfig.getSecretKey()
            
            f2cWSClient = F2CRestWSClient()
            f2cWSClient.setEndpoint(endPoint)
            f2cWSClient.setAccessKeyId(accessKeyId)
            f2cWSClient.setSecretKey(secretKey)
        return f2cWSClient
        
    def config(self, argv):
        parser = argparse.ArgumentParser(
            description='配置FIT2CLOUD Webservice API endpoint, access key id, secret key')
        # prefixing the argument with -- means it's optional
        arg = parser.add_argument
        arg('--endpoint', nargs='?', const=True, default=False, metavar='Endpoint', help='Endpoint, --endpoint is required', required=True)
        arg('--id', nargs='?', const=True, default=False, metavar='AccessKey Id', help='Access Key Id, --id is required', required=True)
        arg('--secret', nargs='?', const=True, default=False, metavar='AccessKey Secret', help='Access Key Secret, --secret is required', required=True)
        # now that we're inside a subcommand, ignore the first
        args = parser.parse_args(sys.argv[2:])
        f2csConfig = F2csConfig()
        f2csConfig.setEndpoint(args.endpoint);
        f2csConfig.setAccessKeyId(args.id)
        f2csConfig.setSecretKey(args.secret)
        
        jsonF2csConfig = f2csConfig.toJSON()
        FileUtil.writeContent(self.F2CSCONFIG_PATH, jsonF2csConfig)
        if os.path.exists(self.F2CSCONFIG_PATH) :
            print "配置成功!"
            print "~/.f2cs/config"
            print FileUtil.readContent(self.F2CSCONFIG_PATH)

    def listClusters(self, argv):
        f2cWsClient = self.getF2CWSClient()
        if f2cWsClient==None :
            self.printAPIConfigRequiredMsg()
            sys.exit()
            pass
        
        jsonClusters = f2cWsClient.getClusters()
        dictClusters = json.loads(jsonClusters)
        jsonClusters = json.dumps(dictClusters, indent=2)
        print jsonClusters
    
    def printAPIConfigRequiredMsg(self):
        print "错误: "
        print "     请首先配置apiEndpoint, access key id and secret key id"
        print "例如: "
        print "     ./f2cs.py config --endpoint=https://aliyun.fit2cloud.com:8443/rest/ --id=xxxx --secret=yyy"
        print "参数说明: "
        print "     1) 对于endpoint, 如果不是aliyun, 请将例子中aliyun替换成您使用的云的名称，如qingcloud,aws,azure"
        print "     2) 对于access key id和secret key, 您可以从FIT2Cloud Web控制台找到, 点击右上角用户名，从下拉菜单中选择API信息"
    
    def getServerInfo(self, argv):
        f2cWsClient = self.getF2CWSClient()
        if f2cWsClient==None :
            self.printAPIConfigRequiredMsg()
            sys.exit()
            pass
        
        parser = argparse.ArgumentParser(
            description='获取集群某Server信息，根据cluster id, server id')
        arg = parser.add_argument
        arg('--cluster-id', nargs='?', const=True, default=False, metavar='Cluster Id', help='Cluster Id, --cluster-id is required', required=True)
        arg('--server-id', nargs='?', const=True, default=False, metavar='Server Id', help='Server Id, --server-id is required', required=True)
        
        args = parser.parse_args(sys.argv[2:])
        if type(args.cluster_id) is str and type(args.server_id) is str:
            jsonServer = f2cWsClient.getServer(args.cluster_id, args.server_id)
            dictServer=json.loads(jsonServer)
            jsonServer = json.dumps(dictServer, indent=2)
            print jsonServer
        else :
            print "错误: 请给出集群Id和虚拟机Id, 例如./f2cs.py getServerInfo --cluster-id=16 --server-id=12166"
        pass
    
    def listClusterVmGroups(self, argv):
        f2cWsClient = self.getF2CWSClient()
        if f2cWsClient==None :
            self.printAPIConfigRequiredMsg()
            sys.exit()
            pass
        
        parser = argparse.ArgumentParser(
            description='列出集群的所有虚拟机组')
        arg = parser.add_argument
        arg('--cluster-id', nargs='?', const=True, default=False, metavar='Cluster Id', help='Cluster Id, --cluster-id is required', required=True)
        
        args = parser.parse_args(sys.argv[2:])
        if args.cluster_id!=None and type(args.cluster_id) is str :
            jsonVMGroups = f2cWsClient.getClusterVMGroups(args.cluster_id)
            dictVMGroups = json.loads(jsonVMGroups)
            jsonVMGroups = json.dumps(dictVMGroups, indent=2)
            print jsonVMGroups
        else :
            print "错误: 请给出集群Id参数, 例如./f2cs.py listClusterVmGroups --cluster-id=16"
        pass
    
    def listClusterVms(self, argv):
        f2cWsClient = self.getF2CWSClient()
        if f2cWsClient==None :
            self.printAPIConfigRequiredMsg()
            sys.exit()
            pass
        
        parser = argparse.ArgumentParser(
            description='列出集群中的所有虚拟机')
        arg = parser.add_argument
        arg('--cluster-id', nargs='?', const=True, default=False, metavar='Cluster Id', help='Cluster Id, --cluster-id is required', required=True)
        
        args = parser.parse_args(sys.argv[2:])
        if args.cluster_id!=None and type(args.cluster_id) is str :
            jsonVMs = f2cWsClient.getClusterVms(args.cluster_id)
            dictVMs = json.loads(jsonVMs)
            jsonVMs = json.dumps(dictVMs, indent=2)
            print jsonVMs
        else :
            print "错误: 请给出集群Id参数, 例如./f2cs.py listClusterVms --cluster-id=16"
        pass
    
    def listClusterVmGroupVms(self, argv):
        f2cWsClient = self.getF2CWSClient()
        if f2cWsClient==None :
            self.printAPIConfigRequiredMsg()
            sys.exit()
            pass
        
        parser = argparse.ArgumentParser(
            description='List servers of specified cluster VM Group')
        arg = parser.add_argument
        arg('--cluster-id', nargs='?', const=True, default=False, metavar='Cluster Id', help='Cluster Id, --cluster-id is required', required=True)
        arg('--cluster-vmgroup-id', nargs='?', const=True, default=False, metavar='VM Group Id', help='VM Group Id, --vmgroup-id is required', required=True)
        
        args = parser.parse_args(sys.argv[2:])
        if type(args.cluster_id) is str and type(args.cluster_vmgroup_id) is str:
            jsonVMs = f2cWsClient.getClusterVmGroupVMs(args.cluster_id, args.cluster_vmgroup_id)
            dictVMs = json.loads(jsonVMs)
            jsonVMs = json.dumps(dictVMs, indent=2)
            print jsonVMs
        else :
            print "错误: 请给出集群Id参数及集群虚拟机组Id, 例如./f2cs.py listClusterVmGroupVms --cluster-id=16 --cluster-vmgroup-id=64"
    
    def executeScript(self, argv):
        f2cWsClient = self.getF2CWSClient()
        if f2cWsClient==None :
            self.printAPIConfigRequiredMsg()
            sys.exit()
            pass
        
        parser = argparse.ArgumentParser(
            description='execute script on specified cluster all servers, cluster vmgroup servers, a server in specified cluster')
        arg = parser.add_argument
        arg('--cluster-id', nargs='?', const=True, default=False, metavar='Cluster Id', help='Cluster Id, --cluster-id is required', required=True)
        arg('--cluster-vmgroup-id', nargs='?', const=True, default=False, metavar='Cluster VM Group Id', help='VM Group Id, --cluster-vmgroup-id is required', required=True)
        arg('--cluster-vm-id', nargs='?', const=True, default=False, metavar='Cluster VM Id', help='VM Group Id, --cluster-vm-id is required', required=True)
        
        args = parser.parse_args(sys.argv[2:])
        print 'Running executeScript, cluster_id=%s' % args.cluster_id
        pass

if __name__ == "__main__":
    F2CS()
