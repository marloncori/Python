import langdetect

def detect_language(text):
    try:
        # Use the langdetect library to detect the language of the text
        language = langdetect.detect(text)
        return language
    except langdetect.lang_detect_exception.LangDetectException:
        # If the language could not be detected, return "unknown"
        return "unknown"

# Example usage
input_data = {
    "name": "Mary",
    "age": "30",
    "gender": "female",
    "marital_status": "single",
    "has_children": "no",
    "profession": "engineer",
    "area_of_interest": "technology"
}

language = detect_language(input_data["gender"])
print(language) # Output: "en"
