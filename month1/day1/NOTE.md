# Day 1 筆記

## 學到的指令
- `wsl` 進入 Linux
- `python -m venv .venv` 建虛擬環境
- `source .venv/bin/activate` 啟動
- `pip install <套件>` 安裝套件
- `git init / add / commit` 版本控制

## 我還不懂的（之後問 Claude Code）
- [x] venv 為什麼要每個專案都建一個？
- [x] pyenv 跟 venv 差在哪？
- [x] .gitignore 還可以加什麼？

## 建立的內容
```python
import sys
import requests

print(f"Python 版本：{sys.version}")
print(f"執行環境：WSL")

# 試試呼叫一個公開 API
r = requests.get("https://api.github.com")
print(f"GitHub API 狀態碼：{r.status_code}")
```