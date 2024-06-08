import requests
import re

import consts


def text_formation(text):
    text = re.sub(r'\*\*', '', text)
    parts = re.split(r'(Задание:|Ответ:)', text, flags=re.IGNORECASE)
    if len(parts[2]) > 150 or len(parts) < 5:
        return None
    formatted_parts = []
    for i in range(len(parts)):
        if i % 2 == 0:
            part = parts[i].strip()
            part = re.sub(r'\n', ' ', part)
            part = part[:-1] if part.endswith('.') else part
            formatted_parts.append(part)
        else:
            formatted_parts.append(parts[i])
    formatted_parts[4] = re.sub(r'[^0-9]', '', formatted_parts[4])
    return {
        "problem": formatted_parts[2],
        "solution": formatted_parts[4]
    }


def yandex_gpt_generation(url, headers, prompt):
    try:
        response = requests.post(url, headers=headers, json=prompt)
        result = response.json()['result']['alternatives'][0]['message']['text']
    except Exception as e:
        print("Restart generation because of Yandex GPT error:", e)
        return yandex_gpt_generation(url, headers, prompt)

    formatted_result = text_formation(result)
    if formatted_result is None:
        print('Restart generation because of request misunderstanding')
        return yandex_gpt_generation(url, headers, prompt)
    return formatted_result


def yandex_gpt_setup():
    prompt = {
        "modelUri": f"gpt://{consts.YANDEX_GPT_DIRECTORY_ID}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты ассистент - учитель математики, который должен проверять ученика на смекалку, "
                        "присылая ему математический пример."
                        r"Начинай свой ответ со слова Задание."
                        r"Условие задания-примера должно содержать не больше 150 символов."
                        r"В задании нужно найти число по какому-то придуманному условию."
                        "В конце пиши правильный ответ для задания-примера, начиная со слова Ответ."
                        "В форматировании текста задачи не должно быть форматирования текста и пробелов между строками."
                        "Ответ должен состоять только из числа, которое является решением для задания-примера."
                        "Единственный допустимый пример формата задачи "
                        "('...' - поле, куда ты должен вставить свой текст):"
                        "Задание: ... "
                        "Ответ: ..."
            },
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {consts.YANDEX_GPT_API_KEY}"
    }

    return yandex_gpt_generation(url, headers, prompt)
