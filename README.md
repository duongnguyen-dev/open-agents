# llmbuddy
Your personal LLM assistant running 100% on your local machine 

## Overall
### Features
- Chat with documents (laws, paper, ...).
- Build your own AI agent or group of agents.
- OCR. 
- Chat with your own database.
- Support multiple embedding/LLM models
### Project information
- Supported OS: `MacOS`, `Windows`, `Ubuntu`
- Build with: `Nuitka`,
- Tech stack: `python`, `fastapi`, `pyqt`, `langchain`, `crewai`, `huggingface`, `gemini`, `docker`

## Development
Clone repository with submodules:
```bash
git clone --recurse-submodules https://github.com/duongnguyen-dev/llmbuddy.git
```
Install required dependencies:
```bash
conda create -n llmbuddy python==3.10
pip install -r requirements.txt
```
