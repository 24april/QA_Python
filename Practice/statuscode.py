import requests


response = requests.get('https://easysmarthub.ru/1')


status_code = response.status_code


if status_code == 200:
    print('запрос выполнен')
elif status_code == 404:
    print('ресурс не найден')
elif status_code == 500:
    print('внутренняя ошибка сервера')
else:
    print(status_code)