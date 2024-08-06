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
        logging.info(f"[{curTime}]Task request enters the queue")


class Consumer(threading.Thread):
    def __init__(self, ThreadName, DataQueue):
        super().__init__()
        self.ThreadName = ThreadName
        self.DataQueue = DataQueue
        curTime = utils.GetTime()
        logging.info(f"[{curTime}]{self.ThreadName} Thread started successfully")


    def run(self):
        while True:
            if not self.DataQueue.empty():
                data = self.DataQueue.get()
                imgList = data.get("imageData")
                curTime = utils.GetTime()
                logging.info(f"[{curTime}]Start detection")
                # 获取检测结果并发送到java后端
                for imgId in imgList:
                    # imgUrl = "/www/wwwroot/gasSafe/data/officeImg/" + imgId + ".jpg"
                    imgUrl = "https://masterwhite.oss-cn-guangzhou.aliyuncs.com/1657593135.jpg"
                    result = ImgProcess.Detect(imgUrl)
                    curTime = utils.GetTime()
                    logging.info(f"[{curTime}]Image ID = {imgId} Detecting completed")
                    RequestServer.PushResult(result, "gasTank", imgId)


if __name__ == '__main__':
    dataQueue = queue.Queue()
    producer = Producer(dataQueue)
    consumer = Consumer(ThreadName = "consumerThread", DataQueue = dataQueue)
    consumer.start()
    data = {
        "imageData": ["0"]
    }
    producer.PutData(data)
