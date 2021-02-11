import re
import datetime


def convertDates(textVal):
  '''
  Converts the dates in the given text value to a format that workflowy
  accepts. It then returns the correct string.
  '''
  splitText = re.split(r'\!\(|\)', textVal)
  for index, str in enumerate(splitText):
    if (index % 2 == 1):
      date = datetime.datetime.strptime(str, '%Y-%m-%d')
      splitText[index] = date.strftime('%a, %b %')
  print(splitText)
