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
                print(result)
                logging.info(f"[{curTime}]result = {result}")


if __name__ == '__main__':
    dataQueue = queue.Queue()
    producer = Producer(dataQueue)
    url = 'http://localhost:8888/Detect'
    imageurl = ["https://masterwhite.oss-cn-guangzhou.aliyuncs.com/1657593135.jpg",
                "https://masterwhite.oss-cn-guangzhou.aliyuncs.com/1657593144.jpg"]
    data = {
        "requestId": "12345",
        "imageUrl": imageurl,
        "type": "gasTank"
    }
    producer.PutData(Data = data)
    consumer = Consumer(ThreadName = "consumerThread", DataQueue = dataQueue)
    consumer.start()

