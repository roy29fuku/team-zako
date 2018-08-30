import json
import requests
import lxml.html
from tqdm import tqdm
import sys

#NIPS第i回
# => [{title, authors[], pdf_url},...]
def get_nips(i):
    data = []
    url = 'https://papers.nips.cc/book/advances-in-neural-information-processing-systems-{}-{}'.format(i,1987+i)
    url_base = 'https://papers.nips.cc'
    res = requests.get(url)
    html = lxml.html.fromstring(res.text)
    for li in tqdm(html.xpath('//div[@class="main wrapper clearfix"]/ul/li')):
        a = li.xpath('a')
        pdf_url = url_base + a[0].attrib['href'] + '.pdf'
        #print('title: ' + a[0].text)
        #print('authors: ' + ', '.join([author.text for author in a[1:]]))
        #print('url: ' + pdf_url)
        '''
	#pdf_urlが生きてるか雑に確認しようとした
        stc = requests.get(pdf_url).status_code
        if stc >= 300:
            sys.stderro.write('!!! responce: {}, title: {}'.format(stc, a[0].text))
            continue
        '''
        data.append({'title':a[0].text, 'authors':[author.text for author in a[1:]], 'pdf': pdf_url})
    return data

#python nips_scraping.py
#python nips_scraping.py <num> <output_file>
if __name__ == '__main__':
    if len(sys.argv) > 2:
        data = get_nips(int(sys.argv[1]))
        if len(data) == 0:
            sys.stderr.write('num => [1,2,...,30]')
            exit()
        with open(sys.argv[2], mode='w') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True, separators=(',', ': '))
    else:
        data = []
        for i in tqdm(range(1,31)):
            data.extend(get_nips(i))
        with open('nips.json', mode='w') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True, separators=(',', ': '))
