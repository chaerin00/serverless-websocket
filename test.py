import json
import requests


def lambda_handler(event, context):
    headers = {
        'Content-type': 'application/json',
    }

    json_data = {
        'text': '안녕하세요 애나봇입니다!',
    }

    response = requests.post(
        'web_hook_url',
        headers=headers,
        json=json_data,
    )
    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

