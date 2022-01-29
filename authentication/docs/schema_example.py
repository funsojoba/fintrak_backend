from drf_yasg import openapi

EMAIL_REGISTRATION_INPUT = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "provider_type": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="Provider Type",
            enum=["AI", "DISI", "OEMI"],
        ),
        "email": openapi.Schema(type=openapi.TYPE_STRING, description="Provider Email"),
    },
)

PHONE_REGISTRATION_INPUT = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "provider_type": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="Provider Type",
            enum=["AI", "DISI", "OEMI"],
        ),
        "phone_number": openapi.Schema(
            type=openapi.TYPE_STRING, description="Provider Phone"
        ),
    },
)

COMPLETE_REGISTRATION_INPUT = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "first_name": openapi.Schema(
            type=openapi.TYPE_STRING, description="Provider First Name"
        ),
        "last_name": openapi.Schema(
            type=openapi.TYPE_STRING, description="Provider Last Name"
        ),
        "provider_type": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="Provider Type",
            enum=["AI", "DISI", "OEMI"],
        ),
        "phone_number": openapi.Schema(
            type=openapi.TYPE_STRING, description="Provider Phone"
        ),
        "email": openapi.Schema(type=openapi.TYPE_STRING, description="Provider Email"),
        "company_name": openapi.Schema(
            type=openapi.TYPE_STRING, description="Provider Company Name"
        ),
        "password": openapi.Schema(
            type=openapi.TYPE_STRING, description="Provider Password"
        ),
    },
)

LOGOUT_INPUT = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "access_token": openapi.Schema(
            type=openapi.TYPE_STRING, description="Access Token"
        )
    },
)

REGISTRATION_SUCCESS_RESPONSE = {
    "application/json": {
        "data": {
            "id": "59a6119e771c4aa09fc8276506d3bae5",
            "first_name": "Jesse",
            "last_name": "Bingo",
            "company_name": "Balh Blah Inc",
        }
    }
}

EMAIL_REGISTRATION_EXISITING_USER_RESPONSE = {
    "application/json": {
        "errors": {"email": ["A user has already registered with this email address"]}
    }
}

PHONE_REGISTRATION_EXISITING_USER_RESPONSE = {
    "application/json": {
        "errors": {
            "phone_number": ["A user has already registered with this phone number"]
        }
    }
}


EMAIL_REGISTRATION_BAD_INPUT_RESPONSE = {
    "application/json": {
        "errors": {
            "email": ["Enter a valid email address."],
            "provider_type": ["This field is required."],
        }
    }
}

PHONE_REGISTRATION_BAD_INPUT_RESPONSE = {
    "application/json": {
        "errors": {
            "phone_number": ["This field is required."],
            "provider_type": ["This field is required."],
        }
    }
}

COMPLETE_REGISTRATION_SUCCESS_RESPONSE = {
    "application/json": {
        "data": {
            "id": "2322f9b3d0774c28904f2ae2dfc197e9",
            "first_name": None,
            "last_name": None,
            "company_name": "Bingo3",
            "email": "jesseinit1345@gmail.com",
            "phone_number": "+2348064667317",
            "provider_type": {"name": "Distributor Installer", "identifier": "DISI"},
        }
    }
}

COMPLETE_REGISTRATION_BAD_INPUT_RESPONSE = {
    "application/json": {
        "errors": {
            "email": ["Enter a valid email address."],
            "password": [
                "Password should be aleast 8-32 characters long and should contain upper, lower case letters and numbers"
            ],
            "company_name": ["This field is required."],
        }
    }
}


LOGIN_SUCCESS_RESPONSE = {
    "application/json": {
        "data": {
            "user": {
                "id": "4a62dd1780834c4e83458067e2829cfb",
                "first_name": "Jesse",
                "last_name": "Bingo",
            },
            "token": {
                "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9....",
                "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9....",
            },
        }
    }
}

LOGIN_WITH_EMAIL_UNAUTHORISED_RESPONSE = {
    "application/json": {"message": "Email or password is not correct"}
}

LOGIN_WITH_EMAIL_BAD_INPUT_RESPONSE = {
    "application/json": {
        "errors": {
            "email": ["This field is required."],
            "password": ["This field is required."],
        }
    }
}

LOGIN_WITH_PHONE_UNAUTHORISED_RESPONSE = {
    "application/json": {"message": "Phone number or password is not correct"}
}

LOGIN_WITH_PHONE_BAD_INPUT_RESPONSE = {
    "application/json": {
        "errors": {
            "phone_number": ["This field is required."],
            "password": ["This field is required."],
        }
    }
}

PASSWORD_RESET_INITIATE_SUCCESS_RESPONSE = {
    "application/json": {"data": {"completed": True, "action": "PASSWORD_RESET"}}
}
PASSWORD_RESET_INITIATE_BAD_INPUT_RESPONSE = {
    "application/json": {"errors": {"email": ["This field is required."]}}
}

PASSWORD_RESET_VALIDATE_SUCCESS_RESPONSE = {
    "application/json": {"data": {"reset_token": "574f8fe2f1b644878fa24ec850e95...."}}
}
PASSWORD_RESET_VALIDATE_BAD_INPUT_RESPONSE = {
    "application/json": {
        "errors": {
            "reset_token": ["This field is required."],
            "reset_code": ["This field is required."],
        }
    }
}
PASSWORD_RESET_FINALIZE_SUCCESS_RESPONSE = {"application/json": {"data": True}}
PASSWORD_RESET_FINALIZE_BAD_INPUT_RESPONSE = {
    "application/json": {
        "errors": {
            "reset_token": ["This field is required."],
            "new_password": ["This field is required."],
        }
    }
}

EMAIL_REGISTRATION_RESPONSES = {
    201: openapi.Response(
        description="Created User", examples=REGISTRATION_SUCCESS_RESPONSE
    ),
    400: openapi.Response(
        description="Bad Input", examples=EMAIL_REGISTRATION_BAD_INPUT_RESPONSE
    ),
    409: openapi.Response(
        description="Existing User", examples=EMAIL_REGISTRATION_EXISITING_USER_RESPONSE
    ),
}

PHONE_REGISTRATION_RESPONSES = {
    201: openapi.Response(
        description="Created User", examples=REGISTRATION_SUCCESS_RESPONSE
    ),
    400: openapi.Response(
        description="Bad Input", examples=PHONE_REGISTRATION_BAD_INPUT_RESPONSE
    ),
    409: openapi.Response(
        description="Existing User", examples=PHONE_REGISTRATION_EXISITING_USER_RESPONSE
    ),
}

COMPLETE_REGISTRATION_RESPONSES = {
    200: openapi.Response(
        description="Complete User Signup",
        examples=COMPLETE_REGISTRATION_SUCCESS_RESPONSE,
    ),
    400: openapi.Response(
        description="Bad Input", examples=COMPLETE_REGISTRATION_BAD_INPUT_RESPONSE
    ),
}


LOGIN_WITH_EMAIL_RESPONSES = {
    200: openapi.Response(
        description="Successful Login", examples=LOGIN_SUCCESS_RESPONSE
    ),
    400: openapi.Response(
        description="Bad Input", examples=LOGIN_WITH_EMAIL_BAD_INPUT_RESPONSE
    ),
    401: openapi.Response(
        description="Invalid Credentials",
        examples=LOGIN_WITH_EMAIL_UNAUTHORISED_RESPONSE,
    ),
}

LOGIN_WITH_PHONE_RESPONSES = {
    200: openapi.Response(
        description="Successful Login", examples=LOGIN_SUCCESS_RESPONSE
    ),
    400: openapi.Response(
        description="Bad Input", examples=LOGIN_WITH_PHONE_BAD_INPUT_RESPONSE
    ),
    401: openapi.Response(
        description="Invalid Credentials",
        examples=LOGIN_WITH_PHONE_UNAUTHORISED_RESPONSE,
    ),
}

PASSWORD_RESET_INITIATE_RESPONSES = {
    200: openapi.Response(
        description="Password Reset Initiate Success",
        examples=PASSWORD_RESET_INITIATE_SUCCESS_RESPONSE,
    ),
    400: openapi.Response(
        description="Bad Input", examples=PASSWORD_RESET_INITIATE_BAD_INPUT_RESPONSE
    ),
}

PASSWORD_RESET_VALIDATE_RESPONSES = {
    200: openapi.Response(
        description="Password Reset Validate Success",
        examples=PASSWORD_RESET_VALIDATE_SUCCESS_RESPONSE,
    ),
    400: openapi.Response(
        description="Bad Input", examples=PASSWORD_RESET_VALIDATE_BAD_INPUT_RESPONSE
    ),
}

SET_AVATAR_SUCCESS_RESPONSE = {"application/json": {"data": True}}

SET_AVATAR_BAD_INPUT_RESPONSE = {
    "application/json": {"errors": {"image": ["This field is required."]}}
}

SET_AVATAR_RESPONSES = {
    200: openapi.Response(
        description="Set Avatar Success", examples=SET_AVATAR_SUCCESS_RESPONSE
    ),
    400: openapi.Response(
        description="Bad Input", examples=SET_AVATAR_BAD_INPUT_RESPONSE
    ),
}

PASSWORD_RESET_FINALIZE_RESPONSES = {
    200: openapi.Response(
        description="Password Reset Finalize Success",
        examples=PASSWORD_RESET_FINALIZE_SUCCESS_RESPONSE,
    ),
    400: openapi.Response(
        description="Bad Input", examples=PASSWORD_RESET_FINALIZE_BAD_INPUT_RESPONSE
    ),
}

EMAIL_VERIFICATION_SUCCESS_RESPONSE = {
    "application/json": {"data": {"completed": True, "action": "EMAIL_VERIFICATION"}}
}

EMAIL_VERIFICATION_OUTPUT_RESPONSES = {
    200: openapi.Response(
        description="Verification Resend Success",
        examples=EMAIL_VERIFICATION_SUCCESS_RESPONSE,
    )
}

PHONE_VERIFICATION_SUCCESS_RESPONSE = {
    "application/json": {"data": {"completed": True, "action": "PHONE_VERIFICATION"}}
}


PHONE_VERIFICATION_OUTPUT_RESPONSES = {
    200: openapi.Response(
        description="Verification Resend Success",
        examples=PHONE_VERIFICATION_SUCCESS_RESPONSE,
    )
}

LOGOUT_SUCCESS_RESPONSE = {
    "application/json": {"data": {}, "message": "successfully logged out"}
}

LOGOUT_RESPONSES = {
    200: openapi.Response(
        description="Successfully logged out", examples=LOGIN_SUCCESS_RESPONSE
    )
}

CHANGE_PASSWORD_SUCCESS_RESPONSE = {
    "application/json": {"data": {}, "message": "password changed successfully"}
}

CHANGE_PASSWORD_BAD_INPUT_RESPONSE = {
    "application/json": [
        {"errors": {"old_password": ["Password is incorrect"]}},
        {"message": "Old password cannot be same as new password"},
    ]
}


GET_USER_DATA_ERROR = {"application/json": [{"message": "Token is invalid or expired"}]}

USER_DATA_EXAMPLE = {
    "id": "07adf107f41c48d282dea1438bdf41a3",
    "first_name": "Danny",
    "last_name": "reigns",
    "street_address": None,
    "city": None,
    "state_of_residence": None,
    "bio": "",
    "education_level": None,
    "email_verified": True,
    "phone_verified": False,
    "state": "ACTIVE",
    "user_types": ["STAFF", "CONSUMER"],
    "email": "dannyreigns015@gmail.com",
    "phone_number": "07037265628",
    "last_login": "2021-12-03T13:27:03.880722Z",
    "provider": {
        "company_name": "Osnuf Comp And Co.",
        "type": {"name": "ASI", "identifier": "AI"},
        "status": "APPROVED",
        "member": False,
    },
    "created_at": "2021-11-16T16:02:34.635435Z",
    "updated_at": "2021-12-03T13:27:03.891243Z",
    "avatar_url": None,
    "role": None,
    "created_by": None,
    "updated_by": None,
    "deleted_by": None,
    "next_stage": None,
    "last_completed_stage": "COMPLETED_SIGN_UP",
}

USER_DATA = {"application/json": {"data": USER_DATA_EXAMPLE, "message": ""}}


USER_ACTIVITY_EXAMPLE = {
    "data": [
        {
            "id": "f379be339dda4621a9761a250b8fca70",
            "category": "ESTIMATIONS",
            "action": "ESTIMATION_APPROVED",
            "performed_by": {
                "id": "07adf107f41c48d282dea1438bdf41a3",
                "first_name": "Danny",
                "last_name": "reigns",
                "street_address": None,
                "city": None,
                "state_of_residence": None,
                "bio": "",
                "education_level": None,
                "email_verified": True,
                "phone_verified": False,
                "state": "ACTIVE",
                "user_types": ["STAFF", "CONSUMER"],
                "email": "dannyreigns015@gmail.com",
                "phone_number": "07037265628",
                "last_login": "2021-12-03T13:27:03.880722Z",
                "provider": {
                    "company_name": "Osnuf Comp And Co.",
                    "type": {"name": "ASI", "identifier": "AI"},
                    "status": "APPROVED",
                    "member": False,
                },
                "created_at": "2021-11-16T16:02:34.635435Z",
                "updated_at": "2021-12-03T13:27:03.891243Z",
                "avatar_url": None,
                "role": None,
                "created_by": None,
                "updated_by": None,
                "deleted_by": None,
            },
            "created_at": "2021-11-30T15:49:13.514749Z",
            "consumer": {
                "user": {
                    "id": "07adf107f41c48d282dea1438bdf41a3",
                    "first_name": "Danny",
                    "last_name": "reigns",
                    "street_address": None,
                    "city": None,
                    "state_of_residence": None,
                    "bio": "",
                    "education_level": None,
                    "email_verified": True,
                    "phone_verified": False,
                    "state": "ACTIVE",
                    "user_types": ["STAFF", "CONSUMER"],
                    "email": "dannyreigns015@gmail.com",
                    "phone_number": "07037265628",
                    "last_login": "2021-12-03T13:27:03.880722Z",
                    "provider": {
                        "company_name": "Osnuf Comp And Co.",
                        "type": {"name": "ASI", "identifier": "AI"},
                        "status": "APPROVED",
                        "member": False,
                    },
                    "created_at": "2021-11-16T16:02:34.635435Z",
                    "updated_at": "2021-12-03T13:27:03.891243Z",
                    "avatar_url": None,
                    "role": None,
                    "created_by": None,
                    "updated_by": None,
                    "deleted_by": None,
                }
            },
        },
        {
            "id": "2e73aac0f4784741ab3edb6ec1d897d9",
            "category": "ESTIMATIONS",
            "action": "ESTIMATION_APPROVED",
            "performed_by": {
                "id": "07adf107f41c48d282dea1438bdf41a3",
                "first_name": "Danny",
                "last_name": "reigns",
                "street_address": None,
                "city": None,
                "state_of_residence": None,
                "bio": "",
                "education_level": None,
                "email_verified": True,
                "phone_verified": False,
                "state": "ACTIVE",
                "user_types": ["STAFF", "CONSUMER"],
                "email": "dannyreigns015@gmail.com",
                "phone_number": "07037265628",
                "last_login": "2021-12-03T13:27:03.880722Z",
                "provider": {
                    "company_name": "Osnuf Comp And Co.",
                    "type": {"name": "ASI", "identifier": "AI"},
                    "status": "APPROVED",
                    "member": False,
                },
                "created_at": "2021-11-16T16:02:34.635435Z",
                "updated_at": "2021-12-03T13:27:03.891243Z",
                "avatar_url": None,
                "role": None,
                "created_by": None,
                "updated_by": None,
                "deleted_by": None,
            },
            "created_at": "2021-11-25T08:21:59.348317Z",
            "consumer": {
                "user": {
                    "id": "07adf107f41c48d282dea1438bdf41a3",
                    "first_name": "Danny",
                    "last_name": "reigns",
                    "street_address": None,
                    "city": None,
                    "state_of_residence": None,
                    "bio": "",
                    "education_level": None,
                    "email_verified": True,
                    "phone_verified": False,
                    "state": "ACTIVE",
                    "user_types": ["STAFF", "CONSUMER"],
                    "email": "dannyreigns015@gmail.com",
                    "phone_number": "07037265628",
                    "last_login": "2021-12-03T13:27:03.880722Z",
                    "provider": {
                        "company_name": "Osnuf Comp And Co.",
                        "type": {"name": "ASI", "identifier": "AI"},
                        "status": "APPROVED",
                        "member": False,
                    },
                    "created_at": "2021-11-16T16:02:34.635435Z",
                    "updated_at": "2021-12-03T13:27:03.891243Z",
                    "avatar_url": None,
                    "role": None,
                    "created_by": None,
                    "updated_by": None,
                    "deleted_by": None,
                }
            },
        },
        {
            "id": "6c5a6e62619a4e2bb5c707f9c64f1fcd",
            "category": "ESTIMATIONS",
            "action": "ESTIMATION_APPROVED",
            "performed_by": {
                "id": "07adf107f41c48d282dea1438bdf41a3",
                "first_name": "Danny",
                "last_name": "reigns",
                "street_address": None,
                "city": None,
                "state_of_residence": None,
                "bio": "",
                "education_level": None,
                "email_verified": True,
                "phone_verified": False,
                "state": "ACTIVE",
                "user_types": ["STAFF", "CONSUMER"],
                "email": "dannyreigns015@gmail.com",
                "phone_number": "07037265628",
                "last_login": "2021-12-03T13:27:03.880722Z",
                "provider": {
                    "company_name": "Osnuf Comp And Co.",
                    "type": {"name": "ASI", "identifier": "AI"},
                    "status": "APPROVED",
                    "member": False,
                },
                "created_at": "2021-11-16T16:02:34.635435Z",
                "updated_at": "2021-12-03T13:27:03.891243Z",
                "avatar_url": None,
                "role": None,
                "created_by": None,
                "updated_by": None,
                "deleted_by": None,
            },
            "created_at": "2021-11-24T16:10:32.627491Z",
            "consumer": {
                "user": {
                    "id": "07adf107f41c48d282dea1438bdf41a3",
                    "first_name": "Danny",
                    "last_name": "reigns",
                    "street_address": None,
                    "city": None,
                    "state_of_residence": None,
                    "bio": "",
                    "education_level": None,
                    "email_verified": True,
                    "phone_verified": False,
                    "state": "ACTIVE",
                    "user_types": ["STAFF", "CONSUMER"],
                    "email": "dannyreigns015@gmail.com",
                    "phone_number": "07037265628",
                    "last_login": "2021-12-03T13:27:03.880722Z",
                    "provider": {
                        "company_name": "Osnuf Comp And Co.",
                        "type": {"name": "ASI", "identifier": "AI"},
                        "status": "APPROVED",
                        "member": False,
                    },
                    "created_at": "2021-11-16T16:02:34.635435Z",
                    "updated_at": "2021-12-03T13:27:03.891243Z",
                    "avatar_url": None,
                    "role": None,
                    "created_by": None,
                    "updated_by": None,
                    "deleted_by": None,
                }
            },
        },
        {
            "id": "693811fa1da14107bc8ba9cd9166e9e1",
            "category": "ESTIMATIONS",
            "action": "ESTIMATION_DECLINED",
            "performed_by": {
                "id": "07adf107f41c48d282dea1438bdf41a3",
                "first_name": "Danny",
                "last_name": "reigns",
                "street_address": None,
                "city": None,
                "state_of_residence": None,
                "bio": "",
                "education_level": None,
                "email_verified": True,
                "phone_verified": False,
                "state": "ACTIVE",
                "user_types": ["STAFF", "CONSUMER"],
                "email": "dannyreigns015@gmail.com",
                "phone_number": "07037265628",
                "last_login": "2021-12-03T13:27:03.880722Z",
                "provider": {
                    "company_name": "Osnuf Comp And Co.",
                    "type": {"name": "ASI", "identifier": "AI"},
                    "status": "APPROVED",
                    "member": False,
                },
                "created_at": "2021-11-16T16:02:34.635435Z",
                "updated_at": "2021-12-03T13:27:03.891243Z",
                "avatar_url": None,
                "role": None,
                "created_by": None,
                "updated_by": None,
                "deleted_by": None,
            },
            "created_at": "2021-11-24T16:03:54.879272Z",
            "consumer": {
                "user": {
                    "id": "07adf107f41c48d282dea1438bdf41a3",
                    "first_name": "Danny",
                    "last_name": "reigns",
                    "street_address": None,
                    "city": None,
                    "state_of_residence": None,
                    "bio": "",
                    "education_level": None,
                    "email_verified": True,
                    "phone_verified": False,
                    "state": "ACTIVE",
                    "user_types": ["STAFF", "CONSUMER"],
                    "email": "dannyreigns015@gmail.com",
                    "phone_number": "07037265628",
                    "last_login": "2021-12-03T13:27:03.880722Z",
                    "provider": {
                        "company_name": "Osnuf Comp And Co.",
                        "type": {"name": "ASI", "identifier": "AI"},
                        "status": "APPROVED",
                        "member": False,
                    },
                    "created_at": "2021-11-16T16:02:34.635435Z",
                    "updated_at": "2021-12-03T13:27:03.891243Z",
                    "avatar_url": None,
                    "role": None,
                    "created_by": None,
                    "updated_by": None,
                    "deleted_by": None,
                }
            },
        },
        {
            "id": "fe672e17cb5e45b5914686fb514ca84a",
            "category": "ESTIMATIONS",
            "action": "ESTIMATION_DECLINED_AND_RE_ESTIMATE",
            "performed_by": {
                "id": "07adf107f41c48d282dea1438bdf41a3",
                "first_name": "Danny",
                "last_name": "reigns",
                "street_address": None,
                "city": None,
                "state_of_residence": None,
                "bio": "",
                "education_level": None,
                "email_verified": True,
                "phone_verified": False,
                "state": "ACTIVE",
                "user_types": ["STAFF", "CONSUMER"],
                "email": "dannyreigns015@gmail.com",
                "phone_number": "07037265628",
                "last_login": "2021-12-03T13:27:03.880722Z",
                "provider": {
                    "company_name": "Osnuf Comp And Co.",
                    "type": {"name": "ASI", "identifier": "AI"},
                    "status": "APPROVED",
                    "member": False,
                },
                "created_at": "2021-11-16T16:02:34.635435Z",
                "updated_at": "2021-12-03T13:27:03.891243Z",
                "avatar_url": None,
                "role": None,
                "created_by": None,
                "updated_by": None,
                "deleted_by": None,
            },
            "created_at": "2021-11-24T15:05:52.095637Z",
            "consumer": {
                "user": {
                    "id": "07adf107f41c48d282dea1438bdf41a3",
                    "first_name": "Danny",
                    "last_name": "reigns",
                    "street_address": None,
                    "city": None,
                    "state_of_residence": None,
                    "bio": "",
                    "education_level": None,
                    "email_verified": True,
                    "phone_verified": False,
                    "state": "ACTIVE",
                    "user_types": ["STAFF", "CONSUMER"],
                    "email": "dannyreigns015@gmail.com",
                    "phone_number": "07037265628",
                    "last_login": "2021-12-03T13:27:03.880722Z",
                    "provider": {
                        "company_name": "Osnuf Comp And Co.",
                        "type": {"name": "ASI", "identifier": "AI"},
                        "status": "APPROVED",
                        "member": False,
                    },
                    "created_at": "2021-11-16T16:02:34.635435Z",
                    "updated_at": "2021-12-03T13:27:03.891243Z",
                    "avatar_url": None,
                    "role": None,
                    "created_by": None,
                    "updated_by": None,
                    "deleted_by": None,
                }
            },
        },
    ],
    "message": "",
}

USER_ACTIVITY_DATA = {
    "application/json": {"data": USER_ACTIVITY_EXAMPLE, "message": ""}
}


CHANGE_PASSWORD_RESPONSES = {
    200: openapi.Response(
        description="Password Changed Successfully",
        examples=CHANGE_PASSWORD_SUCCESS_RESPONSE,
    ),
    400: openapi.Response(
        description="Wrong Password Input", examples=CHANGE_PASSWORD_BAD_INPUT_RESPONSE
    ),
}


GET_USER_DATA = {
    200: openapi.Response(
        description="retrieved user data successfully", examples=USER_DATA
    ),
    403: openapi.Response(description="Unathorized", example=GET_USER_DATA_ERROR),
}

GET_USER_ACTIVITIES = {
    200: openapi.Response(
        description="retrieved user data successfully", examples=USER_ACTIVITY_DATA
    ),
    403: openapi.Response(description="Unathorized", example=GET_USER_DATA_ERROR),
}
