import os
import subprocess
import tempfile
from resume.resume import Resume


class ResumeMaker(Resume):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def generate_latex(self, data):
        """
        Generate LaTeX code for the resume.

        Args:
            data (dict): A dictionary containing the resume data (json).
        """
        font = data.get("font", "")
        font_size = data.get("font_size", 11)
        resume = Resume()
        if font != "" and font_size != 11:
            resume = Resume(font=font, font_size=font_size)
        elif font != "":
            resume = Resume(font=font)
        elif font_size != 11:
            resume = Resume(font_size=font_size)    
        resume.add_personal_info(data)
        
        for key, value in data.items():
            match key:
                case "education":
                    resume.add_education(value)
                case "experience":
                    resume.add_work_experience(value)
                case "skills":
                    resume.add_skills(value)
                case "projects":
                    resume.add_projects(value)
                case "interests":
                    resume.add_interests(value)
                case "page_break":
                    resume.add_page_break()
                case "name":
                    pass
                case "font":
                    pass
                case "font_size":
                    pass
                case "email":
                    pass
                case "phone":
                    pass
                case _:
                    print(f"Unknown key: {key}")
        print('resume.get_complete_latex() <<<\n', resume.get_complete_latex(), '\n>>>')
        return resume.get_complete_latex()

    def generate_pdf(self, data):
        """
        Generate a PDF file for the resume.

        Args:
            data (dict): A dictionary containing the resume data (json).
        """
        temp_dir = os.path.join(os.getcwd(), "temp")
        os.makedirs(temp_dir, exist_ok=True)

        tmpdirname = tempfile.mkdtemp(dir=temp_dir)
        tex_path = os.path.join(tmpdirname, "resume.tex")
        pdf_path = os.path.join(tmpdirname, "resume.pdf")

        with open(tex_path, "w") as tex_file:
            tex_file.write(self.generate_latex(data))
            
        try:
            for _ in range(2):
                _ = subprocess.run(
                    ["pdflatex", "-interaction=nonstopmode", "resume.tex"],
                    cwd=tmpdirname,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    check=True,
                )
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.decode()
            raise RuntimeError(f"pdflatex compilation failed: {error_msg}")

        if not os.path.exists(pdf_path):
            raise RuntimeError("PDF file was not created.")

        return pdf_path

    @staticmethod
    def clean_up_temp_files():
        """
        Clean up the temporary files.
        """
        try:
            subprocess.run(["rm", "-rf", "temp"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
