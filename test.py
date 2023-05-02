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
        'https://hooks.slack.com/services/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',
        headers=headers,
        json=json_data,
    )
    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

