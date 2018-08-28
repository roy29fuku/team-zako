import json
import requests
import lxml.html
from tqdm import tqdm

def get_nips(i):
    data = []
    url = 'https://papers.nips.cc/book/advances-in-neural-information-processing-systems-{}-{}'.format(i,1987+i)
    url_base = 'https://papers.nips.cc'
    res = requests.get(url)
    html = lxml.html.fromstring(res.text)
    for li in tqdm(html.xpath('//div[@class="main wrapper clearfix"]/ul/li')):
        a = li.xpath('a')
        #print('title: ' + a[0].text)
        #print('authors: ' + ', '.join([author.text for author in a[1:]]))
        pdf_url = url_base + a[0].attrib['href'] + '.pdf'
        #print('url: ' + pdf_url)
        '''
        stc = requests.get(pdf_url).status_code
        if stc >= 300:
            print('!!! responce: {}, title: {}'.format(stc, a[0].text))
            continue
        '''
        data.append({'title':a[0].text, 'authors':[author.text for author in a[1:]], 'pdf': pdf_url})
    return data



if __name__ == '__main__':
    '''
    with open('nips.json', mode='r') as f:
        data = json.loads(f.read())
    '''
    #データの更新
    data = []
    for i in tqdm(range(1,31)):
        data.extend(get_nips(i))
    with open('nips.json', mode='w') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True, separators=(',', ': '))
