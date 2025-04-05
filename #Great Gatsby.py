#Great Gatsby 
import urllib.request
import unicodedata
import string

def download_book(url):
    """Allows python access to the book data"""
    try:
        with urllib.request.urlopen(url) as f:
            return f.read().decode('utf-8')
    except Exception as e:
        print("Error downloading the book:", e)
        return None

def normalize_text(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()

def save_to_file(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def preprocess_text(text):
    """tokenize the text for easier processing"""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()

def get_stop_words():
    """Chatgpt gave me this list of stopwords"""
    return set([
        "the", "and", "a", "an", "to", "in", "of", "for", "on", "with", "at", "by",
        "from", "up", "about", "into", "over", "after", "below", "under", "again",
        "further", "then", "once", "here", "there", "all", "any", "both", "each",
        "few", "more", "some", "such", "no", "nor", "not", "only", "own", "same",
        "so", "than", "too", "very", "can", "will", "just", "dont", "should", "now",
        "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
        "do", "does", "did", "but", "if", "or", "because", "as", "until", "while",
        "he", "she", "it", "they", "them", "we", "you", "i", "me", "my", "our", "your",
        "him", "her", "their", "what", "which", "who", "whom", "this", "that", "these", "those"
    ])

def filter_stop_words(words, stop_words):
    return [word for word in words if word not in stop_words]


def main(url, save_path):
    """Run all the tokenazation and processing for clean text and save the final file"""
    raw_text = download_book(url)
    
    if raw_text:
        # Normalize and preprocess the text
        normalized_text = normalize_text(raw_text)
        words = preprocess_text(normalized_text)
        
        # Get stop words
        stop_words = get_stop_words()
        
        # Filter out stop words
        filtered_words = filter_stop_words(words, stop_words)
        
        # Join the filtered words back into a string
        cleaned_text = ' '.join(filtered_words)
        
        # Save the cleaned text to a new file
        save_to_file(save_path, cleaned_text)
        print(f"Cleaned text saved to {save_path}")
    else:
        print("Failed to download the book.")


url_gatsby = "http://www.gutenberg.org/files/64317/64317-0.txt"  
save_path_gatsby = "cleaned_gatsby.txt"  
main(url_gatsby, save_path_gatsby)
