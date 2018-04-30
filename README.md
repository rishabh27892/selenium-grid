# selenium-grid

Legend:
MachineA- Hub
MachineB, C,... - Node
Steps to setup Selenium Grid
1. Download the jar file in Machine-A and Machine-B in any Location(for instance ~/selenium-grid/)
2. Check for Java version- "java - version"
    -sudo apt-get install default-jre
    -sudo apt-get install git 
3. Launch Selenium grid and assign it the role hub in Machine B "java -jar selenium-server-standalone-2.30.0.jar -role hub"
    -Note: Change the version according to the version you are using, it may be diferent
4. After the terminal launches selenium grid , check grid console in the browser- "http://localhost:4444/grid/console"
5. Check by going to the browser in MAchineB- "http://<ip.of.machine.A>:4444/grid/console"
6. Give PATH to geckodriver (Download from "https://github.com/rishabh27892/webui-test-files" or any other version)
        -tar -xvzf geckodriver-v0.18.0-linux64.tar.gz
        -chmod +x geckodriver
        -sudo cp geckodriver /usr/local/bin/
7. Launch the selenium grid in Machine B
    -Navigate to the location of jar file
    -execute "java -jar selenium-server-standalone-3.4.0.jar -role webdriver -hub http://<ip.of.machine.A>:4444/grid/register -port 5566"
    -you can use any port number
6. Go to Selenium Grid Web interface and you should be able to see the updated console wiht Machine B details
    
