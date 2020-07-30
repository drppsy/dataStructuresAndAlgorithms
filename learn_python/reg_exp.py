import re
res = {
    "code": 0,
    "data": {
        "head_img": "https://xd-video-pc-img.oss-cn-beijing.aliyuncs.com/xdclass_pro/default/head_img/1.jpeg",
        "name": "飞塔",
        "token": "xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly94ZC12aWRlby1wYy1pbWcub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tL3hkY2xhc3NfcHJvL2RlZmF1bHQvaGVhZF9pbWcvMS5qcGVnIiwiaWQiOjEyMDU0LCJuYW1lIjoi6aOe5aGUIiwiaWF0IjoxNTk2MTE4NzE3LCJleHAiOjE1OTY3MjM1MTd9.W7wg3DYWt27YOQyLyFw2v8KcpFedwqX8f8_QcNv98Sw"
    },
    "msg": 1
}
nameRegex = re.compile(r"'token':(.*?)}")
mo = nameRegex.search(str(res))
val = mo.group(1)
print(val)