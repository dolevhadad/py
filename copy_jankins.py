import paramiko
import sys
k = paramiko.RSAKey.from_private_key_file("/home/ec2-user/pem/FinalProject.pem")
c = paramiko.SSHClient()
origin =sys.argv[1]
dst =sys.argv[2]
host =sys.argv[3]
print ("host; %s",host)
print ("dst: %s",dst)
print ("origin: %s",origin)
#origin = "/home/ec2-user/jenkinsagent/workspace/build_job/target/courseProject.war"
#dst = "/var/lib/tomcat/webapps/courseProject.war"
#host = "172.31.5.69"
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print "connecting"
c.connect( hostname = host, username = "ec2-user", pkey = k )
print "connected"
sftp = c.open_sftp()
sftp.get(origin, dst)
print "copyed"
c.close()
