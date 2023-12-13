```py
## windows cmd
ping -n 10// 預設值會丟4個icmp封包，那就設定一次丟10個
ping -t  // 狂丟到你停止 ctrl+c
ping -4  // 單測ipv4
ping -6  // 單測ipv6
ping -a  // 反解DNS名稱
ping -l 1280 -f // 指定封包大小(1280) 並禁止切割封包

## linux cil
ping -c 4    // 丟4個icmp封包
ping -i 0.4  // 每隔0.4秒丟一次
ping -I eth0 // 參數指定要測試網卡
ping -s 1280 -M //  指定封包大小(1280) 並禁止切割封包

```
```php
-d <data>            //POST的請求中，指定 <data> 到HTTP Server

# Post data:
curl -d password=x http://x.com/y
```
```
-H <header/@file>    //GET模式下，指定回傳JSON格式
# curl -H "Content-Type: application/json" www.example.com

curl -k              //****跳過驗證步驟並繼續連線而不進行檢查。
# curl --location --request GET -k 'https://192.168.0.14:12345' 

-o <file>    # --output: write to file
--output <file>     //將連線的輸出資訊寫到指定的檔案中
# curl -o output.txt https://www.google.com
```
```bash
# Use Curl to Check if a remote resource is available
# details: https://matthewsetter.com/check-if-file-is-available-with-curl/
curl -o /dev/null --silent -Iw "%{http_code}" https://example.com/my.remote.tarball.gz
```
```php
-u <user:password>   // in server身份驗證
-U <user:password>   // in proxy身份驗證
# curl -u username:password http://example.com
# Auth/data:
curl -u user:pass -d status="Hello" http://twitter.com/statuses/update.xml
```
```
curl -v              //***取得較多的資訊
# curl -v -k https://google.com.tw 2>&1 | grep SSL
####  2>&1  不論出現甚麼都顯示
```bash
# multipart file upload
curl -v -include --form key1=value1 --form upload=@localfilename URL
```
```
-X <method>         //指定request的方法，例如：GET、POST、PUT、DELETE
# curl -X POST https://example.com/post/api \ 
# -H 'Content-Type: application/json' \
# -d '{"key_1":"value_1","key_2":"value_2"}'

-A <str>         # --user-agent
-b name=val      # --cookie
-b FILE          # --cookie
-H "X-Foo: y"    # --header
--compressed     # use deflate/gzip
```
