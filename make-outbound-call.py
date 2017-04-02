import pycurl
import time
import hashlib
from StringIO import StringIO

tcxc_host = "https://members.telecomsxchange.com";

# TCXC login
login = "Enter_Buyer_Username";

#TCXC API key generated from TelecomsXChange members portal:
api_key = "Your API KEY";

#TCXC i_account that you want to use for call billing
i_account = "0001";

#legA parameters
cld1 = "380913105503";
cli1 = "123123123123";
i_connection1 = "220";

#legB parameters
cld2 = "18667478647";
cli2 = "345345345";
i_connection2 = "220";

ts = int(time.time())

check_uri = "/api/callback/initiate/%s/%s/%s/%s/%s/%s/%s/%s/%d/" % (login, i_account, cld1, cli1, i_connection1, cld2, cli2, i_connection2, ts);

sign = hashlib.sha256("%s%s" % (check_uri, api_key));

call_url = "%s%s%s" % (tcxc_host, check_uri, sign.hexdigest() )

#print call_url

curl = pycurl.Curl()
curl.setopt(pycurl.URL, call_url )
curl.setopt(pycurl.HTTPGET, 1)
curl.setopt(pycurl.SSL_VERIFYPEER, 0)
curl.setopt(pycurl.SSL_VERIFYHOST, 0)
buff = StringIO()
curl.setopt(pycurl.WRITEFUNCTION, buff.write)
curl.perform()
print buff.getvalue()
