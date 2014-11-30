#!/usr/bin/python
'''
Created on Nov 29, 2014

@author: jason
'''

import json
#import oauth2 as oauth
import base64
import re
import os

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
    
    def getClusterServers(self, clusterName):
        endPoint = self.endPoint
        accessKeyId = self.accessKeyId
        secretKey = self.secretKey
        clusterId = clusterName
        url='%scluster/%s/servers' % (endPoint, clusterId)
        #logger.info("url=%s" % url)
        
        content = self.get(url, self.accessKeyId, self.secretKey)
        return content
        pass
    
    def getClusterroleServersByName(self, clusterrole_name):
        user_data = self.userDataDao.getUserData()
        endPointURL = user_data.getQueryEnvURL()
        key = user_data.getQueueServerUserName()
        secret = user_data.getQueueServerPassword()
        clusterId = user_data.getClusterID()
        try:
            clusterrole_id = self.getClusterroleId(clusterrole_name)
            if(clusterrole_id!=None) :
                url='%scluster/%s/clusterrole/%s/servers' % (endPointURL, clusterId, clusterrole_id)
                #logger.info("url=%s" % url)
                content = self.get(url, key, secret)
                return content
            else :
                print "clusterrole %s does not exist in cluster." % clusterrole_name
                return None
        except Exception, e:
            #to do, print proper friendly message according to exception
            raise e
    
    def getClusterroleServersById(self, clusterrole_id):
        user_data = self.userDataDao.getUserData()
        endPointURL = user_data.getQueryEnvURL()
        key = user_data.getQueueServerUserName()
        secret = user_data.getQueueServerPassword()
        clusterId = user_data.getClusterID()
        try:
            if(clusterrole_id!=None) :
                url='%scluster/%s/clusterrole/%s/servers' % (endPointURL, clusterId, clusterrole_id)
                #logger.info("url=%s" % url)
                content = self.get(url, key, secret)
                return content
            else :
                print "clusterrole %s does not exist in cluster." % clusterrole_id
                return None
        except Exception, e:
            #to do, print proper friendly message according to exception
            raise e
    
    def getClusterroleId(self, clusterrole_name):
        clusterrole_id = None
        jsonClusterroles = self.getClusterRoles()
        if(jsonClusterroles!=None) :
            try:
                dictClusterroles = json.loads(jsonClusterroles)
                for dictClusterrole in dictClusterroles:
                    if(dictClusterrole.has_key("name")) :
                        name =  dictClusterrole["name"]
                        if(clusterrole_name==name) :
                            clusterrole_id = dictClusterrole["id"]
            except Exception, e:
                raise e
        return clusterrole_id
    
    def getClusterRoles(self):
        user_data = self.userDataDao.getUserData()
        endPointURL = user_data.getQueryEnvURL()
        key = user_data.getQueueServerUserName()
        secret = user_data.getQueueServerPassword()
        clusterId = user_data.getClusterID()
        url='%scluster/%s/roles' % (endPointURL, clusterId)
        content = self.get(url, key, secret)
        return content
    
    def get(self,url,key,secret):
        #logger.debug("url:%s" % url)
        #logger.debug("key:%s" % key)
        #logger.debug("secret:%s" % secret)
        consumer = oauth.Consumer(key=key, secret=secret)
        # token = oauth.Token(key=TOKEN_KEY, secret=TOKEN_SECRET)
        client = oauth.Client(consumer, None,  timeout=10)
        client.ca_certs =  "%s/conf/cacert.pem" % Database.getAgentFolderDirPath()
        http_headers = {}
        #http_headers['X-Tradeshift-TenantId'] = TENANT_ID
        http_headers['User-Agent'] = 'MegaPythonAPIster 2.0'
        http_headers['Accept'] = 'application/json'
        resp = None
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
            raise Exception(e)
            
        return content

import argparse
import textwrap
import sys

class F2CS :
    def __init__(self):
        usage = '''
    ./f2cs.py <command> [<args>]
commands:
    config
    listClusters
    listClusterVMGroups
    listClusterServers
    listClusterVMGroupServers
    executeScript
    getScriptLogs
examples:
    ./f2cs.py config --endpoint=<endpoint> --id=<access key id> --secret=<access key secret>
    ./f2cs.py listClusters --cluster-name=<cluster name>
    ./f2cs.py listClusterVMGroups --cluster-name=<cluster name>
    ./f2cs.py listClusterServers --cluster-name=<cluster name>
    ./f2cs.py listClusterVMGroupServers --cluster-name=<cluster name> --cluster-vmgroup-name=<cluster vmgroup name>
    ./f2cs.py executeScript --cluster-name=<cluster name> --cluster-vmgroup-name=<cluster vmgroup> --cluster-server-id=<cluster server id> --script-file=<script file path> 
    ./f2cs.py getScriptLog --execution-id=<execution id>
    ./f2cs.py -h | --help
    ./f2cs.py -v | --version
        '''
        parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     #description=textwrap.dedent(description),
                                     #epilog=textwrap.dedent(epilog),
                                     usage=usage
                                     )
        parser.add_argument('command', metavar='command', help='Subcommand to run, config|listClusters|listClusterVMGroups|listClusterServers|listClusterVMGroupServers|executeScript|getScriptLogs')
        parser.add_argument('-v', '--version', action='version', version='f2cs 1.0')
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print 'Unrecognized command'
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()
        
    def getF2CWSClient(self):
        endPoint="https://aliyun.fit2cloud.com:8443/rest/"
        accessKeyId="c2hlbnNpZHVhbnhpbmdAZ21haWwuY29t"
        secretKey="15ea94ff-b59a-4727-8cee-045d6f359484"
        f2cWSClient = F2CRestWSClient()
        f2cWSClient.setEndpoint(endPoint)
        f2cWSClient.setAccessKeyId(accessKeyId)
        f2cWSClient.setSecretKey(secretKey)
        return f2cWSClient
        
    def config(self):
        parser = argparse.ArgumentParser(
            description='Config FIT2Cloud Rest Service endpoint, access key id, secret key')
        # prefixing the argument with -- means it's optional
        arg = parser.add_argument
        arg('--endpoint', nargs=1, const=True, default=False, metavar='Endpoint', help='Endpoint, --endpoint is required', required=True)
        arg('--id', nargs=1, const=True, default=False, metavar='AccessKey Id', help='Access Key Id, --id is required', required=True)
        arg('--secret', nargs=1, const=True, default=False, metavar='AccessKey Secret', help='Access Key Secret, --secret is required', required=True)
        # now that we're inside a subcommand, ignore the first
        # TWO argvs, ie the command (git) and the subcommand (commit)
        args = parser.parse_args(sys.argv[2:])
        
        print "config rest api key and secret"
        print 'Running config, id=%s' % args.id
        print 'Running config, secret=%s' % args.secret

    def listClusters(self):
        parser = argparse.ArgumentParser(
            description='List clusters of account')
        arg = parser.add_argument
        arg('--cluster-name', nargs='?', const=True, default=False, metavar='Cluster Name', help='Cluster Name, --cluster-name is required')
        args = parser.parse_args(sys.argv[2:])
        print 'Running listClusters, cluster_name=%s' % args.cluster_name
        pass
    
    def listClusterVMGroups(self):
        parser = argparse.ArgumentParser(
            description='List clusters roles of specified cluster')
        arg = parser.add_argument
        arg('--cluster-name', nargs=1, const=True, default=False, metavar='Cluster Name', help='Cluster Name, --cluster-name is required', required=True)
        
        args = parser.parse_args(sys.argv[2:])
        print 'Running listClusterRoles, cluster_name=%s' % args.cluster_name
        pass
    
    def listClusterServers(self):
        parser = argparse.ArgumentParser(
            description='List servers of specified cluster')
        arg = parser.add_argument
        arg('--cluster-name', nargs=1, const=True, default=False, metavar='Cluster Name', help='Cluster Name, --cluster-name is required', required=True)
        
        args = parser.parse_args(sys.argv[2:])
        print 'Running listClusterServers, cluster_name=%s' % args.cluster_name
        pass
    
    def listClusterVMGroupServers(self):
        parser = argparse.ArgumentParser(
            description='List servers of specified cluster VM Group')
        arg = parser.add_argument
        arg('--cluster-name', nargs=1, const=True, default=False, metavar='Cluster Name', help='Cluster Name, --cluster-name is required', required=True)
        arg('--vmgroup-name', nargs='?', const=True, default=False, metavar='VM Group Name', help='VM Group Name, --vmgroup-name is required', required=True)
        
        args = parser.parse_args(sys.argv[2:])
        print 'Running listClusterVMGroupServers, cluster_name=%s' % args.cluster_name
        print 'Running listClusterVMGroupServers, cluster_name=%s' % args.cluster_name
        pass
    
    def executeScript(self):
        parser = argparse.ArgumentParser(
            description='execute script on specified cluster all servers, cluster vmgroup servers, a server in specified cluster')
        arg = parser.add_argument
        arg('--cluster-name', nargs=1, const=True, default=False, metavar='Cluster Name', help='Cluster Name, --cluster-name is required', required=True)
        arg('--vmgroup-name', nargs='?', const=True, default=False, metavar='VM Group Name', help='VM Group Name, --vmgroup-name is required', required=True)
        
        args = parser.parse_args(sys.argv[2:])
        print 'Running executeScript, cluster_name=%s' % args.cluster_name
        print 'Running executeScript, cluster_name=%s' % args.cluster_name
        pass
    
    def getScriptLogs(self):
        parser = argparse.ArgumentParser(
            description='get script execution scripts logs on specified cluster all servers, cluster vmgroup servers, a server in specified cluster')
        arg = parser.add_argument
        print 'Running getScriptExecutionLogs'
        pass

if __name__ == "__main__":
    F2CS()
