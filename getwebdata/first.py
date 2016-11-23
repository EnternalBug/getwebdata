import  urllib,re,http.cookiejar
def httpCrawler(url):
	'''
	@summary:11
	'''
	content=httpRequest(url)
	title=parseHtml(content)
	saveData(title)
def httpRequest(url):
	'''
	@summary:22
	'''
	try:
		ret=None
		SockFile=None
		request=urllib.request.Request(url)
		request.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)')
		#request.add_header('Pragma','no-cache')
		opener=urllib.request.build_opener()
		SockFile=opener.open(request)
		ret=SockFile.read()
	finally:
		if SockFile:
			SockFile.close()
	return ret
def parseHtml(html):
	'''@summary:33
	'''
	content=None
	pattern='<title>([^<]*?)</title>'
	html=html.decode('gb18030')
	temp=re.findall(pattern,html)
	if temp:
		content=temp[0]
	return content
def saveData(data):
	'''@summary:44'''
	f=open('test','w')
	f.write(data)
	f.close()
if __name__=='__main__':
	url='http://splash.vsatauth.com/vsat/'
	httpCrawler(url)