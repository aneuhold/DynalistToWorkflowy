import re
import datetime


def convertDates(textVal):
  '''
  Converts the dates in the given text value to a format that workflowy
  accepts. It then returns the correct string.
  '''
  datePattern = r'\!\([^)]*\)'
  returnText = re.sub(datePattern, processDateMatch, textVal)
  return returnText


def processDateMatch(matchObj):
  dateText = matchObj.group(0)[2:-1]
  try:
    date = datetime.datetime.strptime(dateText, '%Y-%m-%d')
    dateString = date.strftime('%a, %b %d, %Y')
    dateString = '>' + dateString + '</time>'
    dateString = buildWorkflowyDateString(
        date.year, date.month, date.day, None, None, dateString)
    return dateString
  except:
    try:
      date = datetime.datetime.strptime(dateText, '%Y-%m-%d %H:%M')
      dateString = date.strftime('%a, %b %d, %Y at %I:%M%p')
      dateString = '>' + dateString + '</time>'
      dateString = buildWorkflowyDateString(
          date.year, date.month, date.day, date.hour, date.minute, dateString)
      return dateString
    except:
      print('ERROR' + dateText)
      return dateText


def buildWorkflowyDateString(year, month, day, hour, minute, dateString):
  returnStr = '<time startYear=";' + str(year) + '" '
  returnStr += 'startMonth=";' + str(month) + '" '
  returnStr += 'startDay="' + str(day) + '"'

  # 24 based hour
  if (hour is not None):
    returnStr += ' startHour="' + str(hour) + '"'
    returnStr += ' startMinute="' + str(minute) + '"'
  return returnStr + dateString
