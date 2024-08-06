import threading, multiprocessing, queue, logging, ImgProcess
import utils, RequestServer

logging.basicConfig(filename = "Logs/server.log",
                    filemode = 'a',
                    level = logging.INFO)
logging.basicConfig(filename = "Logs/server.log",
                    filemode = 'a',
                    level = logging.ERROR)


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
                modelType = data.get("type")
                imgList = data.get("imageData")
                curTime = utils.GetTime()
                logging.info(f"[{curTime}]开始检测")
                # 获取检测结果并发送到java后端
                for imgId in imgList:
                    imgUrl = "/www/wwwroot/gasSafe/data/officeImg/" + imgId + ".jpg"
                    result = ImgProcess.Detect(imgUrl, modelType)
                    curTime = utils.GetTime()
                    logging.info(f"[{curTime}]图片id = {imgId} 检测完成")
                    RequestServer.PushResult(result, modelType, imgId)


if __name__ == '__main__':
    dataQueue = queue.Queue()
    producer = Producer(dataQueue)
    consumer = Consumer(ThreadName = "consumerThread", DataQueue = dataQueue)
    consumer.start()
    data = {
        "type": "gasTank",
        "imageData": ["0"]
    }
    for i in range(10):
        producer.PutData(data)
