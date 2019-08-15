PossibleEnds = [".hC",".HC",".hc","retpahc","retpahC"]

def substring_after(s, delim):
    return s.partition(delim)[2]

def format_title(s):
    title = s[6:]
    title = title[::-1]
    for ends in PossibleEnds:
        temp = title
        temp = substring_after(temp,ends)
        if (temp != "") and (len(temp) < len(title)):
            title = temp
    title = title[1:]
    title = title[::-1]
    return title

import requests
import json

cookies = {
    '_ga': 'GA1.3.1038486053.1542561338',
    '_ym_uid': '1542561339647743396',
    '_fbp': 'fb.2.1550331316060.696686415',
    's_fid': '4759FA97A926D66C-0F1B974C52481DC9',
    's_pers': '%20v8%3D1559638183612%7C1654246183612%3B%20v8_s%3DFirst%2520Visit%7C1559639983612%3B%20c19%3Dpr%253Apure%2520portal%253Apersons%253Aview%7C1559639983623%3B%20v68%3D1559638180222%7C1559639983636%3B',
    '_ym_d': '1563123313',
    '_gid': 'GA1.3.263899644.1565534356',
    'has_js': '1',
    'AUTHSSL': '1',
    'SSESS4985c7dbe54e755248659c29e4b83d20': 'SjP2uRMx-kYZ3IuFyM1NFEqhVfC6klgD6EFmtVVt9lw',
}

headers = {
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'headerVal': 'onggfX40Vqkq0EASIloz1cJQAHzFldtSGlQx8-Z2jdY',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://registrar.nu.edu.kz/my-registrar/course-registration',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

params = (
    ('_dc', '1565893034576'),
    ('method', 'getCourseDetails'),
    ('instanceid', '13254'),
)

response = requests.get('https://registrar.nu.edu.kz/my-registrar/course-registration/json', headers=headers, params=params, cookies=cookies)


def loadCreative():
    arrayOfSections = json.loads(response.text)['COMPONENTS']
    responses = []
    for section in arrayOfSections:
         if int(section['REGISTEREDSTUDENTS']) < 16:
             responses.append(
                 section['INSTRUCTORNAME'] + ": " + section['REGISTEREDSTUDENTS'] + "/" + section['CLASSCAPACITY'])

    return ", ".join(responses) if len(responses) !=0 else None


