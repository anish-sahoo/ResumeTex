# %-------------------------
# % Resume in Latex
# % Author : Jake Gutierrez -> Modified by Anish Sahoo
# % Based off of: https://github.com/sb2nov/resume
# % License : MIT
# %------------------------

import os
import tempfile
import subprocess

font_set = {
    "fira": r"\usepackage[sfdefault]{FiraSans}",
    "roboto": r"\usepackage[sfdefault]{roboto}",
    "noto-sans": r"\usepackage[sfdefault]{noto-sans}",
    "sourcesanspro": r"\usepackage[default]{sourcesanspro}",
    "cormorantgaramond": r"\usepackage{CormorantGaramond}",
    "charter": r"\usepackage{charter}",
    "": "",
}


def latexify(text: str) -> str:
    text = (
        text.replace("\\", r"\textbackslash")
        .replace("&", r"\&")
        .replace("%", r"\%")
        .replace("$", r"\$")
        .replace("#", r"\#")
        .replace("_", r"\_")
        .replace("{", r"\{")
        .replace("}", r"\}")
        .replace("~", r"\textasciitilde")
        .replace("^", r"\^")
    )

    return r"{}".format(text)


class Resume:
    def __init__(self, **kwargs):
        font_size = kwargs.get("font_size", 11)
        font = kwargs.get("font", "")

        self.preamble = (
            r"""
\documentclass[letterpaper,"""
            + str(font_size)
            + r"""pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[american]{babel}
\usepackage{tabularx}
\input{glyphtounicode}

"""
            + font_set.get(font, "")
            + r"""

\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.0in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
\vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

% Ensure that generate pdf is machine readable/ATS parsable
\pdfgentounicode=1

%-------------------------
% Custom commands
\newcommand{\resumeItem}[1]{
\item\small{
    {#1 \vspace{-2pt}}
}
}

\newcommand{\resumeSubheading}[4]{
\vspace{-2pt}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
    \textbf{#1} & #2 \\
    \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubheadingSmall}[2]{
\vspace{-2pt}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
    \textbf{#1} & #2 \\
    \end{tabular*}\vspace{-9pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
    \textit{\small#1} & \textit{\small #2} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
    \small#1 & #2 \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

%-------------------------------------------
%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
        )
        self.code = ""

    """
    Example input:
    {
        "name": "Anish Sahoo",
        "phone": "123-456-7890",
        "email": "anish@email.email",
        "links": [
            {
                "url": "https://www.linkedin.com/in/anish-sahoo",
                "text": "linkedin.com/in/anish-sahoo"  
            }, 
            {
                "url": "https://asahoo.dev",
                "text": "asahoo.dev"
            }
        ]
    }
    """

    def add_personal_info(self, resume):
        name = latexify(resume.get("name", ""))
        phone = latexify(resume.get("phone", ""))
        email = latexify(resume.get("email", ""))
        links = resume.get("links", [])

        self.code += r"\begin{center}" + os.linesep

        if name != "":
            self.code += (
                r"\textbf{\Huge \scshape " + name + r"} \\ \vspace{1pt}" + os.linesep
            )

        if phone != "":
            self.code += r"\small " + phone
            if email != "":
                 self.code += r" $|$ "
            self.code += os.linesep

        

        if email != "":
            
            self.code += (
                r"\href{mailto:"
                + email
                + r"}{\underline{"
                + email
            )

            if phone != "":
                self.code += + r"}} $|$ "
            self.code += os.linesep

        for link in links:
            self.code += (
                r"\href{"
                + latexify(link.get("url", ""))
                + r"}{\underline{"
                + latexify(link.get("text", ""))
                + r"}} $|$ "
                + os.linesep
            )

        self.code += r"\end{center}" + os.linesep

    """
    Example input:
    [
        {
            "school": 'Northeastern University',
            "time": 'Expected Graduation: December 2026',
            "degree": 'Bachelor of Science in Computer Science',
            "location": 'Boston, MA',
            "details": [
                'Major GPA: 3.95',
                'Coursework: Machine Learning, Artificial Intelligence',
            ],
        }
    ]"""

    def add_education(self, education, title="Education"):
        if len(education) == 0:
            return
        self.code += os.linesep + r"\section{" + title + r"}" + os.linesep
        self.code += r"\resumeSubHeadingListStart" + os.linesep
        tabs = 0
        for edu in education:
            tabs += 4
            self.code += (
                r"\resumeSubheading"
                + r"{"
                + latexify(edu.get("school", ""))
                + r"}"
                + r"{"
                + latexify(edu.get("time", ""))
                + r"}"
                + r"{"
                + latexify(edu.get("degree", ""))
                + r"}"
                + r"{"
                + latexify(edu.get("location", ""))
                + r"}"
                + os.linesep
            )
            tabs -= 4
            if len(edu.get("details", [])) > 0:
                self.code += r"\resumeItemListStart" + os.linesep
            tabs += 4
            for item in edu.get("details", []):
                self.code += (
                    (" " * tabs) + r"\resumeItem{" + latexify(item) + r"}" + os.linesep
                )
            tabs -= 4
            if len(edu.get("details", [])) > 0:
                self.code += r"\resumeItemListEnd" + os.linesep

        self.code += r"\resumeSubHeadingListEnd" + os.linesep

    """
    Sample input:
    [
        {
            "company": "Company",
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
            "company": "Company",
            "jobs": [
                {
                    "time": "June 2021 - August 2021",
                    "title": "Software Engineer Intern",
                    "details": [
                        "Developed a web application to manage data",
                        "Implemented a feature to allow users to upload files"
                    ]
                },
                {
                    "time": "June 2021 - August 2021",
                    "title": "Software Engineer Intern",
                    "details": [
                        "Developed a web application to manage data",
                    ]
                }
            ]
        }
    ]
    """

    def add_work_experience(self, work_experience, title="Experience"):
        if len(work_experience) == 0:
            return
        self.code += os.linesep + r"\section{" + title + r"}" + os.linesep
        self.code += r"\resumeSubHeadingListStart" + os.linesep
        tabs = 0
        for exp in work_experience:
            if len(exp.get("jobs", [])) > 1:
                self.code += (
                    r"\resumeSubheadingSmall"
                    + r"{"
                    + latexify(exp.get("company", ""))
                    + r"}"
                    + r"{"
                    + latexify(exp.get("jobs", [{}])[0].get("time", ""))
                    + r"}"
                )
                self.code += os.linesep
                for job in exp.get("jobs", []):
                    tabs += 4
                    self.code += (
                        r"\resumeSubSubheading"
                        + r"{"
                        + latexify(job.get("title", ""))
                        + r"}"
                        + r"{"
                        + latexify(job.get("time", ""))
                        + r"}"
                        + os.linesep
                    )
                    if len(job.get("details", [])) > 0:
                        self.code += r"\resumeItemListStart" + os.linesep
                    tabs += 4
                    for item in job.get("details", []):
                        self.code += (
                            (" " * tabs)
                            + r"\resumeItem{"
                            + latexify(item)
                            + r"}"
                            + os.linesep
                        )
                    tabs -= 4
                    if len(job.get("details", [])) > 0:
                        self.code += r"\resumeItemListEnd" + os.linesep
                    tabs -= 4
            else:
                job = exp.get("jobs", [{}])[0]
                self.code += (
                    r"\resumeSubheading"
                    + r"{"
                    + latexify(exp.get("company", ""))
                    + r"}"
                    + r"{"
                    + latexify(job.get("time", ""))
                    + r"}"
                    + r"{"
                    + latexify(job.get("title", ""))
                    + r"}"
                    + r"{"
                    + latexify(job.get("location", ""))
                    + r"}"
                    + os.linesep
                )
                if len(job.get("details", [])) > 0:
                    self.code += r"\resumeItemListStart" + os.linesep
                tabs += 4
                for item in job.get("details", []):
                    self.code += (
                        (" " * tabs)
                        + r"\resumeItem{"
                        + latexify(item)
                        + r"}"
                        + os.linesep
                    )
                tabs -= 4
                if len(job.get("details", [])) > 0:
                    self.code += r"\resumeItemListEnd" + os.linesep

            self.code += os.linesep

        self.code += r"\resumeSubHeadingListEnd" + os.linesep

    def add_skills(self, skills, title="Skills"):
        if len (skills) == 0:
            return
        self.code += os.linesep + r"\section{" + title + r"}" + os.linesep
        self.code += r"\begin{itemize}[leftmargin=0.15in, label={}]" + os.linesep
        self.code += r"    \small{\item{" + os.linesep
        tabs = 4
        # this is when skills is of this form:
        # {
        #     "skills": ["Python", "Java", "C++"]
        # }
        if isinstance(skills, list) and isinstance(skills[0], str):
            self.code += (
                " " * tabs
                + ", ".join(map(lambda a: latexify(a), skills)) + os.linesep
            )
        else:
            # this is when skills is of this form:
            # {
            #     "skills": [
            #         {
            #             "title": "Programming Languages",
            #             "items": ["Python", "Java", "C++"]
            #         },
            #         {
            #             "title": "Web Development",
            #             "items": ["HTML", "CSS", "JavaScript"]
            #         }
            #     ]
            for i, skill in enumerate(skills):
                self.code += (
                    " " * tabs
                    + r"\textbf{"
                    + latexify(skill.get("title", ""))
                    + r"}{: "
                    + ", ".join(map(lambda a: latexify(a), skill.get("items", [])))
                    + r"}"
                    + (r"" if i == len(skills) - 1 else r"\\")
                    + os.linesep
                )
        self.code += r"}}" + os.linesep + r"\end{itemize}" + os.linesep

    def add_projects(self, projects, title="Projects"):
        if len(projects) == 0:
            return
        self.code += os.linesep + r"\section{" + title + r"}" + os.linesep
        self.code += r"\resumeSubHeadingListStart" + os.linesep
        tabs = 0
        for project in projects:
            tabs += 4
            self.code += (
                r"\resumeProjectHeading"
                + os.linesep
                + " " * tabs
                + r"{ \textbf{"
                + latexify(project.get("title", ""))
                + r"}"
                + " " * tabs
                + r"$|$ \emph{"
                + latexify(project.get("subtitle", ""))
                + r"}}"
                + " " * tabs
                + r"{"
                + latexify(project.get("time", ""))
                + r"}"
                + os.linesep
            )
            tabs -= 4
            if len(project.get("details", [""])) > 0:
                self.code += r"\resumeItemListStart" + os.linesep
            tabs += 4
            for item in project.get("details", [""]):
                self.code += (
                    (" " * tabs) + r"\resumeItem{" + latexify(item) + r"}" + os.linesep
                )
            tabs -= 4
            if len(project.get("details", [""])) > 0:
                self.code += r"\resumeItemListEnd" + os.linesep

        self.code += r"\resumeSubHeadingListEnd" + os.linesep

    def add_interests(self, interests, title="Interests"):
        self.code += os.linesep + r"\section{" + title + r"}" + os.linesep
        if len(interests) == 0:
            return
        self.code += r"\resumeItemListStart" + os.linesep
        tabs = 4
        formatted_interests = [latexify(item) for item in interests]
        self.code += (
            (" " * tabs) + r"\resumeItem{" + ", ".join(formatted_interests) + r"}" + os.linesep
        )
        tabs -= 4
        self.code += r"\resumeItemListEnd" + os.linesep

    def add_page_break(self):
        self.code += r"\pagebreak" + os.linesep

    def get_complete_latex(self):
        return (
            self.preamble
            + r"\begin{document}"
            + os.linesep
            + self.code
            + os.linesep
            + r"\end{document}"
        )


# sections = {
#     "personal_info": [{
#         "name": str,
#         "phone": str,
#         "email": str,
#         "links": list,  # List of dicts with 'url' and 'text'
#     }],
#     "education": [{
#         "school": str,
#         "time": str,
#         "degree": str,
#         "location": str,
#         "details": list,  # List of strings
#     }],
#     "work_experience": [{
#         "company": str,
#         "jobs": list,  # List of job dicts
#     }],
#     "skills": [{
#         "title": str,
#         "items": list,  # List of strings
#     }],
#     "projects": [{
#         "title": str,
#         "subtitle": str,
#         "time": str,
#         "details": list,  # List of strings
#     }],
#     "interests": list # List of strings
# }
