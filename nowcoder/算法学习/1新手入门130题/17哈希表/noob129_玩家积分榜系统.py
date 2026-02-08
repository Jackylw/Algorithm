# https://www.nowcoder.com/practice/5b5cb654caa249eb979e4be483e36c1e
def insert_or_update_score(name, score):
    """插入或更新玩家的分数"""
    user_map[name] = score


def query_score(name):
    """查询玩家的分数"""
    if name in user_map:
        return user_map[name]
    else:
        return "Not found"


def delete_player(name):
    """删除玩家记录"""
    if name in user_map:
        del user_map[name]
        return "Deleted successfully"
    else:
        return "Not found"


def count_players():
    """统计玩家总数"""
    return len(user_map)


user_map = {}
Q = int(input())
for _ in range(Q):
    opts = list(map(str, input().split()))
    if opts[0] == '1':
        insert_or_update_score(opts[1], opts[2])
        print("OK")
    elif opts[0] == '2':
        print(query_score(opts[1]))
    elif opts[0] == '3':
        print(delete_player(opts[1]))
    elif opts[0] == '4':
        print(count_players())

