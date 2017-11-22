## 基于慕课网djano项目学习的代码 ##

2017-10-28<br>
完成Model的填写<br>
2017-10-31<br>
机构的列表的筛选的功能<br>
遇到No module named forms的bug<br>
原因：tmd 竟然 没有把写好的forms.py上传上去 很尴尬<br>
2017-11-8
基本实现授课机构相关的所有内容<br>
学习要点<br>
1 反向取数据_set<br>
2 传值id的使用方法<br>
2017-11-20<br>
添加公开课列表的部分内容<br>
学习要点<br>
1通过course拿到org直接返回<br>
2传get参数后class的active的显示与否

2017-11-21<br>
根据id获取详情
<br>Course.objects.get(id=int(course_id))
写/course/video/id

bug<br>
coercing to Unicode: need string or buffer, tuple found<br>
解决方案<br>
def __unicode__(self):
        return self.user<br>
变为<br>
def __unicode__(self):
        return self.user.username<br>

2017-11-22
1添加一个post接口(用于添加评论)
2添加评论详情的页面
3首页添加一些静态数据与后台交互
