import requests
from bs4 import BeautifulSoup
import re
import pathlib
from datetime import datetime
import json
import pytz
import os

root = pathlib.Path(__file__).parent.resolve()

urls = os.getenv("urls")

def replace_chunk(content, marker, chunk, inline=False):
    r = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = "\n{}\n".format(chunk)
    chunk = "<!-- {} starts -->{}<!-- {} ends -->".format(marker, chunk, marker)
    return r.sub(chunk, content)


def fetch_apple_count(urls):
    # 存储所有网站的账号密码
    all_credentials = []
    # 发起请求获取网页内容
    headers = {
        'Accept': 'application/json'
    }
    for url in urls:
        if url.startswith('https://aunlock.laogoubi.net'):
            response = requests.get(url, headers=headers)
            res_text = response.text
            # print(res_text)
            data = json.loads(res_text)
            credentials = []
            for item in data:
                if 'username' in item and 'password' in item:
                    credentials.append({"account": item['username'], "password": item['password']})
            all_credentials.extend(credentials)
        else:
            response = requests.get(url)
            accounts = []
            passwords = []
            # 检查请求是否成功
            if response.status_code == 200:
                html_doc = response.content
                # print(html_doc)
                # 使用BeautifulSoup解析HTML
                soup = BeautifulSoup(html_doc, 'html.parser')
                # print(url, html_doc , '\n')
                # 找到对应的button元素
                buttons = soup.find_all('button', {'class': 'btn-outline-secondary'})
                # print(buttons)
                # 遍历所有匹配的元素
                for button in buttons:
                    # 获取onclick属性的值
                    onclick_value = button.get('onclick')
                    if '复制帐号' in button.text and '账号维护中' not in onclick_value:
                        start_index = onclick_value.find("(") + 1
                        end_index = onclick_value.find(")")
                        account = onclick_value[start_index:end_index].replace("'", "")
                        accounts.append(account)
                    elif '复制密码' in button.text:
                        start_index = onclick_value.find("(") + 1
                        end_index = onclick_value.find(")")
                        password = onclick_value[start_index:end_index].replace("'", "")
                        passwords.append(password)
            # 结合账号和密码
                if len(passwords) == 1:
                    passwords = passwords * len(accounts)
                credentials = [{"account": a, "password": p} for a, p in zip(accounts, passwords)]
                all_credentials.extend(credentials)
            else:
                print(f"Failed to retrieve the webpage from {url}")
    # print(all_credentials)
    return [
        {
            'account': account['account'],
            'password': account['password']
        }
        for account in all_credentials
        ]


if __name__ == "__main__":
    readme = root / "README.md"
    readme_contents = readme.open(encoding="utf-8").read()

    # 获取账号信息
    accounts = fetch_apple_count(urls)

    # 构建账号信息的Markdown格式
    entries_md = "\n".join([
        "* 账号：`{account}` \n * 密码：`{password}`".format(**account)
        for account in accounts
    ])

    # 更新账号信息
    rewritten = replace_chunk(readme_contents, "apple", entries_md)

    # 获取当前日期
    current_datetime = datetime.now()
    target_timezone = pytz.timezone('Asia/Shanghai')
    target_datetime = current_datetime.astimezone(target_timezone)
    entries_update_md = "\n".join([
        "更新时间：**{}**".format(target_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    ])

    # 更新日期信息
    rewritten_update = replace_chunk(rewritten, "updateTime", entries_update_md)

    # 写入全部更新
    readme.open("w", encoding="utf-8").write(rewritten_update)
