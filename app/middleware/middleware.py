from app.threadlocal import thread_local


def multidb_middleware(get_response):

    def middleware(request):
        print(request)
        print(request.GET)
        print(request.get_host())
        print(request.get_host().split(':')[0])

        host = request.get_host().split(':')[0]
        subdomain = host.split('.')[0]
        request.customer = subdomain

        @thread_local(using_db=subdomain)
        def execute_request(request):
            return get_response(request)

        response = execute_request(request)
        return response

    return middleware