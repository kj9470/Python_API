import requests
import xmltodict
import json
from pprint import pprint

def get_corona_data(startCreateDt, endCreateDt) :

    url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"
    params = {
        'serviceKey' : 'S0cE1bTwUnT68+NiRGRQckj0pzc9NTHvK3tdfywgj+9F0lcnqGgdTCL63HLkBMsE1YPpGBCn1+/W88ZxoSoqsA==',
        'pageNo' : '1',
        'numOfRows' : 10,
        'startCreateDt' : startCreateDt, #'20210203',
        'endCreateDt' : endCreateDt, #'20210203',
    }
    check = requests.get(url, params = params)
    #print(check.url)
    #print(check.text)

    # xml to dict
    dict_data = xmltodict.parse(check.text)
    #print(dict_data)

    # dict to json
    json_data = json.dumps(dict_data)
    #print(json_data, type(json_data))

    # json to dict
    dict_data = json.loads(json_data)
    #print(dict_data, type(dict_data))
    #pprint(dict_data['response']['body']['items']['item'])

    # totalCount 값이 제대로 들어왔는지 확인
    totalCount = dict_data['response']['body']['totalCount']
    #print(totalCount)

    # 지역 정보를 담은 리스트
    local_data = dict_data['response']['body']['items']['item']
    local_data.reverse()
    #print(local_data)

    return local_data

if __name__ == '__main__':
    get_data = get_corona_data('20210202', '20210202')
    # print(get_data)
