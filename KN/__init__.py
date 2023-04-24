from KN.LGOEnvironment import LGOEnvironment

environments = [
    LGOEnvironment(
        q_question="Alexandre",
        q_answer="True"
    )
]


def provision_lgo_dashboards():
    for env in environments:
        print(env)


provision_lgo_dashboards()
