import socket  # ソケット通信を扱うためのモジュールをインポートします

# ソケットオブジェクトを作成します。AF_INETはIPv4、SOCK_DGRAMはUDPを指定しています。
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# UDPメッセージを送信します。バイト文字列"test"をローカルホスト（127.0.0.1）のポート80に送ります。
s.sendto(b"test", ("127.0.0.1", 80))

# サーバーからのレスポンスを受信します。4096バイトまで受け取る設定です。
# 受信したデータと送信元のアドレスを取得します。
data, addr = s.recvfrom(4096)

# 受信したデータを表示します。バイナリデータなので、文字列に変換して表示されます。
print(data)
