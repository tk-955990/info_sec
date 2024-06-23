import socket  # ソケット通信を扱うためのモジュールをインポートします

# ソケットオブジェクトを作成します。AF_INETはIPv4、SOCK_STREAMはTCPを指定しています。
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 作成したソケットでGoogleのウェブサーバー（ポート80）に接続します。
s.connect(('www.google.com', 80))

# HTTP GETリクエストを送信します。バイト文字列で送信する必要があります。
# HTTP/1.1を使用し、Hostヘッダーでgoogle.co.jpを指定しています。
s.send(b'GET / HTTP/1.1\r\nHost: google.co.jp\r\n\r\n')

# サーバーからのレスポンスを受信します。4096バイトまで受け取る設定です。
response = s.recv(4096)

# 受信したレスポンスを表示します。バイナリデータなので、文字列に変換して表示されます。
print(response)
