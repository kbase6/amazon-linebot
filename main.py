from linebot import LineBotApi
from linebot.models import TextSendMessage

# Initialize Line API with your Channel Access Token
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')

def forward_to_line(message):
    line_group_id = 'YOUR_LINE_GROUP_ID'
    line_bot_api.push_message(line_group_id, TextSendMessage(text=message))
