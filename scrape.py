from urllib.request import urlopen
from bs4 import BeautifulSoup
#https://game8.co/games/SSBU/archives/281177
#https://game8.co/games/SSBU/archives/281252


def main():
    for SITE_RANGE in range(281177, 281253):
        URL = "https://game8.co/games/SSBU/archives/" + str(SITE_RANGE)
        SITE = urlopen(URL)
        HTML = BeautifulSoup(SITE.read().decode('utf-8'), 'html.parser')

        SBU_PLAYER_NAME = HTML.find(class_='p-archiveHeader__title').get_text()
        print(SBU_PLAYER_NAME.split('Guide', 1)[0])


if __name__ == '__main__':
    main()