from datetime import datetime


# ��ȡ��ǰʱ��
def GetTime():
    curTime = datetime.now()
    formatTime = curTime.strftime("%H:%M:%S")
    return str(formatTime)
