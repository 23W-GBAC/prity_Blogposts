import requests

def send_to_telegram(message):

    apiToken = '6490356169:AAGpU9ojduVolrj6U3gi0dvUmMgAuCp_2wg'
    chatID = '6847742875'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

send_to_telegram("Hello from Python!")