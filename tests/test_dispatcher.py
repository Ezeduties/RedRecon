from core.dispatcher import Dispatcher

dispatcher = Dispatcher()

services = [

    ("10.0.9.5", 21, "ftp"),

    ("10.0.9.5", 22, "ssh"),

    ("10.0.9.5", 25, "smtp"),

    ("10.0.9.5", 80, "http"),

    ("10.0.9.5", 443, "https")

]

for host, port, service in services:

    print("=" * 60)

    print(service.upper())

    evidence = dispatcher.dispatch(
        host,
        port,
        service
    )

    if evidence:

        print(evidence)

    else:

        print("No evidence collected.")
