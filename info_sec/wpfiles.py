import queue
import threading
import os
import urllib.request
import urllib.error

# 使用するスレッドの数
threads = 10

# WordPressサイトのURL
wpurl = "http://192.168.0.6/blog"
# ローカルのWordPressディレクトリのパス
localwp = "/var/www/html/blog"
# フィルタリングするファイル拡張子
filters = [".jpg", ".gif", ".png", ".css", ".js"]

# カレントディレクトリをローカルのWordPressディレクトリに変更
os.chdir(localwp)

# ウェブパスを保持するキューを作成
web_paths = queue.Queue()

# ローカルのWordPressディレクトリを走査
for root, directory, files in os.walk("."):
    for file in files:
        remote_path = "%s/%s" % (root, file)
        if remote_path.startswith("."):
            remote_path = remote_path[1:]
        if os.path.splitext(file)[1] not in filters:
            web_paths.put(remote_path)

# リモートのファイルをテストする関数


def test_remote():
    # キューにまだパスがある間
    while not web_paths.empty():
        path = web_paths.get()
        url = "%s/%s" % (wpurl, path)

        request = urllib.request.Request(url)

        try:
            # URLを開いてみる
            response = urllib.request.urlopen(request)
            content = response.read()

            # レスポンスコードとパスを表示
            print("[%d]=>%s" % (response.code, path))

            response.close()

        except urllib.error.HTTPError as error:
            # HTTPエラーを無視
            pass


# スレッドを作成し開始
for i in range(threads):
    print("スレッドを実行中: %d" % i)
    t = threading.Thread(target=test_remote)
    t.start()
