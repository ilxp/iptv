import requests
#url = 'https://raw.githubusercontent.com/yuanzl77/IPTV/refs/heads/main/live.m3u'  # 替换为你想下载的文件的URL
url = 'https://raw.githubusercontent.com/ilxp/YKTV/main/live.m3u'
local_filename = 'ipv6.m3u'  # 指定保存到本地的文件名
 
with requests.get(url, stream=True) as r:
    with open(local_filename, 'wb') as f:
        f.write(r.content)
 
 
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
        
        if 'IPV4' in lines[i]:
            skip_next = True  # 如果当前行包含'aaa'，标记跳过下一行
            continue
        
        new_lines.append(lines[i])  # 保留当前行

    # 将结果写回文件或另存为新文件
    with open(file_path, 'w') as file:
        file.writelines(new_lines)

# 使用示例
remove_lines_with_aaa('ipv6.m3u')
