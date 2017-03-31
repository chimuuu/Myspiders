# coding=utf-8

# 功能：Ajax与JS文件渲染出的页面图片抓取
# 数据库： MySQL

from requests.exceptions import RequestException
from multiprocessing import Pool
from  bs4 import BeautifulSoup
from urllib import urlencode
from hashlib import md5
from config import *
import MySQL-Python
import requests
import json
import re
import os

import json.decoder

def get_page_index(offset, keyword):
	data = {
		'offset': offset,
		'format': 'json',
		'keyword': keyword,
		'autoload':'true',
		'count': '20',
		'cur_tab': 3
	}
	url = 'http://www.toutiao.com/search_content/?' + urlencode(data)
	
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		print '请求索引页出错'
		return None
	
def parse_page_index(html):
	try:
		data = json.loads(html)
		if data and 'data' in data.keys():
			for item in data.get('data'):
				yield item.get('article_url')
	except :
		pass
		

def get_page_details(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		print '请求详情页出错'
		return None
	
def parse_page_details(html, url):
	soup = BeautifulSoup(html, 'lxml')
	title = soup.select('title')[0].get_text()
	print title
	images_pattern = re.compile('var gallery = (.*?);', re.S)
	result = re.search(images_pattern, html)
	if result:
		# print(result.group(1))
		data = json.loads(result.group(1))
		if data and 'sub_images' in data.keys():
			sub_images = data.get('sub_images')
			images = [item.get('url') for item in sub_images]
			for image in images:download_images(image)
			return{
				'title': title,
				'url': url,
				'images': images
			}

def download_images(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			save_images(response.content)
			print '正在下载图片', url
		return None
	except RequestException:
		print '请求图片出错'
		return None
			
def save_images(content):
	file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
	if not os.path.exists(file_path):
		with open(file_path, 'wb') as f:
			f.write(content)
			
	
def main(offset):
	html = get_page_index(offset, KEY_WORD)
	for url in parse_page_index(html):
		html = get_page_details(url)
		if html:
			result = parse_page_details(html, url)
			print result

if __name__ == '__main__':

	groups = [x * 20 for x in range(GROUP_START, GROUP_END + 1)]
	pool = Pool()
	pool.map(main, groups)





