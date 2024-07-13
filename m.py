import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def extract_ingredients(text):
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens)
    
    # Filter tokens tagged as nouns or adjectives (which might describe ingredients)
    ingredients = [word for word, tag in tagged_tokens if tag.startswith('NN') or tag.startswith('JJ')]
    
    return ingredients

# Example usage
food_description = "This is a delicious spaghetti carbonara with bacon, eggs, and Parmesan cheese."
ingredients = extract_ingredients(food_description)
print("Ingredients:")
for ingredient in ingredients:
    print("-", ingredient)
