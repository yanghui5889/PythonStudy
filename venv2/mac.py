import re
str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
result = re.match('(\d+)\s+(\w+\.\w+\.\w+)\s(\w+)\s+(\w+\d/\d/\d)',str1).groups()
print('VLAN ID    ：'+result[0])
print('MAC        ：'+result[1])
print('Type       ：'+result[2])
print('Interface  ：'+result[3])