# config/middlewares.py

class CorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # response['Access-Control-Allow-Origin'] = 
        response['Origin'] = 'http://43.202.59.123'
        response['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        # print(response['Access-Control-Allow-Origin'], '*'*100)
        print(response['Origin'], '*'*100)
        return response
