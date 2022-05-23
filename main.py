from urllib import response
import requests
from bs4 import BeautifulSoup
import json
import csv
import time

class GoogleScraper:
    base_url = 'https://www.google.com/search'
    
    initial_params = {
        'q': 'site:linktr.ee',
        'sxsrf': "ALiCzsbKXWpw6qTl8JmlX6D0C_SjunQGdA':'1652962983174",
        'ei': 'pzaGYr2iCsiVxc8P1_-G6A8',
        'start': '',
        'sa': 'N',
        'ved': '2ahUKEwj9kcH7xuv3AhXISvEDHde_Af0Q8tMDegQIARA3',
        'biw': '957',
        'bih': '929',
        'dpr': '1',
    }
    
    
    pagination_params = {
        'q': 'site:linktr.ee', 
        'biw': '603',
        'bih': '929',
        'sxsrf': 'ALiCzsbP_aar6-Z2b1CN6wngvCuiRBYr1w:1652956712961',
        'ei': 'KB6GYvuqOs6Pxc8Ppv2m4A8',
        'ved': '0ahUKEwj73tHNr-v3AhXOR_EDHaa-Cfw48AEQ4dUDCA4',
        'uact': '5',
        'oq': 'site:linktr.ee' ,
        'gs_lcp': 'Cgdnd3Mtd2l6EANKBAhBGAFKBAhGGABQ7ARY7ARgvAdoAXAAeACAAYEBiAGBAZIBAzAuMZgBAKABAcABAQ',
        'sclient': 'gws-wiz'
    }
    
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'ANID=AHWqTUnyBm5iROxbMuQpJwyIyYx0eLQqoDfWcOG4xYLVMUQFRxv8xMRuELhnUqOI; OGPC=19025836-1:; OTZ=6470566_48_52_123900_48_436380; SEARCH_SAMESITE=CgQIq5UB; SID=KAhqt5yqlPOuTfVkNwMkSmWQSYxuQl8jkg4lk8DawDPBuyp_BvVBWpBA8useB_ayolfeMA.; __Secure-1PSID=KAhqt5yqlPOuTfVkNwMkSmWQSYxuQl8jkg4lk8DawDPBuyp_m5CBROniZAgb32eIPAHLLA.; __Secure-3PSID=KAhqt5yqlPOuTfVkNwMkSmWQSYxuQl8jkg4lk8DawDPBuyp_Vpld3MKs_anBC-hi6DcoJA.; HSID=AcUQazeCn_gyoCde2; SSID=A_QKRcUGqI7J1OT5f; APISID=1ZuSbeFeciYDqAws/AMrkdBhkczH2p0tC4; SAPISID=AFhkUODEjUhPI0Rc/AEFfk49R1Z3LwPvC-; __Secure-1PAPISID=AFhkUODEjUhPI0Rc/AEFfk49R1Z3LwPvC-; __Secure-3PAPISID=AFhkUODEjUhPI0Rc/AEFfk49R1Z3LwPvC-; NID=511=eTfDgE--5AxAzfQynDEj2MNU5Su0jZ5kRneVr10O9zpTlreXS__7qH1EUziZOvbH4yXuz507iVGtvCwCUMhRrIIXrx9eFPRFs98RBSTe0w7kFR1zvtrwsmjOyC71oSirkKxKMyANE4qjC3VeC2SlXoQQmL2pjJKDYe3C7AZOndFNb7EYQsefYQc0ASEiaeKfmKp2cDoiS2fw7aVG234L1e2u95BxsQbSlKJjYAk4fYKTvvuIcm1XJLSzqrNZhcW_e_-KkqdWdB2fjFNKar0Bj7KpbuVaGa6AWVMQOsorigeVg--J4fDJrufWXGfpJGpagSxn; AEC=AakniGO0OcitY_8D6B-M4gvAVX0duqaeO-fzsSGiVHAmbdvSmulHIAPaXw; 1P_JAR=2022-05-19-11; SIDCC=AJi4QfGW_KRInC-BmKXTgI_gSSoa_sH9pdbT2ls-_BTnBQEj4J6J046vGwnfmf4lwhDCJUfmMnQU; __Secure-3PSIDCC=AJi4QfGFV-NQb9fumMWq_kPfJZDiWNt7RHRct-W88LD1gKk3d1Y4VNv7HMWPPids4HL0EeLr-3uR',
        'referer': 'https://www.google.com/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36x-client-data: CJO2yQEIpbbJAQjEtskBCKmdygEIt/nKAQiWocsBCNvvywEInvnLAQjnhMwBCIiUzAEImprMAQi+qcwBCImrzAEI6qvMAQjDrMwBCKSvzAEYq6nKAQ==Decoded',
        
        
        }
    
    results = []
    
    def fetch(self,querry, page):
        self.initial_params['q'] = querry  
        
        if not page:
            params = self.initial_params
        else:
           params = self.pagination_params
           params['start'] = str(page)
            
        
        print(json.dumps(params, indent=2))
            
        return  requests.get(self.base_url, params= params, headers=self.headers)
        # print(f"Status code: {response.status_code}")    

        return response
     
    def parse(self,html):
        content = BeautifulSoup(html,"html.parser")
        
        link = [link.next_element['href'] for link in content.findAll('div', {'class' : 'yuRUbf'})]
        
        for index in range(0, len(link)):
            self.results.append({
                'link':link[index]
            })
        
    def write_csv(self):
        if len(self.results):
            print('Writing results to "results.csv "',end = '')
            with open('results.csv','w') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames = self.results[0].keys())
                writer.writeheader()
                
                for row in self.results:
                    writer.writerow(row)
        print("Done")
    
    
        
    def store_response(self,response):
        if response.status_code == 200:
            print('Saving response to "res.html"')
            with open('res.html','w') as html_file:
                html_file.write(response.text)
            print('Done')
        else:
            print('Bad response!')
    
    
    def load_response(self):
        html = ''
        with open('res.html', 'r') as html_file:
            for line in html_file.read():
                html += line
            
        return html
                
    
    
    def run(self):
        for page in range(0,2):
            if page:
                response = self.fetch('site:linktr.ee',page)
                self.parse(response.text)
            else:
                response = self.fetch('site:linktr.ee',page)
                self.parse(response.text)
            
            time.sleep(5)
            
        
       
        self.write_csv()
        
        
if __name__ == '__main__':
    
    scraper = GoogleScraper()
    scraper.run()