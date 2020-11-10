import re
str1 = 'Port-channel1.189    192.168.189.254  Yes     CONFIG   up'
result = re.match(r'(\w\S+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+Yes\s+CONFIG\s+(\w+)',
                  str1.strip()).groups()

format_str = '{0:<10}:{1:<30}'
print(format_str.format('接口',result[0]))
print(format_str.format('IP地址',result[1]))
print(format_str.format('状态',result[2]))

# print('接口    :'+result[0])
# print('IP地址  :'+result[1])
# print('状态    :'+result[2])