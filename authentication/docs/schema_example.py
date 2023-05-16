from drf_yasg import openapi


INVALID_CREDENTIALS = {
    "application/json": {
        "error": "invalid credentials"
    }
}



LOGIN_EXAMPLE = {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NDM0NzU0NywiaWF0IjoxNjg0MjYxMTQ3LCJqdGkiOiI0NDcxNWNlNTZkZjk0ZTdlOWM0ZGZmMjM2MzIxOTczMyIsInVzZXJfaWQiOiIzYWI2M2E0Mi1kNWMyLTRhMjktYWZiNS00YTQwNDEwNDAxZjAifQ.EnpdREcu0cwGnECG-Yv8OCpeQpQQC-GzEB2TVgHlYBs",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg0MzQ3NTQ3LCJpYXQiOjE2ODQyNjExNDcsImp0aSI6Ijg3NWVjNjQ2NzVjMzQ1M2VhYWFiYWQ2NWRhNTA0YjRlIiwidXNlcl9pZCI6IjNhYjYzYTQyLWQ1YzItNGEyOS1hZmI1LTRhNDA0MTA0MDFmMCJ9.ZmE0VRosk1H-W_Xn_X-2zY013XhdvoeOgVaZH9CuLbU"
}

LOGIN_DATA = {
    "application/json": {"data": LOGIN_EXAMPLE}
}


REGISTRATION_EXAMPLE = {
    "message": "success",
    "data": {
        "message": "Registration successful",
        "status": True
    },
    "errors": None
}

REGISTRATION_DATA = {
    "application/json": {"data": REGISTRATION_EXAMPLE}
}


LOGIN_RESPONSE = {
    200: openapi.Response(
        description="Access token generated successfully", examples=LOGIN_DATA
    ),
    400: openapi.Response(description="Invalid credentials", examples=INVALID_CREDENTIALS)
}

REGISTRATION_RESPONSE = {
    200: openapi.Response(
        description="User registered successfully", examples=REGISTRATION_DATA
    ),
    400: openapi.Response(description="Invalid credentials", examples=INVALID_CREDENTIALS)
}
