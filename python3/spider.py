#!/usr/bin/python
# -*- coding: UTF-8 -*- 
"""
 需要安装requests模块
 ## python -m pip install --upgrade pip
 ## pip install requests
 ## author Xiaowu@sql.hk
 ## 调用方式
 ## python vqq.py q0681zrmx3c
 ## python vqq.py https://v.qq.com/x/page/q0681zrmx3c.html
## vid = 'q0681zrmx3c' 
""" 
import requests
import json
from sys import argv
import re
class SparkGo_TencentVideo:
    __VQQ_VIDEO_INFO_URL__='http://h5vv.video.qq.com/getinfo'
    __VQQ_VIDEO_KEY_URL__='http://h5vv.video.qq.com/getkey'
    __VQQ_MODEL_LIST__=['shd', 'hd', 'sd']
    __VQQ_URLS__={'shd':[],'hd':[],'sd':[]}
    __VQQ_FILE_NAME__=""
    vid=""
    
    def  GetVid(self):
        pythonfile,videourl=argv
        isHttp = re.match(r'^http[s]?\:\/\/' , videourl )
        if isHttp:  
            if re.match(r'\?' , videourl ):
                urlInfo =  videourl.split('?')
                videourl = urlInfo[0]
            urlTemp =  videourl.split('/')
            urlFileName= urlTemp[len(urlTemp)-1]
            urlBaseName = urlFileName.split('.')
            videourl=urlBaseName[0]      
        self.vid=videourl
        self.__VQQ_FILE_NAME__=videourl + '.mp4'

    def  ReuqestJson(self ,url , param ):
        r = requests.get(url, params=param)
        data = json.loads(r.content[len('QZOutputJson='):-1])  
        return data 

    def GetStream(self,data,videoType):
         url_prefix = data['vl']['vi'][0]['ul']['ui'][0]['url']
         for stream in data['fl']['fi']:
            if stream['name'] != videoType:
                continue
            stream_id = stream['id']   
            for d in data['vl']['vi'][0]['cl']['ci']:
                keyid = d['keyid']
                filename = keyid.replace('.10', '.p', 1) + '.mp4'
                self.__VQQ_FILE_NAME__=filename
                params = {
                    'otype': 'json',
                    'vid': self.vid,
                    'format': stream_id,
                    'filename': filename,
                    'platform': 10901,
                    'vt': 217,
                    'charge': 0,
                }
                data = self.ReuqestJson(self.__VQQ_VIDEO_KEY_URL__, params )
                url = '%s/%s?sdtfrom=v1010&vkey=%s' % (url_prefix, filename, data['key'])
                self.__VQQ_URLS__[stream['name']].append(url)

    def Download(self,url,localPath):
        r = requests.get( url ) 
        with open( self.__VQQ_FILE_NAME__ , "wb" ) as code:
            code.write( r.content )   

    def Start(self):
        self.GetVid()
        for videoType in self.__VQQ_MODEL_LIST__:
            params = {
                'isHLS': False,
                'charge': 0,
                'vid': self.vid,
                'defn': videoType,
                'defnpayver': 1,
                'otype': 'json',
                'platform': 10901,
                'sdtfrom': 'v1010',
                'host': 'v.qq.com',
                'fhdswitch': 0,
                'show1080p': 1,
            }
            data=self.ReuqestJson(self.__VQQ_VIDEO_INFO_URL__ , params )
            self.GetStream(data,videoType)
        for urlObject in self.__VQQ_URLS__:
            print ('stream:', urlObject)
            for url in self.__VQQ_URLS__[urlObject]:
                print (url) 

TencentVideo=SparkGo_TencentVideo()
TencentVideo.Start()
