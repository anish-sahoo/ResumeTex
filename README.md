# Latex Resume Generator

- Heard about Jake's resume but don't know how to use Latex?
- This web app lets you use drag and drop tools for the same purpose!
- And you can get a latex file back!

The JSON file should follow this structure:
```json
{
  "name": "Anish Sahoo",
  "phone": "123-456-7890",
  "email": "anish@email.email",
  "font": "fira",
  "font_size": 12,
  "links": [
    {
      "url": "https://www.linkedin.com/in/anish-sahoo",
      "text": "linkedin.com/in/anish-sahoo"
    },
    {
      "url": "https://asahoo.dev",
      "text": "asahoo.dev"
    }
  ],
  "education": [
    {
      "school": "Northeastern University",
      "time": "Expected Graduation: December 2026",
      "degree": "Bachelor of Science in Computer Science",
      "location": "Boston, MA",
      "details": [
        "Major GPA: 3.95",
        "Coursework: Machine Learning, Artificial Intelligence"
      ]
    },
    {
      "school": "High School",
      "time": "Graduated: June 2022",
      "degree": "High School Diploma",
      "location": "Boston, MA",
      "details": [
        "GPA: 4.0",
        "Honors: Valedictorian"
      ]
    }
  ],
  "experience": [
    {
      "company": "Tech Solutions Inc.",
      "jobs": [
        {
          "time": "June 2021 - August 2021",
          "title": "Software Engineer Intern",
          "location": "Boston, MA",
          "details": [
            "Developed a web application to manage data",
            "Implemented a feature to allow users to upload files"
          ]
        }
      ]
    },
    {
      "company": "Innovative Tech",
      "jobs": [
        {
          "time": "June 2020 - August 2020",
          "title": "Junior Developer",
          "location": "Remote",
          "details": [
            "Assisted in the development of a mobile application",
            "Collaborated with a team of developers to improve app performance"
          ]
        }
      ]
    }
  ],
  "projects": [
    {
      "title": "Personal Portfolio",
      "subtitle": "A personal website to showcase my projects and skills",
      "time": "January 2021 - Present",
      "details": [
        "Built using HTML, CSS, and JavaScript",
        "Includes a blog section where I write about my learning experiences"
      ]
    },
    {
      "title": "E-commerce Platform",
      "subtitle": "A full-stack e-commerce platform",
      "time": "September 2020 - December 2020",
      "details": [
        "Developed using Django and React",
        "Implemented features such as user authentication, product listings, and a shopping cart"
      ]
    }
  ],
  "interests": [
    "Reading",
    "Traveling",
    "Photography",
    "Coding"
  ],
  "skills": [
    {
      "title": "Programming Languages",
      "items": [
        "Python",
        "Java",
        "C++"
      ]
    },
    {
      "title": "Web Development",
      "items": [
        "HTML",
        "CSS",
        "JavaScript"
      ]
    },
    {
      "title": "Tools & Technologies",
      "items": [
        "Git",
        "Docker",
        "Kubernetes"
      ]
    }
  ]
}
```
