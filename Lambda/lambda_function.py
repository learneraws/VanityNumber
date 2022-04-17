import json
import boto3 
from boto3.dynamodb.conditions import Key, Attr
from array import *
import re
from datetime import datetime

s3_client = boto3.client('s3')
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("vf-dict-data2")
resultstable=dynamodb.Table("vf-results-table")
now = datetime.now()

#Function to map digits from phone number with key pad alphabets
def matchdigit(dig):
    if dig=='0':
       return ['O','O','O','']
    elif dig=='1':
       return ['L','L','L','']
    elif dig=='2':
       return ['A','B','C','']
    elif dig=='3':
       return ['D','E','F','']
    elif dig=='4':
       return ['G','H','I','']
    elif dig=='5':
       return ['J','K','L','']
    elif dig=='6':
       return ['M','N','O','']
    elif dig=='7':
       return ['P','Q','R','S']
    elif dig=='8':
       return ['T','U','V','']
    elif dig=='9':
       return ['W','X','Y','Z']
      

def write_to_dynamo(rows,callernum):
   try:
      results_table = dynamodb.Table('vf-results-table')
   except:
      print('Error loading DynamoDB table.')

   try:
     for i in range(len(rows)):
        if 'empty' not in rows[i]:
            results_table.put_item(
               Item={'Id':str(i),
                    'dateAdedd':now.strftime("%d%m%Y%H%M%S"),
                    'Word':rows[i]['Word'],
                    'callernum':callernum,
                    'FirstLetter':rows[i]['FirstLetter'],
                    'SecondLetter':rows[i]['SecondLetter'],
                    'ThirdLetter':rows[i]['ThirdLetter'],
                    'FouthLetter':rows[i]['FouthLetter'],
                    'FifthLetter':rows[i]['FifthLetter'],
                    'SixthLetter':rows[i]['SixthLetter'],
                    'SeventhLetter':rows[i]['SeventhLetter']
                }
            )
   except Exception as err:
      print(err)
      print('Error executing batch_writer')      

def lambda_handler(event, context):
  i=5
  print(event)
  phonenumber=event['Details']['Parameters']['inputphonenumber']
  callernum=event["Details"]["ContactData"]["CustomerEndpoint"]["Address"]
  print(callernum)
  phonenumber=re.sub("\D","",phonenumber)
  while i<=len(phonenumber)-1:
    #print(phonenumber[i])
    if i==5:
      list05=matchdigit(phonenumber[i])
      #print(phonenumber[i])
      #print(list05)
      firstdigoptionone=list05[0]
      firstdigoptiontwo=list05[1]
      firstdigoptionthree=list05[2]
      firstdigoptionfour=list05[3]
      i=i+1
      continue
    if i==6:
      list06=matchdigit(phonenumber[i])
      #print(phonenumber[i])
      #print(list06)
      seconddigoptionone=list06[0]
      seconddigoptiontwo=list06[1]
      seconddigoptionthree=list06[2]
      seconddigoptionfour=list06[3]
      i=i+1
      continue
    if i==7:
      list07=matchdigit(phonenumber[i])
      #print(phonenumber[i])
      #print(list07)
      thirddigoptionone=list07[0]
      thirddigoptiontwo=list07[1]
      thirddigoptionthree=list07[2]
      thirddigoptionfour=list07[3]
      i=i+1
      continue
    if i==8:
      list08=matchdigit(phonenumber[i])
      #print(phonenumber[i])
      #print(list08)
      fourthdigoptionone=list08[0]
      fourthdigoptiontwo=list08[1]
      fourthdigoptionthree=list08[2]
      fourthdigoptionfour=list08[3]
      i=i+1
      continue
    if i==9:
      list09=matchdigit(phonenumber[i])
      #print(phonenumber[i])
      #print(list09)
      fifthdigoptionone=list09[0]
      fifthdigoptiontwo=list09[1]
      fifthdigoptionthree=list09[2]
      fifthdigoptionfour=list09[3]
      i=i+1
      continue
    if i==10:
      list10=matchdigit(phonenumber[i])
      #print(phonenumber[i])
      #print(list10)
      sixthdigoptionone=list10[0]
      sixthdigoptiontwo=list10[1]
      sixthdigoptionthree=list10[2]
      sixthdigoptionfour=list10[3]
      i=i+1
      continue
    if i==11:
      list11=matchdigit(phonenumber[i])
      #print(phonenumber[i])
      #print(list11)
      seventhdigoptionone=list11[0]
      seventhdigoptiontwo=list11[1]
      seventhdigoptionthree=list11[2]
      seventhdigoptionfour=list11[3]
      i=i+1
      continue
    i=i+1
      
  response=table.scan(
        FilterExpression=
        (Key('FirstLetter').eq(firstdigoptionone) | Key('FirstLetter').eq(firstdigoptiontwo) | Key('FirstLetter').eq(firstdigoptionthree) | Key('FirstLetter').eq(firstdigoptionfour))
        &(Attr('SecondLetter').eq(seconddigoptionone) | Attr('SecondLetter').eq(seconddigoptiontwo) | Attr('SecondLetter').eq(seconddigoptionthree) | Attr('SecondLetter').eq(seconddigoptionfour)) 
        &(Attr('ThirdLetter').eq(thirddigoptionone) | Attr('ThirdLetter').eq(thirddigoptiontwo) | Attr('ThirdLetter').eq(thirddigoptionthree) | Attr('ThirdLetter').eq(thirddigoptionfour) | Attr('ThirdLetter').not_exists())
        #&(Attr('FourthLetter').eq(fourthdigoptionone) | Attr('FourthLetter').eq(fourthdigoptiontwo) | Attr('FourthLetter').eq(fourthdigoptionthree) | Attr('FourthLetter').eq(fourthdigoptionfour) | Attr('FourthLetter').not_exists())
        #&(Attr('FifthLetter').eq(fifthdigoptionone) | Attr('FifthLetter').eq(fifthdigoptiontwo) | Attr('FifthLetter').eq(fifthdigoptionthree) | Attr('FifthLetter').eq(fifthdigoptionfour) | Attr('FifthLetter').not_exists())
        #&(Attr('SixthLetter').eq(sixthdigoptionone) | Attr('SixthLetter').eq(sixthdigoptiontwo) | Attr('SixthLetter').eq(sixthdigoptionthree) | Attr('SixthLetter').eq(sixthdigoptionfour)| Attr('SixthLetter').not_exists() ) 
        #&(Attr('SevenththLetter').eq(seventhdigoptionone) | Attr('SevenththLetter').eq(seventhdigoptiontwo) | Attr('SevenththLetter').eq(seventhdigoptionthree) | Attr('SevenththLetter').eq(seventhdigoptionfour) | Attr('SevenththLetter').not_exists())
        )
    
  print(response)
  #print(response['LastEvaluatedKey'])
  
  items=response['Items']   
  #for item in items:
  #   print(item)
     
  print(response['Count'])
  counter=0
  result1=""
  result2=""
  result3=""
  
  c = json.dumps(response["Count"])
  c = int(c)
  result=['empty','empty','empty']
  best=['empty','empty','empty']
  Words=['','','']
  
  if response['Count']> 3:
    for i in range (0,3):
        for j in range (0,c-1):
            if int(response['Items'][j]['Length'])==7 and (response['Items'][j]['Word'] not in Words):
                best[i]=response['Items'][j]
                result[i]=response['Items'][j]
                Words[i]=response['Items'][j]['Word']
          
    if 'empty' in result:
        sixlength=result.index('empty')
        print((sixlength))
        for i in range (sixlength,3):
            for j in range (0,c-1):
                if int(response['Items'][j]['Length'])==6 and (response['Items'][j]['Word'] not in Words):
                    result[i]=response['Items'][j]
                    Words[i]=response['Items'][j]['Word']                    
    
    if 'empty' in result:
        fivelength=result.index('empty')
        print((fivelength))
        for i in range (fivelength,3):
            for j in range (0,c-1):
                if int(response['Items'][j]['Length'])==5 and (response['Items'][j]['Word'] not in Words):
                    result[i]=response['Items'][j]
                    Words[i]=response['Items'][j]['Word']     

    if 'empty' in result:
        fourlength=result.index('empty')
        for i in range (fourlength,3):
            for j in range (0,c-1):
                if int(response['Items'][j]['Length'])==4 and (response['Items'][j]['Word'] not in Words):
                    result[i]=response['Items'][j]
                    Words[i]=response['Items'][j]['Word']     

    if 'empty' in result:
        threelength=result.index('empty')
        for i in range (threelength,3):
            for j in range (0,c-1):
                if int(response['Items'][j]['Length'])==3 and (response['Items'][j]['Word'] not in Words):
                    result[i]=response['Items'][j]
                    Words[i]=response['Items'][j]['Word']   

    if 'empty' in result:
        twolength=result.index('empty')
        for i in range (twolength,3):
            for j in range (0,c-1):
                if int(response['Items'][j]['Length'])==2 and (response['Items'][j]['Word'] not in Words):
                    result[i]=response['Items'][j]
                    Words[i]=response['Items'][j]['Word']           
    
    (result)
    print(best)
    print(Words)
    print(len(result))
    
    
    responseresults=dynamodb.Table('vf-results-table')
    print(responseresults.item_count)
    
    if responseresults.item_count<5:
         write_to_dynamo(best,callernum)
        
  else: 
    if response['Count'] > 0:
       for i in range (0,2):
            for item in response["Items"]:
                result[i]= item  
      
    else:
          resultMap = {"Response":404}
          print(resultMap)
          return resultMap
  for i in phonenumber:
    counter=counter+1
    #
    if counter<=3:
       result1=result1+i
    if counter==4:
       result1=result1+str((result[0]["FirstLetter"]))
    if counter==5:
       result1=result1+str((result[0]["SecondLetter"]))
    if counter==6:
        if (re.sub('"','',result[0]["ThirdLetter"])):
           result1=result1+str((result[0]["ThirdLetter"]))
        else:
           result1=result1+i
    if counter==7:
        if (re.sub('"','',result[0]["FouthLetter"])):
           result1=result1+str((result[0]["FouthLetter"]))
        else:
           result1=result1+i
    if counter==8:
        if (re.sub('"','',result[0]["FifthLetter"])):
           result1=result1+(result[0]["FifthLetter"])
        else: 
           result1=result1+i
    if counter==9:
        if (re.sub('"','',result[0]["SixthLetter"])):
           result1=result1+(result[0]["SixthLetter"])
        else: 
           result1=result1+i
    if counter==10:
        if (re.sub('"','',result[0]["SeventhLetter"])):
           result1=result1+(result[0]["SeventhLetter"])
        else:
           result1=result1+i
         
  result1=re.sub('"','',result1)
  result1='<speak>We have found Vanity a number for you, your First Number is <say-as interpret-as="characters">'+result1
  print(phonenumber)
  #print(result1)
  
  counter2=0
  if response['Count'] > 1:
    #print(response["Items"][1])
    for i in phonenumber:
        #print(response["Items"][1])
        counter2=counter2+1
        if counter2<=3:
           result2=result2+i
        if counter2==4:
           result2=result2+str(result[1]["FirstLetter"])
        if counter2==5:
           result2=result2+str(result[1]["SecondLetter"])
        if counter2==6:
            if (re.sub('"','',result[1]["ThirdLetter"])):
               result2=result2+str((result[1]["ThirdLetter"]))
            else:
               result2=result2+i
        if counter2==7:
            if (re.sub('"','',result[1]["FouthLetter"])):
               result2=result2+((result[1]["FouthLetter"]))
            else:
               result2=result2+i
        if counter2==8:
            if (re.sub('"','',result[1]["FifthLetter"])):
               result2=result2+(result[1]["FifthLetter"])
            else: 
               result2=result2+i
        if counter2==9:
            if (re.sub('"','',result[1]["SixthLetter"])):
               result2=result2+(result[1]["SixthLetter"])
            else: 
               result2=result2+i
        if counter2==10:
            if (re.sub('"','',result[1]["SeventhLetter"])):
               result2=result2+(result[1]["SeventhLetter"])
            else:
               result2=result2+i
  
    result2=re.sub('"','',result2)
    result2='<speak>We have found another Vanity number for you, your Second Number is <say-as interpret-as="characters">'+result2
    #print(result2)
  
  counter3=0
  if response['Count'] > 2:
    #print(response["Items"][2])
    for i in phonenumber:
        #print(response["Items"][2])
        counter3=counter3+1
        if counter3<=3:
           result3=result3+i
        if counter3==4:
           result3=result3+str((result[2]["FirstLetter"]))
        if counter3==5:
           result3=result3+str((result[2]["SecondLetter"]))
        if counter3==6:
            if (re.sub('"','',result[2]["ThirdLetter"])):
               result3=result3+str((result[2]["ThirdLetter"]))
            else:
               result3=result3+i
        if counter3==7:
            if (re.sub('"','',result[2]["FouthLetter"])):
               result3=result3+((result[2]["FouthLetter"]))
            else:
               result3=result3+i
        if counter3==8:
            if (re.sub('"','',result[2]["FifthLetter"])):
               result3=result3+(result[2]["FifthLetter"])
            else: 
               result3=result3+i
        if counter3==9:
            if (re.sub('"','',result[2]["SixthLetter"])):
               result3=result3+(result[1]["SixthLetter"])
            else: 
               result3=result3+i
        if counter3==10:
            if (re.sub('"','',result[2]["SeventhLetter"])):
               result3=result3+(result[2]["SeventhLetter"])
            else:
               result3=result3+i
  
    result3=re.sub('"','',result3)
    result3='<speak>We have found one more Vanity number for you, your Third Number is <say-as interpret-as="characters">'+result3
    #print(result3)  
  resultMap = {"Response":200,"result1":result1,"result2":result2,"result3":result3}
  return resultMap