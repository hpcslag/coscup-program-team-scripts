# import util layer
import sys
sys.path.append('../')

# application imports
import os
clear = lambda: os.system('cls')

from util.pretalx_requests import PretalxAPI

# env variables
pretalx_api_token = os.getenv("pretalx_api_token")
pretalx_api_token = "{{ 自己去拿 }}" 

pretalx_endpoint = "https://pretalx.coscup.org"


def user_select_event(pretalx) -> int:
    events = pretalx.get_reqeust("/api/events")
    print("活動列表:")
    for index, event in enumerate(events):
        print("%d. %s" % (index, event['name']['zh-tw']))
    
    # first interaciton
    while True:
        event_index = input("請選擇活動 (輸入數字): ")
        # check input id in events index list ("user input".includes(events.map((i,e)=>i.toString())))
        if event_index in [str(_idx) for _idx, _ in enumerate(events)]:
           break
        print("請輸入存在的活動")

    return events[int(event_index)]

if __name__ == '__main__':
    pretalx = PretalxAPI(pretalx_endpoint, pretalx_api_token)

    # 
    selected_event = user_select_event(pretalx)
    
    # clear console
    clear()

    # prepare selected data
    event_id = selected_event['slug']
    print("您已選擇活動: %s" % (selected_event['name']['zh-tw']))  

    # second interation
    submissions = pretalx.get_reqeust("/api/events/%s/submissions" % ( event_id ))
    session_type_dict = {}
    for type_name in [proposal['submission_type']['zh-tw'] for proposal in submissions['results']]:
        session_type_dict[type_name] = True
    session_types = [session_type for _, session_type in enumerate(session_type_dict)]

    for index, session_type in enumerate(session_types):
        print("%d. %s" % (index, session_type))

    while True:
        session_type_index = input("請選議程軌 (輸入數字): ")
        # check input id in events index list ("user input".includes(events.map((i,e)=>i.toString())))
        if session_type_index in [str(_idx) for _idx, _ in enumerate(events)]:
           break
        print("請輸入存在的議程軌") 

    # 


