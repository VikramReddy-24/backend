from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import boto3
from .commonFunctions import bucket_name,env
from boto3.dynamodb.conditions import Key, Attr
import traceback


class derivativesApi(APIView):
    def post(self,request):
        try:
            input=request.data
            tableName=f"Derivatives_{env}"
            primaryKey=f"{input['indexName']}_{input['instrumentType']}_{input['expiryDate']}_{input['strikePrice']}"
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table(tableName)
            response = table.query(KeyConditionExpression=Key('identifier').eq(primaryKey))
            items = response['Items']
            print(response['Count'])
            return Response(data=items,status=status.HTTP_200_OK)
        except Exception as Error:
            traceback.print_exc()
            resp_body={'Error':'Internal server Error'}
            return Response(data=resp_body,status=status.HTTP_500_INTERNAL_SERVER_ERROR)