import os



env= os.environ.get('env') if os.environ.get('env') != None else "dev"

bucket_name='kiran-nse-data'