import re

class Query:
  def __init__(self,unparsed, tokens,excludewords=[]):
    self.unparsed = unparsed
    self.tokens = tokens
    self.excludewords = excludewords

  def get_patterns(self):
    patterns = []
    for token in self.tokens:
      patterns.append(r'(?i)\b' + re.escape(token) + r'\b')
    return patterns
