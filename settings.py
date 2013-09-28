# -*- coding: utf-8 -*-
import sys

TIMEZONE = 'Asia/Shanghai'

DATE_FORMATS = {
    'en' : u'%a, %d %b %Y',
    #~ 'zh' : u'%Y-%m-%d',
    #~ 'zhs': u'%Y-%m-%d',
 }
# windows locale: http://msdn.microsoft.com/en-us/library/cdax410z%28VS.71%29.aspx
#~ LOCALE = ['usa', 'cht', 'chs', 'jpn',        # windows
          #~ 'en_US', 'zh_CN', 'ja_JP']  # Unix/Linux
DEFAULT_LANG = 'en'

SITENAME = "Peng's Blog"
AUTHOR = 'Peng Cui'
DEFAULT_DATE = 'fs'

DISQUS_SITENAME = "pengsblog"
#GITHUB_URL = 'https://github.com/pengcui'
#SITEURL = 'http://pengcui.github.com'
GOOGLE_ANALYTICS = 'UA-30756331-1'
TAG_FEED  = 'feeds/%s.atom.xml'
TAG_CLOUD_STEPS = 4
FEED_RSS = 'feeds/all.rss.xml'
#DEFAULT_ORPHANS=3
DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY ='Misc'
OUTPUT_PATH = './output'
#ARTICLE_SAVE_AS = 'out/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{slug}'
#OUTPUT_PATH = 'out/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
PATH = 'posts' 
#~ THEME_STATIC_PATHS=['pelican-themes']
THEME= './pelican-themes/notmyidea-cms'   #'./pelican-themes/bs6'
#MENUITEMS = (('Archives','/output/archives.html'),)

LINKS = (#('dofine', 'http://log.dofine.me/'),
         #('farseerfc', "http://farseerfc.github.com/"),
         #('H.Y.', "http://hyhx2008.github.com/"),
         )

SOCIAL = (
          ('GitHub', 'https://github.com/pengcui'),
          )
          #('twitter', 'http://twitter.com/farseerfc'),
          #~ ('facebook', 'http://www.facebook.com/farseerfc'),
          #~ ('weibo', 'http://weibo.com/farseerfc'),
          #~ ('renren', 'http://www.renren.com/farseer'),
          
GOOGLE_CUSTOM_SEARCH_SIDEBAR = "010017366155264590731:njcqykcxuly"#终于被google收录了!~          








#~ <object type="application/x-shockwave-flash" style="outline:none;" data="http://hosting.gmodules.com/ig/gadgets/file/112581010116074801021/hamster.swf?" width="300" height="225"><param name="movie" value="http://hosting.gmodules.com/ig/gadgets/file/112581010116074801021/hamster.swf?"></param><param name="AllowScriptAccess" value="always"></param><param name="wmode" value="opaque"></param></object>
#~ <br>

#gtalk
#<iframe src="http://www.google.com/talk/service/badge/Show?tk=z01q6amlq8n8dcqb7mphiivq299uh917bh2sph4lo7rip701jaltqve59eica9opvmhfq5h7hm6i7jkdql1kqntt3h8mnto6ns9lt5960d4dhrvdo3963kv040g9344v6q2nslh6sgqnjp5l2oqspe7p29858omr5qthnm8lc&amp;w=200&amp;h=60" frameborder="0" allowtransparency="true" width="200" height="60"></iframe>
#~ TWITTER_USERNAME = 'farseerfc'

#~ PDF_GENERATOR = True

