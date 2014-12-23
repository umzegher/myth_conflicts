#!/usr/bin/python

# Check for recording conflicts on a mythtv-backend

from MythTV import MythBE

be = MythBE()

for program in be.getConflictedRecordings():
    title = "{} - {}".format(program['title'], program['subtitle'])
    starttime = program['starttime'].strftime('%Y-%m-%d %I:%M %p')
    print("{} at {} is in conflict and will not be recorded.\n".format(title, starttime))
