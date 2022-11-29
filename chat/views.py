from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def home(request):
    if request.method == 'GET':
        return Response({
            'status': 200,
            'message': "Hello, world!"
            'method_called':'you called get method!!'
        })

    elif reuset.method == 'PATCH':
         return Response({
            'status': 200,
            'message': "Hello, world!"
            'method_called'_: 'you caleed patch method'
         })
    elif request.method == 'POST':
        return Response({
            'status': 200,
            'message': "Hello, world!"
            'method_called': 'you caleed post method'
            })
    else:
       return Response({
           'status': 400,
           'message': "Hello, world!"
           'method_called': 'you caleed invalid method'
           })