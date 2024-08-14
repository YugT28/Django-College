import mysql.connector as con
mycon=con.connect(user='root',password='root',database='college',host='localhost')
#
# cursor=mycon.cursor()
# query='''
# with t as (SELECT Result.Sid_id,Course.Bid_id,avg(Marks) over(partition by Sid_id) as Percentage
# FROM college.collectionapp_result Result
# INNER JOIN college.collectionapp_course Course
# ON Result.Cid_id=Course.Cid)
# select Sid_id,Bid_id,max(Percentage) from t
# group by Sid_id,Bid_id;'''
# f=cursor.execute(query)
# x=cursor.fetchall()
# y=list(filter(lambda x:True if x[1]==1 else False ,x))
# for a,b,f in y:
#     print(a,b,f)

c=mycon.cursor()
c.execute('INSERT INTO college.collectionapp_result(Cid_id,Sid_id,Marks)VALUES (1,5,234)')
# c.commit()
mycon.commit()
mycon.close()