class ChaiUtilis:
    
    @staticmethod
    def cleanIngridients(text):
        return [word.strip() for word in text.split(",") ]
    

raw = "masala  , ginger , cardomom  , sugar , milk   "

print(ChaiUtilis.cleanIngridients(raw))