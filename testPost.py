#!/usr/bin/env python
#coding : utf8

import httplib, urllib
import json

def TestPost(jsonDic, url):
    httpClient = None
    
    try:
        jsonDic = json.dumps(jsonDic)
        params = jsonDic
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept":
        "text/plain"}
    
        httpClient = httplib.HTTPConnection("210.30.97.149", 4358, timeout=3000)
        httpClient.request("POST", url, params, headers)
    
        response = httpClient.getresponse()
        print response.status
        print response.reason
        print response.read()
        print response.getheaders()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

def testSignup():
    httpClient = None
    
    try:
        jsonDict = {'USER_NAME': 'rightpeter', 
                    'PASSWORD': '123456',
                    'REPASSWORD': '123456'}
        print jsonDict
        encoded_json = json.dumps(jsonDict)
        params = encoded_json
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept":
        "text/plain"}
    
        httpClient = httplib.HTTPConnection("210.30.97.149", 4358, timeout=3000)
        httpClient.request("POST", "/signup", params, headers)
    
        response = httpClient.getresponse()
        print response.status
        print response.reason
        print response.read()
        print response.getheaders()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

def testSignin():
    httpClient = None
    
    try:
        jsonDict = {'USER_NAME': 'rightpeter', 
                    'PASSWORD': '123456',
                    'LAT': '123.456', 
                    'LNG': '123.456'}

        print jsonDict
        encoded_json = json.dumps(jsonDict)
        params = encoded_json
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept":
        "text/plain"}
    
        httpClient = httplib.HTTPConnection("210.30.97.149", 4358, timeout=3000)
        httpClient.request("POST", "/signin", params, headers)
    
        response = httpClient.getresponse()
        print response.status
        print response.reason
        print response.read()
        print response.getheaders()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

if __name__ == "__main__":
    #test signup
    #jsonDict = {'USER_NAME': 'rightpeter', 
    #                'PASSWORD': '123456',
    #                'REPASSWORD': '123456'}
    #TestPost(jsonDict, '/signup')

    #test signin
    #jsonDict = {'USER_NAME': 'rightpeter', 
    #            'PASSWORD': '123456',
    #            'LAT': '123.456', 
    #            'LNG': '123.456'}
    #TestPost(jsonDict, '/signin')

    #test createroom
    #jsonDict = {'LAT': 123.456,
    #            'LNG': 123.456,
    #            'RANGE': 123.456,
    #            'ROOM_NAME': 'lu shao ai mei ling',
    #            'USER_NAME': 'rightpeter',
    #            'THEME': 'Lu shao\'s Love!',
    #            'PASSWORD': '123456',
    #            'MAX_NUM': 15,
    #            'TIME': 15,
    #            'METHOD': 'Pice of shit',
    #            'PWFLAG': 1}
    #TestPost(jsonDict, '/createroom')

    #test queryroom
    #jsonDict = {'LAT': 123.456,
    #            'LNG': 123.456,
    #            'RANGE': 1000}
    #TestPost(jsonDict, '/queryroom')

    #test postidea
    #jsonDict = {'ROOM_ID': 1,
    #            'CONTENT': 'Wo cao lu shao !',
    #            'POSTER_NAME': 'rightpeter'}
    #TestPost(jsonDict, '/postidea')

    #test join
    #jsonDict = {'ROOM_ID': 1,
    #            'USER_NAME': 'rightpeter',
    #            'PASSWORD': '123456'}
    #TestPost(jsonDict, '/join')

    #test acquirestatus
    jsonDict = {'ROOM_ID': 1,
                'USER_NAME': 'ssrightpeter'}
    TestPost(jsonDict, '/acquirestatus')
