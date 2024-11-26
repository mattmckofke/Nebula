def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))