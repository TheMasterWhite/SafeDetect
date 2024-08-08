import threading, multiprocessing, queue, logging, ImgProcess
import utils, RequestServer

logging.basicConfig(filename = "Logs/server.log",
                    filemode = 'a',
                    level = logging.INFO)
modelList = ["exhaustFan", "gasTank", "gasTee", "regulator"]  # 模型表
SafeTypeList = [0, 0, 5, 4]  # 隐患类型表


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
                # 对传入图片列表获取检测结果并发送到java后端
                for imgId in imgList:
                    cnt = -1  # 模型类型下标
                    # imgUrl = "https://masterwhite.oss-cn-guangzhou.aliyuncs.com/1657593135.jpg"
                    imgUrl = "/www/wwwroot/gasSafe/data/officeImg/" + imgId + ".jpg"

                    # 获取单张图片对所有模型的检测结果列表
                    resultList = ImgProcess.Detect(imgUrl)
                    curTime = utils.GetTime()
                    logging.info(f"[{curTime}]Image ID = {imgId} Detection completed")
                    # 对单张图片的所有结果发送到后端
                    for result in resultList:
                        # 获取参数
                        cnt += 1
                        type = modelList[cnt]
                        safeType = SafeTypeList[cnt]

                        if result == []:
                            RequestServer.PushNullResult(Type = type,
                                                         ImgId = imgId,
                                                         SafeType = safeType)
                        else:
                            RequestServer.PushResult(Result = result,
                                                     Type = type,
                                                     ImgId = imgId,
                                                     SafeType = safeType)


if __name__ == '__main__':
    dataQueue = queue.Queue()
    producer = Producer(dataQueue)
    consumer = Consumer(ThreadName = "Consumer", DataQueue = dataQueue)
    consumer.start()
    data = {
        "imageData": ["0"]
    }
    producer.PutData(data)
