import urllib.request
import settings

endpoint = 'https://game.coderunner.jp'
token = settings.token
def submit(text):
    return _request('{0}/q?str={1}&token={2}'.format(endpoint, text, token))

def update_profile(text):
    return _request('{0}/profile?text={1}&token={2}'.format(endpoint, text, token))

def _request(url):
    try:
        res = url, urllib.request.urlopen(url).read(), None
    except urllib.error.HTTPError as e:
        res = url, None, e
    finally:
        f = open(settings.logs, 'a')
        f.writelines(map(lambda x: '{0}\n'.format(x), res))
        f.write('\n')
        f.close()
        return res

