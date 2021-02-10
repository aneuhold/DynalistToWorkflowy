def parseToInt(userInput, min=None, max=None):
  """Parses the given string from the user and lets the user know if it is
  not a valid number. Returns None if the value is not parsable and the number
  if it is.

  If min is provided then it checks to make sure the value is at least that high
  or more. If max is provided then it checks to see if it is that value or 
  less"""
  parsedChoice = None
  try:
    parsedChoice = int(userInput)
  except:
    print('"' + userInput + '" is not a number.')
    return None

  if min is not None and parsedChoice < min:
    print('"' + userInput + '" needs to be more than or equal to ' + str(min))
    return None

  if max is not None and parsedChoice > max:
    print('"' + userInput + '" needs to be less than or equal to ' + str(max))
    return None

  return parsedChoice


def parseToFloat(userInput, min=None, max=None):
  """Parses the given string from the user and lets the user know if it is
  not a valid number. Returns None if the value is not parsable and the number
  if it is.

  If min is provided then it checks to make sure the value is at least that high
  or more. If max is provided then it checks to see if it is that value or 
  less"""
  parsedChoice = None
  try:
    parsedChoice = float(userInput)
  except:
    print('"' + userInput + '" is not a number.')
    return None

  if min is not None and parsedChoice < min:
    print('"' + userInput + '" needs to be more than or equal to ' + str(min))
    return None

  if max is not None and parsedChoice > max:
    print('"' + userInput + '" needs to be less than or equal to ' + str(max))
    return None

  return parsedChoice
