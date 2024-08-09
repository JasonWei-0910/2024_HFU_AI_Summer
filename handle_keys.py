
import os,sys

def get_channel_data():

    channel_secret = os.getenv('YUUKI_LINEBOT_SECRET_KEY', None)
    channel_access_token = os.getenv('YUUKI_LINEBOT_ACCESS_TOKEN', None)
    openai_api_key = os.getenv('OPENAI_API_KEY', None)
    if channel_secret is None:
        print('Specify YUUKI_LINEBOT_SECRET_KEY as environment variable.')
        sys.exit(1)
    if channel_access_token is None:
        print('Specify YUUKI_LINEBOT_ACCESS_TOKEN as environment variable.')
        sys.exit(1)
    if openai_api_key is None:
        print('Specify OPENAI_API_KEY as environment variable.')
        sys.exit(1)

    return{
        'YUUKI_LINEBOT_SECRET_KEY':channel_secret,
        'YUUKI_LINEBOT_ACCESS_TOKEN': channel_access_token,
        'OPENAI_API_KEY': openai_api_key
    }