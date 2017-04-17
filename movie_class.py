# -*- coding=utf-8 -*-
'''
功能：电影名称、类型。简介


Author:chimuuu

time: 2017.4.15

'''
movie = {
		"动作片": "/tag/dzp/",
		"喜剧片": "/tag/xjp/",
		"恐怖片": "/tag/kbp/",
		"科幻片": "/tag/khp/",
		"爱情片": "/tag/aqp/",
		"剧情片": "/tag/jqp/",
		"战争片": "/tag/zzp/",
		"动画片": "/tag/dhp/",
		"冒险片": "/tag/mxp/",
		"功夫片": "/tag/gfp/",
		"悬疑片": "/tag/xyp/",
		"惊悚片": "/tag/jsp/",
		"励志片": "/tag/lzp/",
		"犯罪片": "/tag/fzp/",
		"历史片": "/tag/lsp/",
		"史诗片": "/tag/ssp/",
		"传记片": "/tag/zjp/",
		"古装片": "/tag/gzp/",
		"奇幻片": "/tag/qhp/",
		"幻想片": "/tag/hxp/",
		"歌舞片": "/tag/gwp/",
		"武侠片": "/tag/wxp/",
		"灾难片": "/tag/znp/",
		"神秘片": "/tag/smp/",
		"西部片": "/tag/xbp/",
		"警匪片": "/tag/jfp/",
		"家庭片": "/tag/jtp/",
		"贺岁片": "/tag/hsp/",
		"运动片": "/tag/ydp/",
		"纪录片": "/tag/jlp/",
		"音乐片": "/tag/yyp/",
		"演唱会": "/tag/ych/",
		"电影合集": "/tag/dyhj/",
		"高分电影": "/tag/gfdy/",
		"高清电影": "/tag/gqdy/",
		"720P高清":"/tag/720p/",
		"1080P高清": "/tag/1080p/",
		"3D电影": "/tag/3ddy/",
		"言情剧": "/tag/yqj/",
		"偶像剧": "/tag/oxj/",
		"魔幻剧": "/tag/mhj/",
		"古装剧": "/tag/gzj/",
		"历史剧": "/tag/lsj/",
		"励志剧": "/tag/lzj/",
		"抗战剧": "/tag/kzj/",
		"谍战剧": "/tag/dzj/",
		"武侠剧": "/tag/wxj/",
		"悬疑剧": "/tag/xyj/",
		"警匪剧": "/tag/jfj/",
		"罪案剧": "/tag/zaj/",
		"轻喜剧": "/tag/qxj/",
		"生活剧": "/tag/shj/",
		"都市剧": "/tag/dsj/",
		"革命剧": "/tag/gmj/",
		"剧情剧": "/tag/jqj/",
		"反恐剧": "/tag/fkj/",
		"商战剧": "/tag/szj/",
		"战争剧": "/tag/zzj/",
		"亲情剧": "/tag/qqj/",
		"侦探剧": "/tag/ztj/",
		"推理剧": "/tag/tlj/",
		"动漫剧": "/tag/dmj/",
		"其他剧": "/tag/qtj/"
}

def invert_dict(m):
	return dict((v,k) for k , v in  m.iteritems())

movie_class = invert_dict(movie)

# for k , v in movie_class.iteritems():
# 	print k, v

