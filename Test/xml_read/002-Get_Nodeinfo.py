from xml.dom import minidom

dom=minidom.parse('Class_info.xml')
root=dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)


# from xml.dom import minidom
# with open('Class_info.xml','r',encoding='utf8') as fh:
#      # parse()获取DOM对象
#      dom=minidom.parse(fh)
#      # 获取根节点
#      root=dom.docmentElment
#      # 节点名称
#      print(root.nodeName)
#      # 节点类型：'ELEMENT_NODE'，元素节点； 'TEXT_NODE'，文本节点； 'ATTRIBUTE_NODE'，属性节点
#      print(root.nodeType)
#      # 获取某个节点下所有子节点，是个列表
#      print(root.childNodes)