# Open Agents: The Ultimate Multi-Agents Framework
![GitHub stars](https://img.shields.io/github/stars/duongnguyen-dev/open-agents?style=social)
![GitHub forks](https://img.shields.io/github/forks/duongnguyen-dev/open-agents?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/duongnguyen-dev/open-agents?style=social)
![GitHub repo size](https://img.shields.io/github/repo-size/duongnguyen-dev/open-agents)
![GitHub language count](https://img.shields.io/github/languages/count/duongnguyen-dev/open-agents)
![GitHub top language](https://img.shields.io/github/languages/top/duongnguyen-dev/open-agents)
![GitHub last commit](https://img.shields.io/github/last-commit/duongnguyen-dev/open-agents?color=red)
<!-- [![Discord](https://img.shields.io/badge/Discord-Open_WebUI-blue?logo=discord&logoColor=white)](https://discord.gg/5rJgQTnV4s) -->
<!-- [![](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/tjbck) -->

**OpenAgents is an extensible framework designed to facilitate the creation, coordination and deployment of such systems.**

<p align="center">
<a href=""><img src="docs/resources/openagents_logo_without_text.svg" alt="OpenAgents logo" width="150px"></a>
</p>
<p align="center">
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
<a href="https://discord.gg/xUbfcfeT"><img src="https://dcbadge.vercel.app/api/server/xUbfcfeT?style=flat" alt="Discord Follow"></a>
<!-- <a href="https://twitter.com/MetaGPT_"><img src="https://img.shields.io/twitter/follow/MetaGPT?style=social" alt="Twitter Follow"></a>
</p> -->

## News

## Get started
### Project information
- Supported OS: `MacOS`, `Windows`
- Tech stack: `python`, `fastapi`, `langchain`, `langgraph`, `langsmith`, `huggingface`, `gemini`, `llama`, `bitnet`, `docker`
### Features
- 🪄 Build your own AI agent or group of agents.
- 💬 Chat with your agents. 
- 🖥️ Montoring AI agents workflow.
- 🔨 Integrates with Open WebUI to run the platform locally.
### Installation
Via pip: 
```bash
pip install open-agents
```

For development
- Clone the repository:
    ```bash
    git clone https://github.com/duongnguyen-dev/open-agents.git
    ```
- Install required dependencies:
    ```bash
    conda create -n openagents python==3.11 && conda activate openagents
    pip install -e .
    ```
- Run frontend:
    ```bash
    cd frontend && npm install
    npm run dev
    ```
- Run backend: 
    ```bash
    cd open-agents
    python main.py
    ```