# ResumeTex

[![Production](https://img.shields.io/badge/Production-resumetex.asahoo.dev-blue)](https://resumetex.asahoo.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-green)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)

A fast, reliable REST API for generating professional resumes from JSON data. Built on the popular [Jake's Resume](https://www.overleaf.com/latex/templates/jakes-resume/syzfjbzwjncs) LaTeX template, ResumeTex eliminates the complexity of LaTeX while maintaining the professional quality output.

## Features

- **Multiple Output Formats**: Generate PDF, LaTeX (.tex), or plain text
- **RESTful API**: Simple HTTP endpoints for easy integration
- **Customizable Fonts**: Support for multiple LaTeX font families
- **Flexible Schema**: Comprehensive JSON structure supporting education, experience, projects, skills, and more
- **Docker Ready**: Containerized deployment with all LaTeX dependencies
- **Web Interface**: Interactive HTML frontend for quick testing
- **Production Ready**: Built with FastAPI for high performance

## System Architecture

### Core Components

1. **FastAPI Server** (`server.py`): Handles HTTP requests and routing
2. **Resume Maker** (`resume/resume_maker.py`): Orchestrates resume generation
3. **Resume Class** (`resume/resume.py`): Core LaTeX template and formatting logic
4. **Web Interface** (`public/`): HTML frontend with interactive tools

### Data Flow

1. Client sends JSON resume data via POST request
2. FastAPI validates and routes the request
3. ResumeMaker processes the data and generates LaTeX
4. For PDFs: LaTeX is compiled using pdflatex in a temporary directory
5. Response is returned in the requested format (PDF download, TEX file, or text)
6. Temporary files are cleaned up automatically

## API Endpoints

| Endpoint | Method | Description | Response Type |
|----------|--------|-------------|---------------|
| `/api/v1/pdf` | POST | Generate PDF resume | Binary PDF file |
| `/api/v1/tex` | POST | Generate LaTeX file | LaTeX file download |
| `/api/v1/text` | POST | Get LaTeX as text | Plain text response |
| `/` | GET | Web interface | HTML page |
| `/documentation` | GET | API documentation | HTML page |

## Installation & Setup

### Prerequisites

- Python 3.13+
- pdflatex (for PDF generation)
- Docker (optional, for containerized deployment)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/anish-sahoo/ResumeTex.git
   cd ResumeTex
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install LaTeX (Ubuntu/Debian)**
   ```bash
   sudo apt-get update && sudo apt-get install -y \
       texlive-latex-base \
       texlive-fonts-recommended \
       texlive-fonts-extra \
       texlive-latex-extra
   ```

4. **Run the server**
   ```bash
   uvicorn server:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Access the application**
   - Web Interface: `http://localhost:8000`
   - API Documentation: `http://localhost:8000/documentation`

### Docker Deployment

1. **Build the image**
   ```bash
   docker build -t resumetex .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 resumetex
   ```

The application will be available at `http://localhost:8000`.

### Automated Deployment Script

For production deployments with automatic updates, you can use the included deployment [script](update.sh):

**Usage:**
1. Make the script executable: `chmod +x update.sh`
2. Run the script: `./update.sh`

This script will automatically:
- Stop and remove any existing container
- Pull the latest code from Git
- Rebuild the Docker image
- Start a new container with the updated code

## Usage Examples

### Web Interface

Visit the homepage and use the interactive form to generate resumes instantly.

### cURL Examples

**Generate PDF:**
```bash
curl -X POST -H "Content-Type: application/json" \
  -d @resume.json \
  https://resumetex.asahoo.dev/api/v1/pdf \
  --output resume.pdf
```

**Generate LaTeX file:**
```bash
curl -X POST -H "Content-Type: application/json" \
  -d @resume.json \
  https://resumetex.asahoo.dev/api/v1/tex \
  --output resume.tex
```

**Get LaTeX as text:**
```bash
curl -X POST -H "Content-Type: application/json" \
  -d @resume.json \
  https://resumetex.asahoo.dev/api/v1/text
```

### Python Example

```python
import requests
import json

# Your resume data
resume_data = {
    "name": "Your Name",
    "email": "your.email@example.com",
    "phone": "123-456-7890",
    # ... rest of your resume data
}

# Generate PDF
response = requests.post(
    'https://resumetex.asahoo.dev/api/v1/pdf',
    json=resume_data
)

if response.status_code == 200:
    with open('resume.pdf', 'wb') as f:
        f.write(response.content)
    print("Resume generated successfully!")
else:
    print(f"Error: {response.status_code}")
```

## JSON Schema

The API accepts a flexible JSON structure. All fields except `name` are optional.

### Basic Structure

```json
{
  "name": "Your Name",
  "phone": "123-456-7890",
  "email": "your.email@example.com",
  "font": "fira",
  "font_size": 12,
  "links": [...],
  "education": [...],
  "experience": [...],
  "projects": [...],
  "skills": [...],
  "interests": [...],
  "page_break": true
}
```

### Supported Fonts

- `fira` - Fira Sans (default)
- `roboto` - Roboto
- `noto-sans` - Noto Sans
- `sourcesanspro` - Source Sans Pro
- `cormorantgaramond` - Cormorant Garamond
- `charter` - Charter

### Complete Example
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
    }
  ]
}
```

## Technical Details

### Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for FastAPI
- **Pydantic**: Data validation using Python type hints
- **LaTeX**: Document preparation system for high-quality typesetting

### File Structure

```bash
ResumeTex/
├── server.py               # FastAPI application and routes
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container configuration
├── sample_input.json       # Example resume data
├── public/                 # Web interface assets
│   ├── index.html          # Main web interface
│   └── documentation.html  # API documentation
├── resume/                 # Core resume generation logic
│   ├── __init__.py
│   ├── resume_maker.py     # Main resume orchestrator
│   └── resume.py           # LaTeX template and formatting
└── tests/                  # Test files and examples
    ├── sample_input_bad_col.json
    └── sample_input_pagebreak.json
```

### Performance Considerations

- **Temporary File Management**: PDF generation creates temporary directories that are automatically cleaned up
- **Background Tasks**: Cleanup operations run asynchronously to avoid blocking responses
- **Memory Efficiency**: LaTeX compilation is isolated to prevent memory leaks
- **Error Handling**: Comprehensive error handling for LaTeX compilation failures

## Troubleshooting

### Common Issues

1. **LaTeX Compilation Errors**
   - Ensure all required LaTeX packages are installed
   - Check for special characters that need escaping
   - Verify JSON structure matches the expected schema

2. **Font Issues**
   - Verify the font name is supported (see Supported Fonts section)
   - Font packages must be available in your LaTeX installation

3. **Permission Errors**
   - Ensure the application has write permissions for temporary directories
   - Check that pdflatex is in the system PATH

### Debug Mode

Enable debug logging by setting environment variables:

```bash
export PYTHONPATH=/path/to/ResumeTex
export DEBUG=1
uvicorn server:app --reload --log-level debug
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/

# Run server
fastapi run server.py
```
## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Production**: [resumetex.asahoo.dev](https://resumetex.asahoo.dev)
- **Documentation**: [resumetex.asahoo.dev/documentation](https://resumetex.asahoo.dev/documentation)
- **Issues**: [GitHub Issues](https://github.com/anish-sahoo/ResumeTex/issues)
- **Author**: [Anish Sahoo](https://asahoo.dev)

---

<p align="center">Made with love by <a href="https://asahoo.dev">Anish Sahoo</a></p>
