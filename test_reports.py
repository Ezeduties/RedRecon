from reports import ReportGenerator

sample_scan = {

    "ip": "10.0.9.5",

    "hostname": "Metasploitable2",

    "state": "up",

    "os": "Linux 2.6.9",

    "ports": [

        {
            "port": 21,
            "protocol": "tcp",
            "state": "open",
            "service": "ftp",
            "product": "vsftpd",
            "version": "2.3.4"
        },

        {
            "port": 22,
            "protocol": "tcp",
            "state": "open",
            "service": "ssh",
            "product": "OpenSSH",
            "version": "4.7p1"
        }

    ]

}

report = ReportGenerator(sample_scan)

csv_file = report.save_csv()

print("CSV Report Created")

print(csv_file)
