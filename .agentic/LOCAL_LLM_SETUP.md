# Local LLM Setup Guide  
Use Local Models with VS Code + GitHub Copilot

This guide helps developers configure **local LLMs** on macOS, Windows, or Linux and use them **alongside GitHub Copilot** inside VS Code.

The goal is to give every team member the freedom to choose:
- GitHub Copilot (cloud models)
- Local LLMs (Ollama, LM Studio, llama.cpp, MLX, vLLM)
- Hybrid workflows (Copilot + local models)

This supports privacy, offline development, experimentation, and agentic workflows.

---

# 1. Why Use Local LLMs?

Local LLMs are useful when you need:
- Offline development  
- Private code processing  
- Zero‑cost inference  
- Custom fine‑tuned models  
- High‑speed responses on Apple Silicon  
- Experimental agentic workflows  

Local models do **not** replace GitHub Copilot — they complement it.

---

# 2. Recommended Local LLM Runtimes

Choose any of the following:

## Option A — **Ollama** (Best for simplicity)
- Easiest to install  
- Great model library  
- Works with VS Code extensions  
- Excellent on Apple Silicon  

Install:
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama run llama3

