
# coding: utf-8

# In[ ]:


import sys
import mysql.connector

a=sys.argv[1]
cnx = mysql.connector.connect(user='inf551', password='inf551', host='127.0.0.1', database='inf551')
cursor = cnx.cursor()
query = "select headofstate from country where name=\""+a+"\"" 
cursor.execute(query)
for name in cursor:
    print name
cursor.close()
cnx.close()

