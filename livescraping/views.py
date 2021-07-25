from rest_framework.response import Response
from rest_framework.views import APIView

import requests
from bs4 import BeautifulSoup as bs


class GetLatestKirtan(APIView):
    def get(self, request):
        res_l = []
        res = requests.get('https://www.akj.org/keertan.php')
        soup = bs(res.text, 'html.parser')
        samagams = soup.select('div.krtn_det')
        samagams_lists = soup.select('div.krtn_listing')
        for i in range(1):
            samagam_name = samagams[i].select_one('a').getText()
            shabads = samagams_lists[i].select('tbody tr')
            l = []
            for shabad in shabads:
                try:
                    title = shabad.select('td')[1].select_one(
                        'a').getText().replace('NEW', '')
                    dur = shabad.select('td')[0].getText()
                    try:
                        url = shabad.select('td')[3].select_one(
                            'a').attrs['href']
                    except:
                        url = None
                    type_ = shabad.select('td')[2].getText()

                    res_l.append({
                        'smaagam': samagam_name,
                        'artist': title,
                        'duration': dur,
                        'url': url
                    })
                except:
                    pass

        return Response(res_l)


class GetDropdowns(APIView):
    def get(self, request):
        res_l = []
        res = requests.get('https://www.akj.org/keertan.php')
        soup = bs(res.text, 'html.parser')

        dropdowns = soup.select('select')
        keys = ['country','location','year','month','artist']
        for i in range(5):
            dropdown = dropdowns[i]
            key = keys[i]

            options = dropdown.select('option')
            options_list = [{'value': o.attrs['value'], 'option': o.getText()} for o in options]

            res_l.append({
                key: options_list
            })

        
        return Response(res_l)


class GetSearchResults(APIView):
    def get(self, request, query):
        res_l = []
        res = requests.get(f'https://www.akj.org/keertan.php?{query}')
        soup = bs(res.text, 'html.parser')
        samagams = soup.select('div.krtn_det')
        samagams_lists = soup.select('div.krtn_listing')
        for i in range(len(samagams)):
            samagam_name = samagams[i].select_one('a').getText()
            shabads = samagams_lists[i].select('tbody tr')
            l = []
            for shabad in shabads:
                try:
                    title = shabad.select('td')[1].select_one(
                        'a').getText().replace('NEW', '')
                    dur = shabad.select('td')[0].getText()
                    try:
                        url = shabad.select('td')[3].select_one(
                            'a').attrs['href']
                    except:
                        url = None
                    type_ = shabad.select('td')[2].getText()

                    res_l.append({
                        'smaagam': samagam_name,
                        'artist': title,
                        'duration': dur,
                        'url': url
                    })
                except:
                    pass

        return Response(res_l)


class GetSmaagam(APIView):
    def get(slef, request, page_no):

        res_l = {'page_no': page_no}

        smaagam_list = []

        res = requests.get(f'https://www.akj.org/keertan.php?page={page_no}')
        soup = bs(res.text, 'html.parser')
        samagams = soup.select('div.krtn_det')
        for i in range(len(samagams)):
            samagam_name = samagams[i].select_one('a').getText()
            page_url = samagams[i].select_one('a').attrs['href']
            smaagam_list.append({
                'smaagam_name': samagam_name,
                'id': page_url.split('=')[-1]
            })

        res_l['smaagams'] = smaagam_list

        return Response(res_l)

class GetKirtanFromSmaagam(APIView):
    def get(self, request, id):
        res_l = []
        res = requests.get(f'https://www.akj.org/keertandetail.php?id={id}')
        soup = bs(res.text, 'html.parser')
        samagams = soup.select('div.krtn_det')
        samagams_lists = soup.select('div.krtn_listing')
        for i in range(len(samagams)):
            samagam_name = samagams[i].getText()
            shabads = samagams_lists[i].select('tbody tr')
            l = []
            for shabad in shabads:
                title = shabad.select('td')[1].getText().replace('NEW', '')
                dur = shabad.select_one('td').getText()
                try:
                    url = shabad.select('td')[3].select_one(
                        'a').attrs['href']
                except:
                    url = None
                type_ = shabad.select('td')[2].getText()

                res_l.append({
                    'smaagam': samagam_name,
                    'artist': title,
                    'duration': dur,
                    'url': url
                })

        return Response(res_l)

            


