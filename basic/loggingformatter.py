import logging
import logging.config
import csv

logging.config.fileConfig('logging.config')
logger = logging.getLogger()

line_counter = 0
data_header = []
employee = []
customer_usa_only_list = []
customer = line_counter

logger.info('Open file {0}'.format("TEST",))
try:
    with open("C:\\Users\\user\\atom-workspace\\customers.csv", "r") as customer_data:
        customer_reader = csv.reader(customer_Data, delimiter=',', quotechar='"')
        for customer in customer_reader:
            if customer[3].upper() == 'USA':
                logger.info('ID {0} added'.format(customer[0],))
                customer_usa_only_list.append(customer)


except FileFoundError as e:
    logger.error('File NOT found {0}'.format(e,))

logger.info('Write USQ only data at {0}'.format("customer_usa_only.csv",))
with open("customer_usa_only.csv", "w") as customer_usa_only_csv:
    for customer in customer_usa_only_list:
        customer_usa_only_csv.write(",".join(customer).strip('\n') + "\n")

logger.info('Program finished')
