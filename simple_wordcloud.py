import json
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords", quiet=True)

# fmt: off
# Amharic stop words
amharic_stop_words = set([
    "ነው", "ናት", "የ", "ለ", "በ", "እና", "ከ", "ወደ", "ላይ", "ግን", "እንደ", "አለ",
    "ይህ", "እሱ", "እሷ", "እነሱ", "እኔ", "አንተ", "አንቺ", "እናንተ", "ምን", "ማን",
    "የት", "መቼ", "እንዴት", "ለምን", "አዎ", "አይ", "ወይም", "ስለ", "ምክንያቱም", "እንጂ", "እንጅ",
    "እስከ", "ጋር", "ደግሞ", "ሆነ", "ውስጥ", "ዛሬ", "ነገር", "አሁን", "ብቻ", "ሁሉ","ሁሉም",
    "ሌላ", "እዚህ", "እዚያ", "ብዙ", "ጥቂት", "ያለ", "መሆን", "አድርግ", "ሄደ", "መጣ",
    "ቀን", "ጊዜ", "አገር", "ሰው", "ሰዎች", "ነገሮች", "ዓመት", "ወር", "ሳምንት", "እንኳን"
]) 
# fmt: on

# Extended English stop words
english_stop_words = set(stopwords.words("english"))
# fmt: off
add_stopwords = [
    "rt", "via", "new", "time", "today", "day", "week", "year", "also", "would",
     "could", "should", "may", "one", "two", "many", "much", "well",
     "great", "within", "like"
]
# fmt: on
english_stop_words.update(add_stopwords)

# Combine stop words
stop_words = amharic_stop_words.union(english_stop_words)


def clean_text(text):
    # Remove HTML entity
    text = re.sub(r"&amp;?", "", text)
    # Remove URLs
    text = re.sub(r"http\S+", "", text)
    # Remove mentions
    text = re.sub(r"@\w+", "", text)
    # Remove hashtags
    text = re.sub(r"#\w+", "", text)
    # Remove numbers
    text = re.sub(r"\d+", "", text)
    # Remove punctuation and convert to lowercase
    text = re.sub(r"[^\w\s]", "", text.lower())
    return text


# https://github.com/amueller/word_cloud/tree/main
def create_word_cloud(tweets, file_path: str = None):
    # Combine all tweet texts
    all_words = " ".join([clean_text(tweet["text"]) for tweet in tweets])

    # Create and generate a word cloud image
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white",
        stopwords=stop_words,
        min_font_size=10,
        font_path="~/Library/Fonts/AbyssinicaSIL-Regular.ttf",
    ).generate(all_words)

    # Save the image
    if file_path:
        wordcloud.to_file(file_path)

    # Display the generated image
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()
