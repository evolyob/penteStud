```php
CURLE_OK	(0)	都正確，像往常一樣
CURLE_UNSUPPORTED_PROTOCOL	(1)	您傳送給 libcurl 的網址使用了此 libcurl 不支持的協議。 可能是您沒有使用的編譯時選項造成了這種情況（可能是協議字符串拼寫有誤，或沒有指定協議 libcurl 代碼）。
CURLE_FAILED_INIT	(2)	非常早期的初始化代碼失敗。 可能是內部錯誤或問題。
CURLE_URL_MALFORMAT	(3)	網址格式不正確。
CURLE_COULDNT_RESOLVE_PROXY	(5)	無法解析代理服務器。 指定的代理服務器主機無法解析。
CURLE_COULDNT_RESOLVE_HOST	(6)	無法解析主機。 指定的遠程主機無法解析。
CURLE_COULDNT_CONNECT	(7)	無法通過 connect() 連接至主機或代理服務器。
CURLE_FTP_WEIRD_SERVER_REPLY	(8)	在連接到 FTP 服務器後，libcurl 需要收到特定的回覆。 此錯誤代碼表示收到了不正常或不正確的回覆。 指定的遠程服務器可能不是正確的 FTP 服務器。
CURLE_REMOTE_ACCESS_DENIED	(9)	我們無法訪問網址中指定的資源。 對於 FTP，如果嘗試更改爲遠程目錄，就會發生這種情況。
```
```php
CURLE_FTP_WEIRD_PASS_REPLY	(11)	在將 FTP 密碼發送到服務器後，libcurl 需要收到正確的回覆。 此錯誤代碼表示返回的是意外的代碼。
CURLE_FTP_WEIRD_PASV_REPLY	(13)	libcurl 無法從服務器端收到有用的結果，作爲對 PASV 或 EPSV 命令的響應。 服務器有問題。
CURLE_FTP_WEIRD_227_FORMAT	(14)	FTP 服務器返回 227 行作爲對 PASV 命令的響應。 如果 libcurl 無法解析此行，就會返回此代碼。
CURLE_FTP_CANT_GET_HOST	(15)	在查找用於新連接的主機時出現內部錯誤。
CURLE_FTP_COULDNT_SET_TYPE	(17)	在嘗試將傳輸模式設置爲二進制或 ascii 時發生錯誤。
CURLE_PARTIAL_FILE	(18)	文件傳輸尺寸小於或大於預期。 當服務器先報告了一個預期的傳輸尺寸，然後所傳送的數據與先前指定尺寸不相符時，就會發生此錯誤。
CURLE_FTP_COULDNT_RETR_FILE	(19)	‘RETR’ 命令收到了不正常的回覆，或完成的傳輸尺寸爲零字節。
```
```
CURLE_QUOTE_ERROR	(21)	在向遠程服務器發送自定義 “QUOTE” 命令時，其中一個命令返回的錯誤代碼爲 400 或更大的數字（對於 FTP），或以其他方式表明命令無法成功完成。
CURLE_HTTP_RETURNED_ERROR	(22)	如果 CURLOPT_FAILONERROR 設置爲 TRUE，且 HTTP 服務器返回 >= 400 的錯誤代碼，就會返回此代碼。 （此錯誤代碼以前又稱爲 CURLE_HTTP_NOT_FOUND。）
CURLE_WRITE_ERROR	(23)	在向本地文件寫入所收到的數據時發生錯誤，或由寫入回調 (write callback) 向 libcurl 返回了一個錯誤。
CURLE_UPLOAD_FAILED	(25)	無法開始上傳。 對於 FTP，服務器通常會拒絕執行 STOR 命令。 錯誤緩衝區通常會提供服務器對此問題的說明。 （此錯誤代碼以前又稱爲 CURLE_FTP_COULDNT_STOR_FILE。）
CURLE_READ_ERROR	(26)	讀取本地文件時遇到問題，或由讀取回調 (read callback) 返回了一個錯誤。
CURLE_OUT_OF_MEMORY	(27)	內存分配請求失敗。 此錯誤比較嚴重，若發生此錯誤，則表明出現了非常嚴重的問題。
CURLE_OPERATION_TIMEDOUT	(28)	操作超時。
CURLE_FTP_PORT_FAILED	(30)	FTP PORT 命令返回錯誤。 在沒有爲 libcurl 指定適當的地址使用時，最有可能發生此問題。
CURLE_FTP_COULDNT_USE_REST	(31)	FTP REST 命令返回錯誤。 如果服務器正常，則應當不會發生這種情況。
CURLE_RANGE_ERROR	(33)	服務器不支持或不接受範圍請求。
CURLE_HTTP_POST_ERROR	(34)	此問題比較少見，主要由內部混亂引發。
CURLE_SSL_CONNECT_ERROR	(35)	同時使用 SSL/TLS 時可能會發生此錯誤。 您可以訪問錯誤緩衝區查看相應信息，其中會對此問題進行更詳細的介紹。 可能是證書（文件格式、路徑、許可）、密碼及其他因素導致了此問題。
CURLE_FTP_BAD_DOWNLOAD_RESUME	(36)	嘗試恢復超過文件大小限制的 FTP 連接。
CURLE_FILE_COULDNT_READ_FILE	(37)	無法打開 FILE:// 路徑下的文件。 原因很可能是文件路徑無法識別現有文件。 建議您檢查文件的訪問權限。
CURLE_LDAP_CANNOT_BIND	(38)	LDAP 無法綁定。LDAP 綁定操作失敗。
CURLE_LDAP_SEARCH_FAILED	(39)	LDAP 搜索無法進行。
```
```
CURLE_FUNCTION_NOT_FOUND	(41)	找不到函數。 找不到必要的 zlib 函數。
CURLE_ABORTED_BY_CALLBACK	(42)	由回調中止。 回調向 libcurl 返回了 “abort”。
CURLE_BAD_FUNCTION_ARGUMENT	(43)	內部錯誤。 使用了不正確的參數調用函數。
CURLE_INTERFACE_FAILED	(45)	界面錯誤。 指定的外部界面無法使用。 請通過 CURLOPT_INTERFACE 設置要使用哪個界面來處理外部連接的來源 IP 地址。 （此錯誤代碼以前又稱爲 CURLE_HTTP_PORT_FAILED。）
CURLE_TOO_MANY_REDIRECTS	(47)	重定向過多。 進行重定向時，libcurl 達到了網頁點擊上限。 請使用 CURLOPT_MAXREDIRS 設置上限。
CURLE_UNKNOWN_TELNET_OPTION	(48)	無法識別以 CURLOPT_TELNETOPTIONS 設置的選項。 請參閱相關文檔。
CURLE_TELNET_OPTION_SYNTAX	(49)	telnet 選項字符串的格式不正確。
CURLE_PEER_FAILED_VERIFICATION	(51)	遠程服務器的 SSL 證書或 SSH md5 指紋不正確。
CURLE_GOT_NOTHING	(52)	服務器未返回任何數據，在相應情況下，未返回任何數據就屬於出現錯誤。
CURLE_SSL_ENGINE_NOTFOUND	(53)	找不到指定的加密引擎。
CURLE_SSL_ENGINE_SETFAILED	(54)	無法將選定的 SSL 加密引擎設爲默認選項。
CURLE_SEND_ERROR	(55)	無法發送網絡數據。
CURLE_RECV_ERROR	(56)	接收網絡數據失敗。
CURLE_SSL_CERTPROBLEM	(58)	本地客戶端證書有問題
CURLE_SSL_CIPHER	(59)	無法使用指定的密鑰
CURLE_SSL_CACERT	(60)	無法使用已知的 CA 證書驗證對等證書
```
```php
CURLE_BAD_CONTENT_ENCODING	(61)	無法識別傳輸編碼
CURLE_LDAP_INVALID_URL	(62)	LDAP 網址無效
CURLE_FILESIZE_EXCEEDED	(63)	超過了文件大小上限
CURLE_USE_SSL_FAILED	(64)	請求的 FTP SSL 級別失敗
CURLE_SEND_FAIL_REWIND	(65)	進行發送操作時，curl 必須迴轉數據以便重新傳輸，但迴轉操作未能成功
CURLE_SSL_ENGINE_INITFAILED	(66)	SSL 引擎初始化失敗
CURLE_LOGIN_DENIED	(67)	遠程服務器拒絕 curl 登錄（7.13.1 新增功能）
CURLE_TFTP_NOTFOUND	(68)	在 TFTP 服務器上找不到文件
CURLE_TFTP_PERM	(69)	在 TFTP 服務器上遇到權限問題
CURLE_REMOTE_DISK_FULL	(70)	服務器磁盤空間不足
CURLE_TFTP_ILLEGAL	(71)	TFTP 操作非法
CURLE_TFTP_UNKNOWNID	(72)	TFTP 傳輸 ID 未知
CURLE_REMOTE_FILE_EXISTS	(73)	文件已存在，無法覆蓋
CURLE_TFTP_NOSUCHUSER	(74)	運行正常的 TFTP 服務器不會返回此錯誤
CURLE_CONV_FAILED	(75)	字符轉換失敗
CURLE_CONV_REQD	(76)	調用方必須註冊轉換回調
CURLE_SSL_CACERT_BADFILE	(77)	讀取 SSL CA 證書時遇到問題（可能是路徑錯誤或訪問權限問題）
CURLE_REMOTE_FILE_NOT_FOUND	(78)	網址中引用的資源不存在
CURLE_SSH	(79)	SSH 會話中發生無法識別的錯誤
CURLE_SSL_SHUTDOWN_FAILED	(80)	無法終止 SSL 連接
```
