# encoding=utf-8

class c1:
    bb = "bb"

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


