def calculate_match(resume, job_description):
    resume_lower = resume.lower()
    job_lower = job_description.lower()

    keywords = [
        "python",
        "excel",
        "sql",
        "automation",
        "data analysis",
        "process improvement",
        "root cause analysis",
        "documentation",
        "troubleshooting",
        "quality",
        "manufacturing",
        "engineering"
    ]

    matched_keywords = []
    missing_keywords = []

    for keyword in keywords:
        if keyword in job_lower:
            if keyword in resume_lower:
                matched_keywords.append(keyword)
            else:
                missing_keywords.append(keyword)

    job_keywords = matched_keywords + missing_keywords

    if len(job_keywords) > 0:
        score = int((len(matched_keywords) / len(job_keywords)) * 100)
    else:
        score = 0

    return score, matched_keywords, missing_keywords
resume = input("Paste your resume text: ")
job_description = input("Paste the job description: ")

score, matched, missing = calculate_match(resume, job_description)

print("\n--- Resume Job Match Report ---")
print(f"Match Score: {score}%")
print(f"Matched Keywords: {matched}")
print(f"Missing Keywords: {missing}")

if score >= 70:
    print("Recommendation: Strong match. You can apply, but still tailor your resume.")
elif score >= 40:
    print("Recommendation: Moderate match. Add missing keywords and stronger achievements.")
else:
    print("Recommendation: Weak match. Improve your resume alignment before applying.")

if missing:
    print("\nSuggested Improvements:")
    for keyword in missing:
        print(f"- Add experience or examples related to: {keyword}")
else:
    print("\nSuggested Improvements: No major missing keywords detected.")