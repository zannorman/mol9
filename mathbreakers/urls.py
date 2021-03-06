from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

import mathbreakers.views
import mathbreakers.userviews
import mathbreakers.ajax
import mathbreakers.client
import mathbreakers.bugs
import mathbreakers.commoncore
import mathbreakers.purchase
import mathbreakers.classroom
import mathbreakers.su
import mathbreakers.preorder
import mathbreakers.analytics
import mathbreakers.survey
import mathbreakers.session
import mathbreakers.modifydb
import mathbreakers.unsubscribe
import mathbreakers.game
import mathbreakers.util

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    
    # Legacy and weird redirects
	url(r'^download/mac_home$', mathbreakers.views.simple_page('download.html')),
    url(r'^download/win_home$', mathbreakers.views.simple_page('download.html')),
    url(r'^download/linux_home$', mathbreakers.views.simple_page('download.html')),
    url(r'^download/mac_free$', mathbreakers.views.simple_page('download.html')),
    url(r'^download/win_free$', mathbreakers.views.simple_page('download.html')),
    url(r'^download/linux_free$', mathbreakers.views.simple_page('download.html')),
    url(r'^LASD/', mathbreakers.views.simple_page("lasd.html")),
    url(r'^session/try2/$', mathbreakers.session.teacher_try),
    url(r'^500/', "500"),


    # Simple pages
    url(r'^download/$', mathbreakers.views.simple_page('download.html')),
    url(r'^getmathbreakers/', mathbreakers.views.simple_page('buy_full.html')),
	url(r'^discussion/', mathbreakers.views.simple_page('discussion.html')),
    url(r'^privacy/$', mathbreakers.views.simple_page('privacy.html')),
    url(r'^tos/$', mathbreakers.views.simple_page('tos.html')),
    url(r'^contact/$', mathbreakers.views.simple_page('contact.html')),
    url(r'^learnmore/$', mathbreakers.views.simple_page('learnmore.html')),
    url(r'^sampledashboard/$', mathbreakers.views.simple_page('sampledashboard.html')),    
    url(r'^presskit/$', mathbreakers.views.simple_page('presskit.html')),
    url(r'^about/$', mathbreakers.views.simple_page('about.html')),
    url(r'^faq/$', mathbreakers.views.simple_page('faq.html')),
    url(r'^testimonials/$', mathbreakers.views.simple_page('testimonials.html')),
    url(r'^labs/$', mathbreakers.views.labs),
    url(r'^preorder/', mathbreakers.views.simple_page('buy_full.html')),
    url(r'^postpurchase/teacher/$', mathbreakers.views.simple_page('postpurchase_teacher.html')),
    url(r'^postpurchase/game/$', mathbreakers.views.simple_page('postpurchase_game.html')),
    url(r'^postpurchase/variable/$', mathbreakers.views.simple_page('postpurchase_variable.html')),
    url(r'^testimonials/', mathbreakers.views.simple_page('testimonials.html')),


    # Dynamic pages
    url(r'^$', mathbreakers.views.home),
    url(r'^logout/$', mathbreakers.views.logout),
    url(r'^notifyimage/$', mathbreakers.views.notify),
    url(r'^trial/$', mathbreakers.views.trial),
    url(r'^forgotpassword/$', mathbreakers.views.forgotpassword),
    url(r'^passwordreset/(.+)/$', mathbreakers.views.passwordreset),
    url(r'^download/full/(.+?)/$', mathbreakers.views.download_full),
    url(r'^HSBC/(.+?)/$', mathbreakers.views.hsbc),
    url(r'^HSBC/$', mathbreakers.views.hsbc),
    url(r'^code/(.+?)/$', mathbreakers.views.code),
    url(r'^code/$', mathbreakers.views.code), 
    url(r'^message/$', mathbreakers.views.message),
    url(r'^message_teacher/$', mathbreakers.views.message_teacher),
    url(r'^newsletter/$', mathbreakers.views.newsletter),    
    #url(r'^educents/(.+?)/$', mathbreakers.views.educents),
    url(r'^promotioncode/$', mathbreakers.views.educentspromotion),

    #webgl game
    url(r'^game/$', mathbreakers.game.game),
    url(r'^game/webgl_empty.html.mem', mathbreakers.util.make_redirect('/static/webgl/webgl_empty.html.mem')),
    url(r'^game/webgl_empty.data', mathbreakers.util.make_redirect('/static/webgl/webgl_empty.data')),

    url(r'^workertest/$', mathbreakers.views.simple_page("workertest.html")),

    # Logged in pages
    url(r'^settings/$', mathbreakers.userviews.settings),
    url(r'^settings/changepassword/$', mathbreakers.userviews.change_password),     

    # Ajax pages
    url(r'^ajax/signup/$', mathbreakers.ajax.signup),
    url(r'^ajax/signin/$', mathbreakers.ajax.signin),
    url(r'^ajax/createaccount/$', mathbreakers.ajax.createaccount),
    url(r'^ajax/download/([a-z]+)$', mathbreakers.ajax.download),
    url(r'^ajax/createteacheraccount/$', mathbreakers.ajax.createteacheraccount),
    url(r'^ajax/convertteacheraccount/$', mathbreakers.ajax.convertteacheraccount),
    url(r'^ajax/buttonlog/(.+?)/$', mathbreakers.ajax.buttonlog),

    # Pages used by mathbreakers game client
    url(r'^client/signin/$', mathbreakers.client.signin),
    url(r'^client/register/$', mathbreakers.client.register),
    url(r'^client/report/topics/$', mathbreakers.client.report_topics),
    url(r'^client/report/level/$', mathbreakers.client.report_level),

    url(r'^client/get/costume/$', mathbreakers.client.costume),
    url(r'^client/report/costume/$', mathbreakers.client.report_costume),

    url(r'^client/get/inventory/$', mathbreakers.client.inventory),
    url(r'^client/report/inventory/$', mathbreakers.client.report_inventory),

    url(r'^client/get/gems/$', mathbreakers.client.gems),
    url(r'^client/report/gems/$', mathbreakers.client.report_gems),

    url(r'^client/get/checkpoint/$', mathbreakers.client.checkpoint),
    url(r'^client/report/checkpoint/$', mathbreakers.client.report_checkpoint),

    ####### legacy items ########
    url(r'^client/inventory/$', mathbreakers.client.legacy_costume_gems_inventory),
    url(r'^client/report/items/$', mathbreakers.client.legacy_report_costume_gems_inventory),
    ####### sigh ################

    url(r'^client/refer/$', mathbreakers.client.refer_email),
    url(r'^client/gamestate/$', mathbreakers.client.gamestate),
    #url(r'^client/screenshot/$', mathbreakers.client.screenshot),
    url(r'^client/noticeimage/$', mathbreakers.client.notice_image),
    url(r'^client/assignments/$', mathbreakers.client.assignments),
    url(r'^client/report/heatmap/$', mathbreakers.client.heatmap),
    url(r'^client/report/menuclicks/$', mathbreakers.client.menuclicks),
    url(r'^client/roboterra/login/$', mathbreakers.client.roboterra_login),
    url(r'^client/skills/$', mathbreakers.client.skills),
    url(r'^client/report/skills/$', mathbreakers.client.report_skills),
    
    
    url(r'^client/version/(.+?)/$', mathbreakers.client.version),
    url(r'^client/message/(.+?)/$', mathbreakers.client.client_message),

    # Class sessions
    url(r'^session/client/nearby/$', mathbreakers.session.client_nearby),
    url(r'^session/client/names/$', mathbreakers.session.client_classroom_names),
    url(r'^session/client/login/$', mathbreakers.session.client_login),
    url(r'^session/client/register/$', mathbreakers.session.client_register),
    url(r'^session/classdetails/(.+?)/$', mathbreakers.session.classdetails),
    
    url(r'^session/try/$', mathbreakers.session.teacher_try),
    url(r'^session/start/$', mathbreakers.session.start),
    url(r'^session/later/$', mathbreakers.session.later),

    url(r'^session/ajax/users/$', mathbreakers.session.ajax_users),
    url(r'^session/ajax/playtime/$', mathbreakers.session.ajax_playtime),

    url(r'^session/selectclass/$', mathbreakers.session.selectclass),
    url(r'^session/status/$', mathbreakers.session.status),

    # Bugs
    url(r'^bugs/report/$', mathbreakers.bugs.report),

	# Database
	url(r'^modifydb/deleterow/$', mathbreakers.modifydb.deleterow),

    # Common Core 
    url(r'^cc/grade/$', mathbreakers.commoncore.grade),
    url(r'^cc/category/$', mathbreakers.commoncore.category),
    url(r'^cc/$', mathbreakers.commoncore.index),
    url(r'^cc/full/$', mathbreakers.commoncore.full),

    # Purchases
    url(r'^purchase/teacher/$', mathbreakers.purchase.teacher),
    url(r'^purchase/stripe/(.+)/$', mathbreakers.purchase.purchase_stripe),
    url(r'^pay/$', mathbreakers.purchase.pay_variable),

    url(r'^buy/$', mathbreakers.purchase.buy_full),

    # Classroom stuff
    url(r'^class/$', mathbreakers.classroom.manage),
    url(r'^class/dashboard/$', mathbreakers.classroom.dashboard),
    url(r'^class/ajax/remove/$', mathbreakers.classroom.ajax_remove),
    url(r'^class/ajax/assign/$', mathbreakers.classroom.ajax_assign),
    url(r'^class/ajax/unassign/$', mathbreakers.classroom.ajax_unassign),
    url(r'^class/ajax/getstudents/.*$', mathbreakers.classroom.ajax_getstudents),
    
	# SU
	url(r'^su/company_stats/$', mathbreakers.su.company_stats),
	url(r'^su/buttons/(.+?)/(.+?)$', mathbreakers.su.buttons_for),
	url(r'^su/buttons/(.+?)$', mathbreakers.su.buttons),
    url(r'^su/campsignups/$', mathbreakers.su.campsignups),
    url(r'^su/purchaseusers/$', mathbreakers.su.purchase_users),
    url(r'^su/userprogress/$', mathbreakers.su.user_progress),
	url(r'^su/preorder/$', mathbreakers.su.preorder),
	url(r'^su/generatefullgamecode/$', mathbreakers.su.generatefullgamecode),
	url(r'^su/teacher_emails/$', mathbreakers.su.list_teacher_emails),
	url(r'^su/classrooms/$', mathbreakers.su.classrooms),
    url(r'^su/makehugs/$', mathbreakers.su.makehugs),
    url(r'^su/getsurveys/$', mathbreakers.su.getsurveys),
    url(r'^su/teachersignupflow/$', mathbreakers.su.teacher_signup_flow),
    url(r'^su/partnerships/$', mathbreakers.su.partnerships),
    url(r'^su/userinfo/$', mathbreakers.su.userinfo),
    url(r'^su/loginas/(.+?)/$', mathbreakers.su.loginas),
    url(r'^su/teachers/$', mathbreakers.su.teachers),
	# url(r'^su/nc/$', mathbreakers.su.nc),
	url(r'^su/$', mathbreakers.su.index),
    url(r'^su/ajax/markteacher/$', mathbreakers.su.ajax_mark_teacher),
    url(r'^su/bugs/$', mathbreakers.bugs.show),

    # A/B cohorts
    url(r'^start/(.+?)/', mathbreakers.views.cohort_start),

	# analytics
	url(r'^analytics/heatmap/(.+?)$', mathbreakers.analytics.heatmap),

    # preorder codes
    url(r'^redeem/code/(.+?)$', mathbreakers.preorder.redeemcode),
    url(r'^redeem/code/$', mathbreakers.preorder.redeemcode),

    url(r'^survey/', mathbreakers.survey.survey),
	url(r'^unsubscribe/$', mathbreakers.unsubscribe.unsub),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
