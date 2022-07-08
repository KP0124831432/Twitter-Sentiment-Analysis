resultingDataFile = open("resulting_data.csv","w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def strip_punctuation(x):
    ns = ''
    for w in x:
        if w not in punctuation_chars:
            ns += w
    return ns

# list of positive words to use
positive_words = []

with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(x):
    str_cd = strip_punctuation(x).lower()
    count = 0
    str_splited = str_cd.split()
    for w in str_splited:
        if w in positive_words:
            count += 1
    return count

def get_neg(x):
    str_cd = strip_punctuation(x).lower()
    count = 0
    str_splited = str_cd.split()
    for w in str_splited:
        if w in negative_words:
            count += 1
    return count
#tweet,retweets,replies



with open('project_twitter_data.csv', 'r') as fo :
    handle = fo.readlines()[1:]
    resultingDataFile = open("resulting_data.csv","w")
    header = 'Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n'
    resultingDataFile.write(header)
    for line in handle:
        splited = line.split(',')
        tweet = splited[0]
        retweets = splited[1]
        replies = splited[1]
        tweet_words = tweet.split()
        positive_score = get_pos(tweet)
        negative_score = get_neg(tweet)
        net_score = positive_score - negative_score
        resultingDataFile.write(f'{retweets},{replies},{positive_score},{negative_score},{net_score}\n')
resultingDataFile.close()



