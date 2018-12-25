import psycopg2
import json
import xlwt

#创建工作博
wb  =xlwt.Workbook(encoding='utf-8')
#括号内参数为表名
ws1 = wb.add_sheet('图层配置', cell_overwrite_ok=True)
ws2 = wb.add_sheet('考勤表名', cell_overwrite_ok=True)
ws3 = wb.add_sheet('其他配置', cell_overwrite_ok=True)
ws4 = wb.add_sheet('APP图层配置', cell_overwrite_ok=True)
ws5 = wb.add_sheet('WEB历史轨迹', cell_overwrite_ok=True)
ws6 = wb.add_sheet('用户管理IMEI码修改权限', cell_overwrite_ok=True)
ws7 = wb.add_sheet('用户详情一图一册', cell_overwrite_ok=True)
ws8 = wb.add_sheet('地图打印', cell_overwrite_ok=True)

class Test_Config:
    def setup(self):
        self.conn = psycopg2.connect(database="znxh", user="hlxj_read_only", password="gzshili@2018",
                                host="rm-wz9823mjt2rv76g4kwo.pg.rds.aliyuncs.com", port="3432")
        print("Opened database successfully")

        self.cur = self.conn.cursor()

    def teardown(self):
        wb.save('站点微件配置检测.xls')
        print("Operation done successfully")
        self.conn.close()


    # 每个子系统的图层配置
    def test_01(self):
        self.sql = "SELECT r.name, l.name, l.patrolranglayer  FROM tb_unit AS l RIGHT JOIN tb_unit AS r ON l.pid = r.id WHERE l.unittype IN ('SYSTEM') AND l.patrolranglayer !=''"
        self.cur.execute(self.sql)
        self.rows = self.cur.fetchall()

        ws1.write(0, 0, label='所在市')
        ws1.write(0, 1, label='站点')
        ws1.write(0, 2, label='layers值')
        x = 1

        for self.row in self.rows:
            print(self.row[0], '-', self.row[1], end=' - ')
            ws1.write(x, 0, self.row[0])
            ws1.write(x, 1, self.row[1])
            self.j = json.loads(self.row[2])
            try:
                assert "layers" in self.j.keys()
                print('有配layers数据：',self.j["layers"])
                ws1.write(x, 2, '有配layers数据：% s' % self.j["layers"])
            except AssertionError as e:
                print('图层配置：', self.row[2])
                ws1.write(x, 2, self.row[2])
            x += 1

    # 每个子系统的考勤表名
    def test_02(self):
        self.sql = "SELECT r.name, l.name, l.xbtable  FROM tb_unit AS l RIGHT JOIN tb_unit AS r ON l.pid = r.id WHERE l.unittype IN ('SYSTEM') AND l.xbtable !=''"
        self.cur.execute(self.sql)
        self.rows = self.cur.fetchall()

        ws2.write(0, 0, label='所在市')
        ws2.write(0, 1, label='站点')
        ws2.write(0, 2, label='考勤表名')
        x = 1

        for self.row in self.rows:
            print(self.row[0], '-', self.row[1], end=' - ')
            ws2.write(x, 0, self.row[0])
            ws2.write(x, 1, self.row[1])

            try:
                assert self.row[2]
                print('有配考勤表名数据：', self.row[2])
                ws2.write(x, 2, '有配考勤表名数据：% s' % self.row[2])
            except AssertionError as e:
                print('考勤表名：', self.row[2])
                ws2.write(x, 2, '考勤表名：% s' % self.row[2])
            x += 1

    # 其他配置
    def test_03(self):
        self.sql = "SELECT r.name, l.name, l.configother  FROM tb_unit AS l RIGHT JOIN tb_unit AS r ON l.pid = r.id WHERE l.configother !=''"
        self.cur.execute(self.sql)
        self.rows = self.cur.fetchall()

        ws3.write(0, 0, label='所在市')
        ws3.write(0, 1, label='站点')
        ws3.write(0, 2, label='首页图层')
        ws3.write(0, 3, label='左侧面板')
        x = 1

        for self.row in self.rows:
            print(self.row[0], '-', self.row[1], end=' - ')
            self.j = json.loads(self.row[2])
            ws3.write(x, 0, self.row[0])
            ws3.write(x, 1, self.row[1])
            try:
                assert "mainPageMap" in self.j.keys()
                print('有配首页图层数据：', self.j["mainPageMap"], end=' - ')
                ws3.write(x, 2, '有配首页图层数据：% s' % self.j["mainPageMap"])
                assert "patrolMonitor" in self.j.keys()
                print('有配左侧面板数据：', str(self.j["patrolMonitor"]))
                ws3.write(x, 3, '有配左侧面板数据：% s' % self.j["patrolMonitor"])
            except AssertionError as e :
                print("其他配置：", self.row[2])
                ws3.write(x, 2, '其他配置：% s' % self.row[2])
            x += 1


    # 微件配置（APP图层配置）
    def test_04(self):
        self.sql = "SELECT u1.name, u.name, s.appconfigjson FROM tb_sys_svnroot AS s JOIN tb_sys_menu AS m ON s.widgetid = m.widgetid JOIN tb_unit AS u ON u.id = s.unitid join tb_unit as u1 ON u1.id = u.pid WHERE s.appconfigjson != '' AND m.name = '图层配置' AND u1.name = '将乐县' OR u.name in ('南雅镇','迪口镇','徐墩镇', '永安市', '清流县', '省保护区办', '乐昌十二度水', '儋州市', '金花茶保护区', '木论保护区')"
        self.cur.execute(self.sql)
        self.rows = self.cur.fetchall()

        ws4.write(0, 0, label='所在市')
        ws4.write(0, 1, label='站点')
        ws4.write(0, 2, label='APP图层配置')
        x = 1

        for self.row in self.rows:
            print(self.row[0], '-', self.row[1], end=' - ')
            # print(type(self.row[2]))
            if self.row[2]:
                self.j = json.loads(self.row[2])
            # print(type(self.j))
            ws4.write(x, 0, self.row[0])
            ws4.write(x, 1, self.row[1])
            try:
                assert "appVersion" and "layers" in self.j.keys()
                print('有配APP图层数据：', self.j["appVersion"], ' - ', self.j["layers"])
                # ws4.write(x, 2, '有配APP图层数据：{0}{1}{2}'.format (self.j["appVersion"], ' - ', self.j["layers"]))
                ws4.write(x, 2, '有配APP图层数据：%s %s %s' % (self.j["appVersion"], ' - ', self.j["layers"]))
            except AssertionError as e :
                print("app图层配置：", self.row[2])
                ws4.write(x, 2, self.row[2])
            x += 1

    # 将乐县（金森）微件配置（WEB历史轨迹）
    def test_05(self):
        self.sql = "SELECT u1.name, u.name, webconfigjson FROM tb_sys_svnroot AS s JOIN tb_unit as u ON s.unitid = u.id join tb_unit as u1 on u1.id = u.pid WHERE widgetid = 'HistoricalRoute' AND u.name = '将乐县'"
        self.cur.execute(self.sql)
        self.rows = self.cur.fetchall()

        ws5.write(0, 0, label='所在市')
        ws5.write(0, 1, label='站点')
        ws5.write(0, 2, label='WEB历史轨迹')
        x = 1

        for self.row in self.rows:
            print(self.row[0], '-', self.row[1], end=' - ')
            if self.row[2]:
                self.j = json.loads(self.row[2])
                if self.j["length"] and self.j["subColor"] and self.j["subTime"]:
                    self.length = int(self.j["length"])
                    # print(len(self.j["subColor"]))
                    # print(len(self.j["subTime"]))
            ws5.write(x, 0, self.row[0])
            ws5.write(x, 1, self.row[1])
            try:
                assert self.length == len(self.j["subColor"])
                print("web历史配置正确：", self.row[2])
                ws5.write(x, 2, "web历史配置正确：%s" % self.row[2])
            except AssertionError as e:
                print('e：', e)
                print('web历史轨迹配置：', self.row[2])
                ws5.write(x, 2, "检查：%s" % self.row[2])
            x += 1

    # 将乐县（金森）微件配置（用户管理IMEI码修改权限）
    def test_06(self):
        self.sql = "SELECT u1.name, u.name, webconfigjson FROM tb_sys_svnroot AS s JOIN tb_unit as u ON s.unitid = u.id join tb_unit as u1 on u1.id = u.pid WHERE widgetid = 'widgets_UsersManagementToFour_001' AND u.name = '将乐县'"
        self.cur.execute(self.sql)
        self.rows = self.cur.fetchall()
        # print(self.rows)

        ws6.write(0, 0, label='所在市')
        ws6.write(0, 1, label='站点')
        ws6.write(0, 2, label='用户管理IMEI码修改权限')
        x = 1

        for self.row in self.rows:
            print(self.row[0], '-', self.row[1], end=' - ')

            ws6.write(x, 0, self.row[0])
            ws6.write(x, 1, self.row[1])

            try:
                assert '{"imeiChange":true}' == self.row[2]
                print('用户管理IMEI码权限配置正确')
                ws6.write(x, 2, '用户管理IMEI码权限配置正确')
            except AssertionError as e:
                print('e：', e)
                print('用户管理IMEI码权限：', self.row[2])
                ws6.write(x, 2, "检查：%s" % self.row[2])
            x += 1

    # 永安市（金盾）用户详情一图一册
    def test_07(self):
        self.sql = "SELECT u1.name, u.name, webconfigjson FROM tb_sys_svnroot AS s JOIN tb_unit as u ON s.unitid = u.id join tb_unit as u1 on u1.id = u.pid WHERE widgetid = 'UserDetails_Config' AND u.name = '永安市'"
        self.cur.execute(self.sql)
        self.rows = self.cur.fetchall()

        ws7.write(0, 0, label='所在市')
        ws7.write(0, 1, label='站点')
        ws7.write(0, 2, label='用户详情一图一册')
        x = 1

        for self.row in self.rows:
            print(self.row[0], '-', self.row[1], end=' - ')
            ws7.write(x, 0, self.row[0])
            ws7.write(x, 1, self.row[1])
            try:
                assert '{"showPDF":true}' == self.row[2]
                print('用户详情一图一册配置正确')
                ws7.write(x, 2, '用户详情一图一册配置正确')
            except AssertionError as e:
                print('e：', e)
                print('用户详情一图一册：', self.row[2])
                ws7.write(x, 2, "检查：%s" % self.row[2])
            x += 1

    # 微件配置（地图打印）
    def test_08(self):
        self.sql = "SELECT u1.name, u.name, s.webconfigjson FROM tb_sys_svnroot AS s JOIN tb_unit AS u ON u.id = s.unitid join tb_unit as u1 ON u1.id = u.pid WHERE s.widgetid = 'PrintMap' AND (u1.name = '南岭' OR u.name = '木论保护区')"
        self.cur.execute(self.sql)
        self.rows = self.cur.fetchall()

        ws8.write(0, 0, label='所在市')
        ws8.write(0, 1, label='站点')
        ws8.write(0, 2, label='用户详情一图一册')
        x = 1

        for self.row in self.rows:
            print(self.row[0], '-', self.row[1], end=' - ')
            ws8.write(x, 0, self.row[0])
            ws8.write(x, 1, self.row[1])
            try:
                assert '{"maxNumber":5000,"visible":true}' == self.row[2]
                print('地图打印配置正确')
                ws8.write(x, 2, '地图打印配置正确')
            except AssertionError as e:
                print('e：', e)
                print('地图打印：', self.row[2])
                ws8.write(x, 2, "检查：%s" % self.row[2])
            x += 1