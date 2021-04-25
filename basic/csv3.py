import csv

# f = open("C:\\Users\\user\\atom-workspace\\customers.csv", "r")
# reader = csv.reader(
#     f, # 연결할 대상 파일 객체
#     delimiter=',', # 데이터를 분리하는 기준
#     quotechar='"', # 데이터를 묶을 때 사용하는 문자
#     quoting=csv.QUOTE_ALL # 데이터를 묶는 기준
# )

data = []
header = []
rownum = 0

# with open("C:\\Users\\user\\atom-workspace\\customers.csv", "r", encoding="cp949") as file:
#     csv_data = csv.reader(file)
#
#     for row in csv_data:
#         if rownum == 0:
#             header = row
#         location = row[7]


import logging

logging.debug("틀렸잖아")
logging.info("확인해")
logging.warning("조심해")
logging.error("에러 났어")
logging.critical("망했다.")


logger = logging.getLogger("main")
stream_hander = logging.StreamHandler()
logger.addHandler(stream_hander)
