department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_Python = 1234.3456
End = 'The End!'

line1 = 'Department1 name:%-15sManager:%-15sCOURSE FEES:%-15.2f%-15s' % (department1,depart1_m,COURSE_FEES_SEC,End)
line2 = 'Department2 name:%-15sManager:%-15sCOURSE FEES:%-15.2f%-15s' % (department2,depart2_m,COURSE_FEES_Python,End)

# line1 = f'Department1 name:{department1:<15}Manager:{depart1_m:<15}COURSE FEES:{COURSE_FEES_SEC:<15.2f}{End:<15}'
# line2 = f'Department1 name:{department2:<15}Manager:{depart2_m:<15}COURSE FEES:{COURSE_FEES_Python:<15.2f}{End:<15}'

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)
