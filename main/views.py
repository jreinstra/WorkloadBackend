from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.decorators import login_required

from main.serializers import BlockSerializer

from rest_framework.authtoken.models import Token

# Create your views here.
@login_required
def index(request):
    try:
        request.user.auth_token
    except AttributeError:
        token = Token.objects.create(user=request.user)
        token.save()
    return render(request, "main/index.html", {})

class BlockList(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        blocks = request.user.blocks.all()
        result = [BlockSerializer(x).data for x in blocks]
        return r_success(result)
    
    
class BlockDetail(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        blocks = request.user.blocks.filter(pk=request.GET.get("id"))
        
        if blocks.count() == 1:
            return r_success(BlockSerializer(blocks[0]).data)
        else:
            return r_failure("Block not found.")
        
    def post(self, request):
        blocks = request.user.blocks.filter(pk=request.POST.get("id"))
        if blocks.count() == 1:
            block = blocks[0]
            serializer = BlockSerializer(block, data=request.POST, partial=True)
            message = "Block updated successfully"
        else:
            params = request.POST.copy()
            params['user'] = request.user.pk
            serializer = BlockSerializer(data=params)
            message = "Block created successfully"
            
        if serializer.is_valid():
            print repr(serializer)
            serializer.save()
            return r_success(message)
        else:
            return r_failure(serializer.errors)
        
        
def r_success(result):
    return Response(
        {"success":True, "result":result},
        status=status.HTTP_200_OK
    )

def r_failure(error):
    return Response(
        {"success":False, "error":str(error)},
        status=status.HTTP_400_BAD_REQUEST
    )