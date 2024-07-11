import vonage
def send_msg():
    client = vonage.Client(key="YOUR_KEY", secret="YOUR_SECRET")
    sms = vonage.Sms(client)
    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": "YOUR_NUMBER",
            "text": "MESSAGE_TO_BE_SENT",
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
if __name__=='__main__':
    send_msg()
