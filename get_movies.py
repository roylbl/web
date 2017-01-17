# -*- coding:utf-8 -*-

import requests
import json
import time
import web

db = web.database(dbn='sqlite', db='MovieSite.db')

def add_movie(data):
    movie = json.loads(data)
    print movie['title']
    db.insert('movie',
        id=int(movie['id']),
        title=movie['title'],
        origin=movie['original_title'],
        url=movie['alt'],
        rating=movie['rating']['average'],
        image=movie['images']['large'],
        directors=','.join([d['name'] for d in movie['directors']]),
        casts= ','.join([c['name'] for c in movie['casts']]),
        year=movie['year'],
        genres=','.join(movie['genres']),
        countries=','.join(movie['countries']),
        summary=movie['summary'],
        )

# movie_ids = []
# for index in range(0, 250, 50):
#     response = requests.get('http://api.douban.com/v2/movie/top250?start=%d&count=50' % index)
#     data = response.text
#     # print data
#
#     data_json = json.loads(data)
#     movie250 = data_json['subjects']
#     for movie in movie250:
#         movie_ids.append(movie['id'])
#     time.sleep(3)
# print movie_ids

movie_ids = [u'2334904', u'1305164', u'1297192', u'4268598', u'1292434', u'1293318', u'1298070', u'1296339', u'1291585', u'1652587', u'1291990', u'1418834', u'1297052', u'11525673', u'6985810', u'2353023', u'1305487', u'1294371', u'3443389', u'5322596', u'1295865', u'1292274', u'1295038', u'1417598', u'1293172', u'1578507', u'1293359', u'3287562', u'1292401', u'1296909', u'4202302', u'1291870', u'3792799', u'2209573', u'1297447', u'3008247', u'1304447', u'1295399', u'1292328', u'1907966', u'1291579', u'21318488', u'21360417', u'1937946', u'1300299', u'1293964', u'1291822', u'1309163', u'1292528', u'1978709', u'1865703', u'1418200', u'1297574', u'1294240', u'1300992', u'1858711', u'1303037', u'1302827', u'1295409', u'1306861', u'5989818', u'1293460', u'1760622', u'1291578', u'2297265', u'1388216', u'2043546', u'25814705', u'1300960', u'1302425', u'2213597', u'1397546', u'3011235', u'10777687', u'1308857', u'1419936', u'1291557', u'1291879', u'1292270', u'3007773', u'5964718', u'25917973', u'1292281', u'1304102', u'1308767', u'1306249', u'1905462', u'11026735', u'2363506', u'1292728', u'10577869', u'1305690', u'1300374', u'1307793', u'3395373', u'1296753', u'3011051', u'1293181', u'1307811', u'1291853', u'2300586', u'1292659', u'4798888', u'24750126', u'1294638', u'6874403', u'1291844', u'1793929', u'1291568', u'1292217', u'1291992', u'1292233', u'6307447', u'1307315', u'1292214', u'1292329', u'1959195', u'3075287', u'25814707', u'1292062', u'1297478', u'1302467', u'1401118', u'1292287', u'1395091', u'1303394', u'1299361', u'2053515', u'3217169', u'1308575', u'1438652', u'4739952', u'25773932', u'1293908', u'1292056', u'1302476', u'1308777', u'1293764', u'3157605', u'6534248', u'1308817', u'1867345', u'1299327', u'1305725', u'2365260', u'1292218', u'1301171', u'4023638', u'1428175', u'1298653', u'1309027', u'1300117', u'3073124', u'6146955', u'1862151', u'1300741', u'5908478', u'1293929', u'1293530', u'10463953', u'1304073', u'1301617', u'1316572', u'4286017']
count = 0
for mid in movie_ids:
    print count, mid
    response = requests.get('http://api.douban.com/v2/movie/subject/%s' % mid)
    data = response.text
    add_movie(data)
    count += 1
    time.sleep(3)