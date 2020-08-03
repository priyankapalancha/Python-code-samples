		output = io.StringIO()

		'''head = ["  "   ,  "  "   , "  "  ,  "  "  ,  "  " ,  "  "  , "  "]
		#l = [[123,  'gettaxtips',  'start',  'end',  'request',  'response',  300]]
                l= [[123,'getTaxtips',start_time,end_time,str(json.dumps(JsonObj)),str(json.dumps(result)),status_code]]
                df = pd.DataFrame (l , columns = head)
                #df = pd.DataFrame (l)'''

                head = [123,'getTaxtips',start_time,end_time,str(json.dumps(JsonObj)),str(json.dumps(result)),status_code]
                df = pd.DataFrame (columns = head)

                print(df)

                #output = df.to_csv (index_label="idx", encoding = "utf-8")
                output = df.to_csv()
                print(output)

                accountName = "a1sbdatrsg01diag"
                accountKey = "Pa4udt0XaZdIJBfX5mnzrw6UqEZLj6r4kvsK1h1K6k04V0A/AYPOk27tGX0Nv7GvXHhslIU6mF82vLpoVXAMvg=="
                containerName = "ttipscontainer3"


                blobService = AppendBlobService(account_name=accountName, account_key=accountKey)

                blobService.append_blob_from_text('ttipscontainer3', 'ttips.csv', output)           