# By: https://twitter.com/@i127001
# coding: utf-8
from PyQt4 import QtCore
from bs4 import BeautifulSoup as BS
from time import sleep
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sleep_time = int(random.random() * 10)


# print dir(threading)
class Search_Thread(QtCore.QThread):
    """Searcher Class"""
    def __init__(self, parent=None):
        super(Search_Thread, self).__init__(parent)

    def get_data(self, sess, data):
        self.data = data
        # print(self.data)
        self.sess = sess
        self.path_for_save = str(self.data['workspace_path'])
        self.pages_count = int(self.data['pages_count'])
        self.from_page = int(self.data['from_page'])
        self.cap_x = int(self.data['x_cap'])
        self.cap_y = int(self.data['y_cap'])
        self.server = str(self.data['server'])
        self.t1 = str(self.data['t1'])
        self.t2 = str(self.data['t2'])
        self.t3 = str(self.data['t3'])
        self.t4 = str(self.data['t4'])
        self.t5 = str(self.data['t5'])
        self.t6 = str(self.data['t6'])
        self.t7 = str(self.data['t7'])
        self.t8 = str(self.data['t8'])
        self.t9 = str(self.data['t9'])
        self.t10 = str(self.data['t10'])
        self.max_player_pop = int(self.data['max_pl_pop'])
        self.max_village_pop = int(self.data['max_vl_pop'])
        self.alliance_exception = str(self.data['ignore_alliance']).split(',')
        self.players_exception = str(self.data['ignore_players']).split(',')
        self.timeout = 300
        self.searcher_log = ""
        self.h = {
            "Host": self.server,
            "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "http://ts70.travian.com/",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
        # self.stop = False

    def run(self):
        self.emit(QtCore.SIGNAL("search()"))
        static_from = int(self.data['from_page'])
        # print(static_from)
        # print(self.from_page)
        with self.sess as sess:  # noqa
            while(self.from_page <= self.pages_count + static_from - 1):
                # initializing page url
                self.page_url = "http://" + self.server + "/statistiken.php?id=2&idSub=0&page=" + str(self.from_page)  # noqa
                row = 1
                # if(self.stop):
                #     break
                sleep_time = int(random.random() * 10)
                sleep(sleep_time)
                while(row <= 20):
                    try:
                        # if(self.stop):
                        #     break
                        # get current villages page
                        page_source = sess.get(self.page_url, headers=self.h, verify=False, timeout=self.timeout)
                        bs = BS(page_source.content, 'html.parser')
                        # initializing village info
                        village_table = bs.findAll('table', {"id": "villages", "class": "row_table_data"})[0]
                        vill_row = village_table.findAll("tr")[row]
                        # info
                        village_rank = vill_row.findAll("td", {"class": "ra "})[0].string  # noqa
                        village_name = vill_row.findAll("td", {"class": "vil "})[0].findAll("a")[0].string  # noqa
                        village_link = vill_row.findAll("td", {"class": "vil "})[0].findAll("a")[0]['href']
                        village_z = village_link[12:]  # noqa
                        sleep_time = int(random.random() * 10)
                        sleep(sleep_time)
                        village_link = "http://" + self.server + "/" + village_link  # noqa
                        village_link = sess.get(village_link, headers=self.h, verify=False, timeout=self.timeout)
                        village_link = village_link.url
                        pla_name = vill_row.findAll("td", {"class": "pla "})[0].findAll("a")[0].string  # noqa
                        pla_link = vill_row.findAll("td", {"class": "pla "})[0].findAll("a")[0]['href']
                        pla_link = "http://" + self.server + "/" + pla_link  # noqa
                        village_pop = int(vill_row.findAll("td", {"class": "hab "})[0].string)  # noqa
                        x_y = vill_row.findAll("td", {"class": "coords "})[0].findAll("a")[0]['href']
                        x1 = int(x_y[x_y.index('x=') + 2:x_y.index('&')])
                        y1 = int(x_y[x_y.index('y=') + 2:])
                        # findig distance using co-ordinates
                        x = x1 - self.cap_x
                        y = y1 - self.cap_y
                        x = pow(x, 2)
                        y = pow(y, 2)
                        # distance as integer
                        distance = float(pow((x + y),0.5))  # noqa
                        # enter player profile
                        sleep_time = int(random.random() * 10)
                        sleep(sleep_time)
                        pla_profile = sess.get(pla_link, headers=self.h, verify=False, timeout=self.timeout).content
                        bs = BS(pla_profile, 'html.parser')
                        # intializing
                        pla_table = bs.findAll('table', {"id": "details"})[0]
                        # player_info
                        print(row)
                        try:
                            # if player have alliance
                            pla_alliance = pla_table.findAll('tr')[2].findAll('td')[0].findAll('a')[0].string
                        except Exception as e:  # noqa
                            # pass
                            # if player haven't alliance
                            pla_alliance = pla_table.findAll('tr')[2].findAll('td')[0].string
                        pla_pop = int(pla_table.findAll('tr')[4].findAll('td')[0].string)
                        # check search exceptions
                        if(pla_pop <= self.max_player_pop and village_pop <= self.max_village_pop and (pla_alliance not in self.alliance_exception) and (pla_name not in self.players_exception)):
                            f = open(self.path_for_save + 'farms_' + self.server + '.txt', 'a')
                            f.write("%.1f'|,|'%s'|,|'%s'|,|'%d'|,|'%s'|,|'%s'|,|'%s'|,|'%s'|,|'%s'|,|'%s'|,|'%s'|,|'%s'|,|'%s'|,|'%s'|,|'%d'|,|'%d\n" % (distance, village_z, village_name, village_pop, self.t1, self.t2, self.t3, self.t4, self.t5, self.t6, self.t7, self.t8, self.t9, self.t10, x1, y1))
                            self.searcher_log = "---Farm Added---\n"
                            self.searcher_log += "Village Rank : %s \n" % village_rank
                            self.searcher_log += "Village Name : %s \n" % village_name
                            self.searcher_log += "Village Pop : %s \n" % village_pop
                            self.searcher_log += "Village Link : %s \n" % village_link
                            self.searcher_log += "Player Name : %s \n" % pla_name
                            self.searcher_log += "Player Pop : %s \n" % pla_pop
                            self.searcher_log += "Player Link : %s \n" % pla_link
                            self.searcher_log += "Alliance : %s \n" % pla_alliance
                            self.searcher_log += "Distance : %.1f \n" % distance
                            self.searcher_log += '--------------'
                            self.emit(QtCore.SIGNAL('search_status(QString)'), self.searcher_log)
                            f.close()
                            fl = open(self.path_for_save + 'farms_' + self.server + '_JUST_LINKS.txt', 'a')
                            fl.write(village_link + "\n")
                            fl.close()
                        # increase row number
                    except:
                        pass
                    row = row + 1
                # increase page url
                self.from_page = self.from_page + 1
            self.searcher_log = '\n------------- \n'
            self.searcher_log += "Searching Finished \n"
            self.searcher_log += '-------------'
            self.emit(QtCore.SIGNAL('search_status(QString)'), self.searcher_log)
