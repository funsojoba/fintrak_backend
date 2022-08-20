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
        signature = request.data.get("signature", "")
        # is_verified: bool = cls._verify(
        #     signing_key = settings.NOTIFICATION_PREFERENCE_SIGNING_KEY,
        #     token = signature.get("token", ""),
        #     timestamp = signature.get("timestamp", ""),
        #     signature = signature.get("signature", "")
        # )
        
        print("SIGNATURE: {}".format(signature))
        # if not is_verified:
        #     print("Not verified", is_verified)
        # update the notifcation preference for the user
        # event_data = request.data.get("event_data")
        # event = event_data.get("event")
        # if event == "unsubscribed":
        #     event_data["event"] = "off" # update NotificationPreference to off
        
        return True