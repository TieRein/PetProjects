import json
import requests
import re
import boto3
from boto3.dynamodb.conditions import Key, Attr

lambda_client = boto3.client('lambda')
payload = {}
headers = {
    "User-Agent": "PostmanRuntime/7.29.2",
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate",
    "Connection": "keep-alive",
    "Content-Type": "application/json"
}

#                  Jacob         Kylee         Connor
phone_numbers = [ "5417782508", "3072625482", "5415912393" ]
#phone_numbers = [ "5417782508" ]

def lambda_handler(event, context):
    persistent_data = get_persistent_data()
    
    url = "https://www.visualcapitalist.com/"
    first_regex=r'mvp-feat5-small-main-img left relative\">[\n\t]*<a href=\"(?P<url>[:a-zA-Z\.\/-]*)'
    second_regex=r'(?:<p>|</div>[\n]*)<img src=\"(?P<image>[a-zA-Z0-9:.\-_\/]*)\" (?:alt=\"(?P<alt_text>[a-zA-Z0-9 .]*)|usemap=)'

    ret = scrape_web(url, first_regex, ["url"])
    #ret["url"]="https://www.visualcapitalist.com/sp/how-much-waste-does-a-renovation-create/"
    ret = scrape_web(ret["url"], second_regex, ["image", "alt_text"])
    if (ret["alt_text"] == None):
        ret["alt_text"] = "This post is sponsored"
    
    print("Image: ", ret["image"])
    print("Alt Text: ", ret["alt_text"])
    print("persistent_data: ", persistent_data)
    print('persistent_data != (ret["alt_text"] + ret["image"]): ', (persistent_data != (ret["alt_text"] + ret["image"])))
    if persistent_data != (ret["alt_text"] + ret["image"]):
        message = f'{ret["alt_text"]}\n\n{ret["image"]}'
        for number in phone_numbers:
            send_text(number, message)
        set_persistent_data((ret["alt_text"] + ret["image"]))
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }







def scrape_web(url, regex, groups):
    print("url: ", url)
    print("regex: ", regex)
    print("groups: ", groups)
    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.text
    pattern=re.compile(regex)
    match = pattern.search(response)
    print("match: ", match)
    ret = {}
    for group in groups:
        ret[group] = match.group(group)
    print("ret: ", ret)
    
    return ret
    
def get_persistent_data( lambda_function_name = "VisualCapitalistPoster" ):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('lambda_persistent_data')
    response = table.query(
        KeyConditionExpression=Key('function_name').eq(lambda_function_name)
    )
    items = response['Items']
    if len(items) == 0:
        table.put_item(
            Item={
                'function_name': lambda_function_name,
                'data': ''
            })
        return ''
    else:
        print("items: ", items[0])
        return items[0]["data"]
        
def set_persistent_data( data, lambda_function_name = "VisualCapitalistPoster" ):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('lambda_persistent_data')
    table.put_item(
        Item={
            'function_name': lambda_function_name,
            'data': data
        })
        
def send_text(phone_number, message):
    send_text={
      "phoneNumber": phone_number,
      "message": message
    }
    print("Text to be sent: ", send_text)
    response = lambda_client.invoke(
        FunctionName='text',
        Payload=json.dumps(send_text),
    )
    print(response['Payload'])
    print(response['Payload'].read().decode("utf-8"))
