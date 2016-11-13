import urllib.request;
import urllib;
import os
import hashlib
import Entity
#import os
__author__ = "Crifan Li (admin@crifan.com)"
#__version__ = ""
__copyright__ = "Copyright (c) 2012, Crifan Li"
__license__ = "GPL"
gConst = {
    'UserAgent' : 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
    #'UserAgent' : "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
    
    # also belong to ContentTypes, more info can refer: http://kenya.bokee.com/3200033.html
    # here use Tuple to avoid unexpected change
    # note: for tuple, refer item use tuple[i], not tuple(i)
    'picSufList'   : ('bmp', 'gif', 'jpeg', 'jpg', 'jpe', 'png', 'tiff', 'tif'),
    
    'defaultTimeout': 20, # default timeout seconds for urllib2.urlopen
}

#----------------------------------global values--------------------------------
gVal = {
    'calTimeKeyDict'    : {},
    'picSufChars'       : '', # store the pic suffix char list
    
    'currentLevel'      : 0,
    
    'cj'                : None, # used to store current cookiejar, to support auto handle cookies
    'cookieUseFile'     : False,
}
def saveBinDataToFile(binaryData, fileToSave):
    saveOK = False;
    try:
        savedBinFile = open(fileToSave, "wb"); # open a file, if not exist, create it
        #print "savedBinFile=",savedBinFile;
        savedBinFile.write(bytes(binaryData,encoding="utf8"));
        savedBinFile.close();
        saveOK = True;
    except :
        saveOK = False;
    return saveOK;
def getUrlRespHtml_multiTry(url, postDict={}, headerDict={}, timeout=0, useGzip=True, postDataDelimiter="&", maxTryNum=5):
    """
        get url response html, multiple try version:
            if fail, then retry
    """
    respHtml = "";
    
    # access url
    # mutile retry, if some (mostly is network) error
    for tries in range(maxTryNum) :
        try :
            respHtml = getUrlRespHtml(url, postDict, headerDict, timeout, useGzip, postDataDelimiter);
            #logging.debug("Successfully access url %s", url);
            break # successfully, so break now
        except :
            if tries < (maxTryNum - 1) :
                #logging.warning("Access url %s fail, do %d retry", url, (tries + 1));
                continue;
            else : # last try also failed, so exit
                #logging.error("Has tried %d times to access url %s, all failed!", maxTryNum, url);
                break;

    return respHtml;
def getUrlRespHtml(url, postDict={}, headerDict={}, timeout=0, useGzip=True, postDataDelimiter="&") :
    resp = getUrlResponse(url, postDict, headerDict, timeout, useGzip, postDataDelimiter);
    respHtml = resp.read();
    respInfo = resp.info();
    return respHtml;
def getUrlResponse(url, postDict={}, headerDict={}, timeout=0, useGzip=False, postDataDelimiter="&") :
    """Get response from url, support optional postDict,headerDict,timeout,useGzip

    Note:
    1. if postDict not null, url request auto become to POST instead of default GET
    2  if you want to auto handle cookies, should call initAutoHandleCookies() before use this function.
       then following urllib2.Request will auto handle cookies
    """

    # makesure url is string, not unicode, otherwise urllib2.urlopen will error
    url = str(url);

    if (postDict) :
        if(postDataDelimiter=="&"):
            postData = urllib.urlencode(postDict);
        else:
            postData = "";
            for eachKey in postDict.keys() :
                postData += str(eachKey) + "="  + str(postDict[eachKey]) + postDataDelimiter;
        postData = postData.strip();
        #logging.info("postData=%s", postData);
        req = urllib.request.Request(url, postData);
        #logging.info("req=%s", req);
        req.add_header('Content-Type', "application/x-www-form-urlencoded");
    else :
        req = urllib.request.Request(url);

    defHeaderDict = {
        'User-Agent'    : gConst['UserAgent'],
        'Cache-Control' : 'no-cache',
        'Accept'        : '*/*',
        'Connection'    : 'Keep-Alive',
    };

    # add default headers firstly
    for eachDefHd in defHeaderDict.keys() :
        #print "add default header: %s=%s"%(eachDefHd,defHeaderDict[eachDefHd]);
        req.add_header(eachDefHd, defHeaderDict[eachDefHd]);

    if(useGzip) :
        #print "use gzip for",url;
        req.add_header('Accept-Encoding', 'gzip, deflate');

    # add customized header later -> allow overwrite default header 
    if(headerDict) :
        #print "added header:",headerDict;
        for key in headerDict.keys() :
            req.add_header(key, headerDict[key]);

    if(timeout > 0) :
        # set timeout value if necessary
        resp = urllib.request.urlopen(req, timeout=timeout);
    else :
        resp = urllib.request.urlopen(req);
    #update cookies into local file
    if(gVal['cookieUseFile']):
        gVal['cj'].save();
        #logging.info("gVal['cj']=%s", gVal['cj']);
    return resp;
def appendModInfo(LocalMods):
    appendModInfoByPath("./.minecraft/mods/",LocalMods)
def appendModInfoByPath(filepath,LocalMods):
    for filePath in os.listdir(filepath):
        if os.path.isdir(filepath+filePath) is False:
            myhash = hashlib.md5()
            f = open(filepath+filePath,'rb')
            while True:
                b = f.read(8096)
                if not b :
                    break
                myhash.update(b)
            f.close()
            LocalMods.append(Entity.Mod(filepath+filePath,str(myhash.hexdigest()).upper(),"",False,False))
        else:
            appendModInfoByPath(filepath+filePath+"/",LocalMods)
#------------------------------------------------------------------------------
# download from fileUrl then save to fileToSave
# with exception support
# note: the caller should make sure the fileUrl is a valid internet resource/file
def downloadFile(fileUrl, fileToSave, needReport = False,reportPbr = None,mw=None) :
    isDownOK = False;
    downloadingFile = '';

    #---------------------------------------------------------------------------
    # note: totalFileSize -> may be -1 on older FTP servers which do not return a file size in response to a retrieval request
    
    
    def reportHook(copiedBlocks, blockSize, totalFileSize) :
        per = 100.0 * copiedBlocks * blockSize / totalFileSize
        if per > 100 :
            per = 100
        reportPbr.setProperty('value',per);
        mw.processEvents()
        #global downloadingFile
        # if copiedBlocks == 0 : # 1st call : once on establishment of the network connection
        #     if reportPbr is None:
        #         print 'Begin to download %s, total size=%d'%(downloadingFile, totalFileSize);
            #else:
                ###
        # else : # rest call : once after each block read thereafter
        #     if reportPbr is None:
        #         print 'Downloaded bytes: %d\r' % ( blockSize * copiedBlocks),;
            #else:
                ###
        return;
    #---------------------------------------------------------------------------

    try :
        if fileUrl :
            downloadingFile = fileUrl;
            if os.path.exists(os.path.split(fileToSave)[0]) is False:
                os.makedirs(os.path.split(fileToSave)[0])
                #文件夹不存在 创建文件夹
            if needReport :
                urllib.request.urlretrieve(fileUrl, fileToSave, reportHook);
            else :
                urllib.request.urlretrieve(fileUrl, fileToSave);
            isDownOK = True;
        else :
            print("Input download file url is NULL");
    except :
        isDownOK = False;

    return isDownOK;
