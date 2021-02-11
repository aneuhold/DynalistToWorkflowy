import re


def convertLinks(textVal):
  '''
  Converts the links in the given text value to a format that workflowy
  accepts. It then returns the correct string.
  '''
  linkPattern = r'(\[[^\]]*\]\([^\)]*\))'
  returnText = re.sub(linkPattern, processLinkMatch, textVal)
  return returnText


def processLinkMatch(matchObj):
  linkRawText = matchObj.group(0)

  # Split on the center of the raw text then trim both ends
  linkParts = linkRawText.split('](')
  linkName = linkParts[0][1:]
  href = linkParts[1][:-1]
  return buildWorkflowyLinkString(linkName, href)


def buildWorkflowyLinkString(linkName, href):
  return '<a href="' + href + '">' + linkName + '</a>'
