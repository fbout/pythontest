pages=2
print("hello")
def urls(num):
        for i in num.pages:
           url=num.bashurl+i*20
        return url
start_urls=urls(pages)

print(start_urls)