import re
str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
result = re.match(r'(\w+)\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})\s+\w+\s'
                  r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}),\s+\w+\s+(\d{1,2}):(\d{1,2}):(\d{1,2}),'
                  r'\s+\w+\s+(\d+),\s+\w+\s+(\w+)',str1).groups()
print('protocal       :'+result[0])
print('server         :'+result[1])
print('localserver    :'+result[2])
print('idle           :'+result[3]+'小时 '+result[4]+'分钟 '+result[5]+'秒')
print('bytes          :'+result[6])
print('flags          :'+result[7])