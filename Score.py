import SpellCorrection


def marker_values(values):
  return lambda text: 1 if any(map(lambda t: t.lower() in values, text.split())) else 0

depressed_mood = marker_values(['tears','cry','pain'])
loneliness = marker_values(['miss','much', 'baby'])
hostility = marker_values(['hate','ugh','fucking'])
negative_emotions = marker_values(['smh','fuck', 'hate'])
sadness = marker_values(['miss','lost', 'alone'])
singular = marker_values(['i','my', 'me'])
rumination = marker_values(['mind','alot', 'lot'])
anxiety = marker_values(['scared','upset', 'worry'])
complaint = marker_values(['hurt','head', 'bad'])
health = marker_values(['life','tired', 'sick'])
medical = marker_values(['hospital','pain', 'surgery'])

def calculate_score(text):
  text = SpellCorrection.correct_spellings(text)
  score = 0.15 * depressed_mood(text) + \
        0.14 * loneliness(text) + \
        0.12 * hostility(text) + \
        0.14 * negative_emotions(text) + \
        0.17 * sadness(text) + \
        0.19 * singular(text) + \
        0.11 * rumination(text) + \
        0.08 * anxiety(text) + \
        0.15 * complaint(text) + \
        0.11 * health(text) + \
        0.20 * medical(text)
  return min(1,score)
