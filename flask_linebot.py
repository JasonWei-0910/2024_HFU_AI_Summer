from flask import Flask, request, abort , render_template

import os
from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
from   handle_keys import get_channel_data
from openai_api import chat_with_chatgpt

app = Flask(__name__)
keys = get_channel_data()
configuration = Configuration(access_token=keys['YUUKI_LINEBOT_ACCESS_TOKEN'])
handler = WebhookHandler(keys['YUUKI_LINEBOT_SECRET_KEY'])

@app.route("/")
def say_hello_world(username=""):
    return render_template('hello.html',name=username)



@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    user_id = event.source.user_id
    # print('User_id:',user_id)
    user_message = event.message.text
    api_key =keys['OPENAI_API_KEY']

    response = chat_with_chatgpt(user_id,user_message, api_key)
     




    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=response)]
            )
        )

if __name__ == "__main__":
    app.run(debug = True)