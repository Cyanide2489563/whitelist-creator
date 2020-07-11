import json
from mojang_api import Player

if __name__ == '__main__':
    print('載入資料中')
    file = open('message.txt', 'r')
    whitelist_file = open('whitelist.json', 'w')
    invalid_list_file = open('invalidlist.txt', 'w')

    data = file.read()
    names = data.split(',')
    whitelist = list()

    previous_name = ''
    duplicate = 0
    invalid = 0
    valid = 0
    for name in names:
        try:
            player = Player(username=name)
            if previous_name != name:
                whitelist.append({'uuid': player.uuid, 'name': name})
                valid += 1
                print(name)
                print(player.uuid)
            else:
                duplicate += 1
                print('玩家 ID 重複')
                print('玩家 ID：' + name)
            previous_name = name
        except KeyError:
            invalid += 1
            invalid_list_file.write(name + '\n')
            print('玩家不存在')
            print('玩家 ID：' + name)

    whitelist_file.write(json.dumps(whitelist, indent=4))
    print('已生成 whitelist.json')
    print('有效的玩家數量：' + str(valid))
    print('無效的玩家數量：' + str(invalid))
    print('重複的玩家數量：' + str(duplicate))
    file.close()
    whitelist_file.close()
    invalid_list_file.close()
