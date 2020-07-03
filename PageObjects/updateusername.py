#coding=utf8


class Updateusername:

    def updateusername_success(self,token):
        '''修改用户昵称'''
        url = "https://uat.cubeace.com/gameflaskapi/api/v1/user/updateUserName"
        h = {
            "Authorization": "Bearer "+"accessToken %s" % token
            }
        print(h)
        body = {
                 "newUserName": "1.22225"
             }

        r = self.post(url, json=body,headers=h)
        print(r.text)