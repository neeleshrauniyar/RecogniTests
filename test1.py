from selenium import webdriver
from logger import LogGen

driver= webdriver.Chrome()

driver.get("https://www.google.com/")

logger= LogGen.loggen()
logger.info("Open Website")