#import requests
##url = 'https://raw.githubusercontent.com/yuanzl77/IPTV/main/live.m3u'  # 替换为你想下载的文件的URL
#url = 'https://raw.githubusercontent.com/ilxp/YKTV/main/live.m3u'
#local_filename = 'ipv4.m3u'  # 指定保存到本地的文件名
#with requests.get(url, stream=True) as r:
    #with open(local_filename, 'wb') as f:
        #f.write(r.content)

# --------替换以下变量的值----
import requests
import base64
# 设置
username = 'ilxp'
token = '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'
#token = '${{ secrets.workflow_token }}'
repo = 'YKTV'
file_path = 'live.m3u?ref=main'
save_path = 'ipv4.m3u'  # 保存的本地文件路径
# GitHub API URL
url = f'https://api.github.com/repos/{username}/{repo}/contents/{file_path}'
# 发送请求
response = requests.get(url, auth=(username, token))
# 检查响应状态
if response.status_code == 200:
    content = response.json()
    # GitHub API 返回的内容是 Base64 编码的
    file_content = base64.b64decode(content['content']).decode('utf-8')   
    # 保存文件到指定路径
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(file_content)   
    print(f"文件已保存到 {save_path}")
else:
    print(f"错误: {response.status_code} - {response.json().get('message')}")
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
