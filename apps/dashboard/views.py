from array import *
import random
from flask import Blueprint, render_template, request
from github import Github
import datetime as DT
from datetime import timedelta as TD

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

todayDate = DT.date.today()
todayDT = DT.datetime.now()


def last_seven_days_pos(x):
    diff = (todayDate - x).days

    return (6-diff)
        
##### Method end

commitsDay0 = 0
day0 = (todayDT - TD(days=6)).strftime("%d-%m-%Y")
commitsDay1 = 0
day1 = (todayDT - TD(days=5)).strftime("%d-%m-%Y")
commitsDay2 = 0
day2 = (todayDT - TD(days=4)).strftime("%d-%m-%Y")
commitsDay3 = 0
day3 = (todayDT - TD(days=3)).strftime("%d-%m-%Y")
commitsDay4 = 0
day4 = (todayDT - TD(days=2)).strftime("%d-%m-%Y")
commitsDay5 = 0
day5 = (todayDT - TD(days=1)).strftime("%d-%m-%Y")
commitsDay6 = 0
day6 = todayDT.strftime("%d-%m-%Y")

def formatArrayForReturn(x0, x1, x2, x3, x4, x5, x6):
    tuple0 = (day0, x0)
    tuple1 = (day1, x1)
    tuple2 = (day2, x2)
    tuple3 = (day3, x3)
    tuple4 = (day4, x4)
    tuple5 = (day5, x5)
    tuple6 = (day6, x6)
    formattedTupleArray = [tuple0, tuple1, tuple2, tuple3, tuple4, tuple5, tuple6]

    return formattedTupleArray





def getRepoLanguages(repoName,username):
    g = Github('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')
    user = g.get_user(username)
    user.login
    
    try:
        repo = user.get_repo(repoName)
    except:
        print("Error: Repo not found")
        return
    line_count = ([], [])
    langsDict = repo.get_languages()
    for language in langsDict.keys():
        line_count[0].append(language)
        line_count[1].append(langsDict[language])
    return line_count
#### Method end

@dashboard_bp.route("/")
def graph():
    nameWithRepo = request.args.get("value")
    spaceIndex = nameWithRepo.find(" ")
    
    username = nameWithRepo[0:spaceIndex]
    repoName = nameWithRepo[spaceIndex+1:]
    
    
    # data1 = getCommitsFromLast7Days(username, repoName)

    # labels1 = [row[0] for row in data1]
    # values1 = [row[1] for row in data1]
 

    # DOESNT WORK 
    labels2,values2 = getRepoLanguages(repoName,username)
    
    colorPalette = []
    
    for _ in range(len(labels2)):
        rgb = 'rgb(' + str(round(random.random() *255)) + ',' + str(round(random.random() *255)) + ',' + str(round(random.random() *255)) + ')'
        colorPalette.append(rgb)
    
    
    return render_template("dashboard/graph.html", labels2 = labels2, values2 = values2, username = username, repoName = repoName, colorList = colorPalette)
