Starting Nmap 7.94 ( https://nmap.org ) at 2023-11-23 15:18 Hora estándar de Venezuela
Pre-scan script results:
| broadcast-avahi-dos: 
|   Discovered hosts:
|     224.0.0.251
|   After NULL UDP avahi packet DoS (CVE-2011-1002).
|_  Hosts are all up (not vulnerable).
Nmap scan report for 200.80.43.108
Host is up (0.46s latency).
Not shown: 86 closed tcp ports (reset)
PORT     STATE SERVICE    VERSION
21/tcp   open  ftp        Pure-FTPd
| ssl-dh-params: 
|   VULNERABLE:
|   Anonymous Diffie-Hellman Key Exchange MitM Vulnerability
|     State: VULNERABLE
|       Transport Layer Security (TLS) services that use anonymous
|       Diffie-Hellman key exchange only provide protection against passive
|       eavesdropping, and are vulnerable to active man-in-the-middle attacks
|       which could completely compromise the confidentiality and integrity
|       of any data exchanged over the resulting session.
|     Check results:
|       ANONYMOUS DH GROUP 1
|             Cipher Suite: TLS_DH_anon_WITH_AES_256_GCM_SHA384
|             Modulus Type: Safe prime
|             Modulus Source: Unknown/Custom-generated
|             Modulus Length: 3072
|             Generator Length: 8
|             Public Key Length: 3072
|     References:
|_      https://www.ietf.org/rfc/rfc2246.txt
22/tcp   open  tcpwrapped
25/tcp   open  smtp       Exim smtpd 4.93
| smtp-vuln-cve2010-4344: 
|_  The SMTP server is not Exim: NOT VULNERABLE
| vulners: 
|   cpe:/a:exim:exim:4.93: 
|     	PRION:CVE-2020-28026	9.3	https://vulners.com/prion/PRION:CVE-2020-28026
|     	CVE-2020-28026	9.3	https://vulners.com/cve/CVE-2020-28026
|     	PRION:CVE-2020-28021	9.0	https://vulners.com/prion/PRION:CVE-2020-28021
|     	CVE-2020-28021	9.0	https://vulners.com/cve/CVE-2020-28021
|     	SSV:99253	7.5	https://vulners.com/seebug/SSV:99253	*EXPLOIT*
|     	PRION:CVE-2022-37452	7.5	https://vulners.com/prion/PRION:CVE-2022-37452
|     	PRION:CVE-2020-28024	7.5	https://vulners.com/prion/PRION:CVE-2020-28024
|     	PRION:CVE-2020-28022	7.5	https://vulners.com/prion/PRION:CVE-2020-28022
|     	PRION:CVE-2020-28018	7.5	https://vulners.com/prion/PRION:CVE-2020-28018
|     	PRION:CVE-2020-28017	7.5	https://vulners.com/prion/PRION:CVE-2020-28017
|     	D4A90249-DD8A-53F0-BF5C-2A24402535BB	7.5	https://vulners.com/githubexploit/D4A90249-DD8A-53F0-BF5C-2A24402535BB	*EXPLOIT*
|     	CVE-2022-37452	7.5	https://vulners.com/cve/CVE-2022-37452
|     	CVE-2020-28024	7.5	https://vulners.com/cve/CVE-2020-28024
|     	CVE-2020-28022	7.5	https://vulners.com/cve/CVE-2020-28022
|     	CVE-2020-28018	7.5	https://vulners.com/cve/CVE-2020-28018
|     	CVE-2020-28017	7.5	https://vulners.com/cve/CVE-2020-28017
|     	347B3764-E644-581E-AFCB-F57D6EDDDA1E	7.5	https://vulners.com/githubexploit/347B3764-E644-581E-AFCB-F57D6EDDDA1E	*EXPLOIT*
|     	PRION:CVE-2020-28016	7.2	https://vulners.com/prion/PRION:CVE-2020-28016
|     	PRION:CVE-2020-28015	7.2	https://vulners.com/prion/PRION:CVE-2020-28015
|     	PRION:CVE-2020-28013	7.2	https://vulners.com/prion/PRION:CVE-2020-28013
|     	PRION:CVE-2020-28012	7.2	https://vulners.com/prion/PRION:CVE-2020-28012
|     	PRION:CVE-2020-28011	7.2	https://vulners.com/prion/PRION:CVE-2020-28011
|     	PRION:CVE-2020-28010	7.2	https://vulners.com/prion/PRION:CVE-2020-28010
|     	PRION:CVE-2020-28009	7.2	https://vulners.com/prion/PRION:CVE-2020-28009
|     	PRION:CVE-2020-28008	7.2	https://vulners.com/prion/PRION:CVE-2020-28008
|     	PRION:CVE-2020-28007	7.2	https://vulners.com/prion/PRION:CVE-2020-28007
|     	CVE-2020-28016	7.2	https://vulners.com/cve/CVE-2020-28016
|     	CVE-2020-28015	7.2	https://vulners.com/cve/CVE-2020-28015
|     	CVE-2020-28013	7.2	https://vulners.com/cve/CVE-2020-28013
|     	CVE-2020-28012	7.2	https://vulners.com/cve/CVE-2020-28012
|     	CVE-2020-28011	7.2	https://vulners.com/cve/CVE-2020-28011
|     	CVE-2020-28010	7.2	https://vulners.com/cve/CVE-2020-28010
|     	CVE-2020-28009	7.2	https://vulners.com/cve/CVE-2020-28009
|     	CVE-2020-28008	7.2	https://vulners.com/cve/CVE-2020-28008
|     	CVE-2020-28007	7.2	https://vulners.com/cve/CVE-2020-28007
|     	PRION:CVE-2021-27216	6.3	https://vulners.com/prion/PRION:CVE-2021-27216
|     	CVE-2021-27216	6.3	https://vulners.com/cve/CVE-2021-27216
|     	PRION:CVE-2020-28014	5.6	https://vulners.com/prion/PRION:CVE-2020-28014
|     	CVE-2020-28014	5.6	https://vulners.com/cve/CVE-2020-28014
|     	PRION:CVE-2022-37451	5.0	https://vulners.com/prion/PRION:CVE-2022-37451
|     	PRION:CVE-2021-38371	5.0	https://vulners.com/prion/PRION:CVE-2021-38371
|     	PRION:CVE-2020-28025	5.0	https://vulners.com/prion/PRION:CVE-2020-28025
|     	PRION:CVE-2020-28023	5.0	https://vulners.com/prion/PRION:CVE-2020-28023
|     	PRION:CVE-2020-28019	5.0	https://vulners.com/prion/PRION:CVE-2020-28019
|     	PRION:CVE-2020-12783	5.0	https://vulners.com/prion/PRION:CVE-2020-12783
|     	CVE-2021-38371	5.0	https://vulners.com/cve/CVE-2021-38371
|     	CVE-2020-28025	5.0	https://vulners.com/cve/CVE-2020-28025
|     	CVE-2020-28023	5.0	https://vulners.com/cve/CVE-2020-28023
|     	CVE-2020-28019	5.0	https://vulners.com/cve/CVE-2020-28019
|_    	CNVD-2022-56952	0.0	https://vulners.com/cnvd/CNVD-2022-56952
26/tcp   open  smtp       Exim smtpd 4.93
| smtp-vuln-cve2010-4344: 
|_  The SMTP server is not Exim: NOT VULNERABLE
| vulners: 
|   cpe:/a:exim:exim:4.93: 
|     	PRION:CVE-2020-28026	9.3	https://vulners.com/prion/PRION:CVE-2020-28026
|     	CVE-2020-28026	9.3	https://vulners.com/cve/CVE-2020-28026
|     	PRION:CVE-2020-28021	9.0	https://vulners.com/prion/PRION:CVE-2020-28021
|     	CVE-2020-28021	9.0	https://vulners.com/cve/CVE-2020-28021
|     	SSV:99253	7.5	https://vulners.com/seebug/SSV:99253	*EXPLOIT*
|     	PRION:CVE-2022-37452	7.5	https://vulners.com/prion/PRION:CVE-2022-37452
|     	PRION:CVE-2020-28024	7.5	https://vulners.com/prion/PRION:CVE-2020-28024
|     	PRION:CVE-2020-28022	7.5	https://vulners.com/prion/PRION:CVE-2020-28022
|     	PRION:CVE-2020-28018	7.5	https://vulners.com/prion/PRION:CVE-2020-28018
|     	PRION:CVE-2020-28017	7.5	https://vulners.com/prion/PRION:CVE-2020-28017
|     	D4A90249-DD8A-53F0-BF5C-2A24402535BB	7.5	https://vulners.com/githubexploit/D4A90249-DD8A-53F0-BF5C-2A24402535BB	*EXPLOIT*
|     	CVE-2022-37452	7.5	https://vulners.com/cve/CVE-2022-37452
|     	CVE-2020-28024	7.5	https://vulners.com/cve/CVE-2020-28024
|     	CVE-2020-28022	7.5	https://vulners.com/cve/CVE-2020-28022
|     	CVE-2020-28018	7.5	https://vulners.com/cve/CVE-2020-28018
|     	CVE-2020-28017	7.5	https://vulners.com/cve/CVE-2020-28017
|     	347B3764-E644-581E-AFCB-F57D6EDDDA1E	7.5	https://vulners.com/githubexploit/347B3764-E644-581E-AFCB-F57D6EDDDA1E	*EXPLOIT*
|     	PRION:CVE-2020-28016	7.2	https://vulners.com/prion/PRION:CVE-2020-28016
|     	PRION:CVE-2020-28015	7.2	https://vulners.com/prion/PRION:CVE-2020-28015
|     	PRION:CVE-2020-28013	7.2	https://vulners.com/prion/PRION:CVE-2020-28013
|     	PRION:CVE-2020-28012	7.2	https://vulners.com/prion/PRION:CVE-2020-28012
|     	PRION:CVE-2020-28011	7.2	https://vulners.com/prion/PRION:CVE-2020-28011
|     	PRION:CVE-2020-28010	7.2	https://vulners.com/prion/PRION:CVE-2020-28010
|     	PRION:CVE-2020-28009	7.2	https://vulners.com/prion/PRION:CVE-2020-28009
|     	PRION:CVE-2020-28008	7.2	https://vulners.com/prion/PRION:CVE-2020-28008
|     	PRION:CVE-2020-28007	7.2	https://vulners.com/prion/PRION:CVE-2020-28007
|     	CVE-2020-28016	7.2	https://vulners.com/cve/CVE-2020-28016
|     	CVE-2020-28015	7.2	https://vulners.com/cve/CVE-2020-28015
|     	CVE-2020-28013	7.2	https://vulners.com/cve/CVE-2020-28013
|     	CVE-2020-28012	7.2	https://vulners.com/cve/CVE-2020-28012
|     	CVE-2020-28011	7.2	https://vulners.com/cve/CVE-2020-28011
|     	CVE-2020-28010	7.2	https://vulners.com/cve/CVE-2020-28010
|     	CVE-2020-28009	7.2	https://vulners.com/cve/CVE-2020-28009
|     	CVE-2020-28008	7.2	https://vulners.com/cve/CVE-2020-28008
|     	CVE-2020-28007	7.2	https://vulners.com/cve/CVE-2020-28007
|     	PRION:CVE-2021-27216	6.3	https://vulners.com/prion/PRION:CVE-2021-27216
|     	CVE-2021-27216	6.3	https://vulners.com/cve/CVE-2021-27216
|     	PRION:CVE-2020-28014	5.6	https://vulners.com/prion/PRION:CVE-2020-28014
|     	CVE-2020-28014	5.6	https://vulners.com/cve/CVE-2020-28014
|     	PRION:CVE-2022-37451	5.0	https://vulners.com/prion/PRION:CVE-2022-37451
|     	PRION:CVE-2021-38371	5.0	https://vulners.com/prion/PRION:CVE-2021-38371
|     	PRION:CVE-2020-28025	5.0	https://vulners.com/prion/PRION:CVE-2020-28025
|     	PRION:CVE-2020-28023	5.0	https://vulners.com/prion/PRION:CVE-2020-28023
|     	PRION:CVE-2020-28019	5.0	https://vulners.com/prion/PRION:CVE-2020-28019
|     	PRION:CVE-2020-12783	5.0	https://vulners.com/prion/PRION:CVE-2020-12783
|     	CVE-2021-38371	5.0	https://vulners.com/cve/CVE-2021-38371
|     	CVE-2020-28025	5.0	https://vulners.com/cve/CVE-2020-28025
|     	CVE-2020-28023	5.0	https://vulners.com/cve/CVE-2020-28023
|     	CVE-2020-28019	5.0	https://vulners.com/cve/CVE-2020-28019
|_    	CNVD-2022-56952	0.0	https://vulners.com/cnvd/CNVD-2022-56952
80/tcp   open  http       Apache httpd
|_http-server-header: Apache
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
110/tcp  open  pop3       Dovecot pop3d
| ssl-dh-params: 
|   VULNERABLE:
|   Diffie-Hellman Key Exchange Insufficient Group Strength
|     State: VULNERABLE
|       Transport Layer Security (TLS) services that use Diffie-Hellman groups
|       of insufficient strength, especially those using one of a few commonly
|       shared groups, may be susceptible to passive eavesdropping attacks.
|     Check results:
|       WEAK DH GROUP 1
|             Cipher Suite: TLS_DHE_RSA_WITH_AES_128_CBC_SHA
|             Modulus Type: Safe prime
|             Modulus Source: Unknown/Custom-generated
|             Modulus Length: 1024
|             Generator Length: 8
|             Public Key Length: 1024
|     References:
|_      https://weakdh.org
| ssl-poodle: 
|   VULNERABLE:
|   SSL POODLE information leak
|     State: VULNERABLE
|     IDs:  CVE:CVE-2014-3566  BID:70574
|           The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other
|           products, uses nondeterministic CBC padding, which makes it easier
|           for man-in-the-middle attackers to obtain cleartext data via a
|           padding-oracle attack, aka the "POODLE" issue.
|     Disclosure date: 2014-10-14
|     Check results:
|       TLS_RSA_WITH_AES_128_CBC_SHA
|     References:
|       https://www.openssl.org/~bodo/ssl-poodle.pdf
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3566
|       https://www.securityfocus.com/bid/70574
|_      https://www.imperialviolet.org/2014/10/14/poodle.html
111/tcp  open  rpcbind    2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|_  100000  3,4          111/udp6  rpcbind
143/tcp  open  imap       Dovecot imapd
| ssl-poodle: 
|   VULNERABLE:
|   SSL POODLE information leak
|     State: VULNERABLE
|     IDs:  CVE:CVE-2014-3566  BID:70574
|           The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other
|           products, uses nondeterministic CBC padding, which makes it easier
|           for man-in-the-middle attackers to obtain cleartext data via a
|           padding-oracle attack, aka the "POODLE" issue.
|     Disclosure date: 2014-10-14
|     Check results:
|       TLS_RSA_WITH_AES_128_CBC_SHA
|     References:
|       https://www.openssl.org/~bodo/ssl-poodle.pdf
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3566
|       https://www.securityfocus.com/bid/70574
|_      https://www.imperialviolet.org/2014/10/14/poodle.html
| ssl-dh-params: 
|   VULNERABLE:
|   Diffie-Hellman Key Exchange Insufficient Group Strength
|     State: VULNERABLE
|       Transport Layer Security (TLS) services that use Diffie-Hellman groups
|       of insufficient strength, especially those using one of a few commonly
|       shared groups, may be susceptible to passive eavesdropping attacks.
|     Check results:
|       WEAK DH GROUP 1
|             Cipher Suite: TLS_DHE_RSA_WITH_AES_128_CBC_SHA
|             Modulus Type: Safe prime
|             Modulus Source: Unknown/Custom-generated
|             Modulus Length: 1024
|             Generator Length: 8
|             Public Key Length: 1024
|     References:
|_      https://weakdh.org
443/tcp  open  ssl/http   Apache httpd (PHP 5.6.40)
|_http-server-header: Apache
|_http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)
| http-enum: 
|   /test/: Test page
|   /webmail/: Mail folder
|   /webmail/images/sm_logo.png: SquirrelMail
|_  /controlpanel/: Potentially interesting folder
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
465/tcp  open  ssl/smtp   Exim smtpd 4.93
| vulners: 
|   cpe:/a:exim:exim:4.93: 
|     	PRION:CVE-2020-28026	9.3	https://vulners.com/prion/PRION:CVE-2020-28026
|     	CVE-2020-28026	9.3	https://vulners.com/cve/CVE-2020-28026
|     	PRION:CVE-2020-28021	9.0	https://vulners.com/prion/PRION:CVE-2020-28021
|     	CVE-2020-28021	9.0	https://vulners.com/cve/CVE-2020-28021
|     	SSV:99253	7.5	https://vulners.com/seebug/SSV:99253	*EXPLOIT*
|     	PRION:CVE-2022-37452	7.5	https://vulners.com/prion/PRION:CVE-2022-37452
|     	PRION:CVE-2020-28024	7.5	https://vulners.com/prion/PRION:CVE-2020-28024
|     	PRION:CVE-2020-28022	7.5	https://vulners.com/prion/PRION:CVE-2020-28022
|     	PRION:CVE-2020-28018	7.5	https://vulners.com/prion/PRION:CVE-2020-28018
|     	PRION:CVE-2020-28017	7.5	https://vulners.com/prion/PRION:CVE-2020-28017
|     	D4A90249-DD8A-53F0-BF5C-2A24402535BB	7.5	https://vulners.com/githubexploit/D4A90249-DD8A-53F0-BF5C-2A24402535BB	*EXPLOIT*
|     	CVE-2022-37452	7.5	https://vulners.com/cve/CVE-2022-37452
|     	CVE-2020-28024	7.5	https://vulners.com/cve/CVE-2020-28024
|     	CVE-2020-28022	7.5	https://vulners.com/cve/CVE-2020-28022
|     	CVE-2020-28018	7.5	https://vulners.com/cve/CVE-2020-28018
|     	CVE-2020-28017	7.5	https://vulners.com/cve/CVE-2020-28017
|     	347B3764-E644-581E-AFCB-F57D6EDDDA1E	7.5	https://vulners.com/githubexploit/347B3764-E644-581E-AFCB-F57D6EDDDA1E	*EXPLOIT*
|     	PRION:CVE-2020-28016	7.2	https://vulners.com/prion/PRION:CVE-2020-28016
|     	PRION:CVE-2020-28015	7.2	https://vulners.com/prion/PRION:CVE-2020-28015
|     	PRION:CVE-2020-28013	7.2	https://vulners.com/prion/PRION:CVE-2020-28013
|     	PRION:CVE-2020-28012	7.2	https://vulners.com/prion/PRION:CVE-2020-28012
|     	PRION:CVE-2020-28011	7.2	https://vulners.com/prion/PRION:CVE-2020-28011
|     	PRION:CVE-2020-28010	7.2	https://vulners.com/prion/PRION:CVE-2020-28010
|     	PRION:CVE-2020-28009	7.2	https://vulners.com/prion/PRION:CVE-2020-28009
|     	PRION:CVE-2020-28008	7.2	https://vulners.com/prion/PRION:CVE-2020-28008
|     	PRION:CVE-2020-28007	7.2	https://vulners.com/prion/PRION:CVE-2020-28007
|     	CVE-2020-28016	7.2	https://vulners.com/cve/CVE-2020-28016
|     	CVE-2020-28015	7.2	https://vulners.com/cve/CVE-2020-28015
|     	CVE-2020-28013	7.2	https://vulners.com/cve/CVE-2020-28013
|     	CVE-2020-28012	7.2	https://vulners.com/cve/CVE-2020-28012
|     	CVE-2020-28011	7.2	https://vulners.com/cve/CVE-2020-28011
|     	CVE-2020-28010	7.2	https://vulners.com/cve/CVE-2020-28010
|     	CVE-2020-28009	7.2	https://vulners.com/cve/CVE-2020-28009
|     	CVE-2020-28008	7.2	https://vulners.com/cve/CVE-2020-28008
|     	CVE-2020-28007	7.2	https://vulners.com/cve/CVE-2020-28007
|     	PRION:CVE-2021-27216	6.3	https://vulners.com/prion/PRION:CVE-2021-27216
|     	CVE-2021-27216	6.3	https://vulners.com/cve/CVE-2021-27216
|     	PRION:CVE-2020-28014	5.6	https://vulners.com/prion/PRION:CVE-2020-28014
|     	CVE-2020-28014	5.6	https://vulners.com/cve/CVE-2020-28014
|     	PRION:CVE-2022-37451	5.0	https://vulners.com/prion/PRION:CVE-2022-37451
|     	PRION:CVE-2021-38371	5.0	https://vulners.com/prion/PRION:CVE-2021-38371
|     	PRION:CVE-2020-28025	5.0	https://vulners.com/prion/PRION:CVE-2020-28025
|     	PRION:CVE-2020-28023	5.0	https://vulners.com/prion/PRION:CVE-2020-28023
|     	PRION:CVE-2020-28019	5.0	https://vulners.com/prion/PRION:CVE-2020-28019
|     	PRION:CVE-2020-12783	5.0	https://vulners.com/prion/PRION:CVE-2020-12783
|     	CVE-2021-38371	5.0	https://vulners.com/cve/CVE-2021-38371
|     	CVE-2020-28025	5.0	https://vulners.com/cve/CVE-2020-28025
|     	CVE-2020-28023	5.0	https://vulners.com/cve/CVE-2020-28023
|     	CVE-2020-28019	5.0	https://vulners.com/cve/CVE-2020-28019
|_    	CNVD-2022-56952	0.0	https://vulners.com/cnvd/CNVD-2022-56952
| smtp-vuln-cve2010-4344: 
|_  The SMTP server is not Exim: NOT VULNERABLE
587/tcp  open  smtp       Exim smtpd 4.93
| smtp-vuln-cve2010-4344: 
|_  The SMTP server is not Exim: NOT VULNERABLE
| vulners: 
|   cpe:/a:exim:exim:4.93: 
|     	PRION:CVE-2020-28026	9.3	https://vulners.com/prion/PRION:CVE-2020-28026
|     	CVE-2020-28026	9.3	https://vulners.com/cve/CVE-2020-28026
|     	PRION:CVE-2020-28021	9.0	https://vulners.com/prion/PRION:CVE-2020-28021
|     	CVE-2020-28021	9.0	https://vulners.com/cve/CVE-2020-28021
|     	SSV:99253	7.5	https://vulners.com/seebug/SSV:99253	*EXPLOIT*
|     	PRION:CVE-2022-37452	7.5	https://vulners.com/prion/PRION:CVE-2022-37452
|     	PRION:CVE-2020-28024	7.5	https://vulners.com/prion/PRION:CVE-2020-28024
|     	PRION:CVE-2020-28022	7.5	https://vulners.com/prion/PRION:CVE-2020-28022
|     	PRION:CVE-2020-28018	7.5	https://vulners.com/prion/PRION:CVE-2020-28018
|     	PRION:CVE-2020-28017	7.5	https://vulners.com/prion/PRION:CVE-2020-28017
|     	D4A90249-DD8A-53F0-BF5C-2A24402535BB	7.5	https://vulners.com/githubexploit/D4A90249-DD8A-53F0-BF5C-2A24402535BB	*EXPLOIT*
|     	CVE-2022-37452	7.5	https://vulners.com/cve/CVE-2022-37452
|     	CVE-2020-28024	7.5	https://vulners.com/cve/CVE-2020-28024
|     	CVE-2020-28022	7.5	https://vulners.com/cve/CVE-2020-28022
|     	CVE-2020-28018	7.5	https://vulners.com/cve/CVE-2020-28018
|     	CVE-2020-28017	7.5	https://vulners.com/cve/CVE-2020-28017
|     	347B3764-E644-581E-AFCB-F57D6EDDDA1E	7.5	https://vulners.com/githubexploit/347B3764-E644-581E-AFCB-F57D6EDDDA1E	*EXPLOIT*
|     	PRION:CVE-2020-28016	7.2	https://vulners.com/prion/PRION:CVE-2020-28016
|     	PRION:CVE-2020-28015	7.2	https://vulners.com/prion/PRION:CVE-2020-28015
|     	PRION:CVE-2020-28013	7.2	https://vulners.com/prion/PRION:CVE-2020-28013
|     	PRION:CVE-2020-28012	7.2	https://vulners.com/prion/PRION:CVE-2020-28012
|     	PRION:CVE-2020-28011	7.2	https://vulners.com/prion/PRION:CVE-2020-28011
|     	PRION:CVE-2020-28010	7.2	https://vulners.com/prion/PRION:CVE-2020-28010
|     	PRION:CVE-2020-28009	7.2	https://vulners.com/prion/PRION:CVE-2020-28009
|     	PRION:CVE-2020-28008	7.2	https://vulners.com/prion/PRION:CVE-2020-28008
|     	PRION:CVE-2020-28007	7.2	https://vulners.com/prion/PRION:CVE-2020-28007
|     	CVE-2020-28016	7.2	https://vulners.com/cve/CVE-2020-28016
|     	CVE-2020-28015	7.2	https://vulners.com/cve/CVE-2020-28015
|     	CVE-2020-28013	7.2	https://vulners.com/cve/CVE-2020-28013
|     	CVE-2020-28012	7.2	https://vulners.com/cve/CVE-2020-28012
|     	CVE-2020-28011	7.2	https://vulners.com/cve/CVE-2020-28011
|     	CVE-2020-28010	7.2	https://vulners.com/cve/CVE-2020-28010
|     	CVE-2020-28009	7.2	https://vulners.com/cve/CVE-2020-28009
|     	CVE-2020-28008	7.2	https://vulners.com/cve/CVE-2020-28008
|     	CVE-2020-28007	7.2	https://vulners.com/cve/CVE-2020-28007
|     	PRION:CVE-2021-27216	6.3	https://vulners.com/prion/PRION:CVE-2021-27216
|     	CVE-2021-27216	6.3	https://vulners.com/cve/CVE-2021-27216
|     	PRION:CVE-2020-28014	5.6	https://vulners.com/prion/PRION:CVE-2020-28014
|     	CVE-2020-28014	5.6	https://vulners.com/cve/CVE-2020-28014
|     	PRION:CVE-2022-37451	5.0	https://vulners.com/prion/PRION:CVE-2022-37451
|     	PRION:CVE-2021-38371	5.0	https://vulners.com/prion/PRION:CVE-2021-38371
|     	PRION:CVE-2020-28025	5.0	https://vulners.com/prion/PRION:CVE-2020-28025
|     	PRION:CVE-2020-28023	5.0	https://vulners.com/prion/PRION:CVE-2020-28023
|     	PRION:CVE-2020-28019	5.0	https://vulners.com/prion/PRION:CVE-2020-28019
|     	PRION:CVE-2020-12783	5.0	https://vulners.com/prion/PRION:CVE-2020-12783
|     	CVE-2021-38371	5.0	https://vulners.com/cve/CVE-2021-38371
|     	CVE-2020-28025	5.0	https://vulners.com/cve/CVE-2020-28025
|     	CVE-2020-28023	5.0	https://vulners.com/cve/CVE-2020-28023
|     	CVE-2020-28019	5.0	https://vulners.com/cve/CVE-2020-28019
|_    	CNVD-2022-56952	0.0	https://vulners.com/cnvd/CNVD-2022-56952
993/tcp  open  ssl/imap   Dovecot imapd
| ssl-poodle: 
|   VULNERABLE:
|   SSL POODLE information leak
|     State: VULNERABLE
|     IDs:  CVE:CVE-2014-3566  BID:70574
|           The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other
|           products, uses nondeterministic CBC padding, which makes it easier
|           for man-in-the-middle attackers to obtain cleartext data via a
|           padding-oracle attack, aka the "POODLE" issue.
|     Disclosure date: 2014-10-14
|     Check results:
|       TLS_RSA_WITH_AES_128_CBC_SHA
|     References:
|       https://www.openssl.org/~bodo/ssl-poodle.pdf
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3566
|       https://www.securityfocus.com/bid/70574
|_      https://www.imperialviolet.org/2014/10/14/poodle.html
| ssl-dh-params: 
|   VULNERABLE:
|   Diffie-Hellman Key Exchange Insufficient Group Strength
|     State: VULNERABLE
|       Transport Layer Security (TLS) services that use Diffie-Hellman groups
|       of insufficient strength, especially those using one of a few commonly
|       shared groups, may be susceptible to passive eavesdropping attacks.
|     Check results:
|       WEAK DH GROUP 1
|             Cipher Suite: TLS_DHE_RSA_WITH_AES_128_CBC_SHA
|             Modulus Type: Safe prime
|             Modulus Source: Unknown/Custom-generated
|             Modulus Length: 1024
|             Generator Length: 8
|             Public Key Length: 1024
|     References:
|_      https://weakdh.org
995/tcp  open  ssl/pop3   Dovecot pop3d
| ssl-poodle: 
|   VULNERABLE:
|   SSL POODLE information leak
|     State: VULNERABLE
|     IDs:  CVE:CVE-2014-3566  BID:70574
|           The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other
|           products, uses nondeterministic CBC padding, which makes it easier
|           for man-in-the-middle attackers to obtain cleartext data via a
|           padding-oracle attack, aka the "POODLE" issue.
|     Disclosure date: 2014-10-14
|     Check results:
|       TLS_RSA_WITH_AES_128_CBC_SHA
|     References:
|       https://www.openssl.org/~bodo/ssl-poodle.pdf
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3566
|       https://www.securityfocus.com/bid/70574
|_      https://www.imperialviolet.org/2014/10/14/poodle.html
| ssl-dh-params: 
|   VULNERABLE:
|   Diffie-Hellman Key Exchange Insufficient Group Strength
|     State: VULNERABLE
|       Transport Layer Security (TLS) services that use Diffie-Hellman groups
|       of insufficient strength, especially those using one of a few commonly
|       shared groups, may be susceptible to passive eavesdropping attacks.
|     Check results:
|       WEAK DH GROUP 1
|             Cipher Suite: TLS_DHE_RSA_WITH_AES_128_CBC_SHA
|             Modulus Type: Safe prime
|             Modulus Source: Unknown/Custom-generated
|             Modulus Length: 1024
|             Generator Length: 8
|             Public Key Length: 1024
|     References:
|_      https://weakdh.org
3306/tcp open  mysql      MySQL 5.7.37
| vulners: 
|   cpe:/a:mysql:mysql:5.7.37: 
|     	PRION:CVE-2023-21980	4.6	https://vulners.com/prion/PRION:CVE-2023-21980
|     	PRION:CVE-2022-21592	4.0	https://vulners.com/prion/PRION:CVE-2022-21592
|     	PRION:CVE-2022-21589	4.0	https://vulners.com/prion/PRION:CVE-2022-21589
|     	PRION:CVE-2022-21454	4.0	https://vulners.com/prion/PRION:CVE-2022-21454
|     	PRION:CVE-2022-21427	4.0	https://vulners.com/prion/PRION:CVE-2022-21427
|     	PRION:CVE-2022-21417	4.0	https://vulners.com/prion/PRION:CVE-2022-21417
|     	PRION:CVE-2023-22084	3.3	https://vulners.com/prion/PRION:CVE-2023-22084
|     	PRION:CVE-2023-22028	3.3	https://vulners.com/prion/PRION:CVE-2023-22028
|     	PRION:CVE-2023-22026	3.3	https://vulners.com/prion/PRION:CVE-2023-22026
|     	PRION:CVE-2023-22015	3.3	https://vulners.com/prion/PRION:CVE-2023-22015
|     	PRION:CVE-2023-22007	3.3	https://vulners.com/prion/PRION:CVE-2023-22007
|     	PRION:CVE-2022-21617	3.3	https://vulners.com/prion/PRION:CVE-2022-21617
|     	PRION:CVE-2022-21608	3.3	https://vulners.com/prion/PRION:CVE-2022-21608
|     	PRION:CVE-2022-21460	2.1	https://vulners.com/prion/PRION:CVE-2022-21460
|     	PRION:CVE-2022-21451	2.1	https://vulners.com/prion/PRION:CVE-2022-21451
|_    	PRION:CVE-2022-21444	2.1	https://vulners.com/prion/PRION:CVE-2022-21444
|_mysql-vuln-cve2012-2122: ERROR: Script execution failed (use -d to debug)
Service Info: Host: ca8.toservers.com

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 492.82 seconds
