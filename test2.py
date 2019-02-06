from fake_useragent import UserAgent
from urllib.request import urlopen , Request
import request


ua = UserAgent()
#print(ua.chrome)
hdr = {'User-Agent':str(ua.chrome)}
#print(hdr)
for i in range(285698,353000):

    url = Request('https://bugs.eclipse.org/bugs/show_activity.cgi?id='+str(i),headers=hdr)
    response = urlopen(url)
    webContent = response.read()

    f = open(str(i)+'.html', 'w', encoding='utf-8')
    f.write(webContent.decode())
    f.close


