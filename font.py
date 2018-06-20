# coding: utf-8

from fontTools.ttLib import TTFont
from mysql import Mysql
from config import db_conf

def reset_dict(decrypr_type):
    fonts = TTFont('tyc-num.woff')

    temp = [i for i in range(0, 10)]
    dict = [['de_code', 'co_code'], [decrypr_type, 'type']]

    for glyph_id in range(2, 11):
    	glyph_name = fonts.getGlyphName(glyph_id)
    	dict.append([glyph_id-2, int(glyph_name)])
    	temp.remove(int(glyph_name))

    x = temp[0]

    for i in range(2, len(dict)):
        if dict[i][0] >= x:
            dict[i][0] += 1

    dict.append([x, x])

    db = Mysql(**db_conf)
    db.update('TRUNCATE TABLE dict;')
    db.insert('dict', dict)



def load_dict():
    db = Mysql(**db_conf)
    dict = {}

    decrypr_type = db.select("SELECT de_code FROM dict WHERE co_code='type';")
    data = db.select("SELECT co_code,de_code FROM dict WHERE co_code<>'type';")
    
    for i in range(1, len(data)):
        dict[data[i][0]] = data[i][1]

    print(dict)



reset_dict('font-e10ee038')
load_dict()