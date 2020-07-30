# Get-PrefixSet-IOS-XR 

Get A prefix Set from Router IOS XR as type YAML and JSON

<p>This library helps to obtain prefix-set from Cisco Router (iox-xr)  with two types of formats (YAML, JSON) </p>

<b>HOW TO USER  </b>

1 - you must first instill this library
<br>
<br><code><b>pip3 instill netmiko</b></code>
<br><code><b>pip3 instill paramiko</b></code>
<br>
<br>
2- you just download file Get_PrefixSet_xr.py in your server , then execite it by python  3 
 <b>syntax</b>
 <br>
 <Code> #Python3 Get_PrefixSet_XR.py  Hostname  UserName  Password  TYPE[YAML|JSON] </Code> 
 <br>
 [Hostname : Router  IP address ] 
  <br>
 [UserName : Username Router Loign ] 
  <br>
 [Password : Password Router Loign ] 
   <br>
 [TYPE : Type Data OutPut JSON OR YAML] 
   <br>
 <br>
 <b>Example></b>
 <Code> #Python3 Get_PrefixSet_XR.py  10.10.20.1  cisco  cisco123  YAML </Code> 
 <BR>
	OR
 <BR>
<Code> #Python3 Get_PrefixSet_XR.py  10.10.20.1  cisco  cisco123  JSON </Code> 
 
  
