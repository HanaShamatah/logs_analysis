''' Logs Analysis Project_3rd'''
# !/usr/bin/env python3

import psycopg2
DBNAME = "news"


def popular_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create or replace view article_view as select substring(path,10) as article_title, count(*) as V from log group by path order by V desc;")
    c.execute("select * from article_view offset 1 limit 3;")
    articles = c.fetchall()
    db.close()
    print "The Most Popular Articles: "
    for result in articles:
        print str(result[0]) + " -- " + str(result[1]) + " view"
    return articles
X = popular_articles()

output = open("results.txt", "a")
output.write("The Most Popular Articles: \r\n")
for result in X:
    output.write("   " + str(result[0]) + " -- " + str(result[1]) + " views \r\n")
output.close()


def popular_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create or replace view article_view as select substring(path,10) as article_title, count(*) as V from log group by path order by V desc;")
    c.execute("select name, sum(V) as views from authors, articles, article_view where article_title = slug and author = authors.id group by name order by views desc;")
    authors = c.fetchall()
    db.close()
    print "\r\nThe Authors Views: "
    for result in authors:
        print str(result[0]) + " -- " + str(result[1]) + " view"
    return authors
Y = popular_authors()

output = open("results.txt", "a")
output.write("\r\nThe Authors Views: \r\n")
for result in Y:
    output.write("   " + str(result[0]) + " -- " + str(result[1]) + " views \r\n")
output.close()


def requsts_error():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create or replace view error_req as select date(time)as date, count(*) as num from log where status = '404 NOT FOUND' group by date order by date;")
    c.execute("create or replace view total_req as select date(time)as date, count(*) as num from log group by date order by date;")
    c.execute("select to_char(error_req.date, 'Mon DD, YYYY') as date, cast(100*error_req.num/cast(total_req.num as decimal(10,1)) as decimal(3,2)) as error from error_req, total_req where error_req.date = total_req.date and (100*error_req.num) > total_req.num;")
    error = c.fetchall()
    db.close()
    print "\r\nDays with more than 1% requests error: "
    for result in error:
        print str(result[0]) + " -- " + str(result[1]) + "% errors"
    return error
Z = requsts_error()

output = open("results.txt", "a")
output.write("\r\nDays with more than 1% requests error: \r\n")
for result in Z:
    output.write("   " + str(result[0]) + " -- " + str(result[1]) + " %error \r\n")
output.close()
