		output = io.StringIO()

		'''head = ["  "   ,  "  "   , "  "  ,  "  "  ,  "  " ,  "  "  , "  "]
		#l = [[123,  'Apiname',  'start',  'end',  'request',  'response',  300]]
                l= [[123,'Apiname',start_time,end_time,str(json.dumps(JsonObj)),str(json.dumps(result)),status_code]]
                df = pd.DataFrame (l , columns = head)
                #df = pd.DataFrame (l)'''

                head = [123,'Apiname',start_time,end_time,str(json.dumps(JsonObj)),str(json.dumps(result)),status_code]
                df = pd.DataFrame (columns = head)

                print(df)

                #output = df.to_csv (index_label="idx", encoding = "utf-8")
                output = df.to_csv()
                print(output)

                accountName = "xxxxxxxx"
                accountKey = "xxxxxxxxxxxxx"
                containerName = "xxxxxxxxxx"


                blobService = AppendBlobService(account_name=accountName, account_key=accountKey)

                blobService.append_blob_from_text('ttips3', 'tt.csv', output)           
