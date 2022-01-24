from logging import error
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

null = None


class HomeAll(Resource):
    def get(self):
        return {
            "data": [
                {
                    "header": [
                        {
                            "left": {
                                "tittle": "Meranda",
                                "url": "https://preview.colorlib.com/theme/meranda/index.html"
                            }
                        },
                        {
                            "right": [
                                {
                                    "icon": "icon-facebook",
                                    "url": "https://preview.colorlib.com/theme/meranda/#"
                                },
                                {
                                    "icon": "icon-twitter",
                                    "url": "https://preview.colorlib.com/theme/meranda/#"
                                },
                                {
                                    "icon": "icon-instagram",
                                    "url": "https://preview.colorlib.com/theme/meranda/#"
                                },
                                {
                                    "placeholder": "Search..."
                                },
                                {
                                    "icon": "icon-search"
                                }
                            ]
                        }
                    ]
                },
                {
                    "text": "HOME",
                    "url": "https://preview.colorlib.com/theme/meranda/index.html",
                    "body": [
                        {
                            "sliderbar": [
                                {
                                    "image": "https://preview.colorlib.com/theme/meranda/images/xbig_img_1.jpg.pagespeed.ic.K2N7KNYATl.webp",
                                    "category": "Editor's pick",
                                    "text": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate vero obcaecati natus adipisci necessitatibus eius, enim vel sit ad reiciendis. Enim praesentium magni delectus cum, tempore deserunt aliquid quaerat culpa nemo veritatis, iste adipisci excepturi consectetur doloribus aliquam accusantium beatae?",
                                    "author": "Dave Rogers",
                                    "type": "Food",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "image": "https://preview.colorlib.com/theme/meranda/images/xbig_img_1.jpg.pagespeed.ic.K2N7KNYATl.webp",
                                    "category": "Editor's pick",
                                    "text": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate vero obcaecati natus adipisci necessitatibus eius, enim vel sit ad reiciendis. Enim praesentium magni delectus cum, tempore deserunt aliquid quaerat culpa nemo veritatis, iste adipisci excepturi consectetur doloribus aliquam accusantium beatae?",
                                    "author": "Dave Rogers",
                                    "type": "Food",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                }
                            ]
                        },
                        {
                            "Site Section1": [
                                {
                                    "text": "Editor's Pick",
                                    "content": [
                                        {
                                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_1.jpg.pagespeed.ic.IUFbLUay1G.webp",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_1.jpg.pagespeed.ic.Gl8yKkRUpG.webp",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_2.jpg.pagespeed.ic.LvRqrfFXI1.webp",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_3.jpg.pagespeed.ic._k9cdXbyH3.webp",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        }
                                    ]
                                },
                                {
                                    "text": "trending",
                                    "content": [
                                        {
                                            "Id": "01",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "Id": "02",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "Id": "03",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "Id": "04",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "text": "See All Trends",
                                            "icon": "icon-keyboard_arrow_right",
                                            "url": "https://preview.colorlib.com/theme/meranda/#"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "container": {
                                "image": "https://preview.colorlib.com/theme/meranda/images/xbig_img_1.jpg.pagespeed.ic.K2N7KNYATl.webp",
                                "category": "Editor's pick",
                                "text": "News Needs to Meet Its Audiences Where They Are",
                                "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate vero obcaecati natus adipisci necessitatibus eius, enim vel sit ad reiciendis. Enim praesentium magni delectus cum, tempore deserunt aliquid quaerat culpa nemo veritatis, iste adipisci excepturi consectetur doloribus aliquam accusantium beatae?",
                                "author": "Dave Rogers",
                                "type": "Food",
                                "date": "Jun 14",
                                "read": "3 min read",
                                "icon": "star"
                            }
                        },
                        {
                            "Site Section2": [
                                {
                                    "text": "Politics",
                                    "content": [
                                        {
                                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_1.jpg.pagespeed.ic.Gl8yKkRUpG.webp",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_2.jpg.pagespeed.ic.LvRqrfFXI1.webp",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_3.jpg.pagespeed.ic._k9cdXbyH3.webp",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        }
                                    ]
                                },
                                {
                                    "text": "Business",
                                    "content": [
                                        {
                                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_1.jpg.pagespeed.ic.Gl8yKkRUpG.webp",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_2.jpg.pagespeed.ic.LvRqrfFXI1.webp",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_3.jpg.pagespeed.ic._k9cdXbyH3.webp",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "Site Content3": [
                                {
                                    "text": "Recent News",
                                    "content": [
                                        {
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_4.jpg.pagespeed.ic.peEd0nw2Ox.webp",
                                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_3.jpg.pagespeed.ic.YQVX6P0g2G.webp",
                                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_3.jpg.pagespeed.ic.YQVX6P0g2G.webp",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "pagination": [
                                                {
                                                    "page": "1",
                                                    "url": "https://preview.colorlib.com/theme/meranda/index.html"
                                                },
                                                {
                                                    "page": "2",
                                                    "url": "https://preview.colorlib.com/theme/meranda/index.html"
                                                },
                                                {
                                                    "page": "3",
                                                    "url": "https://preview.colorlib.com/theme/meranda/index.html"
                                                },
                                                {
                                                    "page": "4",
                                                    "url": "https://preview.colorlib.com/theme/meranda/index.html"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "text": "Popular Post",
                                    "content": [
                                        {
                                            "Id": "01",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "Id": "02",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "Id": "03",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "Id": "04",
                                            "text": "News Needs to Meet Its Audiences Where They Are",
                                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                            "author": "Dave Rogers",
                                            "type": "News",
                                            "date": "Jun 14",
                                            "read": "3 min read",
                                            "icon": "star"
                                        },
                                        {
                                            "text": "See All Trends",
                                            "icon": "icon-keyboard_arrow_right",
                                            "url": "https://preview.colorlib.com/theme/meranda/#"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "footer": [
                        {
                            "top": [
                                {
                                    "tittle": "Newslater Subcribe",
                                    "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Perferendis aspernatur ut at quae omnis pariatur obcaecati possimus nisi ea iste!"
                                },
                                {
                                    "placeholder": "Enter your email"
                                },
                                {
                                    "icon": "icon-paper-plane"
                                }
                            ]
                        },
                        {
                            "bottom": {
                                "text": "Copyright ©2022 All rights reserved | This template is made with",
                                "icon": "icon-heart",
                                "by": "colorlib"
                            }
                        }
                    ]
                }
            ]
        }


class Home_slider(Resource):
    def get(self):
        return {
            "data": [
                {
                    "sliderbar": [
                        {
                            "image": "https://preview.colorlib.com/theme/meranda/images/xbig_img_1.jpg.pagespeed.ic.K2N7KNYATl.webp",
                            "category": "Editor's pick",
                            "text": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate vero obcaecati natus adipisci necessitatibus eius, enim vel sit ad reiciendis. Enim praesentium magni delectus cum, tempore deserunt aliquid quaerat culpa nemo veritatis, iste adipisci excepturi consectetur doloribus aliquam accusantium beatae?",
                            "author": "Dave Rogers",
                            "type": "Food",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "image": "https://preview.colorlib.com/theme/meranda/images/xbig_img_1.jpg.pagespeed.ic.K2N7KNYATl.webp",
                            "category": "Editor's pick",
                            "text": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate vero obcaecati natus adipisci necessitatibus eius, enim vel sit ad reiciendis. Enim praesentium magni delectus cum, tempore deserunt aliquid quaerat culpa nemo veritatis, iste adipisci excepturi consectetur doloribus aliquam accusantium beatae?",
                            "author": "Dave Rogers",
                            "type": "Food",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        }
                    ]
                }
            ]
        }


class Home_EditorsPick(Resource):
    def get(self):
        return {
            "data": [
               {
                   "text": "Editor's Pick",
                   "content": [
                       {
                           "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_1.jpg.pagespeed.ic.IUFbLUay1G.webp",
                           "text": "News Needs to Meet Its Audiences Where They Are",
                           "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                           "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                           "author": "Dave Rogers",
                           "type": "News",
                           "date": "Jun 14",
                           "read": "3 min read",
                           "icon": "star"
                       },
                       {
                           "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_1.jpg.pagespeed.ic.Gl8yKkRUpG.webp",
                           "text": "News Needs to Meet Its Audiences Where They Are",
                           "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                           "author": "Dave Rogers",
                           "type": "News",
                           "date": "Jun 14",
                           "read": "3 min read",
                           "icon": "star"
                       },
                       {
                           "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_2.jpg.pagespeed.ic.LvRqrfFXI1.webp",
                           "text": "News Needs to Meet Its Audiences Where They Are",
                           "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                           "author": "Dave Rogers",
                           "type": "News",
                           "date": "Jun 14",
                           "read": "3 min read",
                           "icon": "star"
                       },
                       {
                           "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_3.jpg.pagespeed.ic._k9cdXbyH3.webp",
                           "text": "News Needs to Meet Its Audiences Where They Are",
                           "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                           "author": "Dave Rogers",
                           "type": "News",
                           "date": "Jun 14",
                           "read": "3 min read",
                           "icon": "star"
                       }
                   ]
               }
            ]
        }


class Home_trending(Resource):
    def get(self):
        return {
            "data": [
                {
                    "Body": [
                        {
                            "text": "trending",
                            "content": [
                                {
                                    "Id": "01",
                                    "text": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "Id": "02",
                                    "text": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "Id": "03",
                                    "text": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "Id": "04",
                                    "text": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "text": "See All Trends",
                                    "icon": "icon-keyboard_arrow_right",
                                    "url": "https://preview.colorlib.com/theme/meranda/#"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class Home_banner(Resource):
    def get(self):
        return {
            "data": [
                {
                    "banner": {
                        "image": "https://preview.colorlib.com/theme/meranda/images/xbig_img_1.jpg.pagespeed.ic.K2N7KNYATl.webp",
                        "category": "Editor's pick",
                        "text": "News Needs to Meet Its Audiences Where They Are",
                        "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                        "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate vero obcaecati natus adipisci necessitatibus eius, enim vel sit ad reiciendis. Enim praesentium magni delectus cum, tempore deserunt aliquid quaerat culpa nemo veritatis, iste adipisci excepturi consectetur doloribus aliquam accusantium beatae?",
                        "author": "Dave Rogers",
                        "type": "Food",
                        "date": "Jun 14",
                        "read": "3 min read",
                        "icon": "star"
                    }
                }
            ]
        }


class Home_politics(Resource):
    def get(self):
        return {
            "data": [
                {
                    "text": "Politics",
                    "content": [
                            {
                                "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_1.jpg.pagespeed.ic.Gl8yKkRUpG.webp",
                                "text": "News Needs to Meet Its Audiences Where They Are",
                                "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                "author": "Dave Rogers",
                                "type": "News",
                                "date": "Jun 14",
                                "read": "3 min read",
                                "icon": "star"
                            },
                        {
                                "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_2.jpg.pagespeed.ic.LvRqrfFXI1.webp",
                                "text": "News Needs to Meet Its Audiences Where They Are",
                                "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                "author": "Dave Rogers",
                                "type": "News",
                                "date": "Jun 14",
                                "read": "3 min read",
                                "icon": "star"
                            },
                        {
                                "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_3.jpg.pagespeed.ic._k9cdXbyH3.webp",
                                "text": "News Needs to Meet Its Audiences Where They Are",
                                "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                "author": "Dave Rogers",
                                "type": "News",
                                "date": "Jun 14",
                                "read": "3 min read",
                                "icon": "star"
                            }
                    ]
                }
            ]
        }


class Home_business(Resource):
    def get(self):
        return {
            "data": [
                {
                    "text": "Business",
                    "content": [
                            {
                                "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_1.jpg.pagespeed.ic.Gl8yKkRUpG.webp",
                                "text": "News Needs to Meet Its Audiences Where They Are",
                                "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                "author": "Dave Rogers",
                                "type": "News",
                                "date": "Jun 14",
                                "read": "3 min read",
                                "icon": "star"
                            },
                        {
                                "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_2.jpg.pagespeed.ic.LvRqrfFXI1.webp",
                                "text": "News Needs to Meet Its Audiences Where They Are",
                                "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                "author": "Dave Rogers",
                                "type": "News",
                                "date": "Jun 14",
                                "read": "3 min read",
                                "icon": "star"
                            },
                        {
                                "image": "https://preview.colorlib.com/theme/meranda/images/ximg_v_3.jpg.pagespeed.ic._k9cdXbyH3.webp",
                                "text": "News Needs to Meet Its Audiences Where They Are",
                                "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                "author": "Dave Rogers",
                                "type": "News",
                                "date": "Jun 14",
                                "read": "3 min read",
                                "icon": "star"
                            }
                    ]
                }
            ]
        }


class Home_Recentnews(Resource):
    def get(self):
        return {
            "data": {
                "text": "Recent News",
                "content": [
                    {
                        "text": "News Needs to Meet Its Audiences Where They Are",
                        "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                        "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_4.jpg.pagespeed.ic.peEd0nw2Ox.webp",
                        "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                        "author": "Dave Rogers",
                        "type": "News",
                        "date": "Jun 14",
                        "read": "3 min read",
                        "icon": "star"
                    },
                    {
                        "text": "News Needs to Meet Its Audiences Where They Are",
                        "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                        "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_3.jpg.pagespeed.ic.YQVX6P0g2G.webp",
                        "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                        "author": "Dave Rogers",
                        "type": "News",
                        "date": "Jun 14",
                        "read": "3 min read",
                        "icon": "star"
                    },
                    {
                        "text": "News Needs to Meet Its Audiences Where They Are",
                        "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                        "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_3.jpg.pagespeed.ic.YQVX6P0g2G.webp",
                        "author": "Dave Rogers",
                        "type": "News",
                        "date": "Jun 14",
                        "read": "3 min read",
                        "icon": "star"
                    },
                    {
                        "pagination": [
                            {
                                "page": "1",
                                "url": "https://preview.colorlib.com/theme/meranda/index.html"
                            },
                            {
                                "page": "2",
                                "url": "https://preview.colorlib.com/theme/meranda/index.html"
                            },
                            {
                                "page": "3",
                                "url": "https://preview.colorlib.com/theme/meranda/index.html"
                            },
                            {
                                "page": "4",
                                "url": "https://preview.colorlib.com/theme/meranda/index.html"
                            }
                        ]
                    }
                ]
            }
        }

class Home_popular(Resource):
    def get(self):
        return {
            "data" :[
                {
                    "text": "Popular Post",
                    "content": [
                        {
                            "Id": "01",
                            "text": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "Id": "02",
                            "text": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "Id": "03",
                            "text": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "Id": "04",
                            "text": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "text": "See All Trends",
                            "icon": "icon-keyboard_arrow_right",
                            "url": "https://preview.colorlib.com/theme/meranda/#"
                        }
                    ]
                }
            ]
        }

class Categories(Resource):
    def get(self):
        return {
            "data" :{
                "text": "CATEGORIES",
                "url": "https://preview.colorlib.com/theme/meranda/categories.html",
                "body": [
                    {
                        "leftsection": {
                            "caption": "categories",
                            "section-tittle": "Politics",
                            "content": [
                                {
                                    "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_4.jpg.pagespeed.ic.peEd0nw2Ox.webp",
                                    "tittle": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_3.jpg.pagespeed.ic.YQVX6P0g2G.webp",
                                    "tittle": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_1.jpg.pagespeed.ic.IUFbLUay1G.webp",
                                    "tittle": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_4.jpg.pagespeed.ic.peEd0nw2Ox.webp",
                                    "tittle": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_3.jpg.pagespeed.ic.YQVX6P0g2G.webp",
                                    "tittle": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_1.jpg.pagespeed.ic.IUFbLUay1G.webp",
                                    "tittle": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_4.jpg.pagespeed.ic.peEd0nw2Ox.webp",
                                    "tittle": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_3.jpg.pagespeed.ic.YQVX6P0g2G.webp",
                                    "tittle": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_1.jpg.pagespeed.ic.IUFbLUay1G.webp",
                                    "tittle": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "pagination": [
                                        {
                                            "Id": "1",
                                            "url": "https://preview.colorlib.com/theme/meranda/categories.html#"
                                        },
                                        {
                                            "Id": "2",
                                            "url": "https://preview.colorlib.com/theme/meranda/categories.html#"
                                        },
                                        {
                                            "Id": "3",
                                            "url": "https://preview.colorlib.com/theme/meranda/categories.html#"
                                        },
                                        {
                                            "Id": "4",
                                            "url": "https://preview.colorlib.com/theme/meranda/categories.html#"
                                        }
                                    ]
                                }
                            ]
                        }
                    },
                    {
                        "rightsection": {
                            "section-tittle": "Popular Post",
                            "content": [
                                {
                                    "Id": "01",
                                    "text": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "Id": "02",
                                    "text": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "Id": "03",
                                    "text": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "Id": "04",
                                    "text": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "text": "See All Trends",
                                    "icon": "icon-keyboard_arrow_right",
                                    "url": "https://preview.colorlib.com/theme/meranda/categories.html#"
                                }
                            ]
                        }
                    }
                ]
            }
        }

class Categories_Politics(Resource):
    def get(self):
        return {
            "data" : {
                "leftsection": {
                    "caption": "categories",
                    "section-tittle": "Politics",
                    "content": [
                        {
                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_4.jpg.pagespeed.ic.peEd0nw2Ox.webp",
                            "tittle": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_3.jpg.pagespeed.ic.YQVX6P0g2G.webp",
                            "tittle": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_1.jpg.pagespeed.ic.IUFbLUay1G.webp",
                            "tittle": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_4.jpg.pagespeed.ic.peEd0nw2Ox.webp",
                            "tittle": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_3.jpg.pagespeed.ic.YQVX6P0g2G.webp",
                            "tittle": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_1.jpg.pagespeed.ic.IUFbLUay1G.webp",
                            "tittle": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_4.jpg.pagespeed.ic.peEd0nw2Ox.webp",
                            "tittle": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_3.jpg.pagespeed.ic.YQVX6P0g2G.webp",
                            "tittle": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "image": "https://preview.colorlib.com/theme/meranda/images/ximg_h_1.jpg.pagespeed.ic.IUFbLUay1G.webp",
                            "tittle": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "isi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi temporibus praesentium neque, voluptatum quam quibusdam.",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "pagination": [
                                {
                                    "Id": "1",
                                    "url": "https://preview.colorlib.com/theme/meranda/categories.html#"
                                },
                                {
                                    "Id": "2",
                                    "url": "https://preview.colorlib.com/theme/meranda/categories.html#"
                                },
                                {
                                    "Id": "3",
                                    "url": "https://preview.colorlib.com/theme/meranda/categories.html#"
                                },
                                {
                                    "Id": "4",
                                    "url": "https://preview.colorlib.com/theme/meranda/categories.html#"
                                }
                            ]
                        }
                    ]
                }
            }
        }

class Categories_Popularpost(Resource):
    def get(self):
        return {
            "data" : {
                "rightsection": {
                    "section-tittle": "Popular Post",
                    "content": [
                        {
                            "Id": "01",
                            "text": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "Id": "02",
                            "text": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "Id": "03",
                            "text": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "Id": "04",
                            "text": "News Needs to Meet Its Audiences Where They Are",
                            "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                            "author": "Dave Rogers",
                            "type": "News",
                            "date": "Jun 14",
                            "read": "3 min read",
                            "icon": "star"
                        },
                        {
                            "text": "See All Trends",
                            "icon": "icon-keyboard_arrow_right",
                            "url": "https://preview.colorlib.com/theme/meranda/categories.html#"
                        }
                    ]
                }
            }
        }

class SingleContent(Resource):
    def get(self):
        return {
            "data" : {
                "single-content" : [
                    {
                        "left" : [
                            {
                                "article" : {
                                "img" : "https://preview.colorlib.com/theme/meranda/images/xbig_img_1.jpg.pagespeed.ic.K2N7KNYATl.webp",
                                "tittle" : "News Needs to Meet Its Audiences Where They Are",
                                "profil-pic" : "https://preview.colorlib.com/theme/meranda/images/xperson_1.jpg.pagespeed.ic.Pkude8qe6Y.webp",
                                "author" :"Dave Rogers",
                                "category" : "News",
                                "date" : "Jun 14",
                                "read" :"3 min read",
                                "isi" :"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate vero obcaecati natus adipisci necessitatibus eius, enim vel sit ad reiciendis. Enim praesentium magni delectus cum, tempore deserunt aliquid quaerat culpa nemo veritatis, iste adipisci excepturi consectetur doloribus aliquam accusantium beatae?"
                            }
                            },
                            {
                                "sugestion" :[
                                {
                                    "categories" : [
                                        {
                                            "text" : "desaign",
                                            "url" : "https://preview.colorlib.com/theme/meranda/blog-single.html?#"
                                        },
                                        {
                                            "text" : "Events",
                                            "url" : "https://preview.colorlib.com/theme/meranda/blog-single.html?#"
                                        }
                                    ]
                                },
                                {
                                    "tags" :[
                                        {
                                            "text" : "#html",
                                            "url" : "https://preview.colorlib.com/theme/meranda/blog-single.html?#"
                                        },
                                        {
                                            "text" : "#trends",
                                            "url" : "https://preview.colorlib.com/theme/meranda/blog-single.html?#"
                                        }
                                    ]
                                }
                                ]
                            },
                            {
                                "comments" : [
                                {
                                    "section-tittle" : {
                                        "text" : "6 comment"
                                    }
                                },
                                {
                                    "comment-list" : [
                                        {
                                            "pic-bio" : "https://preview.colorlib.com/theme/meranda/images/xperson_1.jpg.pagespeed.ic.Pkude8qe6Y.webp",
                                            "name" : "Jean Doe",
                                            "date" : "January 9, 2018 at 2:21pm",
                                            "comment" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?",
                                            "button" : "reply"
                                        },
                                        {
                                            "pic-bio" : "https://preview.colorlib.com/theme/meranda/images/xperson_1.jpg.pagespeed.ic.Pkude8qe6Y.webp",
                                            "name" : "Jean Doe",
                                            "date" : "January 9, 2018 at 2:21pm",
                                            "comment" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?",
                                            "reply" : {
                                                "pic-bio" : "https://preview.colorlib.com/theme/meranda/images/xperson_1.jpg.pagespeed.ic.Pkude8qe6Y.webp",
                                                "name" : "Jean Doe",
                                                "date" : "January 9, 2018 at 2:21pm",
                                                "comment" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?",
                                                "reply" : {
                                                    "pic-bio" : "https://preview.colorlib.com/theme/meranda/images/xperson_1.jpg.pagespeed.ic.Pkude8qe6Y.webp",
                                                    "name" : "Jean Doe",
                                                    "date" : "January 9, 2018 at 2:21pm",
                                                    "comment" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?",
                                                    "reply" : {
                                                        "pic-bio" : "https://preview.colorlib.com/theme/meranda/images/xperson_1.jpg.pagespeed.ic.Pkude8qe6Y.webp",
                                                        "name" : "Jean Doe",
                                                        "date" : "January 9, 2018 at 2:21pm",
                                                        "comment" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?",
                                                        "text" : "reply"
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "pic-bio" : "https://preview.colorlib.com/theme/meranda/images/xperson_1.jpg.pagespeed.ic.Pkude8qe6Y.webp",
                                            "name" : "Jean Doe",
                                            "date" : "January 9, 2018 at 2:21pm",
                                            "comment" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?",
                                            "button" : "reply"
                                        }
                                    ]
                                },
                                {
                                    "comment-form" : [
                                        {
                                            "tittle": "Leave Comment"
                                        },
                                        {
                                            "form-group" : [
                                                {
                                                    "text" : "Name*"
                                                },
                                                {
                                                    "text" : "Email**"
                                                },
                                                {
                                                    "text" : "Website*"
                                                },
                                                {
                                                    "text" : "Message*"
                                                },
                                                {
                                                    "button" : "POST COMMENT"
                                                }
                                            ]
                                        }                                
                                    ]
                                }
                            ]
                            }
                            
                        ]
                    },
                    {
                        "right" : {
                            "text": "Popular Post",
                            "content": [
                                {
                                    "Id": "01",
                                    "text": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "Id": "02",
                                    "text": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "Id": "03",
                                    "text": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "Id": "04",
                                    "text": "News Needs to Meet Its Audiences Where They Are",
                                    "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                                    "author": "Dave Rogers",
                                    "type": "News",
                                    "date": "Jun 14",
                                    "read": "3 min read",
                                    "icon": "star"
                                },
                                {
                                    "text": "See All Trends",
                                    "icon": "icon-keyboard_arrow_right",
                                    "url": "https://preview.colorlib.com/theme/meranda/#"
                                }
                            ]                        
                        }
                    }
                ]  
            }
        }

class SingleContent_article(Resource):
    def get(self):
        return {
            "data" : {
                "article" : {
                    "img" : "https://preview.colorlib.com/theme/meranda/images/xbig_img_1.jpg.pagespeed.ic.K2N7KNYATl.webp",
                    "tittle" : "News Needs to Meet Its Audiences Where They Are",
                    "profil-pic" : "https://preview.colorlib.com/theme/meranda/images/xperson_1.jpg.pagespeed.ic.Pkude8qe6Y.webp",
                    "author" :"Dave Rogers",
                    "category" : "News",
                    "date" : "Jun 14",
                    "read" :"3 min read",
                    "isi" :"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate vero obcaecati natus adipisci necessitatibus eius, enim vel sit ad reiciendis. Enim praesentium magni delectus cum, tempore deserunt aliquid quaerat culpa nemo veritatis, iste adipisci excepturi consectetur doloribus aliquam accusantium beatae?"
              }
            }
        }

class SingleContent_sugestion(Resource):
    def get(self):
        return {
            "data" : {
                "sugestion" :[
                    {
                        "categories" : [
                            {
                                "text" : "desaign",
                                "url" : "https://preview.colorlib.com/theme/meranda/blog-single.html?#"
                            },
                            {
                                "text" : "Events",
                                "url" : "https://preview.colorlib.com/theme/meranda/blog-single.html?#"
                            }
                        ]
                    },
                    {
                        "tags" :[
                            {
                                "text" : "#html",
                                "url" : "https://preview.colorlib.com/theme/meranda/blog-single.html?#"
                            },
                            {
                                "text" : "#trends",
                                "url" : "https://preview.colorlib.com/theme/meranda/blog-single.html?#"
                            }
                        ]
                    }
                ]
            }
        }

class SingleContent_Comment(Resource):
    def get(self):
        return {
            "data" : {
                "comments" : [
                    {
                        "section-tittle" : {
                        "text" : "6 comment"
                        }
                    },
                    {
                        "comment-list" : [                            
                            {
                                "pic-bio" : "https://preview.colorlib.com/theme/meranda/images/xperson_1.jpg.pagespeed.ic.Pkude8qe6Y.webp",
                                "name" : "Jean Doe",
                                "date" : "January 9, 2018 at 2:21pm",
                                "comment" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?",
                                "button" : "reply"
                            },
                            {
                                "pic-bio" : "https://preview.colorlib.com/theme/meranda/images/xperson_1.jpg.pagespeed.ic.Pkude8qe6Y.webp",
                                "name" : "Jean Doe",
                                "date" : "January 9, 2018 at 2:21pm",
                                "comment" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?",
                                "reply" : {
                                    "pic-bio" : "https://preview.colorlib.com/theme/meranda/images/xperson_1.jpg.pagespeed.ic.Pkude8qe6Y.webp",
                                    "name" : "Jean Doe",
                                    "date" : "January 9, 2018 at 2:21pm",
                                    "comment" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?",
                                    "reply" : {
                                        "pic-bio" : "https://preview.colorlib.com/theme/meranda/images/xperson_1.jpg.pagespeed.ic.Pkude8qe6Y.webp",
                                        "name" : "Jean Doe",
                                        "date" : "January 9, 2018 at 2:21pm",
                                        "comment" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?",
                                        "reply" : {
                                            "pic-bio" : "https://preview.colorlib.com/theme/meranda/images/xperson_1.jpg.pagespeed.ic.Pkude8qe6Y.webp",
                                            "name" : "Jean Doe",
                                            "date" : "January 9, 2018 at 2:21pm",
                                            "comment" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?",
                                            "text" : "reply"
                                        }
                                    }
                                }
                            },
                            {
                                "pic-bio" : "https://preview.colorlib.com/theme/meranda/images/xperson_1.jpg.pagespeed.ic.Pkude8qe6Y.webp",
                                "name" : "Jean Doe",
                                "date" : "January 9, 2018 at 2:21pm",
                                "comment" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?",
                                "button" : "reply"
                            }
                        ]
                    },
                    {
                        "comment-form" : [
                            {
                                "tittle": "Leave Comment"
                            },
                            {
                                "form-group" : [
                                    {
                                      "text" : "Name*"
                                    },
                                    {
                                      "text" : "Email**"
                                    },
                                    {
                                        "text" : "Website*"
                                    },
                                    {
                                        "text" : "Message*"
                                    },
                                    {
                                        "button" : "POST COMMENT"
                                    }
                                ]
                            }                                
                        ]
                    }
                ]
            }
        }

class SingleContent_Popularpost(Resource):
    def get(self):
        return {
            "data" : {
                  "text": "Popular Post",
                  "content": [
                    {
                        "Id": "01",
                        "text": "News Needs to Meet Its Audiences Where They Are",
                        "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                        "author": "Dave Rogers",
                        "type": "News",
                        "date": "Jun 14",
                        "read": "3 min read",
                        "icon": "star"
                    },
                    {
                        "Id": "02",
                        "text": "News Needs to Meet Its Audiences Where They Are",
                        "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                        "author": "Dave Rogers",
                        "type": "News",
                        "date": "Jun 14",
                        "read": "3 min read",
                        "icon": "star"
                    },
                    {
                        "Id": "03",
                        "text": "News Needs to Meet Its Audiences Where They Are",
                        "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                        "author": "Dave Rogers",
                        "type": "News",
                        "date": "Jun 14",
                        "read": "3 min read",
                        "icon": "star"
                    },
                    {
                        "Id": "04",
                        "text": "News Needs to Meet Its Audiences Where They Are",
                        "url": "https://preview.colorlib.com/theme/meranda/blog-single.html",
                        "author": "Dave Rogers",
                        "type": "News",
                        "date": "Jun 14",
                        "read": "3 min read",
                        "icon": "star"
                    },
                    {
                        "text": "See All Trends",
                        "icon": "icon-keyboard_arrow_right",
                        "url": "https://preview.colorlib.com/theme/meranda/#"
                    }
                ]                        
            }
        }

class Contact(Resource):
    def get(self):
        return {
            "data" : {
                "text": "CONTACT",
                "url": "https://preview.colorlib.com/theme/meranda/contact.html",
                "body" : [
                    {
                        "text" : "Contact Us",
                        "form" : {
                            "first-name" : "Fara",
                            "last-name" : "Paramitha",
                            "Email Address" : "faraparamitha12@gmail.com",
                            "Tel.Number" : "081234567891",
                            "Message" : "Hai",
                            "button" : "SEND MESSAGE"
                        }
                    }
                ]
            }
        }

api.add_resource(HomeAll, '/home/')
api.add_resource(Home_slider, '/home/sliderbar/')
api.add_resource(Home_EditorsPick, '/home/editorspick/')
api.add_resource(Home_trending, '/home/trending/')
api.add_resource(Home_banner, '/home/banner/')
api.add_resource(Home_politics, '/home/politics/')
api.add_resource(Home_business, '/home/business/')
api.add_resource(Home_Recentnews, '/home/recentnews/')
api.add_resource(Home_popular, '/home/popular/')
api.add_resource(Categories, '/categories/')
api.add_resource(Categories_Politics, '/categories/politics/')
api.add_resource(Categories_Popularpost, '/categories/popularpost/')
api.add_resource(SingleContent, '/singlecontent/')
api.add_resource(SingleContent_article, '/singlecontent/article/')
api.add_resource(SingleContent_sugestion, '/singlecontent/sugestion/')
api.add_resource(SingleContent_Comment, '/singlecontent/comment/')
api.add_resource(SingleContent_Popularpost, '/singlecontent/popularpost/')
api.add_resource(Contact, '/contact/')

@app.errorhandler(404)
def page_not_found(e):
    return {"error": "not found end point"}, 404


if __name__ == '__main__':
    app.run(debug=True)
