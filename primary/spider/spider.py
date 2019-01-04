from urllib import request
import re


class Spider():
    url = 'https://www.panda.tv/cate/lol'
    # root_pattern = '<div class="video-info">([\w\W]*?)</div>'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattert = '</i>([\s\S]*?)</span>'
    number_pattert = '<span class="video-number">([\s\S]*?)</span>'

    # 设为私有方法
    def __fetch__content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        # a = 1  # 此处打断点
        # print(htmls)
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattert, html)
            number = re.findall(Spider.number_pattert, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        # print(root_html[0])
        print(anchors[0])
        a = 1
        return anchors

    def __refine(self, anchors):
        l = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': re.sub('\D','',anchor['number'][0])
        }
        return map(l, anchors)

    def __sort(self, anchors):
        pass

    def go(self):
        htmls = self.__fetch__content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        print(anchors)


spider = Spider()
spider.go()

# gg = '<i class="ricon ricon-eye"></i>83'
# print(re.sub('\D', '',gg))
