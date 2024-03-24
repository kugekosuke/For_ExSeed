class school:
    def __init__(self,name,english,math):#引数に必ずselfを入れる必要があります。
        self.name = name
        self.english = english
        self.math = math
    #メソッド↓
    def average(self):#メソッドではクラスが持っている情報をselfとして使用することができます。
        averagescore=(self.english+self.math)/2
        print(averagescore)
        return 0
    
    
tanaka = school("tanaka",70,80)
satou = school("satou",50,60)

student = [tanaka,satou]#オブジェクトをリスト変数に入れて、一括で処理する、なんてこともできるよ
for a in student:
    a.average()
    