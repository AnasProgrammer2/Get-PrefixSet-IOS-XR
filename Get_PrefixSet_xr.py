import netmiko
import paramiko
import re
import yaml
import json
import sys
import urllib3

GetHostname =sys.argv[1];
GetUsername =sys.argv[2];
Getpassword =sys.argv[3];
typeOut =sys.argv[4];
def Parse_PrefixSet(str):
 output="";
 sep = 'prefix-set';
 regex =re.compile('^\d{1,3}(\.\d{1,3}){3}\/\d{1,2}$')
 for line in str.splitlines(True):
  #line= line.replace("prefix-set", "")
  line= line.replace(",", "")
  line = "".join(line.split())
  if line.startswith(('prefix-set', 'Prefix-set')):
    PrefixSetName = line.split(sep, 1)[1]
    line= line.replace("prefix-set", "- prefix-set: ")
    output += "- prefix-set : \n    Name: "+ PrefixSetName + " \n    prefixs:\n";
  elif re.match(regex, line):
    output = output + "      - " + line + '\n';
  if line.startswith(('end', 'end-set')): 
     output +='\n';
 YAML=output;
 ToJSON= yaml.safe_load(output);
 JSON = json.dumps(ToJSON, indent=2) 
 #print(output) 
 if typeOut=="YAML":
  print(YAML)
 elif typeOut=="JSON":
  print(JSON)
 #fout.write(res)

 

def ssh_device(hostname, username, password, device):
    netmiko_exceptions = (paramiko.ssh_exception.SSHException)
    netdev = {
        'device_type': device,
        'ip': hostname,
        'username': username,
        'password': password,
        'global_delay_factor': 1,
    }
    try:
        net_connect = netmiko.ConnectHandler(**netdev)
    except netmiko_exceptions as e:
        return "Failed", e      
    else:
        startup = net_connect.send_command('sh rpl prefix-set')
        #print (startup)
        Parse_PrefixSet(startup)
        net_connect.disconnect()

ssh_device(GetHostname, GetUsername,Getpassword, "cisco_xr")



