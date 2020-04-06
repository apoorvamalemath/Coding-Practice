import boto3
from io import BytesIO
import gzip
import re
import json

s3 = boto3.client('s3')

LOGS_DICT = {}

def GetLogFile():
    fileobj = s3.get_object(
    Bucket = BUCKET_NAME,
    Key = PATH_CONTAINER
        )

    try:
        filedata = fileobj['Body'].read()
        gzipfile = BytesIO(filedata)
        gzipfile = gzip.GzipFile(fileobj=gzipfile)
        content = gzipfile.read()

        data = content.decode('utf-8')
        data_list = data.split('\n')

        #INFO_LIST =[]
        WARN_LIST = []
        ERROR_LIST=[]

        for j in data_list:
            if re.match("^[0-9][0-9][/][0-9][0-9][/][0-9][0-9]",j):
                test1 = j.split()
                #if test1[2] == "INFO":
                #    INFO_LIST.append(j)
                if test1[2] == "WARN":
                    WARN_LIST.append(j)
                elif test1[2] =="ERROR":
                    ERROR_LIST.append(j)



        LOGS_DICT[CONTAINER_ID] = {}
        #LOGS_DICT[PATH_CONTAINER]["INFO"] = INFO_LIST
        LOGS_DICT[CONTAINER_ID]["WARN"] = WARN_LIST
        LOGS_DICT[CONTAINER_ID]["ERROR"] = ERROR_LIST
        return filedata
    except Exception as e:
        print("except")
        pass



#BUCKET_NAME = 'aws-logs-240033045552-us-east-1'
#CLUSTER_ID = input("Cluster ID: ")
#APPLICATION_ID = input("Application ID: ")
CLUSTER_ID="j-1BU6G6F6DKC7G"
APPLICATION_ID="application_1585636916894_0001"

client = boto3.client('emr')
response = client.describe_cluster(
    ClusterId=CLUSTER_ID
)

a=response[u'Cluster'][u'LogUri'].split('/')
BUCKET_NAME=str(a[2])
for i in BUCKET_NAME:
	if i=='':
		bucket_name.remove(i)

folder='/'.join(a[3 :])
#path="".join([folder,CLUSTER_ID,'/containers/',APPLICATION_ID]).strip()

data = s3.list_objects(Bucket=BUCKET_NAME, Prefix='elasticmapreduce/'+CLUSTER_ID+'/containers/'+APPLICATION_ID+'/')['Contents']

for i in data:
    if re.match("^.*stderr\.gz$", str(i['Key'])):

        # LOOP THROUGH EACH CONTAINER WITH STDERR.GZ FILE

        PATH_CONTAINER = str(i['Key'])
        CONTAINER_ID = str(PATH_CONTAINER.split('/')[4])
        t = threading.Thread(target = GetLogFile, args=(PATH_CONTAINER,CONTAINER_ID)).start()


JSON_RESULT = json.dumps(LOGS_DICT,indent=4, sort_keys=True)
print(JSON_RESULT)
output = str(PATH_CONTAINER.split('/')[3]) + ".json"
f=open(output,'w')
f.write(JSON_RESULT)
f.close()
