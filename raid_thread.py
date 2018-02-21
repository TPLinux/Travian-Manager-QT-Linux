# By: https://twitter.com/@i127001
# coding: utf-8
from PyQt4 import QtCore
from bs4 import BeautifulSoup as BS  # noqa
from time import sleep  # noqa
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sleep_time = int(random.random() * 10)
class Raid_Thread(QtCore.QThread):
    """Raider Class"""

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

    def get_data(self, sess, data):
        self.data = data
        self.raider_log = ""
        self.sess = sess
        self.workspace_path = str(data['workspace_path'])
        self.server = str(data['server'])
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
        self.timeout = 300
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

    def run(self):
        self.emit(QtCore.SIGNAL('raid()'))
        file = self.workspace_path + 'farms_' + self.server + ".txt"
        first_lst = []
        lst = []
        # read farms
        f = open(file, 'r')
        # assigment farms in the first_lst to sort them
        lines_ = f.readlines()
        # farms count
        self.farm_numbers = len(lines_)
        # remove \n
        for i in lines_:
            i = i[:i.index('\n')]
            i = i.split("'|,|'")
            first_lst.append(i)
        for n in first_lst:
            lst.append([float(n[0]), n[1], n[2], n[3], n[4], n[5], n[6], n[7], n[8], n[9], n[10], n[11], n[12], n[13], n[14], n[15]])
        # sort farms order by distance
        lst.sort()
        # distance = lst[x][0]
        # Z-ID     = lst[x][1]
        # Vil Name = lst[x][2]
        # vil Pop  = lst[x][3]
        # t1       = lst[x][4]
        # t2       = lst[x][5]
        # t3       = lst[x][6]
        # t4       = lst[x][7]
        # t5       = lst[x][8]
        # t6       = lst[x][9]
        # t7       = lst[x][10]
        # t8       = lst[x][11]
        # t9       = lst[x][12]
        # t10      = lst[x][13]
        # x        = lst[x][14]
        # y        = lst[x][15]
        with self.sess as sess: # noqa
            for farm in lst:
                first_url = "http://" + self.server + "/build.php?id=39&tt=2&z=" + farm[1]
                attack_url = "http://" + self.server + "/build.php?id=39&tt=2"
                first_source = sess.get(first_url, headers=self.h, verify=False, timeout=self.timeout).content
                bs = BS(first_source, 'html.parser')
                # parameters info
                timestamp = bs.findAll('input', {"name": 'timestamp'})[0]['value']
                timestamp_checksum = bs.findAll('input', {"name": 'timestamp_checksum'})[0]['value']
                b = bs.findAll('input', {"name": 'b'})[0]['value']
                current_did = bs.findAll('input', {"name": 'currentDid'})[0]['value']
                # initializing post data
                first_post_data = {  # noqa
                    "timestamp": timestamp,
                    "timestamp_checksum": timestamp_checksum,
                    "b": b,
                    "currentDid": current_did,
                    "t1": farm[4],
                    "t2": farm[5],
                    "t3": farm[6],
                    "t4": farm[7],
                    "t5": farm[8],
                    "t6": farm[9],
                    "t7": farm[10],
                    "t8": farm[11],
                    "t9": farm[12],
                    "t10": farm[13],
                    "dname": "",
                    "x": farm[14],
                    "y": farm[15],
                    "c": "4",
                    "s1": "ok"
                    }
                # send first request
                sleep_time = int(random.random() * 10)
                sleep(sleep_time)
                try:
                    second_source = sess.post(attack_url, data=first_post_data, headers=self.h, verify=False, timeout=self.timeout)
                    bs = BS(second_source.content, 'html.parser')
                    # second post data
                    a = bs.findAll('input', {"type": "hidden", "name": "a"})[0]['value']
                    kid = bs.findAll('input', {"type": "hidden", "name": "kid"})[0]['value']
                    # second post data
                    second_post_data = {
                        "redeployHero": "",
                        "timestamp": timestamp,
                        "timestamp_checksum": timestamp_checksum,
                        "id": "39",
                        "a": a,
                        "c": "4",
                        "kid": kid,
                        "t1": farm[4],
                        "t2": farm[5],
                        "t3": farm[6],
                        "t4": farm[7],
                        "t5": farm[8],
                        "t6": farm[9],
                        "t7": farm[10],
                        "t8": farm[11],
                        "t9": farm[12],
                        "t10": farm[13],
                        "t11": "0",
                        "sendReally": "0",
                        "troopsSent": "1",
                        "currentDid": current_did,
                        "b": "2",
                        "dname": "",
                        "x": farm[14],
                        "y": farm[15],
                        "s1": "ok"
                    }
                    sleep_time = int(random.random() * 10)
                    sleep(sleep_time)
                    final_source = sess.post(attack_url, data=second_post_data, headers=self.h, verify=False, timeout=self.timeout)
                    if("troop_details outRaid" in final_source.content):
                        self.raider_log = "Attack sent To (%s | %s), Village: %s" % (str(farm[14]).encode('utf-8'), str(farm[15]).encode('utf-8'), str(farm[2]).encode('utf-8'))
                        self.raider_log += "\nLink : http://%s" % (self.server + "/karte.php?d=" + str(farm[1]).encode('utf-8'))
                        self.raider_log += "\nDistance : %s" % str(farm[0]).encode('utf-8')
                        self.raider_log += "\n------"
                        self.emit(QtCore.SIGNAL('raid_status(QString)'), self.raider_log)
                except Exception as e:
                    print(e)
                    self.raider_log = '------'
                    self.raider_log += "\nProblem with Send Attack To (%s | %s), Village: %s" % (str(farm[14]).encode('utf-8'), str(farm[15]).encode('utf-8'), str(farm[2]).encode('utf-8'))
                    self.raider_log += "\n------"
                    self.emit(QtCore.SIGNAL('raid_status(QString)'), self.raider_log)
                    pass
            self.raider_log = "\n-------------"
            self.raider_log += "\nRaiding Finished"
            self.raider_log += "\n-------------\n\n"
            self.emit(QtCore.SIGNAL('raid_status(QString)'), self.raider_log)
