import pymysql as mysql
def ConnectionPool():
    db=mysql.connect(host="localhost",port=3306,user="root",password="admin",db='commoditymarket')
    cmd=db.cursor(mysql.cursors.DictCursor)
    return(db,cmd)