
import requests
import json
import os

def handler(event, context):
    
    print(event)
    URL = os.environ['APIGW_URL'] + event['path']
    HTTP_METHOD='';
        
    headers={};
    response = {};
    body = {};
    
    if "authorization" in event['headers']:
        headers['authorization'] = event['headers']['authorization']
        

    if "content-type" in event['headers']:
        headers['content-type'] = event['headers']['content-type']
        
        
    if "body" in event and len(event['body']) != 0:
        body=json.loads(event['body'])
        
        
    
    if "httpMethod" in event:
        HTTP_METHOD = event['httpMethod']
        
    
    if HTTP_METHOD == 'GET':
        r = requests.get(url = URL, headers=headers)
        response["statusCode"] = 200
        response["isBase64Encoded"] = False
        response['body'] = json.dumps(r.json())
        response['headers'] = {'content-type': 'application/json; charset=utf-8'}
        
        

    if HTTP_METHOD == 'POST':
        
        r = requests.post(url = URL, headers=headers, json=body)
        response["statusCode"] = 200
        response["isBase64Encoded"] = False
        response['body'] = json.dumps(r.json())
        response['headers'] = {'content-type': 'application/json; charset=utf-8'}
        
        
        

    if HTTP_METHOD == 'PUT':
        r = requests.put(url = URL, headers=headers, json=body)
        response["statusCode"] = 200
        response["isBase64Encoded"] = False
        response['body'] = json.dumps(r.json())
        response['headers'] = {'content-type': 'application/json; charset=utf-8'}
        
        
     

    print(response);
    
    return response;
  
 