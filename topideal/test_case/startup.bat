
java -jar selenium-server-standalone-3.5.3.jar -role hub
::java -jar selenium-server-standalone-3.5.3.jar -role node -port 5555
::java -jar selenium-server-standalone-3.5.3.jar -role node -port 5556 -hub http://ip:4444:grid/register


