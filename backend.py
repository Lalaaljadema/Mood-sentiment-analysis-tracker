from nltk.sentiment import SentimentIntensityAnalyzer

def mood_analyzer(diaries):
    analyzer = SentimentIntensityAnalyzer()
    positive = {}
    negative = {}
    for nr, diary in enumerate(diaries, 1):
        if diary:
            score = analyzer.polarity_scores(diary)
            positive[f"day{nr}"] = score["pos"]
            negative[f"day{nr}"] = score["neg"]
    return positive, negative

