import re
import responses2oai as resp
import actions
import audio
import keyboard

FILE = "D:\cods\pythonCode\AI project\\responsesConfig.txt"

def getResponse(comment):
    split_comment = re.split(r'\s+|[,;?!.-]\s*', comment.lower())
    response = check_commment(split_comment)
    return response

def check_commment(comment):
    highest_prob_list = {}
    def response(bot_resp, list_of_words, single_resp=False, require_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_resp] = massage_prob(comment, list_of_words, single_resp, require_words)
    for a_respone in resp.botResponse():
        if len(a_respone) == 4:
            response(a_respone[0], a_respone[1], single_resp=a_respone[2], require_words=a_respone[3])
        else:
            if a_respone[2] == (True or False):
                response(a_respone[0], a_respone[1], single_resp=a_respone[2])
            else:
                response(a_respone[0], a_respone[1], require_words=a_respone[2])
        best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return resp.unknown () if highest_prob_list[best_match] < 1 else best_match


def massage_prob(comment, reconised_words, single_resp=False, require_words=[]):
    massge_cert = 0
    has_require_words = True
    for word in comment:
        if word in reconised_words:
            massge_cert += 1

    percentage = float(massge_cert) / float(len(reconised_words))
    for word in reconised_words:
        if word not in comment:
            has_require_words = False
            break

    if has_require_words or single_resp:
        return int(percentage * 100)
    else:
        return 0

def main():
    answer = ''
    while not keyboard.is_pressed('s'):
        ans = audio.get_audio()
        if "Vladimir" in ans:
            if getResponse(ans) not in resp.action_list:
                answer = getResponse(ans)
            else:
                answer = actions.doAction(getResponse(ans))
            audio.speak(answer)

if __name__ == "__main__":
    main()