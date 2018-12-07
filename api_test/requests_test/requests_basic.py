import requests
base_url='http://httpbin.org'

# r=requests.get(base_url+'/get')
# print(r.status_code)
#
# r=requests.post(base_url+'/post')
# print(r.status_code)
#
# r=requests.put(base_url+'/put')
# print(r.status_code)
#
# r=requests.delete(base_url+'/delete')
# print(r.status_code)

#参数传递get
# param_data={'user':'51zxw','passwd':'6666'}
# r=requests.get(base_url+'/get',params=param_data)
# print(r.status_code)
# print(r.url)

#参数传递post
# form_data={'user':'51zxw','passwd':'6666'}
# r=requests.post(base_url+'/post',data=form_data)
# print(r.text)

#请求头参数
form_data={'user':'51zxw','passwd':'6666'}
header={'user-agent':'Mozilla/8.0'}
r=requests.post(base_url+'/post',data=form_data,headers=header)
print(r.text)
