import requests
import random
from func import oai, wph2, headers


file = open('keywords.txt', 'r')
keywords = file.readlines()
file.close()

kw_list = []

for keyword in keywords:
    kw = keyword.strip('\n').replace('best', '')
    kw_list.append(kw)

i = 0

while i <= len(kw_list):
    title = f' Why and How to buy {kw_list[i].title()}'
    intro = oai(f'write a short introduction about {kw_list[i]}')
    pro_feature_head = wph2(f' Main Features of {kw_list[i]}')
    pro_feature_para = oai(f' write details feature of {kw_list[i]}')
    pro_feature_head2 = wph2(f' Why {kw_list[i]} is Important in daily life')
    pro_feature_para2 = oai(f' write a list of Importance of {kw_list[i]} in daily life')
    buying_head = wph2(f' How to Buy {kw_list[i]} in a Minute')
    buying_para = oai(f' write how to buy {kw_list[i]} from web very easily')

    content = f'{intro}{pro_feature_head}{pro_feature_para} {pro_feature_head2}{pro_feature_para2}{buying_head}{buying_para}'

    i += 1

    data = {
        'title': title,
        'content': content,

    }

    header = headers('admin', 'WadR twQH MQwl oMUG Jlnk dKJR')
    endpoint = 'https://localhost/akeem/wp-json/wp/v2/posts'

    res = requests.post(endpoint, data=data, headers=header, verify=False)
    print(res.status_code)
