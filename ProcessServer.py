import threading, multiprocessing, queue, logging, ImgProcess
import utils

dataQueue = queue.Queue()
logging.basicConfig(filename = "Logs/server.log", level = logging.INFO)

class Producer:

    def __init__(self, DataQueue):
        self.DataQueue = DataQueue


    def PutData(self, Data):
        self.DataQueue.put(Data)
        curTime = utils.GetTime()
        logging.info(f"[{curTime}]任务请求进入队列")


class Consumer(threading.Thread):
    def __init__(self, ThreadName, DataQueue):
        super().__init__()
        self.ThreadName = ThreadName
        self.DataQueue = DataQueue
        curTime = utils.GetTime()
        logging.info(f"[{curTime}]{self.ThreadName} 线程启动成功")


    def run(self):
        while True:
            if not self.DataQueue.empty():
                data = self.DataQueue.get()
                requestId = data.get("requestId")
                curTime = utils.GetTime()
                logging.info(f"[{curTime}]requestId = {requestId} 开始检测")
                result = ImgProcess.Detect(data)
                print("result")


if __name__ == '__main__':
    dataQueue = queue.Queue()
    producer = Producer(dataQueue)
    data = {
        "requestId": "12345",
        "imageUrl": "https://masterwhite.oss-cn-guangzhou.aliyuncs.com/1657593144.jpg",
        "returnUrl": "12345",
        "type": "gasTank"
    }

    for i in range(10):
        producer.PutData(Data = data)

    consumer = Consumer(ThreadName = "consumerThread", DataQueue = dataQueue)
    consumer.start()
