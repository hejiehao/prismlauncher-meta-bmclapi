import requests
import os
from datetime import datetime

# 构建API请求URL
api_url = f"https://api.github.com/repos/{os.environ['USERNAME']}/{os.environ['REPO_NAME']}/traffic/data"

# 发送请求
headers = {'Authorization': f"token {os.environ['GITHUB_TOKEN']}"}
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # 假设返回的数据中有月消耗数据量的字段
    monthly_data_usage = data['monthly_data_usage']

    # 获取当前日期
    current_date = datetime.now().strftime("%Y-%M-%d")


# 构建要更新的数据使用量字符串
data_usage_str = f"\n\n## 数据使用量更新 - {current_date}\n本月 GitHub Pages 消耗数据量: {monthly_data_usage} MB"

# 读取README文件
with open('README.md', 'r') as file:
    lines = file.readlines()

# 替换最后一行
lines[-1] = data_usage_str + '\n\n'

# 写入更新后的内容
with open('README.md', 'w') as file:
    file.writelines(lines)

else:
    print("无法获取数据，请检查您的用户名、令牌或仓库名称。")