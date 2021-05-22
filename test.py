from datetime import datetime

# 显示当前时间
s = datetime.now()
print(s)  # 2021-05-22 16:52:05.982242

# 转化为timestamp
t = s.timestamp()
print(t)  # 1621673680.330086

# 再转回datetime
s2 = datetime.fromtimestamp(t)
print(s2)  # 2021-05-22 16:56:07.205572

# datetime格式化
fmt = '%Y-%m-%d %H:%M'
print(s.strftime(fmt))  # 2021-05-22 17:00
