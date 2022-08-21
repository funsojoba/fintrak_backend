import hashlib
import hmac
import json
from django.conf import settings


class NotificationPreferenceService:
    
    @classmethod
    def _verify(cls, signing_key, token, timestamp, signature):
        hmac_digest = hmac.new(
            key=signing_key.encode(), 
            msg=('{}{}'.format(timestamp, token)).encode(), 
            digestmod=hashlib.sha256).hexdigest()
        return hmac.compare_digest(str(signature), str(hmac_digest))
    
    
    @classmethod
    def update_preference(cls, request):
        signature_data = request.data.get("signature", "")
        is_verified = False
        if signature_data:
            is_verified: bool = cls._verify(
                signing_key = settings.NOTIFICATION_PREFERENCE_SIGNING_KEY,
                token = signature_data.get('token', ''),
                timestamp = signature_data.get("timestamp"),
                signature = signature_data.get("signature")
            )
        
        print("is_verified: ", is_verified)
        print("SIGNATURE: {}".format(signature_data))
        # print("TOKEN", signature_data.get('token', ''))
        print("JSON_", json.dumps(signature_data))
        print("Type: ", type(signature_data))
        print("REQUEST", request.data)
        # if not is_verified:
        #     print("Not verified", is_verified)
        # update the notifcation preference for the user
        # event_data = request.data.get("event_data")
        # event = event_data.get("event")
        # if event == "unsubscribed":
        #     event_data["event"] = "off" # update NotificationPreference to off
        
        return True