# Text Comparison 
import string
from textblob import TextBlob
import nltk
nltk.download('punkt')      
nltk.download('punkt_tab')  



# Define stop words as given by chatgpt 
stop_words = set([
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

def preprocess_text(filename):
    """Preprocess the text by converting to lowercase, removing punctuation, and filtering out stop words."""
    
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split into words
    words = text.split()

    # Remove stop words
    filtered_words = [word for word in words if word not in stop_words]

    return text, filtered_words

def count_word_frequencies(words):
    """Count word frequencies from the given list of words."""
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def get_top_n_words(word_counts, n=10):
    """Return the top n most frequent words from the word counts."""
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]

def get_character_interactions(text, characters):
    """
    Calculate the most frequent interactions between characters in the given text
    based on the occurrence of their names across paragraphs.
    """
    interactions = {}

    
    paragraphs = text.split('\n\n')

    for paragraph in paragraphs:
        
        words = paragraph.split()

        
        present_characters = [character for character in characters if character in words]

        
        for i in range(len(present_characters)):
            for j in range(i + 1, len(present_characters)):
                char_pair = tuple(sorted([present_characters[i], present_characters[j]]))
                interactions[char_pair] = interactions.get(char_pair, 0) + 1

    return interactions

def main(gatsby_file, pride_file, gatsby_characters, pride_characters):
    """
    Main function to process both books and calculate the top interactions between characters, and compare word analysis.
    """
    
    # Preprocess the texts and filter out stop words
    gatsby_text, gatsby_filtered_words = preprocess_text(gatsby_file)
    pride_text, pride_filtered_words = preprocess_text(pride_file)

    # Get character interactions
    gatsby_interactions = get_character_interactions(gatsby_text, gatsby_characters)
    pride_interactions = get_character_interactions(pride_text, pride_characters)

    # Sort the interactions to find the top ones
    gatsby_top_interactions = sorted(gatsby_interactions.items(), key=lambda x: x[1], reverse=True)[:10]
    pride_top_interactions = sorted(pride_interactions.items(), key=lambda x: x[1], reverse=True)[:10]

    # Output the results for interactions
    print("Top Character Interactions in The Great Gatsby:")
    for pair, count in gatsby_top_interactions:
        print(f"{pair[0]} and {pair[1]}: {count} interactions")

    print("\nTop Character Interactions in Pride & Prejudice:")
    for pair, count in pride_top_interactions:
        print(f"{pair[0]} and {pair[1]}: {count} interactions")

    # Calculate word frequencies and comparison metrics for both texts
    gatsby_word_counts = count_word_frequencies(gatsby_filtered_words)
    pride_word_counts = count_word_frequencies(pride_filtered_words)

    # Top 10 words for both books
    gatsby_top_words = get_top_n_words(gatsby_word_counts)
    pride_top_words = get_top_n_words(pride_word_counts)

    # Total word count
    gatsby_total_words = len(gatsby_filtered_words)
    pride_total_words = len(pride_filtered_words)

    # Unique word count
    gatsby_unique_words = len(set(gatsby_filtered_words))
    pride_unique_words = len(set(pride_filtered_words))

    # Comparison Output
    print("\nText Comparison Between Gatsby and Pride & Prejudice")

    print("\nTop 10 Most Frequent Words in Gatsby:")
    for word, count in gatsby_top_words:
        print(f"{word}: {count}")

    print("\nTop 10 Most Frequent Words in Pride & Prejudice:")
    for word, count in pride_top_words:
        print(f"{word}: {count}")

    print("\nTotal Word Count:")
    print(f"Gatsby: {gatsby_total_words}")
    print(f"Pride & Prejudice: {pride_total_words}")

    print("\nUnique Word Count:")
    print(f"Gatsby: {gatsby_unique_words}")
    print(f"Pride & Prejudice: {pride_unique_words}")


# Example character lists for the texts
gatsby_characters = ["nick", "gatsby", "daisy", "tom", "jordan", "myrtle"]
pride_characters = ["elizabeth", "darcy", "bingley", "jane", "lydia", "collins"]

# Run the analysis
main("cleaned_gatsby.txt", "cleaned_pride_prejudice.txt", gatsby_characters, pride_characters)

