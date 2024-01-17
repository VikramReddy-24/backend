from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import boto3
import json
from .commonFunctions import bucket_name,env
import traceback

class dropDownApi(APIView):
    def get(self,request):
        try:
            s3 = boto3.client('s3')
            file_name= f'derivative_config/{env}/dropDownData.json' 
            obj = s3.get_object(Bucket=bucket_name, Key=file_name)
            resp_body=json.loads(obj['Body'].read())
            return Response(data=resp_body,status=status.HTTP_200_OK)
        except Exception as Error:
            traceback.print_exc()
            resp_body={'Error':'Internal server Error'}
            return Response(data=resp_body,status=status.HTTP_500_INTERNAL_SERVER_ERROR)