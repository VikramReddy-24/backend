import os



env= os.environ.get('env') if os.environ.get('env') != None else "prod"

bucket_name='kiran-nse-data'