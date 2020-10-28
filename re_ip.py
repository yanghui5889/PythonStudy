import re
str1 = 'Port-channel1.189    192.168.189.254  Yes     CONFIG   up'
result = re.match('(\w+.\w+.\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+Yes\s+CONFIG\s+(\w+)',str1).groups()
print('接口    :'+result[0])
print('IP地址  :'+result[1])
print('状态    :'+result[2])