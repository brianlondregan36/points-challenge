import urllib2
from bs4 import BeautifulSoup



bTeams = ["New Orleans", "Atlanta", "Pittsburgh", "New England", "Dallas", "Oakland", "Tennessee", "Kansas City", "Tampa Bay", "LA Chargers", "LA Rams", "Philadelphia", "Jacksonville", "Cleveland", "Minnesota", "Buffalo"]
sTeams = ["Carolina", "Arizona", "Seattle", "NY Giants", "Denver", "Chicago", "Green Bay", "San Francisco", "Cincinnati", "Washington", "Indianapolis", "Baltimore", "Miami", "Houston", "Detroit", "NY Jets"]

url = "http://www.espn.com/nfl/statistics/team/_/stat/total/year/2017"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())



topContainer = soup.find(id='my-teams-table')

tables = topContainer.find_all("table", class_="tablehead")
if len(tables) == 1:
    table = tables[0]
else: 
    print "[could not locate main table]"
rows = table.find_all("tr")

for thisRow in rows:

    headerCheck = thisRow.attrs['class']
    if headerCheck[0] == "colhead":
        continue

    cells = thisRow.find_all("td")

    thisTeamName = cells[1].find_all("a")[0].string
    thisTeamPoints = int(cells[8].string)

    for x in bTeams: 
        if x == thisTeamName: 
            bTeams.remove(x)
            bTeams.append(thisTeamPoints)
            break
    for y in sTeams: 
        if y == thisTeamName:
            sTeams.remove(y)
            sTeams.append(thisTeamPoints)
            break

'''remove this after week 2'''        
bTeams.remove(bTeams[0])
sTeams.remove(sTeams[0])
'''remove this after week 2'''

b = sum(bTeams)
s = sum(sTeams)
