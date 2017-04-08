from django.http import HttpResponse
from datetime import datetime
from mysqlconnector import MySQLConnector
import json

def get_marital_json(request):
    today = "20170407"
    timefrom = "00"

    timeto = str(datetime.now().hour) + str(datetime.now().minute)

    arguments = (today + timefrom + '%', today + timeto + '%')

    # arguments = ('201704070800%', '201704070810%')
    query = "select b.MaritalStatus as MaritalStatus, count(b.MaritalStatus) as count from uklsoft.FraudDatabase a join uklsoft.ClientRequest b on b.CustEmail = a.CustEmail where b.LeadID > %s and b.LeadID < %s group by b.MaritalStatus"
    # print MySQLConnector().execute_query(query, arguments)


    # return HttpResponse(json.dumps(MySQLConnector().execute_query(query, arguments)), content_type='application/json')


    result_list = MySQLConnector().execute_query(query, arguments)


    return HttpResponse(json.dumps({'data' : result_list, 'key' : 'MaritalStatus'}), content_type='application/json')


def get_industry_json(request):
    today = "20170407"
    timefrom = "00"

    timeto = str(datetime.now().hour) + str(datetime.now().minute)

    arguments = (today + timefrom + '%', today + timeto + '%')

    # arguments = ('201704070800%', '201704070810%')
    query = "select b.TypeofIndustry as TypeofIndustry,count(b.TypeofIndustry) as count from uklsoft.FraudDatabase a join uklsoft.ClientRequest b on b.CustEmail = a.CustEmail where b.LeadID > %s and b.LeadID < %s group by b.TypeofIndustry;"
    # print MySQLConnector().execute_query(query, arguments)


    # return HttpResponse(json.dumps(MySQLConnector().execute_query(query, arguments)), content_type='application/json')


    result_list = MySQLConnector().execute_query(query, arguments)


    return HttpResponse(json.dumps({'data' : result_list, 'key' : 'TypeofIndustry'}), content_type='application/json')