#### kali cli
```php
nano = vim
history | tail -500 // 有帶時間的指令歷史紀錄
或改設定
echo 'export HISTTIMEFORMAT="%F %T "' >>~/.bashrc
source ~/.bashrc

mkdir  //new one 
rmdir  //delete one
locate  = find = which
locate <keyword>
find /path/  -name     //檔案名稱
find /path/  -type     //檔案種類
find /path/  -size+-   //檔案大小
find /path/  -mtime +- //修改時間
find <dir> -user <user>	搜尋時指定使用者
find <dir> -group <group>	搜尋時指定群組

ping -c 1 <target> //ping onetime
cut -d " " -f 4 // 以空格當區隔,前面的第四個字串
sed 's/.$//'
sort -u  //排序？
for ip in $(cat iplist.txt); do nmap -Pn $ip; done //做文件裡面的ip的掃描

;	    指令終止符號，無論前面是否失敗都會繼續執行下一個
&	    讓符號前的指令在背景執行
&&	  指令連接符號，第一個指令失敗則不執行下一個
\|	  指令連接符號，將前項指令輸出當成下一個命令輸入
\|\|	指令連接符號，第一個指令才執行下一個



```
#### google search
```ymal
查子域名 或 phpinfo  真實IP
asm.ca.com/en/ping.php
webkaka
dnsdb.io/
waf : sqli xxs csrf ....

site: <url> //特定網址搜尋結果
-site:<url> //不顯示特定網址開頭結果
filetype:<type>//只搜尋特定檔案種類
"<url>" //精確搜尋
link: <url>//??
"ulr*" //什麼開頭的搜尋
related:<url> //找類似的其他網頁
google search syntax//搜尋指令
google hacking database//搜尋敏感資料指令
shodan //not been secure webcam
theharvester // find type of emailladdres
```
#### TCP UDP
```php
wireshark
TCP Scan= http ftp telnet
UDP= dns dhcp snmp
MSF console // other portscan app
```

```php
ssh -c <cipherType> <target>
// ssh -c aes128-cbc 127.0.0.1
owasp dirbuster 

dirbuster / wordlists //找目錄

dnsrecom -d <target> -t axfr
ftp snmp smtp
```
```php
kioptrix level 1
netcat
connecting listening
bind shells
reverse shells

<filename>.tar.gz and <filename>.tar
tar打包 跟 gz壓縮
tar 命令，
cvf 进行压缩，
xvf 进行解压，
c 是压缩的意思，
v 是显示详细过程，
f 是文件名，
x 是解压
p 保留备份数据的原本权限与属性
P 保留绝对路径
tar -zcvf <filename>.tar.gz path/a/b
tar -zxvf <filename>.tar.gz -C path/a/b //解壓到指定目錄

tar -zcvpf -<traget>| openssl des3 -salt -k <passwd> -out <filename>.tgz
-j 專解 bzip2
tar -jcvf <filename>.tar.bz2 path/a/b
tar -jxvf <filename>.tar.bz2

```
FileTransfers
```
fuzzing??
HTTP
wget // for linux most
FTP
powershell
```

弱口令
tomcat
```php
開個proxy抓封包
得知傳送認證字串組成 usr:passwd encode base64//rules
＃getshell
jsp壓縮成zip  zip後綴改為war
cmd: jar -cvf* .war* .jsp
https://<>:8080/<.war>/<webshellname>
```
RPM
```php
rpm -ivh package_name
-i ：install 的意思
-v ：察看更細部的安裝資訊畫面
-h ：以安裝資訊列顯示安裝進度
--replacepkgs  重新安裝某個已經安裝過的軟體
--nosignature 略過數位簽章的檢查

-Uvh  直接安裝或系統自動更新至新版
-Fvh  未安裝不會被安裝，已安裝就被升級

-q  ：僅查詢，後面接的軟體名稱是否有安裝；
-qa ：列出所有的，已經安裝在本機 Linux 系統上面的所有軟體名稱；
-qc ：列出該軟體的所有設定檔 (找/etc/ )
-ql ：列出該軟體所有的檔案與目錄所在完整檔名 (list)；

yum clean all  清除掉本機上面的舊資料

```
