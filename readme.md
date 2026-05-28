# AI Resume-to-Job Matcher V1

A beginner Python project that compares resume text with a job description and provides a match score, matched keywords, missing keywords, and improvement suggestions.

## Features
- Accepts resume text
- Accepts job description
- Calculates match score
- Detects matched keywords
- Detects missing keywords
- Suggests improvements

## Skills Used
- Python fundamentals
- Functions
- Lists and loops
- String processing
- Keyword matching
- Basic scoring logic
- Resume/job description comparison
- Recommendation system logic

## Sample Output

Resume Text:
I have experience in manufacturing, troubleshooting, documentation, root cause analysis, and process improvement.

Job Description:
We need an engineer with manufacturing experience, troubleshooting skills, documentation, process improvement, quality, and automation.

Output:

--- Resume Job Match Report ---
Match Score: 66%
Matched Keywords: ['process improvement', 'documentation', 'troubleshooting', 'manufacturing']
Missing Keywords: ['automation', 'quality']
Recommendation: Moderate match. Add missing keywords and stronger achievements.

Suggested Improvements:
- Add experience or examples related to: automation
- Add experience or examples related to: quality

## How to Run

1. Download or clone this repository.
2. Open the project folder.
3. Run the Python file:

`python app.py`

4. Paste your resume text.
5. Paste the job description.
6. View the match report.

## Future Improvements
- Add AI API integration
- Add PDF resume upload
- Add ATS-style scoring
- Add role-specific keyword sets
- Add Streamlit web interface
- Export report to PDF
- Suggest improved resume bullet points
