import logging

logger = logging.getLogger('project')
syslog = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s', datefmt='%H:%M:%S')
syslog.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(syslog)

logger.info('Finished setting up logging!')
