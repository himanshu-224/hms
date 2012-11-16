#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect

class LastVisitedMiddleware(object):
    """This middleware sets the last visited url as session field"""

    def process_request(self, request):
        """Intercept the request and add the current path to it"""
        request_path = request.get_full_path()
        if request.session['currently_visiting'] == "/dosa/submitPolicy/NPR/":
            return render_to_response('dosa/submitPolicy.html')

        try:
            request.session['last_visited'] = request.session['currently_visiting']
        except KeyError:
            # silence the exception - this is the users first request
            pass

        request.session['currently_visiting'] = request_path
        

     

