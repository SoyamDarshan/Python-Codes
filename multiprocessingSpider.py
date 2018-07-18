from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string

def random_starting_url():
    starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
    url = ''.join(["http://",starting,'.com'])
    return url
#url = random_starting_url()
#print(url)
    
def handle_local_links(url,link):
    if link.startswith('/'):
        return ''.join([url,link])
    else:
        return link
    
def get_links(url):
    try:
        resp = requests.get(url)
        soup = bs.BeautifulSoup(resp.text,'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]
        links = [handle_local_links(url,link) for link in links]
        links = [str(links.encode("ascii")) for links in links]
        return links
    
    except TypeError as e:
         print(e)
         print('Get a TypeError. Probably get a none that we tried to iterate over')
         return []
    except IndexError as e:
         print(e)
         print('We probably did not find any useful links,returninh empty list')
         return []
    except AttributeError as e:
         print(e)
         print('Likely got none for links, so we are throwing this')
         return[]
    except Exception as e:    
         print(str(e))
         return[]
         
def main():
    how_many = 50 
    p = Pool(processes=how_many)
    parse_us = [random_starting_url() for _ in range(how_many)]
    data = p.map(get_links, [link for link in parse_us])
    data = [url for url_list in data for url in url_list]


    with open('urls.txt','w') as f:
        f.write(str(data))
        
        
        
if __name__ == '__main__':
    main()        