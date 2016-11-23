# import  urllib,re,http.cookiejar
 
# def httpRequest(url):
	# '''
	# @summary:22
	# '''
	# try:
		# ret=None
		# SockFile=None
		# request=urllib.request.Request(url)
		# request.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)')
		# request.add_header('Pragma','no-cache')
		# opener=urllib.request.build_opener()
		# SockFile=opener.open(request)
		# ret=SockFile.read()
	# finally:
		# if SockFile:
			# SockFile.close()
	# return ret
	
# f = open("163News.txt", "w+")
 
# m = re.findall(r"news\.163\.com/\d.+?html",httpRequest("http://www.163.com").decode('gb18030'),re.M)
# print(m)
def add(a, b):
    return a + b
