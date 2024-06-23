import socket  # ソケット通信を扱うためのモジュールをインポートします

# ソケットオブジェクトを作成します。
# AF_INETはIPv4、SOCK_RAWは生のソケット（パケットレベルで操作できる）、
# IPPROTO_ICMPはICMPプロトコルを指定しています。
sniff = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

# ソケットをローカルホスト（127.0.0.1）の任意のポート（0）にバインドします。
sniff.bind(("127.0.0.1", 0))

# ソケットオプションを設定します。IP_HDRINCLを1に設定することで、
# パケットにIPヘッダーを含めるように指示します。
sniff.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# スニッファーがリスニングを開始したことを通知します。
print("Sniffer is listening!")

# パケットを受信し、受信したデータを表示します。
print(sniff.recvfrom(4096))
