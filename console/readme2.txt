Starting Nmap 7.94 ( https://nmap.org ) at 2023-11-10 18:15 Hora est�ndar de Venezuela
Pre-scan script results:
| broadcast-avahi-dos: 
|   Discovered hosts:
|     224.0.0.251
|   After NULL UDP avahi packet DoS (CVE-2011-1002).
|   Hosts that seem down (vulnerable):
|_    224.0.0.251
Nmap scan report for 199.250.215.182
Host is up (0.15s latency).
Not shown: 87 filtered tcp ports (no-response)
PORT      STATE  SERVICE     VERSION
21/tcp    open   ftp         Pure-FTPd
| ssl-dh-params: 
|  +++++++++++++++++yer Security (TLS) services that use anonymous
|       Diffie-Hellman key exchange only provide protection against passive
|       eavesdropping, and are vulnerable to active man-in-the-middle attacks
|       which could completely compromise the confidentiality and integrity
|       of any data exchanged over the resulting session.
|     Check results:
|       ANONYMOUS DH GROUP 1
|             Cipher Suite: TLS_DH_anon_WITH_AES_256_GCM_SHA384
|             Modulus Type: Non-safe prime
|             Modulus Source: RFC5114/2048-bit DSA group with 256-bit prime order subgroup
|             Modulus Length: 2048
|             Generator Length: 2048
|             Public Key Length: 2048
|     References:
|_      https://www.ietf.org/rfc/rfc2246.txt
25/tcp    open   smtp?
80/tcp    open   http        nginx 1.23.4
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
110/tcp   open   pop3        Dovecot pop3d
143/tcp   open   imap        Dovecot imapd
443/tcp   open   ssl/http    nginx 1.23.4
|_http-server-header: nginx/1.23.4
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
465/tcp   open   ssl/smtp    Exim smtpd 4.96.2
| smtp-vuln-cve2010-4344: 
|_  The SMTP server is not Exim: NOT VULNERABLE
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
587/tcp   open   smtp        Exim smtpd 4.96.2
| smtp-vuln-cve2010-4344: 
|_  The SMTP server is not Exim: NOT VULNERABLE
993/tcp   open   ssl/imap    Dovecot imapd
995/tcp   open   ssl/pop3    Dovecot pop3d
3306/tcp  open   mysql       MySQL 5.5.5-10.3.39-MariaDB
| vulners: 
|   cpe:/a:mysql:mysql:5.5.5-10.3.39-mariadb: 
|_    	NODEJS:602	0.0	https://vulners.com/nodejs/NODEJS:602
|_mysql-vuln-cve2012-2122: ERROR: Script execution failed (use -d to debug)
6001/tcp  open   ssl/http    Node.js (Express middleware)
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
|_http-csrf: Couldn't find any CSRF vulnerabilities.
32768/tcp closed filenet-tms
Service Info: Host: cc5472.inmotionhosting.com

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1688.61 seconds
