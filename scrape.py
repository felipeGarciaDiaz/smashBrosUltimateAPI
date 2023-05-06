import urllib.request 
from bs4 import BeautifulSoup
#https://game8.co/games/SSBU/archives/281177
#https://game8.co/games/SSBU/archives/281252


def SBU():

    def clean_data(sbu_data):
        return sbu_data.split("(")[0]

    
    # Loop through all the routes on the page to collect all character data 281253
    for search_site_range in range(281177, 281185):
        url = "https://game8.co/games/SSBU/archives/" + str(search_site_range)
        headers_user_agents = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
        send_request = urllib.request.Request(url, headers=headers_user_agents)
        site = urllib.request.urlopen(send_request)
        html = BeautifulSoup(site.read().decode('utf-8'), 'html.parser')








        def gen_info():
            sbu_table_data = html.find('table', class_='a-table a-table a-table center')
            sbu_player_name = sbu_table_data.find('th')
            sbu_table_rows = sbu_table_data.find_all('td')

            SBU.player_name = sbu_player_name.get_text()
            SBU.fighter_number = sbu_table_rows[3].get_text()
            SBU.unlock_order = sbu_table_rows[4].get_text()
            SBU.number_of_jumps = sbu_table_rows[5].get_text()

            SBU.weight = clean_data(sbu_table_rows[6].get_text())
            SBU.dash_speed = clean_data(sbu_table_rows[7].get_text())
            SBU.air_speed = sbu_table_rows[8].get_text()
            SBU.fast_fall_speed = clean_data(sbu_table_rows[9].get_text())

            SBU.special_attr = sbu_table_rows[10].get_text()

            return print(SBU.player_name + '\n' + SBU.special_attr + '\n' + SBU.fast_fall_speed + '\n\n\n\n\n')

        #gen_info()

        def combos():
            def clean_arrows(sbu_arrow_data):
                special_chars = ['→', '━', '┣', '┗']
                #return sbu_arrow_data.replace("→", " > ")
                x = -1
                for chars in range(3):
                    x+=1
                    print(x)
                    return sbu_arrow_data.replace(special_chars[x], '>')
                    
                    #return print(special_chars[chars])
            sbu_table_data = html.find_all('table', class_='a-table a-table')
            sbu_table_select = sbu_table_data[1]
            sbu_table_rows = sbu_table_select.find_all('tr')

            for rows in sbu_table_rows:
                print(clean_arrows(rows.get_text()))
        combos()

SBU()


















    #def request_sites(site_range, ref_attribute, ref_attribute_name, splice_words, splice_words_range, list_data):
     #   # Init request, obtain url, of the site being scraped
      #  url = "https://game8.co/games/SSBU/archives/" + str(site_range)
       ### Send the request to the server with the header included on the request
        #send_request = urllib.request.Request(url, headers=headers_user_agents)
        #site = urllib.request.urlopen(send_request)
        #html = BeautifulSoup(site.read().decode('utf-8'), 'html.parser')

        
        # If the method is true, this is a class. if not its an id that we are scraping and looking for
       # if ref_attribute:
           # sbu_player_name = html.find(class_=ref_attribute_name).get_text()
        #else:
         #   sbu_player_name = html.find(id=ref_attribute_name).get_text()

        #print(sbu_player_name.split(splice_words, splice_words_range)[list_data])