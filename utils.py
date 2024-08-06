from datetime import datetime


# 获取当前时间
def GetTime():
    curTime = datetime.now()
    formatTime = curTime.strftime("%H:%M:%S")
    return str(formatTime)
