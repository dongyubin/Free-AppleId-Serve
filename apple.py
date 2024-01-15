import requests
from bs4 import BeautifulSoup
import re
import pathlib
from datetime import datetime

root = pathlib.Path(__file__).parent.resolve()

def replace_chunk(content, marker, chunk, inline=False):
    r = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = "\n{}\n".format(chunk)
    chunk = "<!-- {} starts -->{}<!-- {} ends -->".format(marker, chunk, marker)
    return r.sub(chunk, content)

def fetch_apple_count():
    url = 'https://idshare001.me/Anode1.html'

    # 发起请求获取网页内容
    response = requests.get(url)
    accounts = []
    passwords = []
    # 检查请求是否成功
    if response.status_code == 200:
        html_doc = response.content
        # print(html_doc)
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(html_doc, 'html.parser')

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

        # 输出账号和密码
        if len(passwords) == 1:
            return [
                {
                    "account": account,
                    "passwords": passwords[0]
                }
                for account in accounts
            ]
            # for account in accounts:
            #     print(f"账号: {account}")
            # print(f"密码: {passwords[0]}")
        else:
            for i in range(min(len(accounts), len(passwords))):
                print(f"账号{i+1}: {accounts[i]}")
                print(f"密码{i+1}: {passwords[i]}")
    else:
        print("Failed to retrieve the webpage")


if __name__ == "__main__":
    readme = root / "README.md"
    readme_contents = readme.open(encoding="utf-8").read()
    accounts = fetch_apple_count()
    # print(accounts)
    # if not entries:
    #     entries = fetch_blog_entries()
    entries_md = "\n".join(
        [
            "* 账号：`{account}` \n * 密码：`{passwords}`".format(
                **account
            )
            for account in accounts
        ]
    )
    print(entries_md)
    rewritten = replace_chunk(readme_contents, "apple", entries_md)
    readme.open("w", encoding="utf-8").write(rewritten)
    # 获取当前日期
    current_date = datetime.now().date()
    entries_update_md = "\n".join(
        [
            "更新时间：**{current_date}**"
            .format(current_date=current_date)
        ]
    )
    
    # print("Number of entries:", len(entries_md))
    rewritten_update = replace_chunk(readme_contents, "updateTime", entries_update_md)
    readme.open("w", encoding="utf-8").write(rewritten_update)
