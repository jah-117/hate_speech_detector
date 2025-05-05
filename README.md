# Hate Speech Detector

A lightweight Python package to detect hate speech in text using a machine learning model.

This project was developed by [Jahfar Muhammed]as part of my **major project in college** to explore ethical AI applications and contribute to safer digital communication. It uses traditional NLP preprocessing and a trained machine learning model to classify whether input text contains hate speech.

## Features

- Simple API with a single function call
- Returns human-readable and structured results
- Trained on real-world datasets
- Easily integrable with chat apps, moderation systems, and content filters

## Installation

You can install this package using pip:

```bash
pip install hate_speech_detector
```
## Usage

Here's how you can use the package in your code:
```bash
from hate_speech_detector import isHate
result = isHate("I hate you!")
print(result)
# Output: {'message': 'Hate Speech', 'isHate': True}
result = isHate("Have a nice day!")
print(result)
# Output: {'message': 'Not Hate Speech', 'isHate': False}
```

## Function Description
- `isHate(text: str) -> dict`
- Input: A string of text
- Output: A dictionary with:
- `message`: "Hate Speech" or "Not Hate Speech"
- `isHate`: True if hate speech, else False

## Project Information
This package was developed as a **college major project** with the goal of creating a practical ethical and easy-to-use tool for identifying hate speech in textual content. It combines text preprocessing machine learning, and Python packaging into a useful open-source solution.

## Author

- Name: Jahfar Muhammed
- GitHub: https://github.com/jah-117
- Email: jahfarbinmuhammed117@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.