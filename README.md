# Final Project

## AI-Based Emotion Detection Web Application

An AI-powered web application built using Python, Flask, and IBM Watson NLP to analyze text and identify human emotions.

This project was developed as part of IBM's **Developing AI Applications with Python and Flask** course.

The application analyzes user-provided text and identifies five emotions: anger, disgust, fear, joy, and sadness. It also determines the dominant emotion based on the highest confidence score.

## Features

- Emotion detection using IBM Watson NLP
- Classification of five emotions: anger, disgust, fear, joy, and sadness
- Identification of the dominant emotion
- Interactive web interface using Flask
- REST API integration
- Error handling for invalid or empty inputs
- Unit testing using Python's unittest framework
- Static code analysis using PyLint

## Technologies Used

- Python 3
- Flask
- IBM Watson NLP
- REST API
- HTML5
- JavaScript
- Requests
- JSON
- unittest
- PyLint
- Git and GitHub

## Project Structure

```
final_project/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── static/
│   └── mywebscript.js
│
├── templates/
│   └── index.html
│
├── server.py
├── test_emotion_detection.py
├── README.md
└── LICENSE
```

## Installation

1. Clone the Repository

```bash
git clone https://github.com/AnasMRafi/oaqjp-final-project-emb-ai.git
```

2. Navigate to the Project Directory

```bash
cd oaqjp-final-project-emb-ai
```

3. Install Dependencies

```bash
python3 -m pip install flask requests
```

4. Run the Application

```bash
python3 server.py
```

5. Access the Application

Open your browser and navigate to:

```
http://localhost:5000
```

> **Note:** The application requires access to IBM Skills Network's Watson NLP service, which may not be accessible outside the course environment.

## How It Works

1. The user enters text into the web interface.
2. Flask receives the input through the `/emotionDetector` endpoint.
3. The application sends the text to the IBM Watson NLP API.
4. The API returns scores for five emotions.
5. The application determines the dominant emotion.
6. The results are displayed in the browser.

## Example Output

**Input:**

```
I love my life.
```

**Response:**

```
{
    'anger': 0.0063,
    'disgust': 0.0026,
    'fear': 0.0093,
    'joy': 0.9680,
    'sadness': 0.0497,
    'dominant_emotion': 'joy'
}
```

> The scores above are illustrative. Actual API results may vary.

**Displayed Result:**

```
For the given statement, the system response is
'anger': 0.0063, 'disgust': 0.0026,
'fear': 0.0093, 'joy': 0.9680 and
'sadness': 0.0497.
The dominant emotion is joy.
```

## Unit Testing

The application includes five unit tests to validate emotion detection.

| Test Statement | Expected Emotion |
|---|---|
| I am glad this happened | Joy |
| I am really mad about this | Anger |
| I feel disgusted just hearing about this | Disgust |
| I am so sad about this | Sadness |
| I am really afraid that this will happen | Fear |

Run the tests using:

```bash
python3 test_emotion_detection.py
```

## Error Handling

The application handles empty or invalid text input.

When the user submits an empty input, the application displays:

```
Invalid text! Please try again!
```

For an HTTP 400 response, the emotion detection function returns a dictionary containing None values for all emotions and the dominant emotion.

## Static Code Analysis

PyLint is used to evaluate Python code quality and compliance with coding standards.

Run:

```bash
python3 -m pylint server.py
```

The project targets a PyLint score of 10.00/10.

## Course Information

- **Course:** Developing AI Applications with Python and Flask
- **Provider:** IBM
- **Project:** AI-Based Web Application Development and Deployment
- **Project Type:** Final Course Project

## License and Attribution

This project is based on the IBM Developer Skills Network starter repository, licensed under the Apache License 2.0.

Original repository: https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai
