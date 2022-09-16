from concurrent.futures import ThreadPoolExecutor, as_completed
from email.quoprimime import body_check
import os
from urllib.parse import urlparse
import socket
import ipinfo




access_token="ACCESS_TOKEN"
handler = ipinfo.getHandler(access_token)


# Open and read history data
domain_names = set()
with open('history.txt', 'r') as f:
    data = f.readlines()
    for url in data:
        final_url = urlparse(url).netloc
        
        if len(final_url) > 0:
            domain_names.add(final_url)
        

# Convert domain into ip address and store into set.
ip_set = set()
for domain in domain_names:
    try:
        ip_addr = socket.gethostbyname(domain)
        ip_set.add((domain,ip_addr))
    except:
        print(domain)
        

# Get Detail IP info using 'ipinfo API'.
def get_details(ip_address):
    try:
        details = handler.getDetails(ip_address)
        return details.all
    except:
        return
complete_details = []

with ThreadPoolExecutor(max_workers=10) as e:
    for ip in list(ip_set):
        complete_details.append(e.submit(get_details, ip[1]))

'''
Response Example
{
 'ip': '52.231.26.45', 
 'city': 'Seoul', 
 'region': 'Seoul', 
 'country': 'KR', 
 'loc': '37.5660,126.9784', 
 'org': 'AS8075 Microsoft Corporation', 
 'postal': '03141', 
 'timezone': 'Asia/Seoul', 
 'country_name': 'South Korea', 
 'isEU': False, 
 'latitude': '37.5660', 
 'longitude': '126.9784'
 }
'''


locations=[]
for loc in as_completed(complete_details):
    locations.append(loc.result())


def ip_to_sort(ip):
    parsed_ip = ip.split('.')
    str=""
    for part in parsed_ip:
        str+=part
    return str

# Sort with ip
sorted_ip_list = sorted(list(ip_set), key = lambda tup: ip_to_sort(tup[1]))
sorted_locations = sorted(locations, key = lambda loc:ip_to_sort(loc['ip']))

with open('locations.dat', 'w') as f:
    f.write("domain|ip|country|city|org|latitude|longitude\n")
    for i in range(len(sorted_ip_list)):
        f.write(f"{sorted_ip_list[i][0]}|{sorted_locations[i]['ip']}|{sorted_locations[i]['country']}|{sorted_locations[i]['city']}|{sorted_locations[i]['org']}|{sorted_locations[i]['latitude']}|{sorted_locations[i]['longitude']}\n")
        
