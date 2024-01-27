from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import boto3
import json
import pandas as pd
from .commonFunctions import bucket_name,env
import traceback
from decimal import Decimal
class dropDownApi(APIView):
    def get(self,request):
        try:
            dropDownTable_name=f'dropDown_{env}'
            
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table(dropDownTable_name)
            response = table.scan()
            items = response.get('Items', [])
            dropDown={}
            for item in items:
                item['stockName']
                item['instrumentName']=item['instrument_expiry'].split('_')[0]
                item['expiryDates']=item['instrument_expiry'].split('_')[1]
            
            dropDown_df=pd.DataFrame(items)
            print(dropDown_df.head(3))
            for  stock in list(set(dropDown_df['stockName'])):
                dropDown[stock]={}
                instrument_df=dropDown_df[dropDown_df['stockName']==stock]
                for instrument in list(set(instrument_df['instrumentName'])):
                    dropDown[stock][instrument]={}
                    expiry_df=instrument_df[(instrument_df['instrumentName']==instrument)]
                    for expiry in list(expiry_df['expiryDates']):
                        s=list(expiry_df[expiry_df['expiryDates']==expiry]['strikePrice'])[0]
                        s=sorted(s)
                        dropDown[stock][instrument][expiry]=s

            return Response(data=dropDown,status=status.HTTP_200_OK)
        except Exception as Error:
            traceback.print_exc()
            resp_body={'Error':'Internal server Error'}
            return Response(data=resp_body,status=status.HTTP_500_INTERNAL_SERVER_ERROR)