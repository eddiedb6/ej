#!/usr/bin/python

import MySQLdb
import smtplib

from email.mime.text import MIMEText
import datetime

import EJServiceConfig

def IsEventHappendToday(eventDate, eventRepeat):
    now = datetime.datetime.now()
    if eventRepeat == 0:
        return (now.year == eventDate.year) and (now.month == eventDate.month) and (now.day == eventDate.day)
    if ((now.year * 12 + now.month) - (eventDate.year * 12 + eventDate.month)) % eventRepeat == 0:
        return now.day == eventDate.day
    return False

def IsEventNeedPreNotice(eventDate, eventRepeat):
    if eventRepeat != 12:
        return False
    preRemindDays = 3
    preDelta = datetime.timedelta(days = -preRemindDays)
    return IsEventHappendToday(eventDate + preDelta, eventRepeat);

def SendMail(subject, name, date, repeat, note):
    eventDescription = "Description: " + note
    if note == "":
        eventDescription = "Description: None"
    eventDate = str(date.year) + "/" + str(date.month) + "/" + str(date.day)
    if repeat > 0:
        monthStr = " months"
        if repeat == 1:
            monthStr = " month"
        eventDate = eventDate + " and repeat every " + str(repeat) + monthStr
    eventDate = "Date: since " + eventDate
    content = "Event: " + name + "\n" + eventDate + "\n" + eventDescription
    message = MIMEText(content, "plain", "utf-8")
    message["Subject"] = subject + name
    message["To"] = EJServiceConfig.ejMailReceiver
    message["From"] = EJServiceConfig.ejMailSender
    try:
        server = smtplib.SMTP_SSL(EJServiceConfig.ejMailHost, EJServiceConfig.ejMailPort)
        server.login(EJServiceConfig.ejMailUser, EJServiceConfig.ejMailPassword)
        server.sendmail(EJServiceConfig.ejMailSender, EJServiceConfig.ejMailReceiver, message.as_string())
        server.close()
    except:
        print("Mail operation failed")

def SendEventNoticeMail(name, date, repeat, note):
    SendMail("[Reminder of Event] ", name, date, repeat, note)

def SendEventPriorNoticeMail(name, date, repeat, note):
    SendMail("[Prior Reminder of Event] ", name, date, repeat, note)

def HandleCalendarEvent(events):
    for row in events:
        name = row[0]
        date = row[1]
        repeat = row[2]
        note = row[3]
        if IsEventHappendToday(date, repeat):
            SendEventNoticeMail(name, date, repeat, note)
        elif IsEventNeedPreNotice(date, repeat):
            SendEventPriorNoticeMail(name, date, repeat, note)


try: 
    db = MySQLdb.connect(EJServiceConfig.ejDBServer, EJServiceConfig.ejDBUsername, EJServiceConfig.ejDBPassword, EJServiceConfig.ejDBDBName)

    cursor = db.cursor()
<<<<<<< HEAD
    cursor.execute("select Name, Datetime, RepeatMonth, Note from calendar where FID=1")
=======
    cursor.execute("select * from calendar")
>>>>>>> master

    events = cursor.fetchall()
    HandleCalendarEvent(events)

    db.close()
except:
    print("DB operation failed")
