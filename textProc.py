class analysedText(object):
    
    def __init__ (self, text):
        fmtText = text.lower()
        punct = ['.','!',',','?','(',')',';',"'",'"','’']
        for punc in punct:
            fmtText = fmtText.replace(punc,'')
        self.fmtText = fmtText
        self.words = self.fmtText.split()
    
    def freqAll(self):   
        key = set(self.words)
        wordDict = {}
        
        for word in key:
            count = self.words.count(word)
            wordDict[word]=count
        
        return wordDict
    
    def freqOf(self, word):
        count = self.words.count(word)
        return count