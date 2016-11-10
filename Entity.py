# -*- coding: utf-8 -*-
#coding:utf-8
#Mod信息
import os
import crifanLib
class Mod(object):
    def __init__(self,Path,MD5,Href,Ignore,Delete):
        self.Path = Path
        self.MD5 = MD5
        self.Href = Href
        self.Ignore = Ignore
        self.Delete = Delete
#Mod信息Hook
def ConvertModHook(parsed_dict):
    return Mod(
        Path=parsed_dict['Path'],
        MD5=parsed_dict['MD5'],
        Href=parsed_dict['Href'],
        Ignore=parsed_dict['Ignore'],
        Delete=parsed_dict['Delete']
    )
#更新器基础信息
class Updater(object):
    def __init__(self,Url,Name,Port,Version,Debug):
        #客户端Config信息
        self.Url=Url
        self.Name=Name
        self.Port=Port
        self.Version=Version
        if Debug:
            self.Debug=Debug
        #else:
            
        #客户端Config信息
    def FullAddress(self):
        return self.Url+":"+bytes(self.Port)+"/ClientVersion.json"
    def ServerImage(self):
        #return self.ServerIcon
        if self.ServerIcon.strip():
            if os.path.exists('./resources/Server.ico') is False:
                crifanLib.downloadFile(self.ServerIcon,'./resources/Server.ico',True)
    def LoadServerInfo(self):
        #req = urllib2.Request(self.FullAddress())
        #res_data = urllib2.urlopen(req)
        res = crifanLib.getUrlRespHtml_multiTry(self.FullAddress())
        serverinfo = eval(res.replace("\r\n\t",""))
        #服务端Config信息
        self.ServerIcon = (serverinfo.has_key("ServerIcon") and serverinfo['ServerIcon'] or None)
        self.ServerVersion = serverinfo['ServerVersion']
        self.FilesAddress = serverinfo['FilesAddress']
        self.Updates = serverinfo['Updates']
        self.UpdateClientVersion = serverinfo['UpdateClientVersion']
        #服务端Config信息
#更新器基础信息Hook
def ConvertUpdaterHook(parsed_dict):
    return Updater(
        (parsed_dict.has_key("Url") and parsed_dict['Url'] or "http://www.bigcraft.cn")
        ,parsed_dict['Name']
        ,parsed_dict['Port']
        ,(parsed_dict.has_key("Version") and parsed_dict['Version'] or "0.1")
        ,(parsed_dict.has_key("Debug") and parsed_dict['Debug'] or None))
