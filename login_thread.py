from PyQt4 import QtCore
from bs4 import BeautifulSoup as BS
class Login_Thread(QtCore.QThread):

    def __init__(self, parent=None):
        super(Login_Thread, self).__init__(parent)

    def get_data(self, sess, data):
        self.server = str(data['server'])
        self.path_for_save = str(data['workspace_path'])
        # login post info
        self.url = "https://" + self.server + "/dorf1.php"
        self.username = str(data['username'])
        self.password = str(data['password'])
        # request header
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
        # login form data
        self.login_data = {
            "name": self.username,
            "password": self.password,
            "lowRes": "1",
            "s1": "Login",
            "w": "840:460",
            "login": ""
        }
        # time out of request
        self.timeout = 300
        self.sess = sess

    def run(self):
        self.emit(QtCore.SIGNAL("login()"))
        with self.sess as s:
            try:
                resp = s.post(self.url, data=self.login_data, headers=self.h, verify=False, timeout=self.timeout)
                resp = resp.content
                bs = BS(str(resp), 'html.parser')
                pla_name = bs.findAll("div", {"class": "playerName"})[0].findAll('a', {'href': 'spieler.php'})[1].string
                if(str(pla_name).lower() == self.username.lower()):
                    self.emit(QtCore.SIGNAL("login_status(bool)"), True)
                    # return True
                else:
                    self.emit(QtCore.SIGNAL("login_status(bool)"), False)
                    # return False
            except Exception as e:  # noqa
                # print(e)
                self.emit(QtCore.SIGNAL("login_status(bool)"), False)
                pass
                # return False
