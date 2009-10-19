# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('django_authopenid.views',
    # yadis rdf
    url(r'^yadis.xrdf$', 'xrdf', name='yadis_xrdf'),
     # manage account registration
    url(r'^%s$' % 'signin/', 'signin', name='user_signin'),
    url(r'^%s%s$' % ('signin/','newquestion/'), 'signin', kwargs = {'newquestion':True}),
    url(r'^%s%s$' % ('signin/','newanswer/'), 'signin', kwargs = {'newanswer':True}),
    url(r'^%s$' % 'signout/', 'signout', name='user_signout'),
    url(r'^%s%s$' % ('signin/', 'complete/'), 'complete_signin', 
        name='user_complete_signin'),
    url(r'^%s$' % 'register/', 'register', name='user_register'),
    url(r'^%s$' % 'signup/', 'signup', name='user_signup'),
    #disable current sendpw function
    url(r'^%s$' % 'sendpw/', 'signin', name='user_sendpw'),
    #url(r'^%s$' % 'sendpw/', 'sendpw', name='user_sendpw'),
    #url(r'^%s%s$' % ('password/', 'confirm/'), 'confirmchangepw', 
    #    name='user_confirmchangepw'),

    # manage account settings
    #url(r'^$', 'account_settings', name='user_account_settings'),
    #url(r'^%s$' % 'password/', 'changepw', name='user_changepw'),
    url(r'^%s$' % 'email/', 'changeemail', name='user_changeemail',kwargs = {'action':'change'}),
    url(r'^%s%s$' % ('email/','validate/'), 'changeemail', name='user_changeemail',kwargs = {'action':'validate'}),
    #url(r'^%s$' % 'openid/', 'changeopenid', name='user_changeopenid'),
    url(r'^%s$' % 'delete/', 'delete', name='user_delete'),
)
