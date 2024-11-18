from parse_json_logs import parse_json_logs
import json
def test_parse_log():
    with open("caddylog.log.txt", "r") as f:
        log_file_content = f.read()

        parsed_logs = parse_json_logs(log_file_content)

        for log in parsed_logs:
            print(json.dumps(log))


