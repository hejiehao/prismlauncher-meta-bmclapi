          import requests
          import os

          # 构建API请求URL
          api_url = f"https://api.github.com/repos/{os.environ['USERNAME']}/{os.environ['REPO_NAME']}/traffic/data"

          # 发送请求
          headers = {'Authorization': f"token {os.environ['GITHUB_TOKEN']}"}
          response = requests.get(api_url, headers=headers)

          if response.status_code == 200:
              data = response.json()
              # 假设返回的数据中有月消耗数据量的字段
              monthly_data_usage = data['monthly_data_usage']

              # 读取README文件
              with open('README.md', 'r') as file:
                  readme_contents = file.read()

              # 更新数据消耗量
              new_readme_contents = readme_contents.replace('<!-- DATA_USAGE_START -->', f"<!-- DATA_USAGE_START -->\\n本月GitHub Pages消耗数据量: {monthly_data_usage} MB")

              # 写入新的README
              with open('README.md', 'w') as file:
                  file.write(new_readme_contents)

          else:
              print("无法获取数据，请检查您的用户名、令牌或仓库名称。")
