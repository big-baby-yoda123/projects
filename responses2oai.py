import random

FILE = "D:\cods\pythonCode\AI project\\responsesConfig.txt"
action_list = []

def botResponse():
    response_tuple = ()
    resp_list = []
    list_of_tuple = []
    file_resp = open(FILE, 'r')
    file_resp = file_resp.read()
    list_of_resp = file_resp.split('\n')
    for response in list_of_resp:
        if "//" not in response:
            resp_list = response.split(' - ')
            if len(resp_list) >= 2:
                if '*' in resp_list[0]:
                    action_list.append(resp_list[0])
                response_tuple = resp_list[0], list(resp_list[1].split(', ')), resp_list[2] != "", list(resp_list[3].split(', '))
                list_of_tuple.append(response_tuple)
    #print(list_of_tuple)
    #print(action_list)
    return list_of_tuple

def unknown():
    respones = ['could you please try again?',
                "...",
                "i didn't understand that",
                "what did you said"][random.randrange(4)]
    return respones
