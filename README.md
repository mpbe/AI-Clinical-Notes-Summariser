
# AI Clinical Notes Summariser

A Flask-based web application that demonstrates how AI can transform clinical notes into structured summaries, as well as providing proposed codes, while aligning with UK clinical coding standards.

---

## Overview

From the user input, this project produces:

- Structured clinical summaries
- Key diagnoses and co-morbidities
- Procedure identification
- Suggested ICD-10 (UK) and OPCS-4 codes

---

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Jinja templating
- **AI Integration:** Designed for LLM APIs
- **Version Control:** Git, GitHub

---

## Features

- User input is submitted via a web form
- AI powered summary is displayed underneath
- Prompting breaks the summary down into clear sections:
  - Summary
  - Diagnoses
  - Procedures
  - Code Suggestions
- Query history page to review past queries for each session
- Sample input buttons for quick testing of the application
- Input validation and error handling
- Basic UI styling

---

## Example Use Case

This application simulates how AI could support clinical coding workflows by assisting with the interpretation of unstructured medical notes and suggesting relevant coding outputs.

---

## Project Structure

```
ai-clinical-summariser/
│
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── services/
│ │ └── ai_service.py
│ ├── templates/
│ │ ├── index.html
│ │ └── history.html
│ └── static/
│   └── styles.css
│
├── config.py
├── run.py
├── requirements.txt
├── .env (not included)
└── README.md
```

---

## Running the Application

The application is deployed and accessible here:



### Running Locally  


- Create a '.env' file in the root directory, and code the below into it (using your own API code)
- OPENAI_API_KEY=your_api_key_here
- Install dependencies:
  - pip install -r requirements.txt
- Run the application:
  - python run.py
- Then open in browser:
  - http://127.0.0.1:5000

---

## Motivation

The motivation behind this particular project was to combine both my current and aspiring careers into one application. It also is a result of my growing interest in AI and its potential applications across all fields. This served as a good learning project and an introduction to working with AI.

---

## Honest Review of The AI Output
As someone who has worked in the clinical coding field for a long time, I can say from the tests I have performed that the summaries of diagnoses and procedures are very good, and the codes are somewhat accurate. However there are a number of errors that are made in sequencing, selection, and omission of codes. Overall though the results are impressive given the basic nature of this application.    

---

## Future Improvements

- Database storage for improved query history
- Enhanced UI
- More in depth AI prompt engineering
- Authentication for individual User sessions