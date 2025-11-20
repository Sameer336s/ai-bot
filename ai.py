import requests

def chat_with_ai(message):
    url = "https://api.sarvam.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "api-subscription-key": "sk_b7eki6ox_1Ii4uysekYYBOGizGuCUooLb"
    }
    data = {
        "model": "sarvam-m",
        "max_tokens": 9999,
        "messages": [{"role": "user", "content": message}]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.ok:
        result = response.json()
        print("DEBUG:", result)
        return result['choices'][0]['message']['content']   # ✔️ FIXED
    else:
        return "Error: " + response.text


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = chat_with_ai(user_input)
        print("AI:", reply)
