# -*- coding: utf-8 -*-

from weibo.weibo_login import wblogin
from weibo.weibo_sender import WeiboSender
from weibo.weibo_message import WeiboMessage
import urlparse, os, requests, random

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

__MAX_SIZE__ = 5*1024*1024

def weibo_api():
  (wei_session, uid) = wblogin()
  if uid is not None:
    wei_session.get('http://weibo.com/')
    return WeiboSender(wei_session, uid)
  return None

def tweet_multiple_image(urls, message):
    api = weibo_api()
    if not api:
        return
    api.send_weibo(WeiboMessage(message, urls))

def main():
  # -------------------------------------------------------------------------------
  url = "https://vbox-bucket-001.oss-cn-shanghai.aliyuncs.com/vbox/p0666ptf.jpg"
  message = "Nice three"
  tweet_multiple_image([url],message)
  ## -------------------------------------------------------------------------------
  # urls = [
  #   "http://forum1.sybiji.net/forum/5230/c4835217-f864-4d04-9913-0a8761d11df5.jpeg",
  #   "http://forum1.sybiji.net/forum/5230/74c953fd-3fd2-482c-9e6a-caffaf90baef.jpeg",
  #   "http://forum1.sybiji.net/forum/5230/bbaaa46b-f460-4628-b70d-3cd3eff88276.jpeg",
  #   "http://forum1.sybiji.net/forum/5230/d7ee52b4-8932-4f61-8515-1ef473dd27bb.jpeg",
  #   "http://forum1.sybiji.net/forum/5230/43e6158a-47d8-4610-840b-28b1008d97cc.jpeg",
  #   "http://forum1.sybiji.net/forum/5230/1e322cdb-f2ad-468b-831b-164231a34b2b.jpeg",
  #   "http://forum1.sybiji.net/forum/5230/e004d2ca-b1ab-4315-89db-2b389fb12efd.jpeg",
  #   "http://forum1.sybiji.net/forum/5230/a6cbf96b-886b-4449-a858-a2bf6b0cf939.jpeg",
  #   "http://forum1.sybiji.net/forum/5230/58d34e47-cd14-4f56-8c43-4cd3c471e14a.jpeg",
  #   "http://forum1.sybiji.net/forum/5230/cf7d23bc-32f1-46f5-9b74-b3e5841213d2.jpeg",
  # ]
  # message = 'many images!✨'
  # tweet_multiple_image(urls, message)
  ## -------------------------------------------------------------------------------
  # status = api.update_status(status=tweet) 
  pass

if __name__ == "__main__":
  main()