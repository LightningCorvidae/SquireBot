#Queue section of the squire bot.

#Variables

teamSize = 3
numberOfTeams = 3

def showQueue():
    when chat !list
    for number of teams
        team x : usernames

def joinQueue():
    when chat !join
    get username that put !join
    add to team

def leaveQueue():
    when chat !leave
    get username that put !leave
    remove from queue

def addToTeam():
    if team is not full
    add username to team
    else
    check next team number
