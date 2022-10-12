import yake


full_text = "Shock and horror as playgrounds and bridges hit"


print("Preparing Prompts...")
kw_extractor = yake.KeywordExtractor(top=3, stopwords=None)
keywords = kw_extractor.extract_keywords(full_text)

for kw, v in keywords:
  print("Keyphrase: ",kw, ": score", v)


bannedWords = ["porn"]  