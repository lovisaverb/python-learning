import sys
import requests

print(f"Python 版本：{sys.version}")
print(f"執行環境：WSL")

# 試試呼叫一個公開 API
r = requests.get("https://api.github.com")
print(f"GitHub API 狀態碼：{r.status_code}")