import pymysql
import logging.config
import testProject.SocketServer
pymysql.install_as_MySQLdb()
logging.config.fileConfig('logging.conf')
