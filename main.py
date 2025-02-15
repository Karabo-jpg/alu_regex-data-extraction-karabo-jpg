import re

# Regex Patterns
patterns = {
    "emails": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    "urls": r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[\S]*',
    "phone_numbers": r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
    "credit_cards": r'\b(?:\d{4}[-\s]?){3}\d{4}\b',
    "time": r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b',
    "html_tags": r'<[^>]+>',
    "hashtags": r'#\w+',
    "currency": r'[$€£]\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
}

# Function to extract data
def extract_data(text, pattern):
    return re.findall(pattern, text)

# Sample text
sample_text = """
Contact Karabo at karabo@example.com or visit https://kiwumulo.dev for details.
Call Kiwumulo at (123) 456-7890 or 123-456-7890.
Use credit card 1234-5678-9012-3456 for payment.
The event is at 14:30 or 2:30 PM.
#Python #CodingIsFun
Maleng paid $1,234.56.
"""

# Extract and display results
for key, pattern in patterns.items():
    print(f"Extracted {key.capitalize()}: {extract_data(sample_text, pattern)}")

# Basic test cases
def test_regex():
    assert extract_data("karabo@example.com", patterns["emails"]) == ["karabo@example.com"]
    assert extract_data("https://kiwumulo.dev", patterns["urls"]) == ["https://kiwumulo.dev"]
    assert extract_data("(123) 456-7890", patterns["phone_numbers"]) == ["(123) 456-7890"]
    assert extract_data("1234-5678-9012-3456", patterns["credit_cards"]) == ["1234-5678-9012-3456"]
    assert extract_data("14:30 PM", patterns["time"]) == ["14:30 PM"]
    assert extract_data("<p>Hello</p>", patterns["html_tags"]) == ["<p>", "</p>"]
    assert extract_data("#Python", patterns["hashtags"]) == ["#Python"]
    assert extract_data("$1,234.56", patterns["currency"]) == ["$1,234.56"]
    print("All tests passed!")

if __name__ == "__main__":
    test_regex()
