import requests


def translat(text, tran_f, tran_t):
    API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(tran_f, tran_t)
    }

    response = requests.get(URL, params=params)
    return response


if __name__ in '__main__':
    pass

