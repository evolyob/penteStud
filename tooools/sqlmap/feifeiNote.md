Detection
```
--level=LEVEL	指定測試級別 (1-5, 預設為 1)	//	--level=5
--risk=RISK	指定測試風險等級 (1-3, 預設為 1)	//	--risk=2
--string=STRING	當 SQL 語句執行結果為真時，要匹配的字串	//	--string="Welcome admin"
--not-string=NOTSTRING	當 SQL 語句執行結果為假時，要匹配的字串	//	--not-string="Access denied"
--regexp=REGEXP	當 SQL 語句執行結果為真時，要匹配的正則表達式	// --regexp="(true|1)"
--code=CODE	當 SQL 語句執行結果為真時，要匹配的 HTTP 狀態碼	//	--code=200
--smart	只在存在正向啟發時執行徹底的測試	//	--smart
--text-only	僅基於文字內容比較頁面	//	--text-only
--titles	僅比較頁面標題	//	--titles
```

Enumeration
```
-a, --all	擷取所有資料	
-b, --banner	擷取 DBMS 標語	
--current-user	擷取目前使用者	
--current-db	擷取目前資料庫	
--hostname	擷取 DBMS 主機名稱	
--is-dba	檢測目前使用者是否為 DBA	
--users	列舉 DBMS 使用者	
--passwords	列舉 DBMS 使用者密碼雜湊	
--privileges	列舉 DBMS 使用者權限	
--roles	列舉 DBMS 使用者角色

--dbs	列舉 DBMS 資料庫	
--tables	列舉 DBMS 資料庫表格	
--columns	列舉 DBMS 資料庫表格欄位元	
--schema	列舉 DBMS schema	
--count	擷取表格中的資料筆數	
--dump	列出 DBMS 資料庫表格內容	
--dump-all	列出所有 DBMS 資料庫表格內容

--search	搜尋欄位元、表格或資料庫名稱	
--comments	列舉資料庫註解	
--statements	擷取 DBMS 所執行的 SQL 陳述式

-D DB	指定 DBMS 要枚舉的資料庫	
-T TBL	指定要枚舉的資料表	\\ -T table_name
-C COL	指定要枚舉的資料表欄位	\\	-C column_name
-X EXCLUDE	指定不要枚舉的資料庫標識符	//	-X database_identifier
-U USER	指定要枚舉的使用者	//	-U user_name

--exclude-sysdbs	枚舉資料表時排除 DBMS 系統資料庫	
--pivot-column=PNAME	指定當進行資料表樞紐分析時要使用的欄位	//	--pivot-column=column_name
--where=DUMPWHERE	在列出資料表時使用 WHERE 條件式	//	--where="column_name='value'"
--start=LIMITSTART	設定要列出的第一個資料表項目 //	--start=10
--stop=LIMITSTOP	設定要列出的最後一個資料表項目	//--stop=20
--first=FIRSTCHAR	設定要列出的查詢輸出的第一個單詞的字元	//	--first=1
--last=LASTCHAR	設定要列出的查詢輸出的最後一個單詞的字元	//	--last=10

--sql-query=SQLQUERY	指定要執行的 SQL 查詢語句	//	--sql-query="SELECT * FROM table_name"
--sql-shell	使用互動式 
--sql-file=SQLFILE	從指定的檔執行 SQL 查詢語句	 //--sql-file=query_file.sql
```
Brute force
```
--common-tables	檢查常見的資料表是否存在	
--common-columns	檢查常見的欄位是否存在	
--common-files	檢查常見的檔案是否存在	
```
User-defined function injection
```
--udf-inject	注入自訂的使用者定義函數	//	--udf-inject=udf_lib.so
--shared-lib=SHLIB	載入共用庫文件	  //	--shared-lib=/tmp/udf_lib.so
```
File system acces
```
--file-read=FILEPATH	從資料庫檔案系統中讀取文件   	//	--file-read=/etc/passwd
--file-write=FILEPATH	將本地檔寫入資料庫檔系統中	    //	--file-write=local_file.txt
--file-dest=FILEPATH	設定在資料庫檔系統中寫入檔的目標位置	//	--file-dest=/var/www/html/shell.php
```
Operating system access
```
--os-cmd=COMMAND	在資料庫伺服器上執行系統命令	//	--os-cmd="ls -la"
--os-shell	在資料庫伺服器上啟動一個互動式     //	--os-shell
--os-pwn	啟動一個 Out-Of-Band (OOB) shell 或 Meterpreter	Prompt for an OOB shell, Meterpreter or VNC	
--os-smbrelay	啟動一個 Out-Of-Band (OOB) shell 或 Meterpreter
--os-bof	將資料庫上的 Stored Procedure Buffer Overflow 漏洞利用	
--priv-esc	提升資料庫進程的使用者權限	
--msf-path=MSFPATH	指定 Metasploit 框架的路徑	//	--msf-path=/opt/metasploit
--tmp-path=TMPPATH	指定遠端系統的臨時檔目錄	    //	--tmp-path=/var/tmp/
```
Windows registry access
```
--reg-read	讀取 Windows 註冊表鍵值	
--reg-add	寫入 Windows 註冊表鍵值資料	
--reg-del	刪除 Windows 註冊表鍵值	
--reg-key=REGKEY	Windows 註冊表鍵    	// --reg-key="HKLM\SOFTWARE\Microsoft"
--reg-value=REGVAL	Windows 註冊表鍵值	//	--reg-value=Version
--reg-data=REGDATA	Windows 註冊表鍵值資料	//--reg-data=12
--reg-type=REGTYPE	Windows 註冊表鍵值類型	//	--reg-type=REG_DWORD
```
