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

def fetch_apple_account(sample_text):
    # 正则表达式匹配 pattern
    pattern = r"copy\('([^']+)'\)"

    # 使用 re.search() 查找匹配项
    match = re.search(pattern, sample_text)

    # 如果找到了匹配项，则输出
    if match:
        email_address = match.group(1)
        return email_address
    else:
        return ''

def fetch_apple_count(urls):
    # 存储所有网站的账号密码
    all_credentials = []
    # 发起请求获取网页内容
    headers = {
        'Content-Type': 'application/json',
        'Accept':'application/json, text/javascript, */*; q=0.01'
    }
    for url in urls:
        try:
        # print('url:',url)
        # if url.startswith('https://aunlock.laogoubi.net') or url.startswith('https://apple.laogoubi.net'):
            if 'laogou' in url :
                headers['Referer'] = url
                response = requests.get(url, headers=headers)
                res_text = response.text
                print(res_text)
                data = json.loads(res_text)
                credentials = []
                for item in data:
                    if 'username' in item and 'password' in item and item['status']==1:
                        credentials.append({"account": item['username'], "password": item['password'], "country": item['country']})
                all_credentials.extend(credentials)
            elif 'get_apple_id.php' in url:
                headers = {
                    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
                }
                credentials = []
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    try:
                        # 尝试解析 JSON 数据
                        data = response.json()
                        for item in data:
                            if 'apple_id' in item and 'apple_pwd' in item:
                                credentials.append({"account": item['apple_id'], "password": item['apple_pwd'], "country": ''})
                    except json.decoder.JSONDecodeError as e:
                        print(f"Error decoding JSON: {e}")
                all_credentials.extend(credentials)      
            elif url.startswith('https://apid.jcnf.xyz'):
                response = requests.get(url)
                accounts = []
                passwords = []
                if response.status_code == 200:
                    html_doc = response.content
                    # print(html_doc)
                    # 使用BeautifulSoup解析HTML
                    soup = BeautifulSoup(html_doc, 'html.parser')
                    button_account = soup.select_one('button.btn-primary')
                    button_password = soup.select_one('button.btn-success')
                    if button_account and button_password:
                        accounts.append(button_account['data-clipboard-text'])
                        passwords.append(button_password['data-clipboard-text'])
                credentials = [{"account": a, "password": p, "country": ''} for a, p in zip(accounts, passwords)]
                all_credentials.extend(credentials)
            elif url.startswith('https://eg.id888.one'):
                headers = {
                    'Content-Type':'text/html;charset=UTF-8'
                }
                response = requests.get(url, headers=headers, verify=False)
                accounts = []
                passwords = []
                if response.status_code == 200:
                    html_doc = response.content
                    # print(html_doc)
                    # 使用BeautifulSoup解析HTML
                    soup = BeautifulSoup(html_doc, 'html.parser')
                    buttons = soup.find_all('a', {'class': 'copyBtn'})
                    for button in buttons:
                        if '复制账号' in button.text:  
                            accounts.append(button.get('title'))
                        elif '复制密码' in button.text:
                            passwords.append(button.get('title'))
                credentials = [{"account": a, "password": p, "country": ''} for a, p in zip(accounts, passwords)]
                all_credentials.extend(credentials)
            elif url.startswith('https://w.jiesuo.link'):
                response = requests.get(url)
                credentials = []
                if response.status_code == 200:
                    html_doc = response.content
                    # print(html_doc)
                    # 使用BeautifulSoup解析HTML
                    soup = BeautifulSoup(html_doc, 'html.parser')
                    account_input = soup.select_one('input#email')
                    password_input = soup.select_one('input#pass')
                    if account_input and password_input:
                        account_value = account_input.get('value')
                        password_value = password_input.get('value')
                        credentials.append({"account": account_value, "password": password_value, "country": ''})
                all_credentials.extend(credentials)
            elif 'appleID2' in url:
                print(url)
                response = requests.get(url)
                accounts = []
                passwords = []
                account_normal_index = []
                if response.status_code == 200:
                    html_doc = response.content
                    soup = BeautifulSoup(html_doc, 'html.parser')
                    buttons = soup.find_all('button', {'class': 'btn-outline-secondary'})
                    # 账号状态:获取class为card-title
                    card_status = soup.find_all(class_='card-title')
                    # print(card_status)
                    # for i,card_statu in enumerate(card_status):
                    #     if '正常' in card_statu.get_text():
                    #         account_normal_index.append(i)
                    for button in buttons:
                        if '复制帐号' in button.text:
                            account = fetch_apple_account(button.get('onclick'))
                            accounts.append(account)
                        elif '复制密码' in button.text:
                            pwd = fetch_apple_account(button.get('onclick'))
                            passwords.append(pwd)
                credentials = [{"account": a, "password": p, "country": ''} for a, p in zip(accounts, passwords)]
                all_credentials.extend(credentials)
            else:
                response = requests.get(url)
                accounts = []
                passwords = []
                account_normal_index = []
                # 检查请求是否成功
                if response.status_code == 200:
                    html_doc = response.content
                    # print(html_doc)
                    # 使用BeautifulSoup解析HTML
                    soup = BeautifulSoup(html_doc, 'html.parser')
                    # print(url, html_doc , '\n')
                    # 找到对应的button元素
                    buttons = soup.find_all('button', {'class': 'btn-outline-secondary'})
                    # 账号状态:获取class为card-title
                    card_status = soup.find_all(class_='card-title')
                    # print(card_status)
                    for i,card_statu in enumerate(card_status):
                        if '正常' in card_statu.get_text():
                            account_normal_index.append(i)
                            # print(i)
                            # 遍历所有匹配的元素
                    for button in buttons:
                        # 获取onclick属性的值
                        onclick_value = button.get('onclick')
                        if '复制帐号' in button.text and '维护中' not in onclick_value:
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
                    for j in account_normal_index:
                        credentials = [{"account": a, "password": p, "country": ''} for a, p in zip([accounts[j]], [passwords[j]])]
                        all_credentials.extend(credentials)
                else:
                    print(f"Failed to retrieve the webpage from {url}")
        except Exception as e:
            print(f"An error occurred while processing {url}: {e}")
    print(all_credentials)
    return [
        {
            'account': account['account'],
            'password': account['password'],
            'country': account['country']
        }
        for account in all_credentials
        ]


if __name__ == "__main__":
    readme = root / "README.md"
    readme_contents = readme.open(encoding="utf-8").read()
    urls = urls.split(',')
    # print(urls)
    # 获取账号信息
    accounts = fetch_apple_count(urls)

    # 构建账号信息的Markdown格式
    entries_md = "\n".join([
        "\n--------- {i} ---------\n* {country}账号：`{account}`\n* 密码：`{password}`".format(i=i+1, **account)
        for i, account in enumerate(accounts)
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
