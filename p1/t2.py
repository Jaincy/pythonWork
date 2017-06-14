import base64


class c1:
    def __init__(self):
        pass

    bb = "zz"

    def test1(self):
        print "test1"
        print self.bb


def dd():
    print "dd"


cc = c1()
cc.test1()
cc.test1 = dd
cc.test1()

cc = c1()
cc.test1()

b64data = open('base64data.txt').read()
img_data = b64data.decode('base64')
fw = open('img.jpg', 'wb')
fw.write(img_data)
fw.close()