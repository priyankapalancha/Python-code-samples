'''from azure.storage.blob import (
    AppendBlobService
)
import pandas as pd
import io

output = io.StringIO()
#output1 = io.StringIO()
head = ["appteamid"   ,  "apiname"   , "starttime"  ,  "endtime"  ,  "request" ,  "response"  , "statuscode"]

l = [[123,  'gettaxtips',  'start',  'end',  'request',  'response',  500]]
#d = [[123,  'gettaxtips',  'start',  'end',  'request',  'response',  400]]

df = pd.DataFrame (l , columns = head)
#df1 = pd.DataFrame (d , columns = head)
print(df)
#print(df1)
output = df.to_csv (index_label="idx", encoding = "utf-8")
#output1 = df1.to_csv (index_label="idx", encoding = "utf-8")
print(output)
#print(output1)

accountName = "a1sbdatrsg01diag"
accountKey = "Pa4udt0XaZdIJBfX5mnzrw6UqEZLj6r4kvsK1h1K6k04V0A/AYPOk27tGX0Nv7GvXHhslIU6mF82vLpoVXAMvg=="
containerName = "ttipscontainer2"
#blobName = "test3.json"

blobService = AppendBlobService(account_name=accountName, account_key=accountKey)

blobService.append_blob_from_text('ttipscontainer2', 'output.csv', output)
#blobService.create_blob_from_text('ttipscontainer', 'OutFilePy.csv', output1)'''