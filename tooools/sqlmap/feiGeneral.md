General
```
-s SESSIONFILE	從已存的 (.sqlite) 檔案載入 session	// file	-s session.sqlite
-t TRAFFICFILE	將所有 HTTP 流量記錄到文字檔案	      //	-t traffic.txt
--answers=ANSWERS	設定預先定義的回答 (e.g. "quit=N,follow=N")	// 	--answers=quit=N,follow=Y
--base64=BASE64PARAMETER	包含 Base64 編碼資料的參數	//	--base64=auth=bG9naW46cGFzc3dvcmQ=
--base64-safe	使用 URL 和檔案名稱安全的 Base64 字母表 (RFC 4648)	
--batch	永遠不要詢問使用者輸入，使用預設行為	  
--binary-fields=BINARYFIELDS	有二進位值的結果欄位 (e.g. "digest")	//--binary-fields=digest,cookie
--check-internet	評估目標之前，檢查網路連線	
--cleanup	從資料庫中刪除 sqlmap 特定的 UDF 和表格

--crawl=CRAWLDEPTH	從目標 URL 開始爬網站		    //--crawl=3
--crawl-exclude=CRAWLEXCLUDE	排除某些網頁不要爬	//--crawl-exclude=logout
--csv-del=CSVDEL	CSV 輸出時使用的分隔符號號 (預設為 ",")	// --csv-del=";"
--charset=CHARSET	Blind SQL injection 字元集 (e.g. "0123456789abcdef")	//	--charset=utf8
--dump-format=DUMPFORMAT	列出資料的格式 (CSV (預設), HTML 或 SQLITE)	  //	--dump-format=HTML
--encoding=ENCODING	取回資料時使用的字元編碼 (e.g. GBK)	
--eta	每個輸出顯示預計到達時間

--flush-session	刷新當前目標的 session 文件	
--forms	解析和測試目標 URL 上的表單	
--fresh-queries	忽略已儲存在會話文件中的查詢結果	
--gpage=GOOGLEPAGE	從指定頁面使用 Google dork 結果	//	--gpage=2
--har=HARFILE	將所有 HTTP 流量記錄到 HAR 檔中	      //	--har=/path/to/file.har
--hex	使用 16 進制轉換來檢索資料
--output-dir=OUTPUT_DIR	自定義輸出目錄路徑	       //	--output-dir=/path/to/directory
--parse-errors	解析並顯示來自回應的 DBMS 錯誤消息	
--preprocess=PREPROCESS	使用給定的腳本進行預處理（請求）	  //	--preprocess=/path/to/script
--postprocess=POSTPROCESS	使用給定的腳本進行後處理（回應）	//--postprocess=/path/to/script
--repair	重新 dump 具有未知字元標記（?）的條目	
--save=SAVECONFIG	將選項保存到配置 INI 檔	         //	--save=/path/to/file.ini
--scope=SCOPE	正則表達式篩選目標	                  //	--scope=https://iiipp.tw
--skip-heuristics	跳過啟發式偵測 SQLi/XSS 漏洞	
--skip-waf	跳過啟發式偵測 WAF/IPS 保護	
--table-prefix=TABLE_PREFIX	設置暫存表的前綴	     \\	--table-prefix=myapp_
--test-filter=TEST_FILTER	通過 payload 和/或標題選擇測試	//	--test-filter="AND(SELECT 1 FROM DBMS_RANDOM)='"
--test-skip=TEST_SKIP	通過 payload 和/或標題跳過測試	    //--test-skip="AND (SELECT * FROM mytable)='"
--web-root=WEB_ROOT	設置網站根目錄                     	//	--web-root=/var/www/html/
```
Miscellaneous
```
-z MNEMONICS	使用短記憶體技巧 (e.g. "flu,bat,ban,tec=EU")	//-z flu,bat,ban,tec=EU
--alert=ALERT	在發現 SQL 注入時執行主機 OS 命令	            //--alert="ls -la"
--beep	當發現 SQLi/XSS/FI 時發出嗶聲	
--dependencies	檢查是否缺少 (選用的) sqlmap 依賴項	
--disable-coloring	禁用控制台輸出顏色	
--list-tampers	顯示可用的篡改腳本列表	
--offline	在離線模式下工作 (僅使用會話資料)	
--purge	安全地從 sqlmap 資料目錄中刪除所有內容	
--results-file=RESULTS_FILE	CSV 結果檔在多目標模式下的位置	 //	--results-file=/path/to/results.csv
--shell	提示進入互動式 
--tmp-dir=TMPDIR	儲存臨時檔的本地目錄	// --tmp-dir=/path/to/tmpdir
--unstable	調整不穩定連接的選項	
--update	更新 sqlmap	
--wizard	簡單的向導介面供初學者使用	

```
