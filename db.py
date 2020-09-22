'''
# Table imformation 
use music_recmd;

CREATE TABLE user_info (
	ID varchar(30) NOT NULL,
	Password varchar(25) Not NULL,
	Gender enum('남자','여자'),
	Age varchar(25),
	Genre1 varchar(30),
	Genre2 varchar(12),
	Genre3 varchar(20) ,
	Favorite_playlist  json DEFAULT NULL ,
	PRIMARY KEY(ID)
) CHARSET=utf8mb4;

'''

import sys
import requests
import json
import logging
import pymysql



def connect_RDS():
    host = "database-3.clsxzczyrhnn.ap-northeast-2.rds.amazonaws.com"
    port = 3306
    username = "admin"
    database = "music_recmd"
    password = "qudwns1234"

    try :
        conn = pymysql.connect(host, user=username,passwd=password,db=database,port=port, use_unicode=True, charset='utf8')
        cursor=conn.cursor()

    except:
        logging.error("RDS에 연결되지 않았습니다.")
        sys.exit(1)


    return conn,cursor

def user_info_insert(ID,Password,Gender,Age,Genre1,Genre2,Genre3):
    # get headers
    # headers = get_headers(client_id, client_secret)
    # call RdS
    conn,cursor = connect_RDS()
    query = """ insert into `user_info` (ID, Password,Gender, Age,Genre1,Genre2,Genre3) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}' ) 
    on duplicate key update ID ='{0}', Password = '{1}', Gender='{2}', Age = '{3}', Genre1 = '{4}' ,Genre2 = '{5}' ,Genre3 = '{6}' 
    """.format(ID,Password,Gender,Age,Genre1,Genre2,Genre3)
    cursor.execute(query)
    conn.commit()

# on duplicate key update ID ='{0}'
def user_info_select(ID,Password):
    try:
        conn,cursor = connect_RDS()

        query = " select * from user_info where ID = '{0}' and Password = '{1}'   ".format(ID,Password)
        cursor.execute(query)
        result = cursor.fetchall()
        conn.commit()
        result = list(result[0])
        
        print('성별 : ', result[2])
        print('나이 : ', result[3])
        print('선호장르 1 : ', result[4])
        print('선호장르 2 : ', result[5])
        print('선호장르 3 : ', result[6])
        print('playlist : ' ,result[7])
        return result
    except:
        logging.error("비밀번호가 틀렸습니다.")
        sys.exit(1)

def create_playlist(ID,playlist):
    try:
        conn,cursor = connect_RDS()
        query="UPDATE `user_info` SET `Favorite_playlist` = JSON_ARRAY(%s) WHERE `ID` = %s"
        cursor.execute(query,(playlist[0],ID))
        for i in range(len(playlist)-1):
            query2= "UPDATE `user_info` SET `Favorite_playlist`=JSON_ARRAY_APPEND(`Favorite_playlist`,'$',%s) WHERE `ID` = %s"
            cursor.execute(query2,(playlist[i+1],ID))
            conn.commit()
    
    except:
        logging.error("ID가 잘못됐습니다.")
        sys.exit(1)

def select_playlist(ID):
    try:
        conn,cursor = connect_RDS()
        query= " SELECT `Favorite_playlist` FROM  `user_info` WHERE ID='{0}' ".format(ID)
        cursor.execute(query)
        result = cursor.fetchall()

        result= json.loads(result[0][0])
        print(type(result))
        print(ID ," 회원님의 플레이리스트 :",result)
        conn.commit()

        return result

    except:
        logging.error("ID가 잘못됐습니다.")
        sys.exit(1)


        pass

