import psycopg2
import json


class Test_Config:
    def setup(self):
        self.conn = psycopg2.connect(database="hlxj", user="hlxj_read_only", password="gzshili@2018",
                                host="rm-wz9823mjt2rv76g4kwo.pg.rds.aliyuncs.com", port="3432")
        print("Opened database successfully")

        self.cur = self.conn.cursor()

    def teardown(self):
        print("Operation done successfully")
        self.conn.close()

    def test_01(self):
        self.sql = "SELECT r.name, l.name, l.patrolranglayer  FROM tb_unit AS l RIGHT JOIN tb_unit AS r ON l.pid = r.id WHERE l.unittype IN ('SYSTEM') AND l.patrolranglayer !=''"
        self.cur.execute(self.sql)
        self.rows = self.cur.fetchall()
        for self.row in self.rows:
            print(self.row[0], '-', self.row[1], end=' - ')
            self.j = json.loads(self.row[2])
            try:
                assert "layers" in self.j.keys()
                print('有配layers数据：',self.j["layers"])
            except AssertionError as e:
                print('图层配置：', self.row[2])

    def test_02(self):
        self.sql = "SELECT r.name, l.name, l.xbtable  FROM tb_unit AS l RIGHT JOIN tb_unit AS r ON l.pid = r.id WHERE l.unittype IN ('SYSTEM') AND l.xbtable !=''"
        self.cur.execute(self.sql)
        self.rows = self.cur.fetchall()
        for self.row in self.rows:
            print(self.row[0], '-', self.row[1], end=' - ')

            try:
                assert self.row[2]
                print('有配考勤表名数据：', self.row[2])
            except AssertionError as e:
                print('考勤表名：', self.row[2])

    def test_03(self):
        self.sql = "SELECT r.name, l.name, l.configother  FROM tb_unit AS l RIGHT JOIN tb_unit AS r ON l.pid = r.id WHERE l.configother !=''"
        self.cur.execute(self.sql)
        self.rows = self.cur.fetchall()
        for self.row in self.rows:
            print(self.row[0], '-', self.row[1], end=' - ')
            self.j = json.loads(self.row[2])

            try:
                assert "mainPageMap" in self.j.keys()
                print('有配首页图层数据：', self.j["mainPageMap"], end=' - ')
                assert "patrolMonitor" in self.j.keys()
                print('有配左侧面板数据：', self.j["patrolMonitor"])
            except AssertionError as e :
                print("其他配置：", self.row[2])


    def test_04(self):
        self.sql = "SELECT u1.name, u.name, s.appconfigjson FROM tb_sys_svnroot AS s JOIN tb_sys_menu AS m ON s.widgetid = m.widgetid JOIN tb_unit AS u ON u.id = s.unitid join tb_unit as u1 ON u1.id = u.pid WHERE s.appconfigjson != '' AND m.name = '图层配置' AND u1.name = '将乐县' OR u.name in ('南雅镇','迪口镇','徐墩镇', '永安市', '清流县', '省保护区办', '乐昌十二度水', '儋州市', '金花茶保护区', '木论保护区')"
        self.cur.execute(self.sql)
        self.rows = self.cur.fetchall()
        for self.row in self.rows:
            print(self.row[0], '-', self.row[1], end=' - ')
            # print(type(self.row[2]))
            if self.row[2]:
                self.j = json.loads(self.row[2])
            # print(type(self.j))

            try:
                assert "appVersion" in self.j.keys()
                print('有配APP图层数据：', self.j["appVersion"], ' - ', self.j["layers"])
            except AssertionError as e :
                print("app图层配置：", self.row[2])


    def test_05(self):
        self.sql = "SELECT u1.name, u.name, webconfigjson FROM tb_sys_svnroot AS s JOIN tb_unit as u ON s.unitid = u.id join tb_unit as u1 on u1.id = u.pid WHERE widgetid = 'HistoricalRoute' AND u.name = '将乐县'"
        self.cur.execute(self.sql)
        self.rows = self.cur.fetchall()
        for self.row in self.rows:
            print(self.row[0], '-', self.row[1], end=' - ')
            if self.row[2]:
                self.j = json.loads(self.row[2])
                if self.j["length"] and self.j["subColor"] and self.j["subTime"]:
                    self.length = int(self.j["length"])
                    # print(len(self.j["subColor"]))
                    # print(len(self.j["subTime"]))

            try:
                assert self.length == len(self.j["subColor"])
                print("web历史配置正确：", self.row[2])
            except AssertionError as e:
                print('e：', e)
                print('web历史轨迹配置：', self.row[2])


    def test_06(self):
        self.sql = "SELECT u1.name, u.name, webconfigjson FROM tb_sys_svnroot AS s JOIN tb_unit as u ON s.unitid = u.id join tb_unit as u1 on u1.id = u.pid WHERE widgetid = 'widgets_UsersManagementToFour_001' AND u.name = '将乐县'"
        self.cur.execute(self.sql)
        self.rows = self.cur.fetchall()
        print(self.rows)  # 查出的结果是空！！
        for self.row in self.rows:
            print(self.row[0], '-', self.row[1], end=' - ')

            try:
                assert '{"imeiChange":true}' == self.row[2]
            except AssertionError as e:
                print('e：', e)
                print('用户管理IMEI码权限：', self.row[2])