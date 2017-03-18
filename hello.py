bashurl='https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start='
pages=20


for i in range(1,pages):
    url=bashurl+str(i*20)
    print(url)