# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:05:05 2018

@author: peter

"""
import cv2
from pathlib import Path
import tornado.web
import tornado.ioloop



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/index.html')
    
    def post(self):
        text = self.get_body_argument("arg")
        self.redirect("/")
        
        file_name = Path(r"D:\projects\rosoft\rosoft\text.txt")
        with file_name.open('a+') as f:
            f.write(text+'\n')

def make_app():
    return tornado.web.Application([
            (r"/",MainHandler),
            #(r"/logs",LogHandler),
            ])

if __name__=="__main__":
   app = make_app()
   app.listen(8080)
   tornado.ioloop.IOLoop.current().start()
