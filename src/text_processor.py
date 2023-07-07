import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


class TextProcessor:  # Two blank lines before the class definition

    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('stopwords', quiet=True)

    @staticmethod
    def process_text_basic(text: str) -> str:
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = text.lower()
        return text

    @staticmethod
    def process_text_advanced(text: str) -> str:
        # Convert to lowercase
        text = text.lower()

        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Tokenize text
        tokens = word_tokenize(text)

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]

        # Perform lemmatization
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]

        # Join the list of tokens back into a string
        text = ' '.join(tokens)

        return text
