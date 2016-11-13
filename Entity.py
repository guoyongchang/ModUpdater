# -*- coding: utf-8 -*-
#coding:utf-8
#Mod信息
import os
import Helper
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
        return self.Url+":"+str(self.Port)+"/ClientVersion.json"
    def ServerImage(self):
        #return self.ServerIcon
        if self.ServerIcon.strip():
            if os.path.exists('./resources/Server.ico') is False:
                a = "";
                #crifanLib.downloadFile(self.ServerIcon,'./resources/Server.ico',True)
    def LoadServerInfo(self):
        res = Helper.getUrlRespHtml_multiTry(self.FullAddress())
        serverinfo = eval(str(res,encoding="utf8").replace("\r\n\t",""))
        #服务端Config信息
        self.ServerIcon = ("ServerIcon" in serverinfo.keys() and serverinfo['ServerIcon'] or None)
        self.ServerVersion = serverinfo['ServerVersion']
        self.FilesAddress = serverinfo['FilesAddress']
        self.Updates = serverinfo['Updates']
        self.UpdateClientVersion = serverinfo['UpdateClientVersion']
        #服务端Config信息
#更新器基础信息Hook
def ConvertUpdaterHook(parsed_dict):
    return Updater(
        ("Url" in parsed_dict.keys() and parsed_dict['Url'] or "http://www.bigcraft.cn")
        ,parsed_dict['Name']
        ,parsed_dict['Port']
        ,("Version" in parsed_dict.keys() and parsed_dict['Version'] or "0.1")
        ,("Debug" in parsed_dict.keys() and parsed_dict['Debug'] or None))
