from drf_yasg import openapi


UNAUTHENTICATED = {"application/json": {"message": "Token is invalid or expired"}}

UNAUTHORIZED = {
    "application/json": {"message": "You are not authorized to perform this action."}
}


MONTHS_PARAMS = openapi.Parameter(
    "month", in_=openapi.IN_QUERY, description="Month (eg. 5)", type=openapi.TYPE_INTEGER
)

DASHBOARD_EXAMPLE = {
    "message": "success",
    "data": {
        "total_transaction": "5",
        "sum_of_income": "750000.0",
        "sum_of_expenses": "53101.0",
        "available_balance": "696899.0",
        "currency": "$",
        "top_income": [
            {
                "id": "b72c068a-bcd4-474e-a8f7-11ad4a4ea4d4",
                "amount": "400000.00",
                "source": "Salary",
                "description": "April Salary",
                "income_date": "2023-05-01"
            },
            {
                "id": "495fbdbc-4284-4ae9-8bf1-627a650203bc",
                "amount": "200000.00",
                "source": "Salary",
                "description": "Second Salary",
                "income_date": "2023-05-02"
            },
            {
                "id": "967b48c7-e26d-4f19-af41-08e3958462a4",
                "amount": "150000.00",
                "source": "Gift",
                "description": "Birthday gift",
                "income_date": "2023-05-02"
            }
        ],
        "top_expense": [
            {
                "id": "3f74ccad-2f1e-4ded-8d69-e5c6d6af513c",
                "amount": "30000.00",
                "description": "May Rent",
                "category": "Rent",
                "expense_date": "2023-05-21"
            },
            {
                "id": "07060286-64ec-4458-be83-767e4138b94c",
                "amount": "23101.00",
                "description": "May Rent",
                "category": "Rent",
                "expense_date": "2023-05-21"
            }
        ],
        "income_graph_data": [
            "400000.0",
            "150000.0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0"
        ],
        "expense_graph_data": [
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "23101.0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0"
        ],
        "days_label": [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31"
        ]
    },
    "errors": None
}



DASHBOARD_DATA = {"application/json": {"data": DASHBOARD_EXAMPLE}}

DASHBOARD_RESPONSE = {
    200: openapi.Response(
        examples=DASHBOARD_DATA, description="Analysis returned"
    ),
    401: openapi.Response(
        description="Invalid Authentication Token", examples=UNAUTHENTICATED
    ),
    403: openapi.Response(description="Invalid Permission", examples=UNAUTHORIZED),
}
