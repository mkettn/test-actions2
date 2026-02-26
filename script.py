import datetime

with open("index.html", "w") as f:
    print("<h1>Hallo von Python 👋</h1>", file=f)
    print("Es ist gerade :" + str(datetime.datetime.now()), file=f)
