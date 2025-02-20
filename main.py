import re

# Updated Regex Patterns
patterns = {
    "emails": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    "urls": r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[\S]*',
    "phone_numbers": r'\+256\d{9}|\+254\d{9}|\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
    "credit_cards": r'\b(?:\d{4}[-\s]?){3}\d{4}\b',
    "time": r'\b(?:[01]?\d|2[0-3]):[0-5]\d\b',
    "html_tags": r'<[^>]+>',
    "hashtags": r'#\w+',
    "currency": r'UGX\s?\d{1,3}(?:,\d{3})*'
}

# Function to extract data
def extract_data(text, pattern):
    return re.findall(pattern, text)

# Updated Sample Text
sample_text = """
Contact Karabo at karabo@example.com or visit https://kiwumulo.dev for details.
Call Kiwumulo at +256712345678 or +254798765432.
Use credit card 1234-5678-9012-3456 for payment.
The event is at 8:53 or 20:53.
#Python #frontendisannoying
Maleng paid UGX 13,000,000.
"""

# Extract and display results
for key, pattern in patterns.items():
    print(f"Extracted {key.capitalize()}: {extract_data(sample_text, pattern)}")

# Basic test cases
def test_regex():
    assert extract_data("karabo@example.com", patterns["emails"]) == ["karabo@example.com"]
    assert extract_data("https://kiwumulo.dev", patterns["urls"]) == ["https://kiwumulo.dev"]
    assert extract_data("+256712345678", patterns["phone_numbers"]) == ["+256712345678"]
    assert extract_data("+254798765432", patterns["phone_numbers"]) == ["+254798765432"]
    assert extract_data("1234-5678-9012-3456", patterns["credit_cards"]) == ["1234-5678-9012-3456"]
    assert extract_data("8:53", patterns["time"]) == ["8:53"]
    assert extract_data("20:53", patterns["time"]) == ["20:53"]
    assert extract_data("<p>Hello</p>", patterns["html_tags"]) == ["<p>", "</p>"]
    assert extract_data("#Python", patterns["hashtags"]) == ["#Python"]
    assert extract_data("#frontendisannoying", patterns["hashtags"]) == ["#frontendisannoying"]
    assert extract_data("UGX 13,000,000", patterns["currency"]) == ["UGX 13,000,000"]
    print("All tests passed!")

if __name__ == "__main__":
    test_regex()

