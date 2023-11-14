Starting Nmap 7.94 ( https://nmap.org ) at 2023-11-10 18:04 Hora estándar de Venezuela
Nmap scan report for 199.231.166.226
Host is up (0.13s latency).
Not shown: 78 filtered tcp ports (no-response)
PORT      STATE  SERVICE    VERSION
21/tcp    open   ftp        ProFTPD
22/tcp    closed ssh
25/tcp    open   smtp?
26/tcp    open   smtp       Exim smtpd 4.96.2
| vulners: 
|   cpe:/a:exim:exim:4.96.2: 
|     	PRION:CVE-2019-13917	10.0	https://vulners.com/prion/PRION:CVE-2019-13917
|     	PRION:CVE-2019-10149	10.0	https://vulners.com/prion/PRION:CVE-2019-10149
|     	MSF:EXPLOIT-LINUX-LOCAL-EXIM4_DELIVER_MESSAGE_PRIV_ESC-	10.0	https://vulners.com/metasploit/MSF:EXPLOIT-LINUX-LOCAL-EXIM4_DELIVER_MESSAGE_PRIV_ESC-	*EXPLOIT*
|     	EDB-ID:47307	10.0	https://vulners.com/exploitdb/EDB-ID:47307	*EXPLOIT*
|     	EDB-ID:46996	10.0	https://vulners.com/exploitdb/EDB-ID:46996	*EXPLOIT*
|     	EDB-ID:46974	10.0	https://vulners.com/exploitdb/EDB-ID:46974	*EXPLOIT*
|     	PRION:CVE-2020-28018	7.5	https://vulners.com/prion/PRION:CVE-2020-28018
|     	PRION:CVE-2019-16928	7.5	https://vulners.com/prion/PRION:CVE-2019-16928
|_    	PRION:CVE-2020-28019	5.0	https://vulners.com/prion/PRION:CVE-2020-28019
| smtp-vuln-cve2010-4344: 
|_  The SMTP server is not Exim: NOT VULNERABLE
53/tcp    open   domain     PowerDNS Authoritative Server 4.7.3
80/tcp    open   http       LiteSpeed
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-server-header: LiteSpeed
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 404 Not Found
|     Connection: close
|     content-type: text/html
|     date: Fri, 10 Nov 2023 22:04:40 GMT
|     server: LiteSpeed
|     <!DOCTYPE html>
|     <html>
|     <head>
|     <meta http-equiv="Content-type" content="text/html; charset=utf-8">
|     <meta http-equiv="Cache-control" content="no-cache">
|     <meta http-equiv="Pragma" content="no-cache">
|     <meta http-equiv="Expires" content="0">
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">
|     <title>404 Not Found</title>
|     <style type="text/css">
|     body {
|     font-family: Arial, Helvetica, sans-serif;
|     font-size: 14px;
|     line-height: 1.428571429;
|     background-color: #ffffff;
|     color: #2F3230;
|     padding: 0;
|     margin: 0;
|     section, footer {
|     display: block;
|     padding: 0;
|     margin: 0;
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Connection: close
|     content-type: text/html
|     last-modified: Sat, 10 Oct 2020 19:37:25 GMT
|     accept-ranges: bytes
|     content-length: 163
|     date: Fri, 10 Nov 2023 22:04:34 GMT
|     server: LiteSpeed
|     <html><head><META HTTP-EQUIV="Cache-control" CONTENT="no-cache"><META HTTP-EQUIV="refresh" CONTENT="0;URL=/cgi-sys/defaultwebpage.cgi"></head><body></body></html>
|   HTTPOptions: 
|     HTTP/1.0 200 OK
|     Connection: close
|     allow: OPTIONS,HEAD,GET,POST
|     content-length: 0
|     date: Fri, 10 Nov 2023 22:04:35 GMT
|     server: LiteSpeed
|   RTSPRequest: 
|     HTTP/1.1 400 Bad Request
|     Connection: close
|     cache-control: private, no-cache, no-store, must-revalidate, max-age=0
|     pragma: no-cache
|     content-type: text/html
|     content-length: 681
|     date: Fri, 10 Nov 2023 22:04:35 GMT
|     server: LiteSpeed
|     <!DOCTYPE html>
|     <html style="height:100%">
|     <head>
|     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
|     <title> 400 Bad Request
|     </title></head>
|     <body style="color: #444; margin:0;font: normal 14px/20px Arial, Helvetica, sans-serif; height:100%; background-color: #fff;">
|     <div style="height:auto; min-height:100%; "> <div style="text-align: center; width:800px; margin-left: -400px; position:absolute; top: 30%; left:50%;">
|     style="margin:0; font-size:150px; line-height:150px; font-weight:bold;">400</h1>
|     style="margin-top:20px;font-size: 30px;">Bad Request
|     </h2>
|     <p>It is not a valid request!</p>
|_    </div><
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
110/tcp   open   pop3       Dovecot pop3d
143/tcp   open   imap       Dovecot imapd
443/tcp   open   ssl/https  LiteSpeed
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-server-header: LiteSpeed
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 404 Not Found
|     Connection: close
|     cache-control: private, no-cache, no-store, must-revalidate, max-age=0
|     pragma: no-cache
|     content-type: text/html
|     content-length: 1238
|     date: Fri, 10 Nov 2023 22:04:42 GMT
|     server: LiteSpeed
|     <!DOCTYPE html>
|     <html style="height:100%">
|     <head>
|     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
|     <title> 404 Not Found
|     </title></head>
|     <body style="color: #444; margin:0;font: normal 14px/20px Arial, Helvetica, sans-serif; height:100%; background-color: #fff;">
|     <div style="height:auto; min-height:100%; "> <div style="text-align: center; width:800px; margin-left: -400px; position:absolute; top: 30%; left:50%;">
|     style="margin:0; font-size:150px; line-height:150px; font-weight:bold;">404</h1>
|     style="margin-top:20px;font-size: 30px;">Not Found
|     </h2>
|     <p>The resource requested could not be found o
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Connection: close
|     content-type: text/html
|     last-modified: Fri, 27 Aug 2021 17:43:42 GMT
|     accept-ranges: bytes
|     content-length: 18197
|     date: Fri, 10 Nov 2023 22:04:41 GMT
|     server: LiteSpeed
|     <!DOCTYPE html>
|     <html style="font-size: 16px;">
|     <head>
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">
|     <meta charset="utf-8">
|     <meta name="keywords" content="">
|     <meta name="description" content="">
|     <meta name="page_type" content="np-template-header-footer-from-plugin">
|     <title>Avancehost-Hosting</title>
|     <link rel="stylesheet" href="nicepage.css" media="screen">
|     <link rel="stylesheet" href="Pagina-1.css" media="screen">
|     <script class="u-script" type="text/javascript" src="jquery.js" defer=""></script>
|     <script class="u-script" type="text/javascript" src="nicepage.js" defer=""></script>
|     <meta name="generator" content="Nice
|   HTTPOptions: 
|     HTTP/1.0 200 OK
|     Connection: close
|     allow: OPTIONS,HEAD,GET,POST
|     content-length: 0
|     date: Fri, 10 Nov 2023 22:04:41 GMT
|_    server: LiteSpeed
|_ssl-ccs-injection: No reply from server (TIMEOUT)
|_http-dombased-xss: Couldn't find any DOM based XSS.
465/tcp   open   ssl/smtp   Exim smtpd 4.96.2
| smtp-vuln-cve2010-4344: 
|_  The SMTP server is not Exim: NOT VULNERABLE
587/tcp   open   smtp       Exim smtpd 4.96.2
| smtp-vuln-cve2010-4344: 
|_  The SMTP server is not Exim: NOT VULNERABLE
993/tcp   open   ssl/imap   Dovecot imapd
995/tcp   open   ssl/pop3   Dovecot pop3d
3306/tcp  open   mysql      MySQL 8.0.34-cll-lve
|_mysql-vuln-cve2012-2122: ERROR: Script execution failed (use -d to debug)
| vulners: 
|   cpe:/a:mysql:mysql:8.0.34-cll-lve: 
|_    	NODEJS:602	0.0	https://vulners.com/nodejs/NODEJS:602
5432/tcp  closed postgresql
8443/tcp  closed https-alt
49152/tcp closed unknown
49153/tcp closed unknown
49154/tcp closed unknown
49155/tcp closed unknown
49156/tcp closed unknown
49157/tcp closed unknown
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port80-TCP:V=7.94%I=7%D=11/10%Time=654EA8F2%P=i686-pc-windows-windows%r
SF:(GetRequest,173,"HTTP/1\.0\x20200\x20OK\r\nConnection:\x20close\r\ncont
SF:ent-type:\x20text/html\r\nlast-modified:\x20Sat,\x2010\x20Oct\x202020\x
SF:2019:37:25\x20GMT\r\naccept-ranges:\x20bytes\r\ncontent-length:\x20163\
SF:r\ndate:\x20Fri,\x2010\x20Nov\x202023\x2022:04:34\x20GMT\r\nserver:\x20
SF:LiteSpeed\r\n\r\n<html><head><META\x20HTTP-EQUIV=\"Cache-control\"\x20C
SF:ONTENT=\"no-cache\"><META\x20HTTP-EQUIV=\"refresh\"\x20CONTENT=\"0;URL=
SF:/cgi-sys/defaultwebpage\.cgi\"></head><body></body></html>\n")%r(HTTPOp
SF:tions,8F,"HTTP/1\.0\x20200\x20OK\r\nConnection:\x20close\r\nallow:\x20O
SF:PTIONS,HEAD,GET,POST\r\ncontent-length:\x200\r\ndate:\x20Fri,\x2010\x20
SF:Nov\x202023\x2022:04:35\x20GMT\r\nserver:\x20LiteSpeed\r\n\r\n")%r(RTSP
SF:Request,398,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20close
SF:\r\ncache-control:\x20private,\x20no-cache,\x20no-store,\x20must-revali
SF:date,\x20max-age=0\r\npragma:\x20no-cache\r\ncontent-type:\x20text/html
SF:\r\ncontent-length:\x20681\r\ndate:\x20Fri,\x2010\x20Nov\x202023\x2022:
SF:04:35\x20GMT\r\nserver:\x20LiteSpeed\r\n\r\n<!DOCTYPE\x20html>\n<html\x
SF:20style=\"height:100%\">\n<head>\n<meta\x20name=\"viewport\"\x20content
SF:=\"width=device-width,\x20initial-scale=1,\x20shrink-to-fit=no\"\x20/>\
SF:n<title>\x20400\x20Bad\x20Request\r\n</title></head>\n<body\x20style=\"
SF:color:\x20#444;\x20margin:0;font:\x20normal\x2014px/20px\x20Arial,\x20H
SF:elvetica,\x20sans-serif;\x20height:100%;\x20background-color:\x20#fff;\
SF:">\n<div\x20style=\"height:auto;\x20min-height:100%;\x20\">\x20\x20\x20
SF:\x20\x20<div\x20style=\"text-align:\x20center;\x20width:800px;\x20margi
SF:n-left:\x20-400px;\x20position:absolute;\x20top:\x2030%;\x20left:50%;\"
SF:>\n\x20\x20\x20\x20\x20\x20\x20\x20<h1\x20style=\"margin:0;\x20font-siz
SF:e:150px;\x20line-height:150px;\x20font-weight:bold;\">400</h1>\n<h2\x20
SF:style=\"margin-top:20px;font-size:\x2030px;\">Bad\x20Request\r\n</h2>\n
SF:<p>It\x20is\x20not\x20a\x20valid\x20request!</p>\n</div><")%r(FourOhFou
SF:rRequest,2208,"HTTP/1\.0\x20404\x20Not\x20Found\r\nConnection:\x20close
SF:\r\ncontent-type:\x20text/html\r\ndate:\x20Fri,\x2010\x20Nov\x202023\x2
SF:022:04:40\x20GMT\r\nserver:\x20LiteSpeed\r\n\r\n\n\n\n<!DOCTYPE\x20html
SF:>\n<html>\n\x20\x20\x20\x20<head>\n\x20\x20\x20\x20<meta\x20http-equiv=
SF:\"Content-type\"\x20content=\"text/html;\x20charset=utf-8\">\n\x20\x20\
SF:x20\x20<meta\x20http-equiv=\"Cache-control\"\x20content=\"no-cache\">\n
SF:\x20\x20\x20\x20<meta\x20http-equiv=\"Pragma\"\x20content=\"no-cache\">
SF:\n\x20\x20\x20\x20<meta\x20http-equiv=\"Expires\"\x20content=\"0\">\n\x
SF:20\x20\x20\x20<meta\x20name=\"viewport\"\x20content=\"width=device-widt
SF:h,\x20initial-scale=1\.0\">\n\x20\x20\x20\x20<title>404\x20Not\x20Found
SF:</title>\n\x20\x20\x20\x20<style\x20type=\"text/css\">\n\x20\x20\x20\x2
SF:0\x20\x20\x20\x20body\x20{\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20font-family:\x20Arial,\x20Helvetica,\x20sans-serif;\n\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20font-size:\x2014px;\n\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20line-height:\x201\.428571429;\n\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20background-color:\x20#ffffff;\
SF:n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20color:\x20#2F3230;\n\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20padding:\x200;\n\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20margin:\x200;\n\x20\x20\x20\x20\
SF:x20\x20\x20\x20}\n\x20\x20\x20\x20\x20\x20\x20\x20section,\x20footer\x2
SF:0{\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20display:\x20block;\
SF:n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20padding:\x200;\n\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20margin:\x200;\n\x20\x20\x20\x
SF:20\x20\x20\x20\x20}\n\x20\x20\x20\x20\x20\x20");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port443-TCP:V=7.94%T=SSL%I=7%D=11/10%Time=654EA8F8%P=i686-pc-windows-wi
SF:ndows%r(GetRequest,47E7,"HTTP/1\.0\x20200\x20OK\r\nConnection:\x20close
SF:\r\ncontent-type:\x20text/html\r\nlast-modified:\x20Fri,\x2027\x20Aug\x
SF:202021\x2017:43:42\x20GMT\r\naccept-ranges:\x20bytes\r\ncontent-length:
SF:\x2018197\r\ndate:\x20Fri,\x2010\x20Nov\x202023\x2022:04:41\x20GMT\r\ns
SF:erver:\x20LiteSpeed\r\n\r\n<!DOCTYPE\x20html>\n<html\x20style=\"font-si
SF:ze:\x2016px;\">\n\x20\x20<head>\n\x20\x20\x20\x20<meta\x20name=\"viewpo
SF:rt\"\x20content=\"width=device-width,\x20initial-scale=1\.0\">\n\x20\x2
SF:0\x20\x20<meta\x20charset=\"utf-8\">\n\x20\x20\x20\x20<meta\x20name=\"k
SF:eywords\"\x20content=\"\">\n\x20\x20\x20\x20<meta\x20name=\"description
SF:\"\x20content=\"\">\n\x20\x20\x20\x20<meta\x20name=\"page_type\"\x20con
SF:tent=\"np-template-header-footer-from-plugin\">\n\x20\x20\x20\x20<title
SF:>Avancehost-Hosting</title>\n\x20\x20\x20\x20<link\x20rel=\"stylesheet\
SF:"\x20href=\"nicepage\.css\"\x20media=\"screen\">\n<link\x20rel=\"styles
SF:heet\"\x20href=\"Pagina-1\.css\"\x20media=\"screen\">\n\x20\x20\x20\x20
SF:<script\x20class=\"u-script\"\x20type=\"text/javascript\"\x20src=\"jque
SF:ry\.js\"\x20defer=\"\"></script>\n\x20\x20\x20\x20<script\x20class=\"u-
SF:script\"\x20type=\"text/javascript\"\x20src=\"nicepage\.js\"\x20defer=\
SF:"\"></script>\n\x20\x20\x20\x20<meta\x20name=\"generator\"\x20content=\
SF:"Nice")%r(HTTPOptions,8F,"HTTP/1\.0\x20200\x20OK\r\nConnection:\x20clos
SF:e\r\nallow:\x20OPTIONS,HEAD,GET,POST\r\ncontent-length:\x200\r\ndate:\x
SF:20Fri,\x2010\x20Nov\x202023\x2022:04:41\x20GMT\r\nserver:\x20LiteSpeed\
SF:r\n\r\n")%r(FourOhFourRequest,5C4,"HTTP/1\.0\x20404\x20Not\x20Found\r\n
SF:Connection:\x20close\r\ncache-control:\x20private,\x20no-cache,\x20no-s
SF:tore,\x20must-revalidate,\x20max-age=0\r\npragma:\x20no-cache\r\nconten
SF:t-type:\x20text/html\r\ncontent-length:\x201238\r\ndate:\x20Fri,\x2010\
SF:x20Nov\x202023\x2022:04:42\x20GMT\r\nserver:\x20LiteSpeed\r\n\r\n<!DOCT
SF:YPE\x20html>\n<html\x20style=\"height:100%\">\n<head>\n<meta\x20name=\"
SF:viewport\"\x20content=\"width=device-width,\x20initial-scale=1,\x20shri
SF:nk-to-fit=no\"\x20/>\n<title>\x20404\x20Not\x20Found\r\n</title></head>
SF:\n<body\x20style=\"color:\x20#444;\x20margin:0;font:\x20normal\x2014px/
SF:20px\x20Arial,\x20Helvetica,\x20sans-serif;\x20height:100%;\x20backgrou
SF:nd-color:\x20#fff;\">\n<div\x20style=\"height:auto;\x20min-height:100%;
SF:\x20\">\x20\x20\x20\x20\x20<div\x20style=\"text-align:\x20center;\x20wi
SF:dth:800px;\x20margin-left:\x20-400px;\x20position:absolute;\x20top:\x20
SF:30%;\x20left:50%;\">\n\x20\x20\x20\x20\x20\x20\x20\x20<h1\x20style=\"ma
SF:rgin:0;\x20font-size:150px;\x20line-height:150px;\x20font-weight:bold;\
SF:">404</h1>\n<h2\x20style=\"margin-top:20px;font-size:\x2030px;\">Not\x2
SF:0Found\r\n</h2>\n<p>The\x20resource\x20requested\x20could\x20not\x20be\
SF:x20found\x20o");
Service Info: Host: avance3.avancewebs.com

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 395.13 seconds
