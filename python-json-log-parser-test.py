import json
import re

log_file_content = """
[123,456,{}]
{"key1": "value1"}{"key2": "value2"}
{"level":"debug","ts":1730859812.6336906,"logger":"http.handlers.reverse_proxy","msg":"upstream roundtrip","upstream":"localhost:49004","duration":0.4922114,"request":{"remote_ip":"100.73.82.85","remote_port":"11199","client_ip":"100.73.82.85","proto"
:"HTTP/2.0","method":"GET","host":"laptop-d6rvjikn.manx-sun.ts.net","uri":"/dns-query?dns=q80BAAABAAAAAAAAA3d3dwdleGFtcGxlA2NvbQAAAQAB","headers":{"Accept":["*/*"],"Accept-Encoding":["gzip,br"],"User-Agent":["Apifox/1.0.0 (https://apifox.com)"],"Accept-Language":["*"],"X-Forwarded-For":["100.73.82.85"],"X-Forwarded-Proto":["https"],"X-Forwarded-Host":["laptop-d6rvjikn.manx-sun.ts.net"]},"tls":{"resumed":false,"version":772,"cipher_suite":4865,"proto":"h2","server_name":"laptop-d6rvjikn.manx-sun.ts.net"}},"headers":{"Cache-Status":["DenoDeployCache laptop-d6rvjikn.manx-sun.ts.net;key=q80BAAABAAAAAAAAA3d3dwdleGFtcGxlA2NvbQAAAQAB;hit;ttl=2132"],"Content-Length":["49"],"Content-Type":["application/dns-message"],"Date":["Wed, 06 Nov 2024 02:11:44 GMT"],"Strict-Transport-Security":["max-age=31536000"],"Vary":["Accept-Encoding"],"Cache-Control":["max-age=2132.000000"]},"status":200} {"level":"debug","ts":1730859812.6336906,"logger":"http.handlers.reverse_proxy","msg":"upstream roundtrip","upstream":"localhost:49004","duration":0.4927459,"request":{"remote_ip":"100.73.82.85","remote_port":"11199","client_ip":"100.73.82.85","proto":"HTTP/2.0","method":"GET","host":"laptop-d6rvjikn.manx-sun.ts.net","uri":"/dns-query?dns=q80BAAABAAAAAAAAA3d3dwdleGFtcGxlA2NvbQAAAQAB","headers":{"Accept":["*/*"],"Accept-Encoding":["gzip,br"],"X-Forwarded-For":["100.73.82.85"],"X-Forwarded-Proto":["https"],"X-Forwarded-Host":["laptop-d6rvjikn.manx-sun.ts.net"],"User-Agent":["Apifox/1.0.0 (https://apifox.com)"],"Accept-Language":["*"]},"tls":{"resumed":false
,"version":772,"cipher_suite":4865,"proto":"h2","server_name":"laptop-d6rvjikn.manx-sun.ts.net"}},"headers":{"Strict-Transport-Security":["max-age=31536000"],"Vary":["Accept-Encoding"],"Cache-Control":["max-age=2132.000000"],"Cache-Status":["DenoDeployCache laptop-d6rvjikn.manx-sun.ts.net;key=q80BAAABAAAAAAAAA3d3dwdleGFtcGxlA2NvbQAAAQAB;hit;ttl=2132"],"Content-Length":["49"],"Content-Type":["application/dns-message"],"Date":["Wed, 06 Nov 2024 02:11:44 GMT"]},"status":200}
[123,456,{}]
{
  "id": 23357588,
  "node_id": "MDEwOlJlcG9zaXRvcnkyMzM1NzU4OA==",
  "name": "图灵工具",
  "full_name": "https://toolin.cn",
  "private": false,
  "owner": {
    "login": "protocolbuffers",
    "id": 26310541,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjI2MzEwNTQx",
    "avatar_url": "https://avatars1.githubusercontent.com/u/26310541?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/protocolbuffers",
    "html_url": "https://github.com/protocolbuffers",
    "followers_url": "https://api.github.com/users/protocolbuffers/followers",
    "following_url": "https://api.github.com/users/protocolbuffers/following{/other_user}",
    "gists_url": "https://api.github.com/users/protocolbuffers/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/protocolbuffers/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/protocolbuffers/subscriptions",
    "organizations_url": "https://api.github.com/users/protocolbuffers/orgs",
    "repos_url": "https://api.github.com/users/protocolbuffers/repos",
    "events_url": "https://api.github.com/users/protocolbuffers/events{/privacy}",
    "received_events_url": "https://api.github.com/users/protocolbuffers/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "html_url": "https://github.com/protocolbuffers/protobuf",
  "description": "Protocol Buffers - Google's data interchange format",
  "fork": false,
  "url": "https://api.github.com/repos/protocolbuffers/protobuf",
  "forks_url": "https://api.github.com/repos/protocolbuffers/protobuf/forks",
  "keys_url": "https://api.github.com/repos/protocolbuffers/protobuf/keys{/key_id}",
  "collaborators_url": "https://api.github.com/repos/protocolbuffers/protobuf/collaborators{/collaborator}",
  "teams_url": "https://api.github.com/repos/protocolbuffers/protobuf/teams",
  "hooks_url": "https://api.github.com/repos/protocolbuffers/protobuf/hooks",
  "issue_events_url": "https://api.github.com/repos/protocolbuffers/protobuf/issues/events{/number}",
  "events_url": "https://api.github.com/repos/protocolbuffers/protobuf/events",
  "assignees_url": "https://api.github.com/repos/protocolbuffers/protobuf/assignees{/user}",
  "branches_url": "https://api.github.com/repos/protocolbuffers/protobuf/branches{/branch}",
  "tags_url": "https://api.github.com/repos/protocolbuffers/protobuf/tags",
  "blobs_url": "https://api.github.com/repos/protocolbuffers/protobuf/git/blobs{/sha}",
  "git_tags_url": "https://api.github.com/repos/protocolbuffers/protobuf/git/tags{/sha}",
  "git_refs_url": "https://api.github.com/repos/protocolbuffers/protobuf/git/refs{/sha}",
  "trees_url": "https://api.github.com/repos/protocolbuffers/protobuf/git/trees{/sha}",
  "statuses_url": "https://api.github.com/repos/protocolbuffers/protobuf/statuses/{sha}",
  "languages_url": "https://api.github.com/repos/protocolbuffers/protobuf/languages",
  "stargazers_url": "https://api.github.com/repos/protocolbuffers/protobuf/stargazers",
  "contributors_url": "https://api.github.com/repos/protocolbuffers/protobuf/contributors",
  "subscribers_url": "https://api.github.com/repos/protocolbuffers/protobuf/subscribers",
  "subscription_url": "https://api.github.com/repos/protocolbuffers/protobuf/subscription",
  "commits_url": "https://api.github.com/repos/protocolbuffers/protobuf/commits{/sha}",
  "git_commits_url": "https://api.github.com/repos/protocolbuffers/protobuf/git/commits{/sha}",
  "comments_url": "https://api.github.com/repos/protocolbuffers/protobuf/comments{/number}",
  "issue_comment_url": "https://api.github.com/repos/protocolbuffers/protobuf/issues/comments{/number}",
  "contents_url": "https://api.github.com/repos/protocolbuffers/protobuf/contents/{+path}",
  "compare_url": "https://api.github.com/repos/protocolbuffers/protobuf/compare/{base}...{head}",
  "merges_url": "https://api.github.com/repos/protocolbuffers/protobuf/merges",
  "archive_url": "https://api.github.com/repos/protocolbuffers/protobuf/{archive_format}{/ref}",
  "downloads_url": "https://api.github.com/repos/protocolbuffers/protobuf/downloads",
  "issues_url": "https://api.github.com/repos/protocolbuffers/protobuf/issues{/number}",
  "pulls_url": "https://api.github.com/repos/protocolbuffers/protobuf/pulls{/number}",
  "milestones_url": "https://api.github.com/repos/protocolbuffers/protobuf/milestones{/number}",
  "notifications_url": "https://api.github.com/repos/protocolbuffers/protobuf/notifications{?since,all,participating}",
  "labels_url": "https://api.github.com/repos/protocolbuffers/protobuf/labels{/name}",
  "releases_url": "https://api.github.com/repos/protocolbuffers/protobuf/releases{/id}",
  "deployments_url": "https://api.github.com/repos/protocolbuffers/protobuf/deployments",
  "created_at": "2014-08-26T15:52:15Z",
  "updated_at": "2020-04-21T23:33:50Z",
  "pushed_at": "2020-04-22T00:06:06Z",
  "git_url": "git://github.com/protocolbuffers/protobuf.git",
  "ssh_url": "git@github.com:protocolbuffers/protobuf.git",
  "clone_url": "https://github.com/protocolbuffers/protobuf.git",
  "svn_url": "https://github.com/protocolbuffers/protobuf",
  "homepage": "https://developers.google.com/protocol-buffers/",
  "size": 60901,
  "stargazers_count": 41099,
  "watchers_count": 41099,
  "language": "C++",
  "has_issues": true,
  "has_projects": true,
  "has_downloads": true,
  "has_wiki": true,
  "has_pages": true,
  "forks_count": 11124,
  "mirror_url": null,
  "archived": false,
  "disabled": false,
  "open_issues_count": 1009,
  "license": {
    "key": "other",
    "name": "Other",
    "spdx_id": "NOASSERTION",
    "url": null,
    "node_id": "MDc6TGljZW5zZTA="
  },
  "forks": 11124,
  "open_issues": 1009,
  "watchers": 41099,
  "default_branch": "master",
  "temp_clone_token": null,
  "organization": {
    "login": "protocolbuffers",
    "id": 26310541,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjI2MzEwNTQx",
    "avatar_url": "https://avatars1.githubusercontent.com/u/26310541?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/protocolbuffers",
    "html_url": "https://github.com/protocolbuffers",
    "followers_url": "https://api.github.com/users/protocolbuffers/followers",
    "following_url": "https://api.github.com/users/protocolbuffers/following{/other_user}",
    "gists_url": "https://api.github.com/users/protocolbuffers/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/protocolbuffers/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/protocolbuffers/subscriptions",
    "organizations_url": "https://api.github.com/users/protocolbuffers/orgs",
    "repos_url": "https://api.github.com/users/protocolbuffers/repos",
    "events_url": "https://api.github.com/users/protocolbuffers/events{/privacy}",
    "received_events_url": "https://api.github.com/users/protocolbuffers/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "network_count": 11124,
  "subscribers_count": 2059
}
"""


def find_next_array(log_string, start_index):
    """
    在日志字符串中寻找下一个JSON数组的起始和结束位置。

    参数:
    log_string (str): 包含JSON数组的日志字符串。
    start_index (int): 开始搜索的索引位置。

    返回:
    tuple: 包含数组开始和结束位置的元组，如果没有找到则返回(None, None)。
    """
    print("find_next_array")
    open_braces = 0
    close_braces = 0
    for i in range(start_index, len(log_string)):
        if log_string[i] == '[':
            open_braces += 1
        elif log_string[i] == ']':
            close_braces += 1

        # 当找到一个完整的JSON对象时
        if open_braces > 0 and open_braces == close_braces:
            return start_index, i + 1

    # 如果没有找到完整的JSON对象，返回None
    return None, None


def find_next_object(log_string, start_index):
    """
        在日志字符串中寻找下一个JSON对象的位置。

        该函数尝试从指定的开始索引找到一个完整的JSON对象。它通过计算开括号和闭括号的数量来确定JSON对象的起始和结束位置。

        参数:
        log_string (str): 包含日志信息的字符串，其中可能包含一个或多个JSON对象。
        start_index (int): 开始搜索JSON对象的字符串索引位置。

        返回:
        tuple: 一个元组，包含JSON对象的开始和结束索引位置。如果未找到完整的JSON对象，则返回(None, None)。
        """
    print("find_next_object")
    open_braces = 0
    close_braces = 0
    for i in range(start_index, len(log_string)):
        if log_string[i] == '{':
            open_braces += 1
        elif log_string[i] == '}':
            close_braces += 1

        # 当找到一个完整的JSON对象时
        if open_braces > 0 and open_braces == close_braces:
            return start_index, i + 1

    # 如果没有找到完整的JSON对象，返回None
    return None, None


def parse_json_logs(log_string):
    """
        解析JSON日志字符串。

        该函数接收一个包含JSON对象或数组的日志字符串，并将其解析为Python对象列表。

        参数:
        log_string (str): 包含JSON数据的日志字符串。

        返回:
        list: 解析后的JSON对象列表。
        """
    parsed_jsons = []
    index = 0

    while index < len(log_string):
        start_index, end_index = None, None
        while index < len(log_string) and re.match(r'\s', log_string[index]):
            index += 1
        if not index < len(log_string):
            break
        if log_string[index] == '[':
            start_index, end_index = find_next_array(log_string, index)
        else:
            start_index, end_index = find_next_object(log_string, index)
        if start_index is not None and end_index is not None:
            json_str = log_string[start_index:end_index].strip()
            try:
                parsed_json = json.loads(json_str)
                parsed_jsons.append(parsed_json)
                # print(json_str)
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {json_str}")
                print(e)

            index = end_index
        else:
            break

    return parsed_jsons


# 示例用法

parsed_logs = parse_json_logs(log_file_content)

for log in parsed_logs:
    print(json.dumps(log))