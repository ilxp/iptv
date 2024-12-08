#import requests
##url = 'https://raw.githubusercontent.com/yuanzl77/IPTV/main/live.m3u'  # 替换为你想下载的文件的URL
#url = 'https://raw.githubusercontent.com/ilxp/YKTV/main/live.m3u'
#local_filename = 'ipv4.m3u'  # 指定保存到本地的文件名
#with requests.get(url, stream=True) as r:
    #with open(local_filename, 'wb') as f:
        #f.write(r.content)

# --------替换以下变量的值----

#token = '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'
#token = '${{ secrets.PRIVATE_REPO }}

import requests
import os

# GitHub 个人访问令牌
token = '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'
# GitHub 仓库信息
owner = 'ilxp'
repo = 'YKTV'
branch = 'main'
file_path = 'live.m3u'

# 目标保存路径
save_to_path = 'ipv4.m3u'

# 创建 GitHub 文件 URL
url = f'https://api.github.com/repos/{owner}/{repo}/contents/{file_path}?ref={branch}'

# 设置请求头
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# 发送 GET 请求获取文件内容
response = requests.get(url, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    file_content = response.json()
    
    # 获取文件内容的 Base64 编码
    content = file_content['content']
    
    # 将 Base64 编码内容解码
    decoded_content = base64.b64decode(content).decode('utf-8')
    
    # 创建目标文件路径的目录
    os.makedirs(os.path.dirname(save_to_path), exist_ok=True)
    
    # 将内容写入本地文件
    with open(save_to_path, 'w') as file:
        file.write(decoded_content)
    
    print(f'File saved to {save_to_path}')
else:
    print(f'Failed to retrieve file: {response.status_code}')
    print(response.json())

# -------------------------------------------------


def remove_lines_with_aaa(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    # 创建一个新的列表用于保存要保留的行
    new_lines = []
    skip_next = False  # 标记是否跳过下一行

    for i in range(len(lines)):
        if skip_next:
            skip_next = False
            continue
        
        if 'IPV6' in lines[i]:
            skip_next = True  # 如果当前行包含'aaa'，标记跳过下一行
            continue
        
        new_lines.append(lines[i])  # 保留当前行

    # 将结果写回文件或另存为新文件
    with open(file_path, 'w') as file:
        file.writelines(new_lines)

# 使用示例
remove_lines_with_aaa('ipv4.m3u')
