import csv

def createQuery(dataBaseName, tableName):
    # file = open('RedditNews.csv', 'r')
    # x = file.read()
    # print(x)
    file_reader = open('RedditNews.csv', 'r')
    read = csv.reader(file_reader)
    category = "News"
    f = open("redditSQL.sql", "a+")
    j = 0
    #f.write("Use " + dataBaseName)
    for i in read:
        query = "INSERT INTO "+tableName +" VALUES ('','"+ category +"','" +i[0].replace("'", "\\'")+ "');"
        f.write(query)
        print(j)
        j += 1


createQuery("Humor_Detection", "humordataset")

